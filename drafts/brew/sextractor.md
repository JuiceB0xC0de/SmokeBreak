---
name: sextractor
title: SExtractor
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astronomy, catalogues, images, science]
homepage: https://www.astromatic.net/software/sextractor/
scout_score: 6
status: draft
---

# SExtractor

**TLDR;** Reads an astronomical image and writes a catalogue of every star and galaxy it finds, with measurements for each: real survey-grade astronomy software.

SExtractor, short for "Source Extractor", takes an astronomical image and produces a catalogue of the objects detected in it. Each detected source gets a row of measurements. The homepage says it is "particularly oriented towards reduction of large-scale galaxy-survey data", but it can also "perform reasonably well on moderately crowded star fields".

It was written by Emmanuel Bertin as part of the AstrOmatic suite of pipeline tools, and it is described in a 1996 paper by Bertin and Arnouts. The user manual's section headings hint at the stages involved: background modelling, weighting, flagging, isophotal and windowed positional measurements, aperture photometry, and model fitting. The brief does not explain how each stage works, so the manual is the place to learn that.

The idea underneath is that a picture of the sky is data waiting to become a table. Turning pixels into a list of objects with positions and brightnesses is the first step of much of observational astronomy, and this tool does that step. It is driven by a configuration file and a catalog parameter file that choose which measurements get written out. It can also write XML-VOTable metadata, a format used in astronomy data sharing.

Homebrew installs two executables: `sex`, the extractor itself, and `ldactoasc`. The brief does not say what `ldactoasc` does.

## Install

```
brew install sextractor
```

## Try this

```
sex --help
```
Prints the command-line usage summary for the extractor, a first look at how it is invoked and configured.

```
ldactoasc --help
```
Prints the usage text for the second installed executable, whose purpose the brief does not describe.

## What's unique

It is a long-standing, widely cited tool from a 1996 paper, and it is real survey-grade astronomy software you can run on your own images rather than a toy demo.

## Caveats

The official documentation is, in the homepage's words, "unfortunately still far from complete", the newest homepage news post is from 2014, and you need a FITS image of the sky to get anything meaningful out of it.

## Links

- [Homepage (Astromatic.net)](https://www.astromatic.net/software/sextractor/)
- [GitHub repository](https://github.com/astromatic/sextractor)
- [Online user manual](https://astromatic.github.io/sextractor)
