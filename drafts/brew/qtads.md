---
name: qtads
title: QTads
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, game, gui, interactive-fiction, language, tads]
homepage: https://realnc.github.io/qtads/
scout_score: 5
status: draft
---

# QTads

**TLDR;** A graphical interpreter that plays TADS interactive fiction games, including the Multimedia TADS ones with pictures and sound that text-only players skip.

QTads runs compiled game files for TADS, the Text Adventure Development System. TADS is a C-like, object-oriented language for writing interactive fiction, the parser-driven genre of Infocom and Legend Entertainment games like Zork. QTads plays both Tads 2 and Tads 3 games with a Qt-based interface on Linux, macOS and Windows.

It does not reimplement the virtual machine. The project says it "is not written from scratch; it uses Mike Roberts' reference implementations of the Tads VM." The TADS compiler turns a game's source into a program for that VM, and QTads runs the program and adds the graphical and multimedia front end.

The door here is interactive fiction itself. A game is a program in a language built around objects, rooms and a parser that turns typed sentences into actions. Playing a few games shows what the genre can do, and TADS is also a language you can write in yourself.

QTads ships no games. The homepage points to the Interactive Fiction Archive and IFDB for finding them.

## Install

```
brew install qtads
# Homebrew marks this formula deprecated. The homepage also offers AppImages for Linux, and Windows and macOS builds.
# You need a TADS game file (.gam or .t3) to play; none are included.
```

## Try this

```
QTads
```
Opens the QTads window, where you can open a TADS game file you downloaded from IFDB or the IF Archive.

## What's unique

Gargoyle, Spatterlight, Zoom and FrobTADS run TADS games in text-only mode. QTads is one of the few free interpreters that plays Multimedia TADS games with their graphics and sound.

## Caveats

Homebrew marks the formula deprecated, though the homepage still lists 3.4 (May 2023) as current, so updates have slowed.

## Links

- [QTads homepage](https://realnc.github.io/qtads/)
- [QTads GitHub repository (README)](https://github.com/realnc/qtads)
- [TADS home page](https://www.tads.org)
- [Interactive Fiction Database (IFDB)](https://ifdb.org)
