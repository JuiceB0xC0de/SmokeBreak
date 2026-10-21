---
name: fairymax
title: fairymax
source: brew
category: games
commitment: afternoon
tags: [afternoon, chess, engine, game-ai, variants]
homepage: https://www.chessvariants.com/index/msdisplay.php?itemid=MSfairy-max
scout_score: 7
status: draft
---

# fairymax

**TLDR;** A small chess engine built to play fairy chess variants, with separate executables for chess-like games such as Xiangqi and Shogi.

fairymax is described in its Homebrew metadata as AI for playing chess variants. The scout's note calls it a tiny engine written for fairy chess, meaning chess with altered rules or unusual pieces. It installs three executables: `fairymax`, `maxqi`, and `shamax`.

The brief could not read the homepage (HTTP 403), so what follows about the executables is inference from their names and not confirmed. `maxqi` and `shamax` look like variants of the same engine tuned for other games, possibly Xiangqi and Shogi. How the engine takes input, whether through a board position, a move list, or a chess GUI protocol, is unverified.

The idea underneath is the interesting part. Most chess engines hard-code the rules of one game. An engine that handles many rule sets has to treat piece movement as data rather than code, which makes it a small, readable example of how game AI generalises. Start with `--help` and see what it tells you.

## Install

```
brew install fairymax
```

## Try this

```
fairymax --help
```
Prints the engine's usage text, if it offers any, which is the quickest way to learn how it expects to be driven.

```
maxqi --help
```
Shows the options for the second executable, so you can compare it with fairymax.

```
shamax --help
```
Shows the options for the third executable.

## What's unique

Per the scout note, it is a tiny engine aimed at fairy chess variants rather than standard chess, which makes it a compact example of rule-agnostic game AI.

## Caveats

The homepage returned HTTP 403 and no README was read, so what it does, how you talk to it, and whether it is maintained are all unverified.

## Links

- [Homepage (returned HTTP 403 when fetched)](https://www.chessvariants.com/index/msdisplay.php?itemid=MSfairy-max)
