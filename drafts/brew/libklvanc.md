---
name: libklvanc
title: libklvanc
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, broadcast, library, needs-hardware, protocol, sdi, vanc, video]
homepage: https://github.com/stoth68000/libklvanc
scout_score: 6
status: draft
---

# libklvanc

**TLDR;** A C library and set of small tools for decoding and generating VANC, the hidden ancillary data (captions, ad cues, timecode) carried inside broadcast SDI video.

Broadcast video travelling over SDI cable carries more than pictures. In the lines above and below the visible frame sits Vertical Ancillary Data, or VANC: closed captions, aspect-ratio hints, ad-insertion triggers, timecodes and HDR metadata, all packed into small checksummed packets. Libklvanc parses those lines into structured packets, and can encode packets back into VANC lines for an SDI output.

The README lists a long set of formats: CEA-708 captions (SMPTE ST 334), AFD and Bar Data (ST 2016), SCTE-104 ad triggers, ST 2038 arbitrary VANC encapsulation, ST 12-2 timecodes, RDD 8 subtitle packets and ST 2108-1 HDR/WCG metadata. It validates checksums at several levels and handles line-formatting edge cases such as keeping packets contiguous. It also has helpers for colour formats such as V210, used by Blackmagic DeckLink cards.

The idea underneath is that a video signal is a carrier with side channels. Once you see that a frame has room for a second, data-only stream, a lot of broadcast plumbing makes sense: how a station knows when to cut to an ad, or how captions travel with the picture. The library is meant to sit beneath real capture tools. The separate klvanc-tools project pairs it with Blackmagic cards to capture live SDI.

The package installs a set of executables, such as klvanc_parse, klvanc_scte104 and klvanc_afd. The README does not describe them, so they are best explored through their own help output.

## Install

```
brew install libklvanc
# Real SDI capture needs Blackmagic hardware and the separate klvanc-tools project. The library alone needs no hardware or account.
```

## Try this

```
klvanc_parse --help
```
Shows the options of the general VANC parsing tool installed with the library.

```
klvanc_scte104 --help
```
Shows the options of the SCTE-104 ad-trigger tool.

```
klvanc_util --help
```
Lists what the general utility executable can do.

## What's unique

It handles both directions, decoding captured VANC and generating it for output, across many SMPTE and SCTE ancillary formats in one library. Many tools only decode, or only cover one protocol.

## Caveats

Real-world use needs SDI capture hardware such as Blackmagic cards, and the brief could not confirm project activity or what the bundled executables do.

## Links

- [Homepage (GitHub repository)](https://github.com/stoth68000/libklvanc)
- [klvanc-tools (real-world capture application)](https://github.com/stoth68000/klvanc-tools)
