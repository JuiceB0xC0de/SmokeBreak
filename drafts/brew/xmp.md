---
name: xmp
title: xmp
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, demoscene, quick, retro, tracker, tui]
homepage: https://xmp.sourceforge.net/
scout_score: 7
status: draft
---

# xmp

**TLDR;** A terminal player for tracker music files like MOD, S3M, XM and IT, the sample-and-pattern formats of the demoscene, with per-channel muting.

xmp, the Extended Module Player, plays tracker modules: small files that hold a song as patterns of notes plus the samples or instruments used to play them. Give it a Protracker .mod, a Scream Tracker .s3m, a Fast Tracker II .xm or an Impulse Tracker .it, and it renders the song to audio. The homepage says it handles many mainstream and obscure formats, including Amiga, Atari and Acorn ones.

The terminal screen shows the module name, type, pattern and channel counts, duration and a live position readout. Single keypresses skip between patterns and songs, mute individual channels, and show instrument and sample lists. That makes it behave a bit like a tracker's own view of a song, so you can solo the bassline or see what a sample was called.

Since release 4.0 the project is split in two. libxmp is a library that loads a module and renders it to linear PCM at a rate and format the caller picks. xmp is the player built on top of it. The author wants the library reused elsewhere, for example in players, information extractors, module-to-mp3 renderers and game music. The homepage frames the whole thing as preservation of music that the demoscene trackers produced, and points to archives such as Modland and Aminet for files to play.

xmp can also read compressed modules, with built-in depackers for formats such as zip, gzip, xz and LHA. In an archive it plays only the first module.

## Install

```
brew install xmp
# pulls in libxmp; no accounts or special hardware needed. You need a module file to play, e.g. from Modland or Aminet.
```

## Try this

```
xmp -L
```
Lists every module format this build can play.

```
xmp m5v-nwlf.itz
```
Plays the homepage's example Impulse Tracker module, printing its header info and a live status line. Press h for help.

```
xmp --help
```
Lists the command-line options, including --nocmd to turn off interactive mode.

## What's unique

It covers a very wide range of obscure tracker formats and packers. Its interactive controls (pattern skip, channel mute, instrument and sample dumps) are unusual for a command-line player.

## Caveats

A few incomplete formats such as DTT and DMF were disabled in recent releases, MO3 and RAR need external helpers, and the homepage and README list different interactive keys, so check the README.

## Links

- [Homepage (Extended Module Player)](https://xmp.sourceforge.net/)
- [xmp-cli on GitHub (README)](https://github.com/libxmp/xmp-cli)
- [libxmp on GitHub](https://github.com/libxmp/libxmp)
