---
name: pachi
title: Pachi
source: brew
category: games
commitment: afternoon
tags: [afternoon, ai, game, go, gtp, mcts]
homepage: https://pachi.or.cz/
scout_score: 6
status: draft
---

# Pachi

**TLDR;** An open-source Go engine built on Monte Carlo tree search, showing how game AI played Go before AlphaGo, and it still plays strongly.

Pachi plays Go (also called Weiqi or Baduk), but it has no board or interface of its own. It speaks GTP, the Go Text Protocol. A frontend such as GoGui, Sabaki or Lizzie sends it moves and time settings, and Pachi replies with its own move. The homepage describes it as "a simple modular framework for programs playing the game of Go/Weiqi/Baduk, and a reasonably strong engine built within this framework."

The default engine is classic Monte Carlo tree search. It plays many semi-random games to the end, using the "Moggy" playout policy, which relies on 3x3 patterns and tactical checks. It then steers the search tree with UCB1AMAF and RAVE statistics. Pattern matching and an optional neural network (dcnn) guide the search, but the network is used at the root node only. The README says the dcnn makes it "about 1 stone stronger" at large playout counts.

The idea underneath is that a game too large to search exhaustively can still be played well by sampling. Pachi shows how that worked before deep-learning players took over. The author, Petr Baudis, wrote a master's thesis on its architecture, and there is a paper, "Pachi: State of the art open source Go program". The homepage also reports a 7-stone handicap win against a 9-dan professional, using a 64-machine cluster.

## Install

```
brew install pachi
# Pachi has no board of its own. You also need a GTP frontend such as GoGui (recommended), Sabaki or Lizzie. kgsGtp is for playing on KGS.
```

## Try this

```
pachi --help
```
Prints the command-line options. The README says there is no full options manual, so this is the starting point.

```
pachi --list-dcnn
```
Lists the neural networks Pachi can use to suggest moves.

```
pachi -t 30 threads=4 max_tree_size=500 pondering
```
Starts the engine with 30 seconds per move on 4 threads and a 500 MB tree cap. It keeps thinking during the opponent's turn. Run it from a GTP frontend.

## What's unique

The default engine is a hand-built MCTS/UCT program with RAVE and pattern-based playouts, not a pure neural-net player. That makes it a readable example of pre-AlphaGo game AI that still plays well.

## Caveats

It has no GUI and needs a separate GTP frontend. The README warns not to expose its GTP interface to untrusted users because the parser is not secure. Engine options are only documented in the source.

## Links

- [Pachi homepage](https://pachi.or.cz/)
- [GitHub repository and README](https://github.com/pasky/pachi)
- [Baudis master's thesis](http://pasky.or.cz/go/prace.pdf)
- [Pachi scientific paper (tr)](http://pasky.or.cz/go/pachi-tr.pdf)
