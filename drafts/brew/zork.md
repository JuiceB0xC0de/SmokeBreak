---
name: zork
title: zork
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, history, public-domain, terminal, text-adventure]
homepage: https://github.com/devshane/zork
scout_score: 6
status: draft
---

# zork

**TLDR;** The public-domain mainframe Zork, called Dungeon, translated from FORTRAN to C so you can play the older, larger game on a modern terminal.

Dungeon, also known as Zork, is a text adventure. You type commands at a prompt and the game answers in prose. It opens in a field west of a white house with a boarded front door. This repository holds the C version of the mainframe game, converted from the FORTRAN source of Zork 2.6. The banner reads: "Welcome to Dungeon. This version created 11-MAR-91."

The README says the primary design goal is code preservation. The aim is to keep the game's logic and behavior as accurate as possible while letting the code compile and run on modern C compilers and operating systems. It is a museum piece that still runs, not a remake with new features.

The lineage is documented. The game began in MDL (MUDDLE) at MIT, went to DEC FORTRAN on the PDP-11 under Bob Supnik, then to f77 on UNIX, and then to C. The C code was generated with f2c, the FORTRAN-to-C translator, and then edited to remove the FORTRAN I/O library, add simple more processing, and change the format of the database file.

This is not the same game as Zork I. The README explains that Zork I is a microcomputer adaptation covering about a third of the original map and puzzles. In its words, "Dungeon represents the more complete, albeit earlier, mainframe experience." Playing it is a way into the history of interactive fiction, and of porting code across languages and decades.

## Install

```
brew install zork
```

## Try this

```
zork
```
Starts the game at the field west of the white house. Type commands at the prompt and read the replies.

```
zork --help
```
Shows whatever options the binary offers, if any.

```
make
```
Builds the game from source in the repository, for platforms without a package.

## What's unique

It is a machine-translated descendant of the original MIT mainframe game, with a documented chain from MDL to FORTRAN to f77 to C. It is the fuller Dungeon, not the shorter Zork I.

## Caveats

It is a preservation project, so expect original behavior and no new features, and it is a different game from the better-known Zork I.

## Links

- [Homepage and README (GitHub)](https://github.com/devshane/zork)
