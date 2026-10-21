---
name: libansilove
title: libansilove
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ansi-art, bbs, c, library, png]
homepage: https://www.ansilove.org
scout_score: 6
status: draft
---

# libansilove

**TLDR;** A small C library that turns BBS-era ANSI art and related text-mode formats into PNG images, the engine behind the Ansilove converter.

libansilove reads the file formats that the 1990s BBS art scene used for text-mode pictures: ANSi (.ANS, including PabloDraw 24-bit color sequences), PCBoard (.PCB), raw text-mode video memory (.BIN), Artworx (.ADF), iCE Draw (.IDF), TundraDraw (.TND) and XBin (.XB). It draws the characters onto a canvas and writes a PNG through the GD graphics library.

These files are not images. They are streams of characters and escape sequences that were meant to be replayed on a terminal, with a specific font and palette. To render one faithfully, the loaders have to parse the escape codes, apply the font data and palette, and read SAUCE metadata. The changelog shows the loaders moved to state machines and got format validation and fuzzing, because these are untrusted files from a very old scene.

The code was split out of Ansilove/C 3.0.9, with almost 200 commits since, so it could be a reusable library instead of part of one converter. The homepage says Ansilove goes back to 2003. The library has bindings for Racket and is used by a PS3 viewer, PixelView and Abydos.

This is a library, not a program. The command-line converter, Ansilove, is built on top of it. The README points to an example directory for how to call it, and there is no separate API reference.

## Install

```
brew install libansilove
# installs a library only, no executables. Building from source needs a C compiler, CMake and GD with headers:
# brew install cmake gd
# mkdir build && cd build && cmake .. && make && make install
```

## Try this

```
brew install cmake gd
```
Installs the build dependencies the README lists for macOS, if you want to build from source.

```
cmake ..
```
Run from a build directory inside the cloned repo, this configures the library build.

```
make
```
Compiles the library after configuring, ready for make install.

## What's unique

It is one small C library covering the main BBS-era art formats, split out of a converter that has existed since 2003. Other tools can reuse it, which is why it shows up in viewers and language bindings.

## Caveats

It is a library with no command-line tool, and the README documents usage only through an example directory, so you need to write C or use the separate Ansilove converter to see output.

## Links

- [Project homepage](https://www.ansilove.org)
- [libansilove GitHub repository](https://github.com/ansilove/libansilove)
- [Ansilove converter (built on libansilove)](https://github.com/ansilove/ansilove)
