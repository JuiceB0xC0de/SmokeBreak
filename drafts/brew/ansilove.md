---
name: ansilove
title: ansilove
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [ansi, artscene, ascii-art, bbs, demoscene, png, quick]
homepage: https://www.ansilove.org
scout_score: 6
status: draft
---

# ansilove

**TLDR;** Turns old BBS-era ANSI and ASCII art files into PNG images, using the original DOS and Amiga fonts so they look the way they did on screen.

ansilove reads text-mode art files from the BBS and demoscene era (ANS, PCB, BIN, ADF, IDF, TND, XB and others) and writes them out as small 4-bit PNGs. It reads the SAUCE metadata record if one is present, and it can output Retina @2x or other scales.

The interesting part is that this art was never made of pixels. A file is a stream of characters, colour codes and escape sequences, and the picture only exists once something draws each character cell with a particular font. ansilove carries embedded PC and Amiga bitmap fonts so the result matches the original text modes rather than a generic monospace look. Options like `-b 9` for the 9th block column and `-m ced` for Amiga-style black-on-gray output reproduce specific hardware quirks.

The author started the project in 2003 to convert their own ASCII and ANSI artworks into PNGs for a demoscene gallery. This C version is a rewrite of the earlier AnsiLove/PHP, chosen to drop the PHP dependency, run faster, and let the parsing and rendering live in a reusable library, libansilove. The tool is by Frederic Cambus, Stefan Vogt and Brian Cassidy.

It also works as a SAUCE reader with `-s`, which is a handy way to see who made a file, what group it came from and which font it expects.

## Install

```
brew install ansilove
```

## Try this

```
ansilove --help
```
Prints the option summary: output file, font, column count, bit mode, scale factor and file type.

```
ansilove -o out.png file.ans
```
Renders an ANSI art file to out.png, using the default 80-column layout and the detected format.

```
ansilove -s file.ans
```
Shows the SAUCE metadata record of the file instead of rendering it.

## What's unique

It reproduces real DOS and Amiga text-mode rendering with embedded fonts and hardware quirks, and it is a small BSD-licensed C99 tool backed by an embeddable library.

## Caveats

You need your own ANSI art files to feed it, and font names like cp437 and topaz500+ are case-sensitive.

## Links

- [Project homepage](https://www.ansilove.org)
- [GitHub repository (AnsiLove/C README)](https://github.com/ansilove/ansilove)
- [libansilove library](https://github.com/ansilove/libansilove)
- [Homebrew formula](https://formulae.brew.sh/formula/ansilove)
