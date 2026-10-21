---
name: gnuastro
title: Gnuastro
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astronomy, fits, gnu, images, science]
homepage: https://www.gnu.org/software/gnuastro/
scout_score: 6
status: draft
---

# Gnuastro

**TLDR;** An official GNU package of 27 command-line programs for astronomical images and tables, from cropping and warping to NoiseChisel source detection, all sharing one interface.

Gnuastro, the GNU Astronomy Utilities, is a set of separate command-line programs and library functions for manipulating and analysing astronomical data. The names point at familiar FITS-style operations: `astarithmetic` for arithmetic on images, `astconvolve`, `astcrop`, `astwarp`, `asttable`, `aststatistics`, plus `astnoisechisel` for detecting faint sources, `astsegment`, and `astmkcatalog` for building catalogues. There are also a number of `astscript-*` helpers, for example for radial profiles and PSF work.

The idea underneath it is that astronomy pipelines can be built the Unix way. Each program does one job, and all of them share the same basic command-line interface, so learning one teaches you the rest. The project follows the GNU coding standards so that building, installing and running it feels like any other GNU software. In its own words, "All the programs share the same basic command-line user interface for the comfort of both the users and developers."

Documentation is the way in. The whole book is available through `info gnuastro`, each program has its own Info entry and man page, and every program accepts `--cite`, which prints how to cite Gnuastro and that particular program. That is a small but rare nicety in scientific software.

The project is about eleven years old and still under active development. The current stable release is 0.24, from November 2025.

## Install

```
brew install gnuastro
# Pulls in the required libraries: cfitsio, gsl and wcslib, plus a few others. You will need FITS images of your own to do anything real with it.
```

## Try this

```
astnoisechisel --help
```
Prints a description of the source-detection program and its full option list, grouped by context.

```
info gnuastro
```
Opens the complete Gnuastro book in Info format, starting from the beginning.

```
info astcrop
```
Shows the 'Invoking' section of the manual for the cropping program.

## What's unique

Real observational-astronomy tooling packaged as a polite GNU citizen: one shared interface across every program, a book-length Info manual, and a built-in `--cite` option on each tool.

## Caveats

The homepage gives no worked examples on real data, so you need your own FITS files and the manual to get anywhere, and there is still no single introductory paper to cite.

## Links

- [Homepage](https://www.gnu.org/software/gnuastro/)
- [Manual (all formats)](https://www.gnu.org/software/gnuastro/manual/)
- [Download mirror (latest tarball)](https://ftpmirror.gnu.org/gnuastro/gnuastro-latest.tar.gz)
