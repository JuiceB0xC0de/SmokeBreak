---
name: libltc
title: libltc
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, c, library, smpte, timecode]
homepage: https://x42.github.io/libltc/
scout_score: 5
status: draft
---

# libltc

**TLDR;** A small C library that turns audio into SMPTE timecode and back, using the Manchester-biphase buzz that film and video gear records onto an audio track.

Linear (or Longitudinal) Timecode, LTC, is timecode data encoded as a Manchester-biphase audio signal. Film and video gear has long recorded it on an audio track so that cameras, tape machines and recorders can agree on what time it is. libltc decodes that signal from audio samples into HH:MM:SS:FF frames, and encodes timecode values back into audio samples.

On the decode side it takes 8-bit unsigned samples and returns LTC frames, each tagged with the audio sample positions where it starts and ends. A signal tracker recovers the bit stream and maps the 80 LTC bits to timecode, including SMPTE date support. It follows speed variations and reverse-played tape. The encoder takes a speed parameter and can step timecode forward or backward.

The author wrote it as the successor to libltcsmpte, whose API and ABI had problems from early design choices. The new design is deliberately narrow: libltc works on LTC frames only and stays ignorant of framerate and timecode semantics, which the author says belong to the application or to the separate libtimecode project. The idea underneath is that time can travel as a sound, and a few hundred lines of C can pull it back out.

It is a library, not an application, so it installs no commands. The self-tests and example code in the source tree double as the way to see it work.

## Install

```
brew install libltc
# This installs a library and headers only, with no executables. To run the examples, build from a release tarball with a C toolchain and autotools: ./configure && make && make check
```

## Try this

```
./configure
```
Prepares the build from a release tarball using the standard autotools step.

```
make
```
Builds libltc.

```
make check
```
Compiles and runs the self-test scenarios and example code, which the README says also serve as examples.

## What's unique

Most LTC tools are tied to a frame rate or a particular application. libltc strips out timecode semantics, works only on LTC frames, and handles vari-speed and reverse-played LTC as a deliberate part of its API.

## Caveats

The core accepts only 8-bit unsigned samples, needs signals above about -36 dB, and the brief could not confirm when the project was last active; the homepage shows version 1.3.2 with docs dated September 2022.

## Links

- [Project homepage and API docs](https://x42.github.io/libltc/)
- [GitHub repository](https://github.com/x42/libltc)
