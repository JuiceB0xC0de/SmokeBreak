---
name: dmagnetic
title: dMagnetic
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, interactive-fiction, interpreter, retro, text-adventure]
homepage: https://www.dettus.net/dMagnetic/
scout_score: 7
status: draft
---

# dMagnetic

**TLDR;** A terminal interpreter that runs 1980s Magnetic Scrolls text adventures like The Pawn and Jinxter from their original game files, with pictures drawn as text or sixels.

dMagnetic plays the text adventures published by Magnetic Scrolls in the 1980s and 90s: The Pawn, The Guild of Thieves, Jinxter, Myth, Fish!, Corruption and Wonderland. It is an interpreter, not a game. It reads the original game data and runs it in your terminal.

It accepts an unusual range of inputs. The homepage lists .mag/.gfx files, MS-DOS binaries, Magnetic Windows .RSC files, and disk images from the Commodore 64, Amstrad CPC, Archimedes, Spectrum +3, Atari XL and Apple II. The same adventures shipped on many incompatible machines, and one program can open the data from all of them.

These games had illustrations, which is the odd part in a terminal. dMagnetic can draw them in several modes: none, monochrome ASCII art, low or high ANSI colour, UTF-8 characters used as pixels, or sixel graphics where the terminal supports it. The page mentions mlterm and `xterm -ti vt340` for sixel.

The idea underneath is preservation through portability. The author says it was "designed with portability in mind, and can be compiled on anything with a C-Compiler." The game files are a small virtual machine's program, so a small interpreter keeps them playable on machines that did not exist when they were written. The author also has a separate write-up of the data structures, linked from the homepage as a PDF.

## Install

```
brew install dMagnetic
# The game files are not included. You must supply original Magnetic Scrolls binaries or disk images yourself; the homepage points to a Magnetic Scrolls memorial site.
```

## Try this

```
dMagnetic --help
```
Lists the options, including how to point it at a game file and choose a graphics mode.

## What's unique

It reads original disk images from many 8-bit and 16-bit platforms, not just PC binaries, and renders the old pictures in a plain terminal as ASCII, ANSI, UTF-8 blocks or sixel.

## Caveats

It ships with no games, so you need to find the original Magnetic Scrolls files yourself, and full graphics need a sixel-capable terminal.

## Links

- [dMagnetic homepage](https://www.dettus.net/dMagnetic/)
