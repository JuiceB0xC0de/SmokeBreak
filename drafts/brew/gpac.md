---
name: gpac
title: GPAC
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, containers, dash, filters, mp4, streaming, video]
homepage: https://gpac.io/
scout_score: 6
status: draft
---

# GPAC

**TLDR;** A multimedia framework whose MP4Box tool opens up MP4 files and DASH streams, and whose gpac command lets you wire media filters together like a pipeline.

GPAC is an open-source multimedia framework written in C, with a library (libgpac) and command-line tools. It can process, inspect, package, stream, encode, decode and play audio, video, subtitles, metadata and encrypted media. Input can be files, pipes, sockets, HTTP or capture devices. Output can be remuxed or segmented files, streams, or playback.

Its best-known tool is MP4Box, a command-line manipulator for MP4 (ISOBMFF) files. It imports and extracts media, inspects file structure, does DASH segmentation and RTP hinting. Most people meet GPAC through it, and it is a practical way to see that an MP4 is a tree of boxes rather than an opaque blob.

Underneath, features are packaged as processing modules called filters, and a filter engine manages the flow of streams between them. The `gpac` command exposes that engine directly, so you can chain any combination of filters. MP4Box is a front end on the same engine. The README describes the tools as mostly wrappers around libgpac, which can be embedded in other projects.

The project is aimed at video enthusiasts, academic researchers, standardization bodies and broadcasters, and it puts standards compliance first. It also ships MP4Box.js, a JavaScript library that parses and writes MP4 in browsers and Node.js.

## Install

```
brew install gpac
```

## Try this

```
gpac -h filters
```
Lists the filters available in the engine, which shows the range of what GPAC can do.

```
MP4Box -h
```
Prints MP4Box's options for importing, extracting, inspecting and segmenting.

```
man gpac-filters
```
Opens the man page on the filter system, the idea behind the whole project.

## What's unique

GPAC is a filter graph engine rather than just a converter, and MP4Box is one front end on that general pipeline system. Its focus on standards makes it a good way to read how MP4 and DASH are actually structured.

## Caveats

The code is C and parses untrusted bitstreams, and CISA has issued advisories on it; the project says they were low to medium severity and are patched. Most of it is also sold under a commercial license by MotionSpell.

## Links

- [GPAC homepage](https://gpac.io/)
- [GPAC wiki (documentation)](https://wiki.gpac.io)
- [GitHub repository](https://github.com/gpac/gpac)
- [libgpac developer docs (doxygen)](https://doxygen.gpac.io)
