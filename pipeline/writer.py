"""Writer: Sonnet writes the entry from the reader's brief. One call, no tools.

Run:  python3 -m pipeline.writer brew              # every brief in data/briefs/brew/
      python3 -m pipeline.writer brew --limit 2    # just two, to look at the output
      python3 -m pipeline.writer brew --dry-run    # print the first request, call nothing

Sonnet never sees the README. Haiku read it (pipeline/reader.py) and left a brief,
so Sonnet's input is a couple of thousand tokens instead of twenty.

Output: drafts/<source>/<name>.md and <name>.json for the judge, rejected.jsonl for the rest.
"""
import argparse
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "pipeline" / "prompts" / "writer.md"
CATEGORIES = ROOT / "pipeline" / "categories.json"

# {writer conf}
MODEL = "claude-sonnet-5-5"
EFFORT = "medium"
WORKERS = 3


# ---------- the entry shape ----------

def entry_schema() -> dict:
    slugs = [c["slug"] for c in json.loads(CATEGORIES.read_text())]
    s = {"type": "string"}
    return {
        "type": "object",
        "properties": {
            "verdict": {"type": "string", "enum": ["write", "reject"]},
            "reject_reason": s,
            "title": s,
            "tldr": s,
            "deeper_look": s,
            "install": s,
            "try_this": {"type": "array", "items": {
                "type": "object",
                "properties": {"cmd": s, "what_happens": s},
                "required": ["cmd", "what_happens"], "additionalProperties": False}},
            "whats_unique": s,
            "caveats": s,
            "commitment": {"type": "string", "enum": ["quick", "afternoon", "days-off"]},
            "category": {"type": "string", "enum": slugs},
            "tags": {"type": "array", "items": s},
            "links": {"type": "array", "items": {
                "type": "object",
                "properties": {"label": s, "url": s},
                "required": ["label", "url"], "additionalProperties": False}},
        },
        "required": ["verdict", "reject_reason", "title", "tldr", "deeper_look", "install", "try_this",
                     "whats_unique", "caveats", "commitment", "category", "tags", "links"],
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
        "brief": b["brief"],
    }
    return "Write the Smoke Break entry for this candidate.\n\n" + json.dumps(facts, indent=1)


# ---------- one call ----------

def write_entry(client: anthropic.Anthropic, b: dict, formula: dict, system: str) -> tuple[dict, dict]:
    resp = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": job_message(b, formula)}],
        output_config={"effort": EFFORT, "format": {"type": "json_schema", "schema": entry_schema()}},
    )
    usage = {"in": resp.usage.input_tokens, "out": resp.usage.output_tokens}
    if resp.stop_reason == "refusal":
        return {"verdict": "reject", "reject_reason": f"writer refused: {resp.stop_details}"}, usage
    text = next(x.text for x in resp.content if x.type == "text")
    return json.loads(text), usage


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
        e["deeper_look"].strip(),
        "",
        "## Install",
        "",
        "```",
        e["install"].strip(),
        "```",
        "",
        "## Try this",
        "",
    ]
    for t in e["try_this"]:
        out += ["```", t["cmd"], "```", t["what_happens"], ""]
    out += ["## What's unique", "", e["whats_unique"], ""]
    if e["caveats"].strip():
        out += ["## Caveats", "", e["caveats"], ""]
    out += ["## Links", ""] + [f"- [{l['label']}]({l['url']})" for l in e["links"]] + [""]
    return "\n".join(out)


# ---------- main ----------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    briefs = sorted((ROOT / "data" / "briefs" / args.source).glob("*.json"))
    outdir = ROOT / "drafts" / args.source
    outdir.mkdir(parents=True, exist_ok=True)
    rejected_f = outdir / "rejected.jsonl"

    done = {p.stem for p in outdir.glob("*.md")}
    if rejected_f.exists():
        done |= {json.loads(l)["name"] for l in rejected_f.read_text().splitlines() if l.strip()}
    todo = [json.loads(p.read_text()) for p in briefs if p.stem not in done]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(done)} already written, {len(todo)} to go", file=sys.stderr)

    formulae = {f["name"]: f for f in json.loads((ROOT / "data" / "raw" / "brew" / "formula.json").read_text())}
    system = system_prompt()

    if args.dry_run:
        print(system[:1200], "...\n")
        print(job_message(todo[0], formulae.get(todo[0]["name"], {})))
        return

    client = anthropic.Anthropic(max_retries=5)
    lock = threading.Lock()
    total = {"in": 0, "out": 0}
    n_ok = n_rej = 0

    def one(b):
        return b, *write_entry(client, b, formulae.get(b["name"], {}), system)

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
                    (outdir / f"{b['name']}.json").write_text(json.dumps({**b, "entry": entry}, indent=1))
                    n_ok += 1
                    print(f"[{k}/{len(todo)}] wrote {b['name']}: {entry['tldr']}", file=sys.stderr)
                else:
                    with rejected_f.open("a") as f:
                        f.write(json.dumps({"name": b["name"], "reason": entry["reject_reason"]}) + "\n")
                    n_rej += 1
                    print(f"[{k}/{len(todo)}] rejected {b['name']}: {entry['reject_reason']}", file=sys.stderr)

    # {rough cost, sonnet 5.5 list price}
    cost = total["in"] * 2.0 / 1e6 + total["out"] * 10.0 / 1e6
    print(f"done. wrote={n_ok} rejected={n_rej} tokens in={total['in']} out={total['out']} ~${cost:.2f}", file=sys.stderr)


if __name__ == "__main__":
    main()
