---
name: wumpus
title: Wumpus
source: brew
category: games
commitment: quick
tags: [basic, game, history, quick, retrocomputing]
homepage: http://www.catb.org/~esr/wumpus/
scout_score: 7
status: draft
---

# Wumpus

**TLDR;** An exact clone of Gregory Yob's 1973 Hunt the Wumpus, bad interface included, plus a bundled satire called superhack.

Wumpus is a command-line reproduction of the old BASIC game Hunt the Wumpus. Eric S. Raymond made it by transcribing the original BASIC source, which the README says is kept in comments in the code. The README says this version fixes two minor bugs from his original USENET posting of the source. It is meant to be faithful, not improved.

The author's own description: "WUMPUS is a bit of retrocomputing nostalgia. It is an *exact* clone, even down to the godawful user interface, of an ancient classic game." Expect text prompts, not a modern game UI. The pages read for this entry do not spell out the input format or the rules, so start the game and see what it asks you.

The idea underneath is historical. The README credits Gregory Yob's game as the first exploration game to use a non-grid world map, and it predates Colossal Cave Adventure. Playing it shows what a game looked like when the map was a graph of connected rooms rather than a grid, and when a few lines of BASIC were the whole program.

The package also installs a second executable, superhack. The README describes it as "a satire, structurally quite similar to WUMPUS."

## Install

```
brew install wumpus
```

## Try this

```
wumpus
```
Starts Hunt the Wumpus in the terminal, with the original game's text interface.

```
superhack
```
Runs the bundled satire, which the README says is structurally similar to Wumpus.

```
wumpus --help
```
Asks the program for usage information, if it provides any.

## What's unique

It is a deliberately exact transcription of a 1970s original, flaws and all, with the BASIC source preserved in the code comments. It also ships a satirical second game.

## Caveats

The interface is intentionally clumsy, and the sources disagree slightly on dates: the README says 1973, while the man page says the Atari game is from 1974.

## Links

- [Homepage](http://www.catb.org/~esr/wumpus/)
- [Man page](http://www.catb.org/~esr/wumpus/wumpus.html)
- [README](http://www.catb.org/~esr/wumpus/README.html)
- [Project repository](https://gitlab.com/esr/wumpus)
