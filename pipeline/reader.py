"""Reader: Haiku fetches the homepage and README and writes a brief for the writer.

Run:  python3 -m pipeline.reader brew              # everything in data/picks/brew.jsonl
      python3 -m pipeline.reader brew --limit 2
      python3 -m pipeline.reader brew --dry-run

This is the agent in the pipeline. The loop in read_one() is the whole mechanism:
send the job plus a tool the model may call, run the tool when it asks, send the
result back, repeat until it answers. Haiku does this because reading is where the
tokens go, and Haiku's input tokens cost a twentieth of Sonnet's.

Output: data/briefs/<source>/<name>.json
"""
import argparse
import json
import re
import sys
import threading
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path

import anthropic

from pipeline import env  # noqa: F401  loads .env

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "pipeline" / "prompts" / "reader.md"

# {reader conf}
MODEL = "claude-haiku-5-5"
WORKERS = 4
MAX_FETCHES = 5
MAX_PAGE_CHARS = 60_000     # a page past this is cut, the model is told so
MAX_TURNS = 8               # hard stop on the loop


# ---------- the tool ----------

class _Text(HTMLParser):
    """Just enough HTML-to-text to read a project page: keep text, drop scripts and styles."""
    def __init__(self):
        super().__init__()
        self.parts, self._skip = [], 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "footer"):
            self._skip += 1
        if tag in ("p", "br", "li", "h1", "h2", "h3", "h4", "pre", "tr", "div"):
            self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer") and self._skip:
            self._skip -= 1
    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def fetch_url(url: str) -> str:
    """GET a page and return readable text. GitHub repo roots come back as their README."""
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)/?$", url)
    if m:
        owner, repo = m.group(1), m.group(2).removesuffix(".git")
        for name in ("README.md", "README.rst", "README.txt", "README", "readme.md"):
            text = _get(f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/{name}")
            if not text.startswith("ERROR"):
                return text
    return _get(url)


def _get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "smokebreak-reader/0.1 (+https://github.com/JuiceB0xC0de/smokebreak)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            ctype = r.headers.get("Content-Type", "")
            body = r.read(2_000_000).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return f"ERROR: HTTP {e.code} fetching {url}"
    except Exception as e:
        return f"ERROR: {type(e).__name__} fetching {url}"
    if "html" in ctype:
        p = _Text(); p.feed(body)
        body = re.sub(r"\n{3,}", "\n\n", "".join(p.parts))
    if len(body) > MAX_PAGE_CHARS:
        body = body[:MAX_PAGE_CHARS] + f"\n\n[cut at {MAX_PAGE_CHARS} characters]"
    return body


TOOLS = [{
    "name": "fetch_url",
    "description": "Fetch a web page and return its text. A GitHub repository URL returns the README.",
    "strict": True,
    "input_schema": {
        "type": "object",
        "properties": {"url": {"type": "string"}},
        "required": ["url"],
        "additionalProperties": False,
    },
}]


# ---------- the brief shape ----------

def brief_schema() -> dict:
    s = {"type": "string"}
    strings = {"type": "array", "items": s}
    pairs = lambda a, b: {"type": "array", "items": {
        "type": "object", "properties": {a: s, b: s}, "required": [a, b], "additionalProperties": False}}
    return {
        "type": "object",
        "properties": {
            "what_it_is": s,
            "history": s,
            "how_it_works": s,
            "features": strings,
            "commands_seen": pairs("cmd", "context"),
            "example_session": s,
            "install_notes": s,
            "standout": s,
            "status": s,
            "caveats": s,
            "quotes": strings,
            "links": pairs("label", "url"),
            "fetch_log": strings,
        },
        "required": ["what_it_is", "history", "how_it_works", "features", "commands_seen", "example_session",
                     "install_notes", "standout", "status", "caveats", "quotes", "links", "fetch_log"],
        "additionalProperties": False,
    }


def job_message(pick: dict, formula: dict) -> str:
    facts = {
        "name": pick["name"],
        "desc": pick["desc"],
        "homepage": pick["homepage"],
        "executables": formula.get("executables") or [],
        "caveats_from_brew": formula.get("caveats") or "",
        "scout_notes": pick["why"],
    }
    return "Read this project and write the brief. Start with the homepage.\n\n" + json.dumps(facts, indent=1)


# ---------- the agent loop ----------

def read_one(client: anthropic.Anthropic, pick: dict, formula: dict, system: str) -> tuple[dict, dict]:
    messages = [{"role": "user", "content": job_message(pick, formula)}]
    usage = {"in": 0, "out": 0}
    fetches = 0

    for _ in range(MAX_TURNS):
        resp = client.messages.create(
            model=MODEL,
            max_tokens=12000,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            messages=messages,
            tools=TOOLS,
            output_config={"format": {"type": "json_schema", "schema": brief_schema()}},
        )
        usage["in"] += resp.usage.input_tokens
        usage["out"] += resp.usage.output_tokens

        if resp.stop_reason == "refusal":
            raise RuntimeError(f"reader refused: {resp.stop_details}")

        calls = [b for b in resp.content if b.type == "tool_use"]
        if not calls:
            # no more tool calls: the text block is the brief, as JSON
            text = next(b.text for b in resp.content if b.type == "text")
            return json.loads(text), usage

        # the model asked for pages. fetch them, hand the text back, go around again.
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for call in calls:
            fetches += 1
            if fetches > MAX_FETCHES:
                text = f"ERROR: fetch limit of {MAX_FETCHES} reached, write the brief with what you have"
            else:
                text = fetch_url(call.input["url"])
            results.append({"type": "tool_result", "tool_use_id": call.id, "content": text,
                            "is_error": text.startswith("ERROR")})
        messages.append({"role": "user", "content": results})

    raise RuntimeError("reader never finished within the turn limit")


# ---------- main ----------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    picks = [json.loads(l) for l in (ROOT / "data" / "picks" / f"{args.source}.jsonl").read_text().splitlines() if l.strip()]
    outdir = ROOT / "data" / "briefs" / args.source
    outdir.mkdir(parents=True, exist_ok=True)

    done = {p.stem for p in outdir.glob("*.json")}
    todo = [p for p in picks if p["name"] not in done]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(done)} already read, {len(todo)} to go", file=sys.stderr)

    formulae = {f["name"]: f for f in json.loads((ROOT / "data" / "raw" / "brew" / "formula.json").read_text())}
    system = PROMPT.read_text()

    if args.dry_run:
        if not todo:
            print("nothing to do", file=sys.stderr)
            return
        print(job_message(todo[0], formulae.get(todo[0]["name"], {})))
        return

    client = anthropic.Anthropic(max_retries=5)
    lock = threading.Lock()
    total = {"in": 0, "out": 0}
    n = 0

    def one(pick):
        return pick, *read_one(client, pick, formulae.get(pick["name"], {}), system)

    with ThreadPoolExecutor(WORKERS) as pool:
        futs = [pool.submit(one, p) for p in todo]
        for k, fut in enumerate(as_completed(futs), 1):
            try:
                pick, brief, usage = fut.result()
            except Exception as e:
                print(f"failed: {e}", file=sys.stderr)
                continue
            with lock:
                total["in"] += usage["in"]; total["out"] += usage["out"]
                (outdir / f"{pick['name']}.json").write_text(json.dumps({**pick, "brief": brief}, indent=1))
                n += 1
                print(f"[{k}/{len(todo)}] read {pick['name']}: {len(brief['commands_seen'])} commands, {brief['status']}", file=sys.stderr)

    # {rough cost, haiku 5.5 list price}
    cost = total["in"] * 0.10 / 1e6 + total["out"] * 0.50 / 1e6
    print(f"done. briefs={n} tokens in={total['in']} out={total['out']} ~${cost:.2f}", file=sys.stderr)


if __name__ == "__main__":
    main()
