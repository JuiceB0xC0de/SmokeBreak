---
name: ucon64
title: uCON64
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cli, emulation, file-formats, retro, reverse-engineering, rom]
homepage: https://ucon64.sourceforge.io/
scout_score: 5
status: draft
---

# uCON64

**TLDR;** A command-line Swiss Army knife for video game ROM dumps: it identifies, patches, converts and checks cartridge files from dozens of old consoles.

uCON64 reads ROM and SRAM files from consoles, handhelds and arcade systems and prints verbose information about each one. It can also rewrite and modify ROMs, apply patch formats (IPS, APS, BSL, PPF, Game Genie), and create or check RomCenter DAT files to spot bad dumps. The homepage calls it "the backup tool and wonderful emulator's Swiss Army knife program".

The unusual part is the physical side. Its homepage lists support for many cartridge backup units, flash carts and Nintendo 64 and Game Boy devices, so the same tool that identifies a file can also copy ROMs and SRAM to and from real carts. Each of these has its own option, such as --xfal for the Flash Advance Linker, --xmd for the MD-PRO and --xlit for the Atari Lynx Lynxit unit.

The idea underneath is that every old console invented its own file layout: headers, interleaving, bank sizes, checksums. A tool that knows many of them is a quiet tour of how cartridge data was actually arranged. DAT files add another idea: a known-good checksum database tells you whether your dump is a faithful copy.

The project is open source under the GPL and has been ported to many platforms with code from various people.

## Install

```
brew install ucon64
# After the first run, check $HOME/.ucon64rc for configuration.
# You can copy or move DAT files into $HOME/.ucon64/dat.
# Backup-unit features need the hardware, and often extra loader files from the homepage.
```

## Try this

```
ucon64 --help
```
Prints the full option list, which shows how many consoles, patch formats and backup devices it covers.

```
ucon64 --mkdat=DATFILE
```
Generates a DAT file from your ROMs, per the homepage's DAT section. Pass your ROM files along with it.

## What's unique

Few ROM tools cover both the file side (identify, patch, check against DATs) and the physical copier side, with support for many cart backup units in one program.

## Caveats

The homepage's newest news item is 2.2.2 from November 2021, and many backup-unit features need old hardware, Windows drivers, DOS extenders or separate loader downloads.

## Links

- [uCON64 homepage](https://ucon64.sourceforge.io/)
- [emulationrealm.net (linked from the homepage for more DAT files)](https://emulationrealm.net/)
