---
name: openmsx
title: openMSX
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, debugger, emulator, gui, msx, retro, tcl]
homepage: https://openmsx.org/
scout_score: 7
status: draft
---

# openMSX

**TLDR;** An emulator for the MSX, a 1980s home computer standard, built to be accurate down to chip timing, with a debugger and Tcl scripting.

openMSX emulates the MSX, a home computer standard from the 1980s, along with many hardware variants and extensions. It runs software from emulated cartridges, disk images and tapes. Its release history also covers related machines: the Spectravideo SVI-318/328, ColecoVision and Sega SG-1000.

The project describes itself as "the MSX emulator that aims for perfection". Release notes mention cycle-accurate VDP (video chip) timing, floppy accuracy and chip-level details. That focus makes it more than a way to run old games: it is a model of how the hardware actually behaved, quirks included.

That accuracy makes it a good place to look inside an old machine. It has a built-in debugger, and a graphical interface (added in 20.0) for configuring the emulated computer. Version 21.0 added "setups", which save a whole machine configuration, such as a Philips VG 8020 with a disk drive, joystick, data recorder and printer, so it can start automatically. Tcl scripting is built in, and the release notes mention reverse/rewind and TAS scripts.

The emulator also has a niche standing: it is one of the few MSX emulators approved for tool-assisted speedrun work on tasvideos.org, approved in 2010.

## Install

```
brew install openmsx
# Needs a system with OpenGL 2 or later. You will also need MSX software or system ROMs to run anything meaningful; the brief does not cover where to get them.
```

## Try this

```
openmsx --help
```
Prints the command-line options so you can see how to choose a machine and load media.

## What's unique

It puts accuracy first, down to VDP access timing and floppy copy protection, and pairs that with a debugger, rewind and Tcl scripting that TAS makers use.

## Caveats

It needs OpenGL 2 or later, and the brief found no documented commands beyond the manuals bundled in the source tree.

## Links

- [openMSX homepage](https://openmsx.org/)
- [openMSX source repository](https://github.com/openMSX/openMSX)
- [GitHub project page](https://github.com/openMSX/)
