---
name: zvbi
title: zvbi
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, analog-tv, broadcast, closed-captions, library, teletext, vbi]
homepage: https://github.com/zapping-vbi/zvbi
scout_score: 5
status: draft
---

# zvbi

**TLDR;** A C library that pulls Teletext and closed captions out of the vertical blanking interval of analog TV signals, the hidden data lines above the picture.

In an analog TV signal, the electron beam has to fly back to the top of the screen between frames. That gap is the vertical blanking interval, and because nothing sent during it is displayed, broadcasters used it to carry other data. The README lists test signals, closed captioning and other digital data. ZVBI is the layer that captures and decodes that data.

It reads raw VBI from Linux V4L and V4L2 capture devices, FreeBSD BKTR devices, or Linux DVB devices. A proxy daemon, zvbid, lets several applications share one capture device. The library demodulates the raw samples into sliced data in software, then decodes services such as Teletext and Closed Caption. It also has a Teletext page cache with search, text export and rendering functions.

It was written for the Zapping TV viewer, and the README puts it this way: "Basically ZVBI offers all functions needed by VBI applications except for the user interface." That makes it a library first. The one tool in the Homebrew formula is zvbi-ntsc-cc, which handles NTSC closed captions.

The larger idea is that a video signal was never only a picture. Teletext pages and captions rode along in lines nobody saw, and reading the library is a way into how those forgotten broadcast data services were encoded.

## Install

```
brew install zvbi

Live capture needs a supported device: V4L/V4L2, BKTR, or a Linux DVB card. Building from source needs GNU autotools (git clone, ./autogen.sh, ./configure, make, make install).
```

## Try this

```
zvbi-ntsc-cc --help
```
Prints the options for the NTSC closed caption extractor, the one command-line tool the formula installs.

```
CONFIGURE=1 ./autogen.sh
```
When building from a cloned repo, generates the autotools files and runs configure in one step.

```
make check
```
Runs the library's test suite after building from source.

## What's unique

It is a reusable decoding library, not an app. It covers raw capture, software demodulation and decoding of old broadcast data services like Teletext in one place, and includes a proxy for sharing a capture device.

## Caveats

It is a library with no user interface, the README barely explains zvbi-ntsc-cc, and seeing real data needs analog or DVB capture hardware; it is tested only on Linux and FreeBSD.

## Links

- [Homepage / repository](https://github.com/zapping-vbi/zvbi)
- [INSTALL file](https://github.com/zapping-vbi/zvbi/blob/main/INSTALL)
- [Perl bindings (Video::ZVBI)](https://search.cpan.org/~TOMZO/Video-ZVBI)
