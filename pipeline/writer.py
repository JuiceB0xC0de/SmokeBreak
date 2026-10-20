"""Writer: the agent. Sonnet reads the real README and writes the entry.

Run:  python3 -m pipeline.writer brew              # everything in data/picks/brew.jsonl
      python3 -m pipeline.writer brew --limit 2    # just two, to look at the output
      python3 -m pipeline.writer brew --dry-run    # print the first request, call nothing

This is the one real agent in the pipeline. The loop at the bottom of write_entry()
is the whole mechanism: send the job plus a tool the model may call, run the tool when
it asks, send the result back, repeat until it answers.

Output: drafts/<source>/<name>.md and <name>.json for the judge, rejected.jsonl for the rest.
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

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "pipeline" / "prompts" / "writer.md"
CATEGORIES = ROOT / "pipeline" / "categories.json"

# {writer conf}
MODEL = "claude-sonnet-5-5"
EFFORT = "medium"
WORKERS = 3
MAX_FETCHES = 5
MAX_PAGE_CHARS = 30_000     # a README past this is cut, the model is told so
MAX_TURNS = 8               # hard stop on the loop, fetches + the final answer


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
            raw = f"https://raw.githubusercontent.com/{owner}/{repo}/HEAD/{name}"
            text = _get(raw)
            if not text.startswith("ERROR"):
                return text
        # fall through and read the page itself
    return _get(url)


def _get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "smokebreak-writer/0.1 (+https://github.com/JuiceB0xC0de/smokebreak)"})
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


def job_message(pick: dict, formula: dict) -> str:
    facts = {
        "name": pick["name"],
        "desc": pick["desc"],
        "homepage": pick["homepage"],
        "installs_last_365_days": pick.get("installs_365d"),
        "executables": formula.get("executables") or [],
        "dependencies": formula.get("dependencies") or [],
        "caveats_from_brew": formula.get("caveats") or "",
        "license": formula.get("license"),
        "deprecated": pick.get("deprecated"),
        "scout": {"score": pick["score"], "category": pick["category"], "tags": pick["tags"], "why": pick["why"]},
    }
    return "Write the Smoke Break entry for this candidate. Read the homepage first.\n\n" + json.dumps(facts, indent=1)


# ---------- the agent loop ----------

def write_entry(client: anthropic.Anthropic, pick: dict, formula: dict, system: str) -> tuple[dict, dict]:
    messages = [{"role": "user", "content": job_message(pick, formula)}]
    usage = {"in": 0, "out": 0}
    fetches = 0

    for _ in range(MAX_TURNS):
        resp = client.messages.create(
            model=MODEL,
            max_tokens=16000,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            messages=messages,
            tools=TOOLS,
            output_config={"effort": EFFORT, "format": {"type": "json_schema", "schema": entry_schema()}},
        )
        usage["in"] += resp.usage.input_tokens
        usage["out"] += resp.usage.output_tokens

        if resp.stop_reason == "refusal":
            return {"verdict": "reject", "reject_reason": f"writer refused: {resp.stop_details}"}, usage

        calls = [b for b in resp.content if b.type == "tool_use"]
        if not calls:
            # no more tool calls: the text block is the entry, as JSON
            text = next(b.text for b in resp.content if b.type == "text")
            return json.loads(text), usage

        # the model asked for pages. fetch them, hand the text back, go around again.
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for call in calls:
            fetches += 1
            if fetches > MAX_FETCHES:
                text = f"ERROR: fetch limit of {MAX_FETCHES} reached, write the entry with what you have"
            else:
                text = fetch_url(call.input["url"])
            results.append({"type": "tool_result", "tool_use_id": call.id, "content": text,
                            "is_error": text.startswith("ERROR")})
        messages.append({"role": "user", "content": results})

    return {"verdict": "reject", "reject_reason": "writer never finished within the turn limit"}, usage


# ---------- rendering ----------

def render(pick: dict, e: dict) -> str:
    tags = sorted(set(e["tags"]) | {e["commitment"]})
    out = [
        "---",
        f"name: {pick['name']}",
        f"title: {e['title']}",
        f"source: {pick['source']}",
        f"category: {e['category']}",
        f"commitment: {e['commitment']}",
        f"tags: [{', '.join(tags)}]",
        f"homepage: {pick['homepage']}",
        f"scout_score: {pick['score']}",
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

    picks = [json.loads(l) for l in (ROOT / "data" / "picks" / f"{args.source}.jsonl").read_text().splitlines() if l.strip()]
    outdir = ROOT / "drafts" / args.source
    outdir.mkdir(parents=True, exist_ok=True)
    rejected_f = outdir / "rejected.jsonl"

    done = {p.stem for p in outdir.glob("*.md")}
    if rejected_f.exists():
        done |= {json.loads(l)["name"] for l in rejected_f.read_text().splitlines() if l.strip()}
    todo = [p for p in picks if p["name"] not in done]
    if args.limit:
        todo = todo[:args.limit]
    print(f"{len(done)} already written, {len(todo)} to go", file=sys.stderr)

    # brew's full record, for executables and caveats
    formulae = {f["name"]: f for f in json.loads((ROOT / "data" / "raw" / "brew" / "formula.json").read_text())}
    system = system_prompt()

    if args.dry_run:
        print(system[:1500], "...\n")
        print(job_message(todo[0], formulae.get(todo[0]["name"], {})))
        return

    client = anthropic.Anthropic(max_retries=5)
    lock = threading.Lock()
    total = {"in": 0, "out": 0}
    n_ok = n_rej = 0

    def one(pick):
        return pick, *write_entry(client, pick, formulae.get(pick["name"], {}), system)

    with ThreadPoolExecutor(WORKERS) as pool:
        futs = [pool.submit(one, p) for p in todo]
        for k, fut in enumerate(as_completed(futs), 1):
            try:
                pick, entry, usage = fut.result()
            except Exception as e:
                print(f"failed: {e}", file=sys.stderr)
                continue
            with lock:
                total["in"] += usage["in"]; total["out"] += usage["out"]
                if entry["verdict"] == "write":
                    (outdir / f"{pick['name']}.md").write_text(render(pick, entry))
                    (outdir / f"{pick['name']}.json").write_text(json.dumps({**pick, "entry": entry}, indent=1))
                    n_ok += 1
                    print(f"[{k}/{len(todo)}] wrote {pick['name']}: {entry['tldr']}", file=sys.stderr)
                else:
                    with rejected_f.open("a") as f:
                        f.write(json.dumps({"name": pick["name"], "reason": entry["reject_reason"]}) + "\n")
                    n_rej += 1
                    print(f"[{k}/{len(todo)}] rejected {pick['name']}: {entry['reject_reason']}", file=sys.stderr)

    # {rough cost, sonnet 5.5 list price}
    cost = total["in"] * 2.0 / 1e6 + total["out"] * 10.0 / 1e6
    print(f"done. wrote={n_ok} rejected={n_rej} tokens in={total['in']} out={total['out']} ~${cost:.2f}", file=sys.stderr)


if __name__ == "__main__":
    main()
