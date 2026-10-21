"""Writer: a model writes the full entry from the reader's brief. One call, no tools.

Run:  python3 -m pipeline.writer brew                       # every keep in data/judged/brew/keep.jsonl
      python3 -m pipeline.writer brew --limit 2
      python3 -m pipeline.writer brew --dry-run
      python3 -m pipeline.writer brew --model local:gemma-4-e4b-it --from-tag gemma --tag gemma
                                                             # the comparison run: gemma's keeps, written by gemma

The writer never sees the README. The reader (pipeline/reader.py) left a brief, the judge
(pipeline/judge.py) said keep, and only then does the writer spend tokens on it.

Output: drafts/<source>[.<tag>]/<name>.md and <name>.json, rejected.jsonl for the rest.
"""
import argparse
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from pipeline import llm

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "pipeline" / "prompts" / "writer.md"
CATEGORIES = ROOT / "pipeline" / "categories.json"

# {writer conf}
DEFAULT_MODEL = "anthropic:claude-sonnet-5-5"
EFFORT = "medium"      # anthropic only
WORKERS = 3


# ---------- the entry shape ----------

def entry_schema() -> dict:
    slugs = [c["slug"] for c in json.loads(CATEGORIES.read_text())]
    s = {"type": "string"}
    pairs = lambda *keys: {"type": "array", "items": {
        "type": "object", "properties": {k: s for k in keys}, "required": list(keys), "additionalProperties": False}}
    return {
        "type": "object",
        "properties": {
            "verdict": {"type": "string", "enum": ["write", "reject"]},
            "reject_reason": s,
            "title": s,
            "tldr": s,
            "what_it_is": s,
            "how_it_works": s,
            "install": s,
            "first_session": pairs("cmd", "what_you_see"),
            "whats_interesting": s,
            "caveats": s,
            "commitment": {"type": "string", "enum": ["quick", "afternoon", "days-off"]},
            "category": {"type": "string", "enum": slugs},
            "tags": {"type": "array", "items": s},
            "go_deeper": pairs("label", "url", "why"),
        },
        "required": ["verdict", "reject_reason", "title", "tldr", "what_it_is", "how_it_works", "install",
                     "first_session", "whats_interesting", "caveats", "commitment", "category", "tags", "go_deeper"],
        "additionalProperties": False,
    }


def system_prompt() -> str:
    cats = json.loads(CATEGORIES.read_text())
    lines = [f"- `{c['slug']}`: {c['what']}" for c in cats]
    return PROMPT.read_text().replace("{{categories}}", "\n".join(lines))


def job_message(b: dict, formula: dict) -> str:
    facts = {
        "name": b["name"],
        "desc": b["desc"],
        "homepage": b["homepage"],
        "installs_last_365_days": b.get("installs_365d"),
        "executables": formula.get("executables") or [],
        "dependencies": formula.get("dependencies") or [],
        "caveats_from_brew": formula.get("caveats") or "",
        "license": formula.get("license"),
        "deprecated": b.get("deprecated"),
        "scout": {"score": b["score"], "category": b["category"], "tags": b["tags"], "why": b["why"]},
        "judge": b.get("judge"),
        "brief": b["brief"],
    }
    return "Write the Smoke Break entry for this candidate.\n\n" + json.dumps(facts, indent=1)


# ---------- rendering ----------

def render(b: dict, e: dict) -> str:
    tags = sorted(set(e["tags"]) | {e["commitment"]})
    out = [
        "---",
        f"name: {b['name']}",
        f"title: {e['title']}",
        f"source: {b['source']}",
        f"category: {e['category']}",
        f"commitment: {e['commitment']}",
        f"tags: [{', '.join(tags)}]",
        f"homepage: {b['homepage']}",
        f"scout_score: {b['score']}",
        "status: draft",
        "---",
        "",
        f"# {e['title']}",
        "",
        f"**TLDR;** {e['tldr']}",
        "",
        "## What it is",
        "",
        e["what_it_is"].strip(),
        "",
        "## How it works",
        "",
        e["how_it_works"].strip(),
        "",
        "## Install",
        "",
        "```",
        e["install"].strip(),
        "```",
        "",
        "## First session",
        "",
    ]
    for i, t in enumerate(e["first_session"], 1):
        out += [f"{i}. `{t['cmd']}`", "", f"   {t['what_you_see']}", ""]
    out += ["## What's interesting", "", e["whats_interesting"].strip(), ""]
    if e["caveats"].strip():
        out += ["## Caveats", "", e["caveats"].strip(), ""]
    out += ["## Go deeper", ""] + [f"- [{l['label']}]({l['url']}): {l['why']}" for l in e["go_deeper"]] + [""]
    return "\n".join(out)


# ---------- main ----------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="vendor:model, see pipeline/llm.py")
    ap.add_argument("--from-tag", default="", help="read keeps from data/judged/<source>.<from-tag>/")
    ap.add_argument("--tag", default="", help="write to drafts/<source>.<tag>/")
    args = ap.parse_args()

    judged = ROOT / "data" / "judged" / (f"{args.source}.{args.from_tag}" if args.from_tag else args.source)
    keeps = [json.loads(l) for l in (judged / "keep.jsonl").read_text().splitlines() if l.strip()]
    outdir = ROOT / "drafts" / (f"{args.source}.{args.tag}" if args.tag else args.source)
    outdir.mkdir(parents=True, exist_ok=True)
    rejected_f = outdir / "rejected.jsonl"

    done = {p.stem for p in outdir.glob("*.md")}
    if rejected_f.exists():
        done |= {json.loads(l)["name"] for l in rejected_f.read_text().splitlines() if l.strip()}
    todo = [b for b in keeps if b["name"] not in done]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(done)} already written, {len(todo)} to go, model {args.model}", file=sys.stderr)

    formulae = {f["name"]: f for f in json.loads((ROOT / "data" / "raw" / "brew" / "formula.json").read_text())}
    system = system_prompt()

    if args.dry_run:
        if not todo:
            print("nothing to do", file=sys.stderr)
            return
        print(system[:1200], "...\n")
        print(job_message(todo[0], formulae.get(todo[0]["name"], {})))
        return

    lock = threading.Lock()
    total = {"in": 0, "out": 0}
    n_ok = n_rej = 0
    effort = EFFORT if args.model.startswith("anthropic:") else None

    def one(b):
        entry, usage = llm.complete_json(args.model, system, job_message(b, formulae.get(b["name"], {})),
                                         entry_schema(), effort)
        return b, entry, usage

    with ThreadPoolExecutor(WORKERS) as pool:
        futs = [pool.submit(one, b) for b in todo]
        for k, fut in enumerate(as_completed(futs), 1):
            try:
                b, entry, usage = fut.result()
            except Exception as e:
                print(f"failed: {e}", file=sys.stderr)
                continue
            with lock:
                total["in"] += usage["in"]; total["out"] += usage["out"]
                if entry["verdict"] == "write":
                    (outdir / f"{b['name']}.md").write_text(render(b, entry))
                    (outdir / f"{b['name']}.json").write_text(json.dumps({**b, "entry": entry, "writer_model": args.model}, indent=1))
                    n_ok += 1
                    print(f"[{k}/{len(todo)}] wrote {b['name']}: {entry['tldr']}", file=sys.stderr)
                else:
                    with rejected_f.open("a") as f:
                        f.write(json.dumps({"name": b["name"], "reason": entry["reject_reason"]}) + "\n")
                    n_rej += 1
                    print(f"[{k}/{len(todo)}] rejected {b['name']}: {entry['reject_reason']}", file=sys.stderr)

    print(f"done. wrote={n_ok} rejected={n_rej} {llm.cost_line(args.model, total)}", file=sys.stderr)


if __name__ == "__main__":
    main()
