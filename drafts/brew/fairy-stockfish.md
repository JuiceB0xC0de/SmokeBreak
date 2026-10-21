---
name: fairy-stockfish
title: Fairy-Stockfish
source: brew
category: games
commitment: afternoon
tags: [afternoon, chess, engine, game, uci, variants]
homepage: https://fairy-stockfish.github.io/
scout_score: 6
status: draft
---

# Fairy-Stockfish

**TLDR;** A Stockfish-derived engine that plays Xiangqi, Shogi, Janggi, Crazyhouse and any chess-like game you define in a config file.

Fairy-Stockfish takes the search code from Stockfish and generalises the rules underneath it. One engine plays regional games such as Xiangqi, Janggi, Shogi and Makruk, modern variants such as Crazyhouse and Atomic, and games whose rules you write yourself. It has no interface of its own. It reads a position and a rule set, then returns moves and evaluations over standard engine protocols: UCI, UCCI, USI, UCI-cyclone and CECP/XBoard. A chess GUI is meant to drive it.

The README states the goal as "to create an engine supporting a large variety of chess-like games, equipped with the powerful search of Stockfish." Variants are defined in built-in code or in a variant configuration file (the README points to src/variants.ini and the wiki). Optional NNUE neural-network evaluation files are loaded separately, and the README says they can raise playing strength significantly.

The idea underneath is that a game's rules are data. Change the board size, the pieces, the movement and the win conditions, and the same alpha-beta search still plays well. Writing your own variant and watching a strong engine play it is a quick way into how game search works, and into the large family of chess-like games.

The README also describes Python, JavaScript and WebAssembly bindings that expose move generation, SAN and FEN handling, and game-end checks.

## Install

```
brew install fairy-stockfish
# No GUI is included. Pair it with a UCI-compatible chess GUI, or play online at pychess, lishogi or lichess. Optional NNUE network files are listed on the project site.
```

## Try this

```
fairy-stockfish --help
```
Prints the engine's usage information. Without arguments it starts and waits for protocol commands on standard input.

## What's unique

One engine covers a very wide range of chess-like games, from Xiangqi and Shogi to user-defined rule sets, while keeping Stockfish's search. The README claims it is the world's strongest engine in Janggi, Crazyhouse and S-Chess.

## Caveats

It has no GUI, so you need a separate chess GUI or an online site, and the homepage says the site is still under construction.

## Links

- [Homepage](https://fairy-stockfish.github.io/)
- [GitHub repository](https://github.com/fairy-stockfish/Fairy-Stockfish)
- [Wiki (usage, variant configuration, GUIs)](https://github.com/fairy-stockfish/Fairy-Stockfish/wiki)
- [Browser playground](https://fairyground.vercel.app/)
