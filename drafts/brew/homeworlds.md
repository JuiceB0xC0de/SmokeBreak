---
name: homeworlds
title: Homeworlds
source: brew
category: games
commitment: afternoon
tags: [afternoon, ai, c++, game, library, strategy]
homepage: https://github.com/Quuxplusone/Homeworlds/
scout_score: 6
status: draft
---

# Homeworlds

**TLDR;** A C++ framework, command-line player and GUI for Binary Homeworlds, a two-player "space chess" played with pyramids and no board.

Binary Homeworlds is an abstract strategy game for two players, normally played with Icehouse pieces in four colors. There is no board. Pieces on the table stand in for star systems and spaceships, and you win by eliminating the enemy's homeworld ships through capture, catastrophe, or attacking the binary star system. This project is a software framework for that game.

The core is a C++14 library with types such as GameState and WholeMove, and functions like ApplyMove, AllMoves, InferMove and AIMove. It is a full move generator, not only a rules checker. It can also infer a complete move from a partial entry such as "build g1". On top of the library sit homeworlds-cli, a command-line player and analyzer, and homeworlds-wx, a wxWidgets GUI that works out your move by tracking where you drag a piece from and to. There is also a Python extension and a partial archive of over 700 SuperDuperGames.org transcripts, with a converter script.

The author built it as a personal experiment, both to play against a computer and to explore analysis and AI. The README is frank about the state of things: the library is "poorly structured" and the AI is "very weak". The branching factor is high, so the AI cannot usually look more than one move ahead. That makes it an open problem rather than a finished product, and the README invites patches for a better GUI and a stronger AI.

## Install

```
brew install homeworlds
# pulls in wxwidgets for the GUI. No account or hardware needed; the Icehouse pieces are optional.
```

## Try this

```
homeworlds-cli --help
```
Lists the options of the command-line player and analyzer.

```
homeworlds-wx
```
Opens the graphical board, where you drag pieces and the program deduces the move.

```
ai_move
```
Typed at the homeworlds-cli prompt during a game, it makes the computer play its move.

## What's unique

It is a small, open framework around an unusual abstract game, built on a complete move generator. The GUI infers moves from drag and drop, and a bundled archive of real games is ready for analysis.

## Caveats

The README calls the library poorly structured and the AI very weak, and it gives no maintenance status, so treat it as a hobby project.

## Links

- [Project homepage and README (GitHub)](https://github.com/Quuxplusone/Homeworlds/)
- [BoardGameGeek entry for Homeworlds](http://boardgamegeek.com/boardgame/14634/homeworlds)
- [SuperDuperGames.org game archive](http://superdupergames.org/main.html)
- [Andy's Homeworlds page (wunderland.com)](http://www.wunderland.com/WTS/Andy/Games/ILoveHomeworlds.html)
