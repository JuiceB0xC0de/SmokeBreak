---
name: asar
title: asar
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, assembly, retro, reverse-engineering, rom-hacking, snes]
homepage: https://github.com/RPGHacker/asar
scout_score: 7
status: draft
---

# asar

**TLDR;** An assembler for the Super Nintendo's 65c816, SPC700 and Super FX chips, used to patch existing ROMs or build new ones from assembly source.

Asar takes assembly source, called a patch file, plus a ROM image, and writes the assembled bytes into the ROM. It targets three SNES-era processors: the 65c816 main CPU, the SPC700 audio chip, and the Super FX coprocessor. It can also build a ROM from scratch. The README does not spell out exactly how output files are handled, so check the manual before trusting it with your only copy of anything.

It was created by Alcaro and modelled after xkas v0.06 by byuu, an older assembler from the same scene. The README describes it as a tool for SNES patching and ROM creation, and it is the assembler the ROM hacking community uses for this work.

The interesting idea is the patch as a small, surgical edit to someone else's program. You do not rebuild a game, you overwrite a few bytes at chosen addresses with new instructions. That is a way into 65816 assembly, memory maps, and how old cartridge software was laid out.

Asar also has a built-in test syntax. Lines starting with ;` declare the bytes expected in the ROM after patching, and ;E>, ;W> and ;P> lines check errors, warnings and prints. A patch can carry its own regression checks inside the assembly source. Asar can also be built as a DLL or static library for embedding in other tools.

## Install

```
brew install asar
# You also need your own SNES ROM image to patch. Prebuilt binaries are on the GitHub Releases page, or build from source with CMake.
```

## Try this

```
asar --help
```
Prints the command-line usage. The README itself documents no command-line examples, so this is the quickest way to see the options.

## What's unique

Patches can embed their own tests, with expected ROM bytes, errors, warnings and prints written as comments in the assembly source. It is also the assembler the SNES ROM hacking community actually uses.

## Caveats

Project status is unclear (the README.txt path is labelled master_archived), the online manual is a stub pointing to other versions, and the docs mostly describe Windows usage.

## Links

- [GitHub repository (homepage)](https://github.com/RPGHacker/asar)
- [Releases](https://github.com/RPGHacker/asar/releases)
- [Online manual](https://rpghacker.github.io/asar/manual/)
- [Changelog](https://rpghacker.github.io/asar/changelog/)
