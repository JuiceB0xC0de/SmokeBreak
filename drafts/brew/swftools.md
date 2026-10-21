---
name: swftools
title: swftools
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary, file-formats, flash, reverse-engineering]
homepage: https://github.com/swftools/swftools
scout_score: 6
status: draft
---

# swftools

**TLDR;** A set of command-line tools that take apart, rebuild and generate Adobe Flash SWF files, a good way to look inside a dead binary format.

SWFTools is a collection of small programs for working with SWF files, the format Flash used. Some read: `swfdump` prints what is inside a file, `swfstrings` pulls out text, `swfextract` lifts out movieclips, sounds and images, and `swfbbox` reports bounding boxes. Others write: `png2swf`, `wav2swf` and `font2swf` turn ordinary images, audio and fonts into SWF, and `swfc` and `as3compile` build from source. `swfcombine` merges or rewrites existing files.

The README describes it as "a collection of utilities for working with Adobe Flash files (SWF files)." It does not give a broader motivation, but the shape of the toolkit explains itself. Each program does one narrow job, so you can watch a SWF being taken apart or assembled one piece at a time.

The interesting part is the format. SWF is a tagged binary container holding shapes, bitmaps, sounds, fonts and bytecode. Flash is discontinued, so nothing needs these files anymore, which makes it a low-stakes place to learn how a multimedia container is laid out. The README notes that some tools borrow from other projects: the PDF converter is based on the xpdf parser, and `wav2swf` uses the L.A.M.E. MP3 encoder library.

## Install

```
brew install swftools
```

## Try this

```
swfdump --help
```
Lists the options for dumping a SWF file's structure, the usual first step in looking inside one.

```
swfextract --help
```
Shows how to pull movieclips, sounds and images out of an existing SWF.

```
swfc --help
```
Shows the options for the SWF compiler, which builds a SWF from a script.

## What's unique

It is one of the few complete open-source toolchains that can both dissect and generate SWF files. The dump output exposes much of the format's internal structure.

## Caveats

Flash is discontinued, so generated SWFs have limited playback today, and the README gives no release date. The brew install also omits pdf2swf, jpeg2swf and gif2swf, which the README lists.

## Links

- [GitHub homepage and README](https://github.com/swftools/swftools)
