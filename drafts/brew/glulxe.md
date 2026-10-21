---
name: glulxe
title: glulxe
source: brew
category: languages-and-oddities
commitment: quick
tags: [glulx, interactive-fiction, old-school, quick, text-adventure, virtual-machine, z-machine]
homepage: https://www.eblong.com/zarf/glulx/
scout_score: 6
status: draft
---

# glulxe

**TLDR;** The reference interpreter for Glulx, a 32-bit virtual machine for interactive fiction games, and a way to run text adventures built on a documented spec.

Glulxe ("Glulx Execute") runs Glulx game files. These are usually compiled from Inform 6 source and end in .ulx, or come packaged as Blorb files (.gblorb or .blb). It is a C program that does its input and output through a Glk library.

Glulx was designed as a successor to the Z-machine, the older virtual machine behind Infocom-era text adventures. In the author's words: "Glulx is a portable VM, like the Z-machine. Unlike the Z-machine, it uses 32-bit data and addresses, so it can handle game files up to four gigabytes long." It also has native Glk I/O, so games can use any capability Glk offers, which the Z-machine cannot.

The idea underneath is that a game is bytecode for a small, specified machine, so one file can run on any platform that has an interpreter. The Glulx spec is versioned (currently 3.1.3) and has a public test suite of small games that exercise individual opcodes and features. The interpreter, spec, compiler notes and browser ports are all documented on one site, so you can follow the whole lineage from source to running game. The same games also run in Quixe, a JavaScript interpreter for browsers, and in Lectrote, which packages Quixe as a desktop app.

## Install

```
brew install glulxe
# You need a Glulx game file (.ulx, .gblorb or .blb) to play. The homepage says Glulxe must be built against a Glk library; whether the formula handles that was not verified.
```

## Try this

```
glulxe --help
```
Prints the interpreter's usage and options, which is the safest first look at what it accepts.

## What's unique

Glulx is treated as a documented, versioned spec with a public test suite, and the interpreter, spec and browser ports sit side by side, so the lineage is unusually easy to follow.

## Caveats

The homepage does not give build steps and says a Glk library is required, and some sample games need specific older Glulxe versions, so not every game is guaranteed to run on 0.6.1.

## Links

- [Glulx homepage (author's site)](https://www.eblong.com/zarf/glulx/)
