---
name: befunge93
title: Befunge-93
source: brew
category: languages-and-oddities
commitment: quick
tags: [1993, 2d, esoteric, language, quick, self-modifying]
homepage: https://catseye.tc/article/Languages.md#befunge-93
scout_score: 8
status: draft
---

# Befunge-93

**TLDR;** A 1993 esoteric language where code is a grid, the instruction pointer moves in any of four directions, and programs can rewrite themselves.

Befunge-93 is an esoteric programming language by Chris Pressey. A program is a fixed grid of ASCII characters, usually one instruction per cell. The instruction pointer starts in the upper-left corner moving right and keeps going in that direction until an instruction turns it. It can move up, down, left or right, so you read a program by following a path through the grid, not by reading lines top to bottom.

Data lives on a stack. Control flow is steering: arrow instructions set the direction, and conditional instructions send the pointer horizontally or vertically depending on the top of the stack. The `g` and `p` instructions read and write grid cells by coordinate, so a program can change its own code while it runs.

Pressey's stated goal, per the esolangs.org entry, was a language as difficult to compile as possible. Self-modifying code and the same cell being executed in four directional contexts make that hard. Compilers have been written anyway. The catseye listing says the language begat Befunge-97, Funge-98 and Wierd.

The brew package installs the reference interpreter `bef`, which the catseye listing describes as ANSI C under a BSD license. The formula also lists `bef2c` and `befprof`, but the pages read for this entry say nothing about them.

## Install

```
brew install befunge93
```

## Try this

```
bef --help
```
Prints the interpreter's usage text, if it has any. The sources read for this entry did not document its options.

## What's unique

The program is a two-dimensional playfield, not a line of text. Control flow is a path you trace by eye, and the code can edit itself while it runs.

## Caveats

Maintenance status is unknown, the original playfield is limited to 80x25 cells, and the sources disagree on the compiler's name (bf2c versus bef2c); esolangs.org says that compiler mishandles `p`.

## Links

- [Cat's Eye Technologies language list (Befunge-93 section)](https://catseye.tc/article/Languages.md#befunge-93)
- [Esolang wiki entry for Befunge-93](https://esolangs.org/wiki/Befunge-93)
