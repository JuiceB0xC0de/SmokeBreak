---
name: libmysofa
title: libmysofa
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, c, hrtf, library, spatial-audio]
homepage: https://github.com/hoene/libmysofa
scout_score: 7
status: draft
---

# libmysofa

**TLDR;** A small C library that reads SOFA files of head-related transfer functions, so you can ask how a sound from any direction reaches each ear.

libmysofa reads AES SOFA files, the AES69-2015 standard for storing head-related transfer functions (HRTFs). An HRTF is a pair of filters, one per ear, that describes how a sound from a given direction is changed by a head, ears and shoulders. Apply them to ordinary audio and it seems to come from outside your head, which is the basis of binaural spatial audio.

You give the library a .sofa file (or a buffer already in memory) and a target sample rate. Then you ask for a position as [x,y,z]. It returns left and right impulse responses plus left and right delays. It builds a nearest-neighbour search over the measurement grid. It can interpolate between neighbouring measurements or return the exact stored filter. Your code then applies the delays and convolves the audio with the impulse responses.

The author wrote it to support MySofa, work on designing personal HRTFs, since a filter measured on your own head tends to localise better than a generic one. The idea underneath is that hearing direction is mostly filtering, and a SOFA file is a lookup table of those filters. This makes it a good door into how ears localise sound.

It is a library rather than a program. The formula also installs an executable called mysofa2json, but the README does not describe it.

## Install

```
brew install libmysofa
# To build from source instead you need CMake, a C compiler, zlib headers and CUnit. No hardware or account is needed, but you need a .sofa file to read.
```

## Try this

```
mysofa2json --help
```
Prints whatever usage the tool offers. The README does not document it, so this is the safest way to see what it does.

```
ctest -j8
```
Runs the test suite from a source build, which exercises reading real SOFA data.

## What's unique

It goes beyond parsing the file and gives a ready lookup: ask for a direction and it returns an interpolated filter with delays. It also has a cached open that shares one copy of an HRTF across handles.

## Caveats

Activity is hard to confirm from the README, which still mentions Ubuntu 14.04 CI and has references from 2017, and mysofa2json is undocumented there.

## Links

- [GitHub repository (homepage)](https://github.com/hoene/libmysofa)
- [MySofa project site](https://mysofa.audio/)
- [AES Convention Paper 9764, MySofa: Design Your Personal HRTF](http://www.aes.org/e-lib/browse.cfm?elib=18640)
