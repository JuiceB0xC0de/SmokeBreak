---
name: atari800
title: atari800
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, atari, emulator, retro, sdl, vintage-hardware]
homepage: https://atari800.github.io/
scout_score: 7
status: draft
---

# atari800

**TLDR;** A free emulator of the Atari 400/800, XL/XE computers and the 5200 console that runs disk, cartridge, tape and program images.

Atari800 emulates the Atari 8-bit home computers (400/800, XL/XE and related models) and the Atari 5200 console. You hand it files: disk images (ATR, XFD, ATX), programs (COM, EXE, XEX, BAS), cartridge images, cassette images (CAS) or saved emulator states. It runs them on an emulated machine with video, sound, joystick and mouse emulation. SDL2 is the recommended build for desktop use, but the source also targets curses text mode, X11, DOS, Amiga, Android and others.

The project began as David Firth's GPL emulator in 1995. No new versions appeared after 1997, so several developers picked up the v0.8.0 source and carried it forward. Petr Stehlik now maintains it. The homepage states the aim plainly: "Our main objective is to create a freely distributable portable emulator (i.e. with source code available)."

The door it opens is old hardware seen from the inside. The emulator covers a wide range of peripherals: 80-column boards, the XEP80, Voice Box, Black Box, MIO, and several mouse and light-pen types. It also has detailed NTSC artifacting and colour-adjustment options. Running the same software through different emulated configurations shows how much of that era's behaviour depended on the exact machine, the OS ROM, and even the TV.

The formula also installs a second executable named cart. The brief did not find it described anywhere, so this entry does not say what it does.

## Install

```
brew install atari800
# Some OS and hardware features need ROM images the project does not ship. Supply them with -osa_rom, -osb_rom, -xlxe_rom, -5200_rom and -basic_rom.
```

## Try this

```
atari800 --help
```
Prints the command-line options so you can see what the emulator can be told to do.

```
atari800 -run <filename>
```
Runs an Atari program file (EXE, COM, XEX, BAS or LST) on the emulated machine.

```
atari800 -turbo <disk image>
```
Mounts the disk image in drive 1 and runs the emulator at maximum speed. F12 toggles turbo at runtime.

## What's unique

One program covers a very wide range of Atari 8-bit hardware and peripherals, from the 5200 console to the XEP80 and Black Box. Its NTSC artifacting and colour options are unusually detailed.

## Caveats

Some OS and hardware features need ROM images you must supply yourself, and tape support is limited to standard 600 baud without copy-protected tapes.

## Links

- [Project homepage](https://atari800.github.io/)
- [GitHub repository](https://github.com/atari800/atari800)
- [Usage and key mappings (DOC/USAGE)](https://github.com/atari800/atari800/blob/master/DOC/USAGE)
