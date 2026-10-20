"""Load KEY=VALUE lines from .env at the repo root into the environment.

Real environment variables win over the file. Lines starting with # are ignored.
Put keys here, never in the code, and .env is gitignored so it never gets pushed.
"""
import os
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parents[1] / ".env"


def load() -> None:
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


load()
