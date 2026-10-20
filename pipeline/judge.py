"""Judge: a model from a different vendor reads each brief and says keep or reject.

Run:  python3 -m pipeline.judge brew              # every brief in data/briefs/brew/
      python3 -m pipeline.judge brew --limit 5
      python3 -m pipeline.judge brew --dry-run

Needs two environment variables:
  OPENAI_API_KEY   your key
  OPENAI_MODEL     the model to judge with, e.g. the one you use day to day

This talks to the OpenAI API with nothing but the standard library on purpose, so you
can see what a model call is: build a JSON body, POST it, read the reply. Same thing
as a SOAP call to a router, different envelope.

Output: data/judged/<source>/keep.jsonl and reject.jsonl. The writer reads keep.jsonl.
"""
import argparse
import json
import os
import sys
import threading
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "pipeline" / "prompts" / "judge.md"

# {judge conf}
URL = "https://api.openai.com/v1/chat/completions"
WORKERS = 4


def judge_one(b: dict, system: str, model: str, key: str) -> tuple[dict, dict]:
    facts = {
        "name": b["name"],
        "desc": b["desc"],
        "homepage": b["homepage"],
        "installs_last_365_days": b.get("installs_365d"),
        "scout": {"score": b["score"], "category": b["category"], "why": b["why"]},
        "brief": b["brief"],
    }
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": "Judge this candidate.\n\n" + json.dumps(facts, indent=1)},
        ],
        "response_format": {"type": "json_object"},
    }
    req = urllib.request.Request(
        URL,
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            reply = json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode()[:300]}")
    verdict = json.loads(reply["choices"][0]["message"]["content"])
    usage = reply.get("usage", {})
    return verdict, {"in": usage.get("prompt_tokens", 0), "out": usage.get("completion_tokens", 0)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    briefs = sorted((ROOT / "data" / "briefs" / args.source).glob("*.json"))
    outdir = ROOT / "data" / "judged" / args.source
    outdir.mkdir(parents=True, exist_ok=True)
    keep_f, rej_f = outdir / "keep.jsonl", outdir / "reject.jsonl"

    done = set()
    for f in (keep_f, rej_f):
        if f.exists():
            done |= {json.loads(l)["name"] for l in f.read_text().splitlines() if l.strip()}
    todo = [json.loads(p.read_text()) for p in briefs if p.stem not in done]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(done)} already judged, {len(todo)} to go", file=sys.stderr)

    system = PROMPT.read_text()
    if args.dry_run:
        print(system[:800], "...\n")
        print(json.dumps({"name": todo[0]["name"], "brief": todo[0]["brief"]}, indent=1)[:1500])
        return

    key = os.environ.get("OPENAI_API_KEY")
    model = os.environ.get("OPENAI_MODEL")
    if not key or not model:
        sys.exit("set OPENAI_API_KEY and OPENAI_MODEL first")

    lock = threading.Lock()
    total = {"in": 0, "out": 0}
    n_keep = n_rej = 0

    def one(b):
        return b, *judge_one(b, system, model, key)

    with ThreadPoolExecutor(WORKERS) as pool:
        futs = [pool.submit(one, b) for b in todo]
        for k, fut in enumerate(as_completed(futs), 1):
            try:
                b, v, usage = fut.result()
            except Exception as e:
                print(f"failed: {e}", file=sys.stderr)
                continue
            with lock:
                total["in"] += usage["in"]; total["out"] += usage["out"]
                row = {**b, "judge": v}
                if v.get("verdict") == "keep":
                    keep_f.open("a").write(json.dumps(row) + "\n"); n_keep += 1
                else:
                    rej_f.open("a").write(json.dumps(row) + "\n"); n_rej += 1
                print(f"[{k}/{len(todo)}] {v.get('verdict','?'):6} {b['name']}: {v.get('reason','')}", file=sys.stderr)

    print(f"done. keep={n_keep} reject={n_rej} tokens in={total['in']} out={total['out']} (model {model})", file=sys.stderr)


if __name__ == "__main__":
    main()
