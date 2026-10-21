"""Judge: a model from a different vendor reads each brief and says keep or reject.

Run:  python3 -m pipeline.judge brew                 # every brief, with openai:$OPENAI_MODEL
      python3 -m pipeline.judge brew --limit 20
      python3 -m pipeline.judge brew --dry-run
      python3 -m pipeline.judge brew --model local:gemma-4-e4b-it --tag gemma
                                                     # the comparison run, into data/judged/brew.gemma/

The default judge is whatever OPENAI_MODEL names in .env. A different vendor than the
scout and reader, on purpose: Claude should not grade Claude.

Output: data/judged/<source>[.<tag>]/keep.jsonl and reject.jsonl. The writer reads keep.jsonl.
"""
import argparse
import json
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from pipeline import llm

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "pipeline" / "prompts" / "judge.md"

# {judge conf}
WORKERS = 4

VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["keep", "reject"]},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "reason": {"type": "string"},
    },
    "required": ["verdict", "confidence", "reason"],
    "additionalProperties": False,
}


def job_message(b: dict) -> str:
    facts = {
        "name": b["name"],
        "desc": b["desc"],
        "homepage": b["homepage"],
        "installs_last_365_days": b.get("installs_365d"),
        "scout": {"score": b["score"], "category": b["category"], "why": b["why"]},
        "brief": b["brief"],
    }
    return "Judge this candidate.\n\n" + json.dumps(facts, indent=1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", default="", help="vendor:model, default openai:$OPENAI_MODEL")
    ap.add_argument("--tag", default="", help="write to data/judged/<source>.<tag>/")
    args = ap.parse_args()

    model = args.model or (f"openai:{os.environ['OPENAI_MODEL']}" if os.environ.get("OPENAI_MODEL") else "")
    if not model and not args.dry_run:
        sys.exit("set OPENAI_MODEL in .env or pass --model vendor:model")

    briefs = sorted((ROOT / "data" / "briefs" / args.source).glob("*.json"))
    outdir = ROOT / "data" / "judged" / (f"{args.source}.{args.tag}" if args.tag else args.source)
    outdir.mkdir(parents=True, exist_ok=True)
    keep_f, rej_f = outdir / "keep.jsonl", outdir / "reject.jsonl"

    done = set()
    for f in (keep_f, rej_f):
        if f.exists():
            done |= {json.loads(l)["name"] for l in f.read_text().splitlines() if l.strip()}
    todo = [json.loads(p.read_text()) for p in briefs if p.stem not in done]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(done)} already judged, {len(todo)} to go, model {model or '(dry run)'}", file=sys.stderr)

    system = PROMPT.read_text()
    if args.dry_run:
        if not todo:
            print("nothing to do", file=sys.stderr)
            return
        print(system[:800], "...\n")
        print(job_message(todo[0])[:1500])
        return

    lock = threading.Lock()
    total = {"in": 0, "out": 0}
    n_keep = n_rej = 0

    def one(b):
        v, usage = llm.complete_json(model, system, job_message(b), VERDICT_SCHEMA)
        return b, v, usage

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
                row = {**b, "judge": {**v, "model": model}}
                if v.get("verdict") == "keep":
                    keep_f.open("a").write(json.dumps(row) + "\n"); n_keep += 1
                else:
                    rej_f.open("a").write(json.dumps(row) + "\n"); n_rej += 1
                print(f"[{k}/{len(todo)}] {v.get('verdict','?'):6} {b['name']}: {v.get('reason','')}", file=sys.stderr)

    print(f"done. keep={n_keep} reject={n_rej} {llm.cost_line(model, total)}", file=sys.stderr)


if __name__ == "__main__":
    main()
