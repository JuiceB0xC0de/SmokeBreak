---
name: dvd-vr
title: dvd-vr
source: brew
category: take-things-apart
commitment: quick
tags: [dvd, file-formats, quick, reverse-engineering, video]
homepage: https://www.pixelbeat.org/programs/dvd-vr/
scout_score: 6
status: draft
---

# dvd-vr

**TLDR;** Reads the navigation file on a DVD-VR disc from a recorder or camcorder and lists every recording on it, built by reverse engineering.

dvd-vr is a small command-line tool for a niche consumer format. DVD recorders and camcorders often write discs in DVD-VR, which keeps its recordings in a different layout from a normal video DVD. The tool reads the navigation file, `VR_MANGR.IFO`, and prints what it finds. It can also optionally copy recordings out.

The report gives the format version (the homepage example shows DVD-VR V1.1), the video and audio parameters of each VOB (TV system, resolution, MPEG2, AC-3 audio), and for each program a title, date, VOB format number, and size in bytes. The example output includes Japanese title text, so non-ASCII titles come through.

The author wrote it in February 2007 by reverse engineering DVD-VR discs, not from a published spec. That is the idea underneath it: a disc is just bytes with structure, and a patient person with a few sample discs can work out the index, the stream descriptions, and the title table. The tool is a compact example of how a closed consumer format gets opened up.

The homepage does not explain the parsing internals, so the source is the place to learn how the file is laid out.

## Install

```
brew install dvd-vr
# You also need a mounted DVD-VR disc, or a copy of its files, to point it at.
```

## Try this

```
dvd-vr --help
```
Prints usage. The homepage documents only the file argument, so expect little.

```
dvd-vr /media/dvd/DVD_RTAV/VR_MANGR.IFO
```
Reads the navigation file on a mounted disc and prints the format version, per-VOB video and audio details, and each recording's title, date and size.

## What's unique

It targets a consumer disc format most rippers ignore, and it was built by reverse engineering rather than from a spec.

## Caveats

Quiet for years: the latest listed release is V0.9.7 and the page footer is dated 2010. It is only useful if you have a DVD-VR disc, and the page documents just one example run.

## Links

- [Homepage](https://www.pixelbeat.org/programs/dvd-vr/)
