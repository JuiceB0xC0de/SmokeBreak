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
feeder  ->  scout  ->  picker  ->  reader  ->  judge  ->  writer  ->  drafts/
```

- **Feeder** pulls candidates from a package index. `pipeline/feeders/brew.py` is the first one. pip, npm, nix come later as more feeders.
- **Scout** (Claude Haiku) reads every candidate and scores it against the standard. Cheap enough to run on all of Homebrew. Its brain is `pipeline/prompts/scout.md`, a plain text file. Edit that to change its taste.
- **Picker** takes N from the passes, spread evenly across categories, best score first, obscure breaking ties.
- **Reader** (Claude Haiku) is the one real agent. It fetches the homepage or README with a tool, follows a link or two, and leaves a brief: what it is, why it exists, every command seen verbatim, status, caveats. Haiku does the reading because that is where the tokens go. Brain: `pipeline/prompts/reader.md`.
- **Judge** (a model from a different vendor, via plain HTTP) reads the brief and says keep or reject before any writing happens. The brief is cheap, the entry is not, so the judge goes first. Brain: `pipeline/prompts/judge.md`.
- **Writer** (Claude Sonnet) writes the entry from the brief in one call, only for keeps, never sees the README, and can still reject. Output is structured JSON rendered to markdown in `drafts/`. Brain: `pipeline/prompts/writer.md`.

## Running the scout

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env     # then fill in the keys; .env is gitignored
python3 -m pipeline.scout brew --limit 3   # a taste: 3 batches of 20
python3 -m pipeline.scout brew             # all of it
```

## Picking and writing

```
python3 -m pipeline.pick brew --n 2400       # choose across categories -> data/picks/brew.jsonl
python3 -m pipeline.reader brew              # Haiku reads every homepage -> data/briefs/brew/
python3 -m pipeline.judge brew               # keep or reject each brief -> data/judged/brew/
python3 -m pipeline.writer brew              # Sonnet writes the keeps -> drafts/brew/
```

Every stage skips what it has already done, so `--limit N` on any of them is a cheap taste before the full run.

Briefs land in `data/briefs/brew/<name>.json`. Drafts land in `drafts/brew/<name>.md`, with a `.json` beside each for the judge. Writer rejections go to `drafts/brew/rejected.jsonl`. Re-running skips anything already written.

Results from the scout land in `data/scout/brew/`: `all.jsonl` (everything), `passes.jsonl` (score 4 and up), `close_calls.jsonl` (score 2 to 3, the "no, but barely" pile). Re-running skips anything already scored. Moved the line? `python3 -m pipeline.scout brew --rebucket` re-sorts the saved scores without calling the API.
