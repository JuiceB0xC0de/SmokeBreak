---
name: mftrace
title: mftrace
source: brew
category: take-things-apart
commitment: quick
tags: [fonts, metafont, quick, reverse-engineering, tex, vectorizing]
homepage: https://lilypond.org/mftrace/
scout_score: 6
status: draft
---

# mftrace

**TLDR;** Turns TeX's METAFONT bitmap fonts like Computer Modern into scalable outline fonts by rendering them large and tracing the pixels back into curves.

mftrace is a small Python program that takes a TeX font name such as `cmr10` and writes a scalable font: PostScript Type 1 (PFA or PFB) by default, or TrueType, AFM and SVG if FontForge is installed. It is mostly a conductor. The vectorizing is done by potrace (recommended) or autotrace, and t1utils and FontForge handle the rest.

The pipeline is a round trip through raster. mftrace runs MetaFont on the font's source at a high magnification to get a GF bitmap for each glyph. Its own `gf2pbm` tool converts those to PBM, the tracer turns the bitmaps into outlines, and the outlines are assembled into a Type 1 font. The encoding comes from the TFM file or an encoding file. Optional FontForge steps round, simplify and autohint the result.

The idea underneath is that METAFONT fonts are programs, not drawings. Computer Modern was defined as code that draws glyphs with a pen at a given resolution, so the only way to get a conventional outline font out of the source is to render it and trace it. The README's practical argument is that scalable fonts render correctly at many printer resolutions, and that Ghostscript makes much better PDF from scalable PostScript fonts than from bitmaps.

It was called `pktrace` before version 1.0.5. The README compares it with MetaFog, which works on the curves directly but is proprietary, and with MetaType1, which cannot handle overlaps.

## Install

```
brew install mftrace
# Needs a TeX installation that provides kpsewhich and MetaFont. Homebrew pulls in fontforge, potrace and t1utils.
```

## Try this

```
mftrace cmr10
```
Traces the Computer Modern Roman 10pt font into a default PFA (Type 1) font file.

```
mftrace --help
```
Lists the options, including output formats, glyph selection and simplification.

## What's unique

It works from the font's own METAFONT source rather than from existing bitmaps, so fonts that exist only as METAFONT programs, like Computer Modern, can become outline fonts.

## Caveats

The documentation still mentions Python 2.2 and Debian 3.0, recent activity is unclear, TTF and SVG output need FontForge, and some MetaFont fonts overflow at high magnification.

## Links

- [mftrace homepage](https://lilypond.org/mftrace/)
- [GitHub repository](https://github.com/hanwen/mftrace)
- [Release tarball 1.2.20](http://lilypond.org/downloads/sources/mftrace/mftrace-1.2.20.tar.gz)
