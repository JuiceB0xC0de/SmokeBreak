---
name: adplay
title: adplay
source: brew
category: sound-and-live-coding
commitment: quick
tags: [adlib, audio, dos, opl2, quick, retro]
homepage: https://adplug.github.io
scout_score: 6
status: draft
---

# adplay

**TLDR;** A terminal player for 1990s AdLib and Sound Blaster OPL2 music files, using an emulated Yamaha chip, so no sound card is needed.

adplay is the console front end to AdPlug, a library that plays AdLib music from its original file formats. The homepage lists over 60 of them, including A2M, CMF, D00, RAD, S3M and ROL, taken from DOS games and trackers. You give it one or more files and it plays them.

The interesting part is what it does not do. AdPlug has a separate replayer for each format, so every game or tracker file is interpreted by its own rules instead of being converted to MIDI or WAV first. The replayers produce OPL2 register writes, the same kind of instructions a game once sent to the sound chip, and those go to a software emulator of the chip. In the project's words, "No OPL chip is required for playback."

That makes it a small door into how early PC sound worked. The music is not recorded audio. It is a stream of settings for a simple FM synthesis chip, which is why these tunes have such a recognisable sound. The README says the UNIX player supports only emulated output, though the library itself can drive real hardware.

## Install

```
brew install adplay
```

## Try this

```
adplay --help
```
Lists the command-line options, including the choice of output device. The README says the man page covers them too.

## What's unique

It plays the original files of 1990s DOS games and trackers directly, through per-format replayers and a software OPL2, with a far wider format list than most players of this kind.

## Caveats

The README admits the documentation is thin, and you need to supply your own OPL2 music files, since the brief mentions none bundled.

## Links

- [AdPlug homepage](https://adplug.github.io)
- [AdPlay/UNIX repository and README](https://github.com/adplug/adplay-unix)
- [AdPlug core repository](https://github.com/adplug/adplug)
