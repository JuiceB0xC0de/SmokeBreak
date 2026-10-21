---
name: uade
title: UADE
source: brew
category: sound-and-live-coding
commitment: quick
tags: [amiga, audio, chiptune, emulation, quick, retro, tracker]
homepage: https://zakalwe.fi/uade/
scout_score: 8
status: draft
---

# UADE

**TLDR;** Plays more than 200 old Amiga music formats by running the original Amiga player code inside a 68k CPU emulator, from the command line.

UADE, the Unix Amiga Delitracker Emulator, plays music files from the Amiga era on modern Unix-like systems. You give it a tracker or chiptune file and it plays audio. The project page describes it as covering 200+ Amiga computer music formats.

Most players decode each format with a fresh parser. UADE does not. It emulates the Amiga's m68k processor, built on the UAE emulation work, and runs the original player routines inside that emulated machine. Around them it provides a free reimplementation of the Eagleplayer and Delitracker player APIs, so code written for AmigaOS has the environment it expects.

The idea underneath is preservation by emulation. Amiga musicians and player authors wrote small programs that knew how to turn each format into sound. Rather than rewrite them, UADE keeps them alive and runs them as they were. In the project's words, "UADE makes these players reusable on modern platforms." That makes it a way to hear how the Amiga itself would have rendered a song, and an entry point into the Eagleplayer and Delitracker ecosystem.

The brew formula installs three executables: uade123, a command-line player, bencat, and a script called mod2ogg2.sh. The brief did not cover what the last two do, so check their help output before relying on them.

## Install

```
brew install uade
# depends on libao for audio output; the brief did not cover first-run configuration
```

## Try this

```
uade123 --help
```
Prints the command-line player's options so you can see how to point it at an Amiga music file.

## What's unique

It runs the original Amiga player code under 68k emulation instead of decoding each format itself, and it covers a very large number of obscure tracker formats.

## Caveats

The brief found no usage examples, and sources disagree on the license (GPL on the homepage, LGPLv2.1 on GitLab); you will also need your own Amiga music files.

## Links

- [Homepage](https://zakalwe.fi/uade/)
- [GitLab project](https://gitlab.com/uade-music-player/uade)
