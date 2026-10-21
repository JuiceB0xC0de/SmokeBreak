---
name: mame
title: MAME
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, arcade, emulation, preservation, vintage-hardware]
homepage: https://mamedev.org/
scout_score: 7
status: draft
---

# MAME

**TLDR;** An emulator whose source code doubles as documentation for thousands of arcade boards, computers, consoles and calculators, built to preserve old hardware.

MAME stands for Multiple Arcade Machine Emulator. It began with arcade cabinets and, after absorbing its sister project MESS, now also covers vintage computers, game consoles and calculators. The homepage says it emulates thousands of distinct hardware architectures.

The stated purpose is preservation: "MAME's purpose is to preserve decades of software history." Old hardware fails and the software on it goes with it. The README makes an unusual claim about how that works: "The source code to MAME serves as this documentation." Running software is mainly a way to check that the documentation is accurate. A game that plays correctly is evidence that the written description of the chips and boards is right.

That framing is what makes it a door into something larger. Each supported machine is a worked description of real hardware: its processors, memory maps, video and sound chips. Reading how a machine is described in the source is a way to learn how that machine actually worked.

The project is active, with roughly monthly releases. Recent news mentions additions such as NS32000-based machines, classic Mac OS on PowerPC, and A/UX.

## Install

```
brew install mame

MAME emulates hardware, so the software for a machine (ROMs, disk images) is separate. The pages behind this entry do not say where to get it or how first run works, so check the docs on mamedev.org.
```

## Try this

```
mame --help
```
Prints the command-line usage, a first look at the options the emulator accepts.

## What's unique

The source code is treated as the specification of the hardware, and running software is the test that the spec is right. Preservation, not play, is the stated goal.

## Caveats

The pages read do not explain where to obtain software for the emulated machines, so a first run may need some digging in the docs.

## Links

- [Homepage (MAMEdev.org)](https://mamedev.org/)
- [Source code on GitHub (README)](https://github.com/mamedev/mame)
- [Compiling MAME docs page](http://docs.mamedev.org/initialsetup/compilingmame.html)
