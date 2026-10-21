---
name: netpbm
title: Netpbm
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [classic, converters, images, pipelines, quick, unix-filters]
homepage: https://netpbm.sourceforge.net/
scout_score: 6
status: draft
---

# Netpbm

**TLDR;** Over 350 tiny command-line programs that convert and transform images through a few plain intermediate formats, a 1990s Unix toolbox that still ships everywhere.

Netpbm is a toolkit of single-purpose image programs. Roughly 100 of them are converters between graphics formats, most of which are now museum pieces. The rest shrink, crop, flip, fade, and otherwise rework pictures. It has no GUI and no interactive tools. You type a command, or another program calls it for you.

The stated goal is to be a single source for all the primitive graphics utilities, especially converters, that one might need. It grew out of Pbmplus, whose last release was December 10, 1991. Netpbm collected the many filters that circulated on the net after that, hence the name.

The idea underneath is the interesting part. Instead of one big program with many options, Netpbm uses a few simple intermediate formats (PBM, PGM, PPM and PAM). Every converter reads its format and writes one of those, and every filter works on them. Any format can therefore reach any other through small steps. That is the modular design the homepage means when it says "Among the niche of engineers who appreciate modular design, code reuse, and building things from building blocks, Netpbm has no equal."

The project is maintained, with releases roughly every three months. Bryan Henderson, the maintainer, answers bug reports by email.

## Install

```
brew install netpbm
```

## Try this

```
pnmfile --help
```
Shows usage for pnmfile, one of the small tools that reports what an image file contains.

```
pamscale --help
```
Lists the options of the scaling filter, a typical single-purpose tool in the set.

```
ppmforge --help
```
Shows how to use the generator that makes fractal-style images from scratch.

## What's unique

It treats image work as a set of tiny filters around a few plain formats, rather than one big editor. The format converters double as a catalogue of old graphics history.

## Caveats

There is no GUI, no bug tracker and no mailing list. Most of the roughly 100 formats are seen only in museums, and most people reach for GIMP or ImageMagick instead.

## Links

- [Netpbm homepage](https://netpbm.sourceforge.net/)
- [Change history](https://netpbm.sourceforge.net/change.html)
