---
name: adplug
title: AdPlug
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [adlib, afternoon, audio, file-formats, library, opl, retro, reverse-engineering]
homepage: https://adplug.github.io
scout_score: 5
status: draft
---

# AdPlug

**TLDR;** A library that plays music from AdLib-era DOS games in dozens of original file formats, with no OPL sound chip required.

AdPlug reads music in the formats written for AdLib and Sound Blaster cards, such as IMF, CMF, RAD, S3M and ROL. It then produces audio by driving a software model of the Yamaha OPL2/OPL3 chip. It can also drive real OPL hardware if you have it. Each format gets its own replayer, "in order to achieve the best possible replay quality", according to the homepage.

The idea underneath is that these files are not recordings. They are instructions for a particular FM synthesis chip: which registers to set, when, and to what. Playing them faithfully means reproducing the chip and the quirks of each composer's tools. Every format in the list is a small piece of reverse engineering, and the library is a catalogue of how different DOS-era tools stored music.

The project describes itself as "just the backend to many different audio player frontends". Those include AdPlay/UNIX, AdPlay/DOS, and plugins for Winamp and XMMS. The emulator is WoodyOPL, an LGPL emulator from the DOSBox team. It replaced a MAME-derived one to keep the library cleanly LGPL.

The Homebrew formula installs one executable, `adplugdb`. The sources read for this entry do not describe it, so the library is the real subject here.

## Install

```
brew install adplug
# also pulls in libbinio. No hardware or account needed.
```

## Try this

```
adplugdb --help
```
Prints the usage text for the one executable Homebrew installs. The project's pages do not document it, so this is the way to find out what it does.

## What's unique

It covers a large, obscure set of AdLib-era formats, many with a dedicated replayer, and plays them with no OPL chip. The project has also been fuzzed and patched for buffer overflows in several format loaders.

## Caveats

It is a backend library, so you mostly hear music through a frontend such as AdPlay/UNIX, and the `adplugdb` tool is undocumented in the pages read; some formats like MKJ and VGM are marked preliminary.

## Links

- [Homepage](https://adplug.github.io)
- [GitHub repository](https://github.com/adplug/adplug)
- [libbinio](http://adplug.github.io/libbinio/)
