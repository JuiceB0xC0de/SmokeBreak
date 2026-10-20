"""Homebrew feeder: every formula in homebrew/core as a candidate dict.

Downloads two public JSON files from formulae.brew.sh and caches them in data/raw/brew/
for a day. No scraping, no auth.
"""
import json
import time
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parents[2] / "data" / "raw" / "brew"
FORMULA_URL = "https://formulae.brew.sh/api/formula.json"
ANALYTICS_URL = "https://formulae.brew.sh/api/analytics/install/365d.json"
MAX_AGE = 24 * 3600


def _fetch(url: str, dest: Path) -> dict | list:
    if dest.exists() and time.time() - dest.stat().st_mtime < MAX_AGE:
        return json.loads(dest.read_text())
    RAW.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as r:
        data = r.read()
    dest.write_bytes(data)
    return json.loads(data)


def candidates() -> list[dict]:
    formulae = _fetch(FORMULA_URL, RAW / "formula.json")
    analytics = _fetch(ANALYTICS_URL, RAW / "analytics_365d.json")

    # {installs by formula name}
    installs = {}
    for item in analytics["items"]:
        installs[item["formula"]] = int(item["count"].replace(",", ""))

    out = []
    for f in formulae:
        if f.get("disabled"):
            continue  # brew will not install these at all
        out.append({
            "name": f["name"],
            "desc": f.get("desc") or "",
            "homepage": f.get("homepage") or "",
            "installs_365d": installs.get(f["name"], 0),
            "deprecated": bool(f.get("deprecated")),
            "source": "brew",
        })
    return out


if __name__ == "__main__":
    c = candidates()
    print(len(c), "candidates")
    for x in c[:5]:
        print(x)
