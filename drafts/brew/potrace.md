---
name: potrace
title: potrace
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [graphics, quick, svg, tracing, vector]
homepage: https://potrace.sourceforge.net/
scout_score: 6
status: draft
---

# potrace

**TLDR;** Potrace traces a bitmap and turns it into smooth, scalable vector curves, the tracer behind much of the open-source graphics world.

Potrace reads a bitmap (PBM, PGM, PPM or BMP) and writes a vector image: SVG, PDF, EPS, PostScript, DXF, GeoJSON, XFig and a few others. The pixel edges become smooth Bézier curves, so the result can be rendered at any resolution. In the author's words, the result is "not "jaggy" like a bitmap, but smooth."

It exists for jobs like rescuing a scanned logo or handwritten notes from the resolution it was scanned at. A companion program, mkbitmap, ships with it. It pre-processes greyscale and colour images into the black-and-white input that potrace wants.

The options hint at how tracing works. A turd-size filter drops speckles, an alphamax threshold decides which corners stay sharp, a curve-optimization tolerance simplifies the curves, and a turn policy settles ambiguous spots when the bitmap is split into paths. Tuning them shows what "tracing" actually decides on your behalf. The homepage links a separate technical write-up of the algorithm.

The homepage lists downstream projects, including FontForge, Inkscape, and LilyPond via mftrace. It also lists physical-world uses such as stained glass and stencils.

## Install

```
brew install potrace
```

## Try this

```
potrace --help
```
Prints the usage text and the full list of options, including backends, speckle size and corner threshold.

```
mkbitmap --help
```
Shows the options of the companion tool that turns greyscale or colour images into traceable bitmaps.

```
potrace [options] [filename...]
```
The usage synopsis. Give it a PBM, PGM, PPM or BMP file and pick a backend, such as -s for SVG output, to get a vector file.

## What's unique

It has been the standard open-source bitmap tracer for years, and it produces smooth Bézier curves rather than jagged traces. Its ecosystem of ports and downstream projects is unusually broad.

## Caveats

Input is limited to PNM and BMP, there is no colour tracing, and the last release (1.16) dates from September 2019.

## Links

- [Potrace homepage](https://potrace.sourceforge.net/)
