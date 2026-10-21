---
name: joyce
title: Joyce
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, amstrad, cp/m, emulator, retro, z80]
homepage: https://www.seasip.info/Unix/Joyce/index.html
scout_score: 8
status: draft
---

# Joyce

**TLDR;** An emulator of the Amstrad PCW, a 1980s all-in-one word processor that ran CP/M, kept alive with a deep archive of documentation.

JOYCE emulates the Amstrad PCW, a British word-processor appliance sold with a screen, keyboard, disc drive and printer in one box. It runs on Unix, Windows and Mac OS X and is written with SDL. It emulates the PCW's hardware, including a Z80 processor, so the machine's CP/M environment boots and runs the original software.

It works with PCW disc images in DSK format, and it can map host folders as emulated drives. Host joysticks are supported. Printer output can be written to PDF or PNG files, though the homepage places those features in the development releases. It also bundles ANNE, an emulator of the later PcW16, a different machine.

The project is John Elliott's, and the homepage gives no mission statement. It is framed around keeping the machine and its software usable, and the site carries a large reference archive of PCW hardware, file formats and public-domain software catalogues. The idea underneath is that an emulator doubles as documentation: to make old software run, someone had to write down exactly how the machine behaved.

One detail from the release notes: the author recommends upgrading if you run CP/M programs downloaded from the Internet, because a security fix stops malicious CP/M programs from touching host files.

## Install

```
brew install joyce
# installs the executables dskconv, dsklabel, lsgotek, xanne and xjoyce
# depends on libdsk, libpng and sdl12-compat; you need PCW disc images (DSK format) to have something to run
```

## Try this

```
xjoyce --help
```
Lists the command-line options for the PCW emulator.

```
xanne --help
```
Shows the options for ANNE, the bundled PcW16 emulator.

```
dskconv --help
```
Shows how to convert between disc image formats.

## What's unique

It emulates the hardware of a 1990s word-processor appliance that also ran CP/M, and it ships alongside an unusually deep archive of the machine's documentation.

## Caveats

Stable (2.4.2) and development (2.5.x) branches differ, newer features like PDF/PNG printing are in development releases, and the Gem Drive and Flash Drive hardware is not emulated.

## Links

- [JOYCE homepage (seasip.info)](https://www.seasip.info/Unix/Joyce/index.html)
