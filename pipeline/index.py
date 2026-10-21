"""Index: walk the entries and write the shelf pages. No models, no cost.

Run:  python3 -m pipeline.index

Reads every drafts/<source>/<name>.md, takes the frontmatter and the TLDR line, and writes
  catalogue/README.md          the front page: counts and one link per category
  catalogue/<category>.md      one shelf per category: title, TLDR, tags, link to the entry
Run it again whenever entries change. It overwrites both.
"""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = json.loads((ROOT / "pipeline" / "categories.json").read_text())
OUT = ROOT / "catalogue"

FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)
TLDR = re.compile(r"^\*\*TLDR;\*\*\s*(.+)$", re.M)


def read_entry(path: Path) -> dict | None:
    text = path.read_text()
    m = FRONT.match(text)
    if not m:
        return None
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    tags = meta.get("tags", "").strip("[]")
    meta["tags"] = [t.strip() for t in tags.split(",") if t.strip()]
    t = TLDR.search(text)
    meta["tldr"] = t.group(1).strip() if t else ""
    meta["path"] = path.relative_to(ROOT).as_posix()
    return meta


def main() -> None:
    entries = []
    for p in sorted((ROOT / "drafts").rglob("*.md")):
        e = read_entry(p)
        if e and e.get("name"):
            entries.append(e)

    by_cat = defaultdict(list)
    for e in entries:
        by_cat[e.get("category", "uncategorised")].append(e)

    OUT.mkdir(exist_ok=True)
    cats = {c["slug"]: c for c in CATEGORIES}

    # {front page}
    front = ["# Smoke Break: the shelf", "",
             f"{len(entries)} things worth a break. Pick a shelf.", ""]
    for slug in list(cats) + [c for c in by_cat if c not in cats]:
        if slug not in by_cat:
            continue
        name = cats.get(slug, {}).get("name", slug)
        what = cats.get(slug, {}).get("what", "")
        front += [f"## [{name}]({slug}.md)  ({len(by_cat[slug])})", "", what, ""]
    (OUT / "README.md").write_text("\n".join(front))

    # {one shelf per category}
    for slug, rows in by_cat.items():
        name = cats.get(slug, {}).get("name", slug)
        what = cats.get(slug, {}).get("what", "")
        page = [f"# {name}", "", what, "", f"{len(rows)} entries. [Back to the shelf](README.md)", ""]
        for commit in ("quick", "afternoon", "days-off"):
            group = [r for r in rows if r.get("commitment") == commit]
            if not group:
                continue
            page += [f"## {commit}", ""]
            for r in sorted(group, key=lambda r: r["name"]):
                tags = ", ".join(t for t in r["tags"] if t != commit)
                page += [f"- **[{r.get('title') or r['name']}](../{r['path']})**: {r['tldr']}"
                         + (f"  \n  `{tags}`" if tags else "")]
            page.append("")
        (OUT / f"{slug}.md").write_text("\n".join(page))

    print(f"{len(entries)} entries across {len(by_cat)} shelves -> catalogue/")
    for slug, rows in sorted(by_cat.items(), key=lambda kv: -len(kv[1])):
        print(f"  {len(rows):4}  {slug}")


if __name__ == "__main__":
    main()
