---
name: lcdf-typetools
title: LCDF Typetools
source: brew
category: take-things-apart
commitment: quick
tags: [file-formats, fonts, opentype, quick, tex, truetype, type1]
homepage: https://www.lcdf.org/type/
scout_score: 6
status: draft
---

# LCDF Typetools

**TLDR;** Eleven small command-line tools that open up OpenType, TrueType and Type 1 fonts to read their features and convert them into TeX and PostScript files.

LCDF Typetools is a set of C programs, each parsing one font format and emitting another format or a plain-text report. The inputs are Type 1 (PFA/PFB), Type 1 Multiple Master, OpenType (CFF and TrueType flavored) and TrueType files. The outputs include Type 1 fonts converted from CFF (cfftot1), AFM metrics (mmafm, t1rawafm), TeX metrics and encodings (otftotfm), Type 42 wrappers (ttftotype42) and PostScript test pages (t1testpage). otfinfo prints reports on a font's features and codepoints, and t1lint checks Type 1 fonts.

Eddie Kohler wrote it so that Adobe OpenType and multiple master fonts could be used from TeX and other UNIX font toolchains. The homepage says it lets multiple master fonts 'work with UNIX programs for single-master fonts, like afm2tfm, ps2pk, GhostScript ps2pdf, and the X11 Type 1 font server.' The package is old in spirit, since it fills gaps from an era when those toolchains knew nothing about OpenType.

The idea underneath is that a font is a structured database: glyph outlines, metrics, and tables that say which glyphs substitute for others and how pairs are positioned. otftotfm reads those substitution, positioning and ligature tables and writes TeX metrics from them, optionally switching on features you name. Multiple master fonts are interpolated: mmpfb and mmafm take weight and width values and produce a single concrete instance. Poking at these tools is a practical way to learn what is inside a font file.

## Install

```
brew install lcdf-typetools
```

## Try this

```
otfinfo --help
```
Lists the options for inspecting a font file, such as its features and codepoints.

```
mmafm --help
```
Prints the full option summary for generating AFM metrics from a multiple master font.

```
mmpfb MyriadMM.pfb --weight=300 --width=585 > MyriadMM_300_585_.pfb
```
Writes a single-master Type 1 font for one weight and width instance of a multiple master font you supply.

## What's unique

otftotfm uses the font's own substitution and positioning tables to build TeX metrics, rather than relying on a hand-written mapping. The multiple master tools let you carve a concrete instance out of an interpolated font.

## Caveats

The multiple master tools need companion font files (AMFM and AFM, or multiple master PFB) that are not included, and the author does not support Windows ports.

## Links

- [LCDF Type Software homepage](https://www.lcdf.org/type/)
- [Source on GitHub](https://github.com/kohler/lcdf-typetools)
