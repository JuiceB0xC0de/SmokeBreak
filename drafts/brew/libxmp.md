---
name: libxmp
title: libxmp
source: brew
category: sound-and-live-coding
commitment: quick
tags: [ancient, audio, library, preservation, quick, tracker]
homepage: https://xmp.sourceforge.net/
scout_score: 7
status: draft
---

# libxmp

**TLDR;** A C library that renders tracker module music (MOD, S3M, XM, IT and 90-plus other formats) into raw audio, keeping decades-old Amiga and PC songs playable.

Libxmp loads a tracker module file and renders it as linear PCM samples into a buffer, at whatever rate and format the calling program asks for. It is a library, not a player. Players, module information extractors, module-to-mp3 renderers and game soundtracks are the uses the homepage names.

Tracker modules are an old way of making music. Instead of a recorded waveform, a file holds small instrument samples plus a grid of patterns that says which note triggers which sample on which channel, and with which effect. The format started on the Amiga with Protracker MOD and spread to PC trackers like Scream Tracker 3 (S3M), Fast Tracker II (XM) and Impulse Tracker (IT). Playing one correctly means reproducing the quirks of the original replayer. Libxmp does this by choosing a replayer style per file. Protracker MODs get a mix of Protracker 2/3 behaviour, other 4-channel Amiga MODs get a Noisetracker/Protracker-style replayer, and multichannel MODs get a Fasttracker II style one.

It also reads obscure Amiga, Atari, Acorn and PC formats, many Amiga packers, and compressed archives (gzip, bzip2, zip, LZX built in; MO3 and RAR via external helpers). The project's own framing is preservation of classic and rare modules.

The Homebrew formula installs only the library. To hear anything you want the separate xmp command-line player, which is built on libxmp.

## Install

```
brew install libxmp
# library only, no executables. The xmp command-line player is a separate package (github.com/libxmp/xmp-cli) and needs libxmp 4.4.0 or newer, 4.7.0 or newer recommended.
# MO3 and RAR modules need the external helpers unmo3 and unrar.
```

## Try this

```
xmp m5v-nwlf.itz
```
With the separate xmp player installed, plays an Impulse Tracker module and shows its name, type, pattern and channel counts, and playback position. Press 'h' for help.

## What's unique

It is a portable, embeddable renderer covering an unusually wide range of tracker formats, including obscure Amiga, Atari and Acorn ones that most modern players skip. A MIT-licensed 'lite' build covers MOD, S3M, XM and IT for games and embedded use.

## Caveats

It is a library with no executable of its own, so you need xmp-cli or your own C code to hear anything; only the first module in an archive plays, and a few formats such as DTT and DMF were disabled in recent releases.

## Links

- [Homepage (Extended Module Player)](https://xmp.sourceforge.net/)
- [libxmp GitHub repository and README](https://github.com/libxmp/libxmp)
- [xmp-cli player GitHub repository](https://github.com/libxmp/xmp-cli)
