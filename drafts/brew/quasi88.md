---
name: quasi88
title: QUASI88
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [8-bit, afternoon, emulator, japanese, pc-8801, retro, sdl2]
homepage: https://www.eonet.ne.jp/~showtime/quasi88/
scout_score: 6
status: draft
---

# QUASI88

**TLDR;** An SDL2 emulator for NEC's PC-8801, a Japanese 8-bit home computer, so you can run its software in a window with sound.

QUASI88 emulates the PC-8801, an 8-bit home computer from NEC that was popular in Japan. It runs the machine in a window with sound. It targets SDL2 on UNIX and Windows, so it should work wherever SDL2 does.

The emulator does not ship with software. You supply the machine's ROM files and disk images yourself, and it looks for them in `~/quasi88/rom/`, `~/quasi88/disk/` and `~/quasi88/tape/`. The `-romdir`, `-diskdir` and `-tapedir` options point it elsewhere. The Homebrew caveats do not name which ROM files are required.

The homepage says the emulator was written with reference to the fMSX source code. Its sound output section was ported from MAME and xmame, and it includes the fmgen FM sound generator by cisc. That lineage is a way into how 8-bit machines were emulated and how their FM sound chips were reproduced in software.

The project is current: the homepage lists version 0.7.4, released 2026/05/01. The homepage is in Japanese only, which is part of the appeal and part of the effort.

## Install

```
brew install quasi88
# Then place your own ROM and disk files in ~/quasi88/rom/, ~/quasi88/disk/ and ~/quasi88/tape/
# Needs PC-8801 ROM files and disk images that you supply; SDL2 is pulled in as a dependency.
```

## Try this

```
quasi88 --help
```
Prints the available options, including the directory overrides for ROMs, disks and tapes.

## What's unique

It is a PC-8801 emulator built on SDL2 for UNIX, which is an unusual target for this machine. It reuses sound code from MAME and xmame plus the fmgen FM generator.

## Caveats

You must provide ROM and disk files yourself, the homepage is entirely in Japanese, and macOS and Linux support is reported but unverified by the author's main platforms (Windows 11 and FreeBSD).

## Links

- [QUASI88 homepage](https://www.eonet.ne.jp/~showtime/quasi88/)
- [SDL (referenced by the homepage)](https://www.libsdl.org/)
