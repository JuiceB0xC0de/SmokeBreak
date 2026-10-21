"""One door to every model. Ask for JSON in a shape, get a dict back.

A model is named "vendor:model":
  anthropic:claude-sonnet-5-5     Anthropic SDK, structured output enforced by the API
  openai:gpt-...                  OpenAI, plain HTTP, JSON mode
  local:gemma-4-e4b-it            any OpenAI-compatible server on your machine (Ollama, LM Studio)
                                  base URL from LOCAL_BASE_URL in .env, default is Ollama's

Returns (parsed_json, {"in": tokens, "out": tokens}).
"""
import json
import os
import urllib.error
import urllib.request

from pipeline import env  # noqa: F401  loads .env

OPENAI_URL = "https://api.openai.com/v1"
LOCAL_URL_DEFAULT = "http://localhost:11434/v1"


def complete_json(model: str, system: str, user: str, schema: dict, effort: str | None = None) -> tuple[dict, dict]:
    vendor, _, name = model.partition(":")
    if vendor == "anthropic":
        return _anthropic(name, system, user, schema, effort)
    if vendor == "openai":
        return _openai_compatible(OPENAI_URL, os.environ.get("OPENAI_API_KEY", ""), name, system, user, schema)
    if vendor == "local":
        base = os.environ.get("LOCAL_BASE_URL", LOCAL_URL_DEFAULT).rstrip("/")
        return _openai_compatible(base, os.environ.get("LOCAL_API_KEY", "none"), name, system, user, schema)
    raise ValueError(f"unknown vendor in model name {model!r}, use anthropic:, openai: or local:")


def _anthropic(name, system, user, schema, effort):
    import anthropic
    client = anthropic.Anthropic(max_retries=5)
    cfg = {"format": {"type": "json_schema", "schema": schema}}
    if effort:
        cfg["effort"] = effort
    resp = client.messages.create(
        model=name,
        max_tokens=16000,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user}],
        output_config=cfg,
    )
    usage = {"in": resp.usage.input_tokens, "out": resp.usage.output_tokens}
    if resp.stop_reason == "refusal":
        raise RuntimeError(f"refused: {resp.stop_details}")
    text = next(b.text for b in resp.content if b.type == "text")
    return json.loads(text), usage


def _openai_compatible(base, key, name, system, user, schema):
    # JSON mode is the common ground across OpenAI, Ollama and LM Studio. The schema goes in the prompt.
    system_with_shape = system + "\n\nReply with JSON only, matching this JSON Schema exactly:\n" + json.dumps(schema)
    body = {
        "model": name,
        "messages": [{"role": "system", "content": system_with_shape}, {"role": "user", "content": user}],
        "response_format": {"type": "json_object"},
    }
    req = urllib.request.Request(
        f"{base}/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            reply = json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} from {base}: {e.read().decode()[:300]}")
    text = reply["choices"][0]["message"]["content"]
    u = reply.get("usage") or {}
    data = json.loads(text)
    missing = [k for k in schema.get("required", []) if k not in data]
    if missing:
        raise RuntimeError(f"model left out required fields: {missing}")
    return data, {"in": u.get("prompt_tokens", 0), "out": u.get("completion_tokens", 0)}


# {list prices per million tokens, for the cost line; unknown models print tokens only}
PRICES = {
    "anthropic:claude-haiku-5-5": (0.10, 0.50),
    "anthropic:claude-sonnet-5-5": (2.00, 10.00),
    "anthropic:claude-opus-5-5": (4.00, 20.00),
}


def cost_line(model: str, usage: dict) -> str:
    p = PRICES.get(model)
    base = f"tokens in={usage['in']} out={usage['out']}"
    if not p:
        return base + f" (no list price for {model})"
    return base + f" ~${usage['in'] * p[0] / 1e6 + usage['out'] * p[1] / 1e6:.2f}"
