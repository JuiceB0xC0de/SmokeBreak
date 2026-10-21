---
name: libaribcaption
title: libaribcaption
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, broadcast, c++, captions, library, protocol]
homepage: https://github.com/xqq/libaribcaption
scout_score: 5
status: draft
---

# libaribcaption

**TLDR;** A C++ library that decodes and renders ARIB STD-B24, the closed-caption system of Japanese digital TV, so video players can display captions as a television does.

libaribcaption is a portable C++17 library with a C API. It decodes ARIB STD-B24 captions, the caption format used in Japanese ISDB broadcasting, and renders them as graphics. It is meant to be embedded in video players rather than run on its own. The README points to an ffmpeg-based sample, which suggests the caption data comes from a demuxed broadcast stream, but it does not name the input format.

The README says why it exists: "Though ISDB-based TV broadcasting has been operating for about 20 years, ARIB based caption is still lacking support in general players." The aim is to render ARIB captions "with the same effect (or even better) as Television." Supported variants are Japanese (ARIB JIS), Latin (ABNT NBR 15606-1) and Philippine UTF-8.

The interesting part is how far a broadcast caption system sits from plain subtitles. ARIB captions use additional symbols called gaiji and custom glyphs called DRCS, and the library ships a built-in table that maps known DRCS characters to alternative Unicode. Text drawing is pluggable: DirectWrite on Windows, CoreText on macOS and iOS, FreeType and Fontconfig elsewhere, with font fallback built in. It credits aribb24, aribb24.js and TVCaptionMod2 as inspirations.

This is a library, so there is no command to run. The entry point is building it, reading the headers, and linking a small C program against it. It is a door into a broadcast standard few people outside Japan ever see.

## Install

```
brew install libaribcaption
# Library only, no executables. Building from source needs CMake 3.28+ and a C++17 compiler. On Linux it needs libfreetype and libfontconfig. A Japanese font such as Rounded M+ 1m for ARIB is recommended for good rendering.
```

## Try this

```
cmake .. -DCMAKE_BUILD_TYPE=Release
```
Configures a Release build from inside a build/ directory in the cloned source.

```
cmake --build . -j8
```
Compiles the library with 8 parallel jobs, producing a static library by default.

```
gcc main.c -o main `pkg-config --cflags --libs --static libaribcaption`
```
Links your own C program against the static library through pkg-config.

## What's unique

It is one of the few portable, MIT-licensed ARIB decoders that also includes a renderer, and on Windows and macOS it needs no third-party dependencies by default.

## Caveats

It is a library with no executables, the README gives no release dates so recent activity is unconfirmed, and the input container format is not stated.

## Links

- [libaribcaption on GitHub](https://github.com/xqq/libaribcaption)
- [ARIB STD-B24 specification (English page)](https://www.arib.or.jp/english/std_tr/broadcasting/std-b24.html)
- [aribb24, an inspiration cited in the README](https://github.com/nkoriyama/aribb24)
