"""Picker: choose N candidates from the scout's passes, spread across categories.

Run:  python3 -m pipeline.pick brew --n 150
      python3 -m pipeline.pick brew --n 2400 --min-score 5     # the stronger half first
      python3 -m pipeline.pick brew --n 150 --include-close-calls

Round-robin over categories, best score first inside each, lowest install count
breaking ties (obscure wins). Skips anything already drafted or in the catalogue.
Writes data/picks/<source>.jsonl, which is what the writer reads.
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def already_done(source: str) -> set[str]:
    names = set()
    for folder in (ROOT / "drafts" / source, ROOT / "catalogue"):
        if folder.exists():
            names |= {p.stem for p in folder.rglob("*.md")}
    rejected = ROOT / "drafts" / source / "rejected.jsonl"
    if rejected.exists():
        names |= {json.loads(l)["name"] for l in rejected.read_text().splitlines() if l.strip()}
    return names


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--n", type=int, default=150)
    ap.add_argument("--include-close-calls", action="store_true")
    ap.add_argument("--min-score", type=int, default=0, help="only candidates scored at least this")
    args = ap.parse_args()

    scout = ROOT / "data" / "scout" / args.source
    files = [scout / "passes.jsonl"]
    if args.include_close_calls:
        files.append(scout / "close_calls.jsonl")
    rows = [json.loads(l) for f in files for l in f.read_text().splitlines() if l.strip()]

    skip = already_done(args.source)
    by_cat = defaultdict(list)
    for r in rows:
        if r["category"] != "none" and r["name"] not in skip and r["score"] >= args.min_score:
            by_cat[r["category"]].append(r)
    for cat in by_cat:
        by_cat[cat].sort(key=lambda r: (-r["score"], r.get("installs_365d", 0)))

    # {round robin: one from each category per lap until we have n}
    picks = []
    cats = sorted(by_cat)
    while len(picks) < args.n and any(by_cat[c] for c in cats):
        for c in cats:
            if by_cat[c] and len(picks) < args.n:
                picks.append(by_cat[c].pop(0))

    out = ROOT / "data" / "picks"
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{args.source}.jsonl").write_text("".join(json.dumps(p) + "\n" for p in picks))

    counts = defaultdict(int)
    for p in picks:
        counts[p["category"]] += 1
    print(f"picked {len(picks)} (skipped {len(skip)} already done)")
    for c in sorted(counts):
        print(f"  {counts[c]:3}  {c}")


if __name__ == "__main__":
    main()
