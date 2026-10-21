---
name: libopenmpt
title: libopenmpt
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, library, modules, quick, retro, tracker]
homepage: https://lib.openmpt.org/libopenmpt/
scout_score: 5
status: draft
---

# libopenmpt

**TLDR;** A library and terminal player, openmpt123, that decodes tracker module music files, the compact song format of the demoscene and old PC games.

libopenmpt decodes tracked music files, usually called modules, into a raw PCM audio stream. A module is a song stored as note patterns plus the small samples that play them, rather than as recorded audio. The library takes a module file and hands decoded samples to a host program to play or process.

It is based on the player code of OpenMPT, the Open ModPlug Tracker. In the homepage's words: "In order to avoid code base fragmentation, libopenmpt is developed in the same source code repository as OpenMPT." The tracker and the library share one player, so a module should sound the same in both.

The Homebrew formula also installs openmpt123, which the homepage describes as "a cross-platform command-line or terminal based module file player." That is the quick way in: point it at a module file and listen. The deeper door is the format family itself. Tracker music is a distinct culture with decades of files, and a decoder like this is what keeps those files playable.

The library has a libmodplug-compatible layer, libopenmpt-modplug, so older software written against libmodplug can use it. A wiki page lists many players and language bindings built on top.

## Install

```
brew install libopenmpt
# installs the openmpt123 player; you need a module file (.mod, .xm, .it, .s3m) to play
```

## Try this

```
openmpt123 --help
```
Lists the player's options and the audio output and file format choices it supports.

## What's unique

It reuses the player code of the OpenMPT tracker instead of maintaining a separate decoder, so playback follows a living tracker. It also offers a libmodplug-compatible layer for older software.

## Caveats

It is a library first, with openmpt123 as a companion player, and you must supply your own module files; the brief did not cover install or build details beyond the brew formula.

## Links

- [libopenmpt and openmpt123 homepage](https://lib.openmpt.org/libopenmpt/)
