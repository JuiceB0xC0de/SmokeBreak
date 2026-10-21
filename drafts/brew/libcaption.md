---
name: libcaption
title: libcaption
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, closed-captions, h264, library, protocol, video]
homepage: https://github.com/szatmary/libcaption
scout_score: 5
status: draft
---

# libcaption

**TLDR;** A small C library that writes and reads CEA-608 and CEA-708 closed captions, the hidden caption data riding inside broadcast video.

libcaption is a C library for creating and parsing closed-caption data. For CEA-608 it handles the control and preamble codes plus the Basic North American, Special North American, and Extended Western European character sets, in both directions. For CEA-708 it only encodes, by placing 608 data inside an NTSC field 1 user data structure.

It also includes helpers that wrap a 708 payload into an H.264 SEI NAL unit and unwrap it again. The wrapping is fiddly: a three-byte prefix (nal_unit_type 6, payloadType 4, and a variable payload size), a stop byte of 127, and an emulation prevention byte (3) inserted whenever the payload would otherwise contain the start code 0,0,1.

The README says the aim is to help community-developed broadcast tools handle captions consistently across platforms. It implements a deliberately narrow subset of EIA-608 and CEA-708, chosen to match what Apple iOS supports.

The idea underneath is that captions are not a separate subtitle file. They are a byte stream tucked into the video itself, in a place decoders know to look. Reading this library is a compact way to see how that works, from legacy analog-era 608 codes to modern H.264 containers.

## Install

```
brew install libcaption
# From source on macOS or Linux: needs git, cmake, a C compiler; re2c and ffmpeg are optional
# cmake . && make && sudo make install
```

## Try this

```
cmake . && make
```
Builds the library from a source checkout with re2c enabled, the default.

```
cmake -DENABLE_RE2C=OFF . && make
```
Builds the library without re2c, for machines that do not have it.

```
sudo make install
```
Installs the built library and headers system-wide on macOS or Linux.

## What's unique

It targets a narrow 608/708 subset matched to Apple iOS, so output behaves the same across platforms. It also bundles the H.264 SEI NAL wrapping step, which most caption tooling handles separately.

## Caveats

It is a library with no executables, so you need to write C to use it; 708 is encode-only, 608 coverage is partial, Windows is untested, and the brief could not confirm when it was last updated.

## Links

- [GitHub repository (README)](https://github.com/szatmary/libcaption)
