---
name: weave
title: weave
source: brew
category: take-things-apart
commitment: quick
tags: [ai-agents, git, merge, quick, tree-sitter, version-control]
homepage: https://ataraxy-labs.github.io/weave/
scout_score: 5
status: draft
---

# weave

**TLDR;** A Git merge driver that parses files with tree-sitter and merges functions and classes instead of lines, so edits to different functions stop conflicting.

Git merges by line. If you change one function and a teammate changes another function in the same file, Git can still declare a conflict when the edits sit close together. Weave replaces that step. It parses the base, ours, and theirs versions of a file with tree-sitter into entities (functions, classes, config keys), matches them by identity including renames, and merges entity by entity.

The rules are simple. If only one side changed an entity, that side wins. If both changed the same entity, weave tries a three-way merge inside it and conflicts only if that fails. The merge is a pure function over three file revisions. It covers about 38 languages and formats, including JSON, YAML, TOML, CSV, and Markdown. Anything it can't handle falls back to Git's normal line merge.

The interesting part is where it declines to merge. When two branches add different decorators to the same Python or TypeScript function, weave won't pick a stacking order, because decorator order changes meaning. In the project's words: "Weave refuses rather than fabricate an order, and a tool that merges those cleanly is wrong, not better." Remaining conflict markers name the entity and the reason.

The stated motivation is several AI agents editing one codebase, which makes false conflicts common. The package also ships `weave-mcp`, a server for agents. You don't need that to use it as a plain merge driver.

## Install

```
brew install weave
# installs both `weave` and `weave-driver`; both must be on PATH, since `weave setup` fails without weave-driver
# building from source needs Rust and two `cargo install --path` commands, one per binary
```

## Try this

```
weave setup
```
Run inside a Git repo, it writes .gitattributes so git merge uses weave for supported file types.

```
weave preview feature-branch
```
Dry-runs a merge of that branch and prints a verdict per file without writing anything.

```
weave setup --off
```
Reverts the repo to normal Git merging.

## What's unique

It treats merging as a question about code entities rather than text lines, and it refuses on purpose where a merge would be semantically wrong. Its README and benchmark page also disclose regressions against Git.

## Caveats

The homepage and README disagree on benchmark numbers (the README's 0.5.3 table lists regressions against Git on several repos), the benchmark corpus is the author's own, and Vue, Svelte, ERB, Haskell, binary files, and files over 1MB fall back to line merge.

## Links

- [Homepage](https://ataraxy-labs.github.io/weave/)
- [GitHub repository and README](https://github.com/Ataraxy-Labs/weave)
- [Benchmarks page](https://ataraxy-labs.github.io/weave/benchmarks.html)
