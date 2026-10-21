---
name: psftools
title: psftools
source: brew
category: take-things-apart
commitment: quick
tags: [bitmap, file-formats, fonts, quick, retro, reverse-engineering]
homepage: https://www.seasip.info/Unix/PSF/
scout_score: 6
status: draft
---

# psftools

**TLDR;** A NetPBM-style toolkit that converts bitmap fonts from old machines like the BBC Micro, Amstrad CP/M and DOS into PSF and back out again.

PSF Tools is a set of small command-line programs for simple fixed-width bitmap fonts. The homepage says it is "an attempt to do something similar to NetPBM, for simple fixed-width bitmap fonts." Each program reads one format and writes another, and the names say which: `raw2psf`, `psf2bdf`, `zx2psf`.

PSF, the PC Screen Font format, is the hub. Converters bring fonts in from raw DOS fonts, Windows FNT/FON, Spectrum +3, MDA ROM dumps, DOS CPI codepages, Hercules WOF, Wyse-60, BBC Micro, Amstrad CP/M, plain text and Berkeley vfont. Others take PSF out to BDF, a C include file, XBM, per-character PBM, plain text and raw bytes. To get between two non-PSF formats, chain two tools.

The idea underneath is that a font is just a grid of bits per glyph. Once you see that, the text on an old terminal or home computer stops being magic and becomes a file you can dump to text, edit by hand and convert back. `txt2psf` and `psf2txt` suggest a font can be read and edited as plain text, though the brief does not show their syntax.

The homepage also mentions `psfdiff`, which compares two PSF files as a visual image, and `psfxsaa`, which upscales fonts using the SAA5050 smoothing algorithm. Both are described there but are not in the Homebrew executable list.

## Install

```
brew install psftools
# Homebrew installs about 35 converters. To load PSF fonts into the Linux console you also need the kbd package.
```

## Try this

```
psf2txt --help
```
Shows usage for the converter that turns a PSF font into a plain-text view of its glyphs.

```
psf2bdf --help
```
Shows usage for converting a PSF font to BDF, the format X11 tools read.

```
raw2psf --help
```
Shows how to wrap a raw dump of font bytes, such as one pulled from a DOS machine, into a PSF file.

## What's unique

It is a hub-and-spoke converter for a very obscure corner of computing, routing dozens of legacy machine font formats through one common format.

## Caveats

Only simple fixed-width fonts are supported, and some formats convert in one direction only.

## Links

- [PSF Tools homepage](https://www.seasip.info/Unix/PSF/)
