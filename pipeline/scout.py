"""Scout: Haiku reads every candidate and scores it against the standard.

Run:  python3 -m pipeline.scout brew            # all of brew
      python3 -m pipeline.scout brew --limit 3  # just 3 batches, to look at output
      python3 -m pipeline.scout brew --dry-run  # print one request, call nothing

Writes to data/scout/<source>/
  all.jsonl          every result, one per line (this is what makes re-runs resumable)
  passes.jsonl       score >= 6
  close_calls.jsonl  score 4 or 5, the "no, but barely" pile
"""
import argparse
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import anthropic

from pipeline.feeders import brew

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "pipeline" / "prompts" / "scout.md"
CATEGORIES = ROOT / "pipeline" / "categories.json"

# {scout conf}
MODEL = "claude-haiku-5-5"
BATCH = 20          # formulae per request
WORKERS = 4         # parallel requests
PASS = 6            # score >= PASS goes to passes.jsonl
CLOSE = 4           # CLOSE <= score < PASS goes to close_calls.jsonl

FEEDERS = {"brew": brew.candidates}


def system_prompt() -> str:
    cats = json.loads(CATEGORIES.read_text())
    lines = [f"- `{c['slug']}`: {c['what']}" for c in cats]
    return PROMPT.read_text().replace("{{categories}}", "\n".join(lines))


def output_schema() -> dict:
    slugs = [c["slug"] for c in json.loads(CATEGORIES.read_text())] + ["none"]
    return {
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "score": {"type": "integer", "enum": list(range(0, 11))},
                        "category": {"type": "string", "enum": slugs},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "why": {"type": "string"},
                    },
                    "required": ["name", "score", "category", "tags", "why"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["results"],
        "additionalProperties": False,
    }


def request_params(batch: list[dict], system: str) -> dict:
    """One scout request. The system prompt is the brain, the user turn is the batch."""
    return dict(
        model=MODEL,
        max_tokens=8000,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": json.dumps(batch, indent=1)}],
        output_config={"format": {"type": "json_schema", "schema": output_schema()}},
    )


def score_batch(client: anthropic.Anthropic, batch: list[dict], system: str) -> tuple[list[dict], object]:
    resp = client.messages.create(**request_params(batch, system))
    if resp.stop_reason == "refusal":
        raise RuntimeError(f"refused: {resp.stop_details}")
    text = next(b.text for b in resp.content if b.type == "text")
    results = json.loads(text)["results"]
    by_name = {r["name"]: r for r in results}
    out = []
    for c in batch:
        r = by_name.get(c["name"])
        if r is None:
            r = {"name": c["name"], "score": -1, "category": "none", "tags": [], "why": "scout skipped it"}
        out.append({**c, **r})
    return out, resp.usage


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", choices=FEEDERS)
    ap.add_argument("--limit", type=int, default=0, help="stop after N batches")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    outdir = ROOT / "data" / "scout" / args.source
    outdir.mkdir(parents=True, exist_ok=True)
    all_f = outdir / "all.jsonl"
    pass_f = outdir / "passes.jsonl"
    close_f = outdir / "close_calls.jsonl"

    # {resume: skip anything already scored}
    done = set()
    if all_f.exists():
        for line in all_f.read_text().splitlines():
            if line.strip():
                done.add(json.loads(line)["name"])

    todo = [c for c in FEEDERS[args.source]() if c["name"] not in done]
    batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
    if args.limit:
        batches = batches[:args.limit]
    print(f"{len(done)} already scored, {len(todo)} to go, {len(batches)} batches of {BATCH}", file=sys.stderr)

    system = system_prompt()
    if args.dry_run:
        print(json.dumps(request_params(batches[0], system), indent=2)[:6000])
        return

    client = anthropic.Anthropic(max_retries=5)
    lock = threading.Lock()
    usage = {"in": 0, "out": 0, "cache_read": 0}
    n_pass = n_close = 0

    def write(rows, u):
        nonlocal n_pass, n_close
        with lock:
            with all_f.open("a") as fa, pass_f.open("a") as fp, close_f.open("a") as fc:
                for r in rows:
                    line = json.dumps(r) + "\n"
                    fa.write(line)
                    if r["score"] >= PASS:
                        fp.write(line); n_pass += 1
                    elif r["score"] >= CLOSE:
                        fc.write(line); n_close += 1
            usage["in"] += u.input_tokens
            usage["out"] += u.output_tokens
            usage["cache_read"] += u.cache_read_input_tokens or 0

    with ThreadPoolExecutor(WORKERS) as pool:
        futures = {pool.submit(score_batch, client, b, system): i for i, b in enumerate(batches)}
        for k, fut in enumerate(as_completed(futures), 1):
            i = futures[fut]
            try:
                rows, u = fut.result()
            except Exception as e:  # one bad batch should not kill the run
                print(f"batch {i} failed: {e}", file=sys.stderr)
                continue
            write(rows, u)
            print(f"[{k}/{len(batches)}] batch {i}: passes so far {n_pass}, close calls {n_close}", file=sys.stderr)

    # {rough cost, haiku 5.5 list price}
    cost = usage["in"] * 0.10 / 1e6 + usage["out"] * 0.50 / 1e6
    print(f"done. passes={n_pass} close_calls={n_close} tokens in={usage['in']} out={usage['out']} "
          f"cache_read={usage['cache_read']} ~${cost:.2f}", file=sys.stderr)


if __name__ == "__main__":
    main()
