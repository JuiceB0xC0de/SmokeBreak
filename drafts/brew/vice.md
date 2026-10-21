---
name: vice
title: VICE
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, commodore, emulator, gui, retro, sid]
homepage: https://sourceforge.net/projects/vice-emu/
scout_score: 7
status: draft
---

# VICE

**TLDR;** A family of emulators for Commodore's 8-bit computers, from the C64 to the PET, with tools for disk images, cartridges and SID music.

VICE is a collection of emulators for Commodore's 8-bit machines. The project lists the C64, C64DTV, C128, VIC20, practically all PET models, the PLUS4 and the CBM-II, plus a separate emulator for a C64 with the CMD SuperCPU. Each machine gets its own program: `x64sc` for the C64, `x128`, `xvic`, `xpet`, `xplus4` and so on. You feed it Commodore program, disk, tape or cartridge files, and it gives you the machine's screen and sound.

The helper tools are the part that opens things up. `c1541` works with disk images, `cartconv` converts cartridge files, `petcat` turns BASIC text into tokenised programs and back, and `vsid` plays SID music files without the rest of the machine. Together they let you look inside the file formats these computers used, not just run them.

The project also offers a binary monitor interface, which it describes as stable and which other projects use to build debuggers and IDE integrations. That makes VICE a practical target for writing and debugging code for hardware that is decades old. One user review calls the emulation cycle-exact with strong SID sound, but that is the reviewer's claim, not the project's.

Development is volunteer-run in spare time, and the site says: "We always need more help to keep all things going, so here is the usual call for volunteers... ;-)"

## Install

```
brew install vice
# GUI application (GTK3); no account or hardware needed. The brief does not cover ROM or first-run setup.
```

## Try this

```
x64sc --help
```
Lists the command-line options of the C64 emulator.

```
c1541 --help
```
Shows how the disk image tool is used.

```
petcat --help
```
Shows the options for converting between BASIC text and tokenised program files.

## What's unique

One package covers many Commodore machines, including a PET family few emulators touch, and it ships tools for the file formats and a binary monitor interface that outside debuggers build on.

## Caveats

The executable names are cryptic (x64sc, xscpu64, x64dtv), and some reviews describe confusing file-loading dialogs and settings problems in earlier releases.

## Links

- [SourceForge project page](https://sourceforge.net/projects/vice-emu/)
- [VICE project site](https://vice-emu.sourceforge.io/)
- [Bug tracker](https://sourceforge.net/p/vice-emu/bugs/)
