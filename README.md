# Smoke Break

A catalogue of things worth taking a short break to poke at. Terminal tools, odd libraries, protocols you use all day and never looked at, simulations, instruments, languages. The kind of thing where you run `--help`, learn it a little, and come back from your break with something new in your head.

Not a list of everything. A short shelf of things you have probably never heard of.

Entries are drafted by Claude, judged by a second model from a different vendor, and the whole pipeline is in this repo. Links go to the real projects. Status: building the catalogue. No CLI yet.

## What gets in

1. **Somewhat unknown.** Loved by thousands is fine if most developers never heard of it. Famous defaults are out.
2. **Has a huh.** Does something you did not know was possible, or opens a door into an idea. Pretty alone does not count.
3. **Standouts only.** In a crowded niche, the most solid or the strangest one. Not all nine.
4. **Interesting beats category.** A library, a language, a whole suite, a protocol. Anything, if it is unique.

Commitment is a tag, not a filter: `quick`, `afternoon`, `days-off`. Difficult installs are allowed. Sometimes that is the fun.

## Categories

See `pipeline/categories.json`. Quick weird payoffs, sound and live coding, take things apart, radio and hardware, fundamentals you never look at twice, deeper rabbit holes, languages and unusual utilities, games.

## How the catalogue gets built

```
feeder  ->  scout  ->  writer  ->  judge  ->  catalogue/
```

- **Feeder** pulls candidates from a package index. `pipeline/feeders/brew.py` is the first one. pip, npm, nix come later as more feeders.
- **Scout** (Claude Haiku) reads every candidate and scores it against the standard. Cheap enough to run on all of Homebrew. Its brain is `pipeline/prompts/scout.md`, a plain text file. Edit that to change its taste.
- **Writer** (Claude Sonnet) reads the real README and writes the entry. Not built yet.
- **Judge** (a different vendor's model) decides keep or reject. Not built yet.

## Running the scout

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...
python3 -m pipeline.scout brew --limit 3   # a taste: 3 batches of 20
python3 -m pipeline.scout brew             # all of it
```

Results land in `data/scout/brew/`: `all.jsonl` (everything), `passes.jsonl` (score 6+), `close_calls.jsonl` (score 4 to 5, the "no, but barely" pile). Re-running skips anything already scored.
