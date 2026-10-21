---
name: dungeon
title: dungeon
source: brew
category: games
commitment: afternoon
tags: [afternoon, fortran, game, history, text-adventure, zork]
homepage: https://github.com/GOFAI/dungeon
scout_score: 6
status: draft
---

# dungeon

**TLDR;** The original MIT text adventure that became Zork, in Robert Supnik's 1980 FORTRAN port, updated so it builds with gfortran today.

DUNGEON is a text adventure. You type commands at a prompt, such as looking around, taking objects and opening doors, and the game prints prose back. It began as a program written in MDL on a DEC PDP-10 at MIT in the late 1970s, and it is the game the Zork series grew out of. In 1980 Robert Supnik ported it to VAX FORTRAN.

This repository is a version 4.0 update of that port. The original source depended on a nonstandard VAX FORTRAN extension that modern compilers no longer support. The update changes only what gfortran needs, so the code stays close to Supnik's. The README says there are no functional differences from his late-1994 V3.2B release. Its stated aim is "enabling a new generation of adventurers to 'GET LAMP.'"

The game is a way into early interactive fiction. The source is old, readable FORTRAN, so you can play the game and then read how a 1980 program parsed commands and stored its world and text. The data lives in two files, dindx and dtext, which the executable reads at startup.

## Install

```
brew install dungeon
# Homebrew builds it with gcc. Run it from the directory that holds the dindx and dtext data files, or it will not find them.
```

## Try this

```
dungeon --help
```
Runs the listed executable with a help flag. The brief does not document flags, so the game may simply start. Run it from the directory with dindx and dtext.

```
make
```
Only if you build from source: run it in the repo's src directory to build the dungeon executable. It needs gfortran and make.

## What's unique

It is the original 1977-80 MIT game with its source largely intact, not a rewrite or a clone. The port is a compatibility update, so the history stays visible.

## Caveats

The license is non-commercial use only, the README gives no release or maintenance dates, and the game must be run from the directory containing dindx and dtext.

## Links

- [GitHub repository (homepage)](https://github.com/GOFAI/dungeon)
