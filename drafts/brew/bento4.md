---
name: bento4
title: Bento4
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, containers, dash, hls, mp4, reverse-engineering, video]
homepage: https://www.bento4.com/
scout_score: 5
status: draft
---

# Bento4

**TLDR;** A C++ MP4 toolkit whose mp4dump prints the full box tree of any MP4 file, so you can see how video containers are built.

Bento4 is a C++ class library and about thirty command-line tools for reading and writing ISO-MP4 files. It also packages media for MPEG DASH, HLS and CMAF. Inputs are MP4 files and elementary streams (H.264, H.265, AAC). Outputs include fragmented MP4, MPEG-TS, HLS playlists and segments, DASH presentations, and encrypted or decrypted files.

The door into something larger is the box structure. An MP4 file is a tree of boxes (QuickTime called them atoms), each with a type and a size, nested inside one another. `mp4info` gives a summary of tracks and codecs. `mp4dump` shows the entire box tree. `mp4edit` and `mp4extract` can add, replace or pull out individual boxes. Most of what a player does with a file starts at this level.

The packaging tools show what streaming video does behind the scenes. `mp4fragment` rewrites a file into fragments, and `mp4dash` and `mp42hls` produce manifests and segments from it. The encryption tools implement several schemes, including MPEG Common Encryption (CENC), PIFF, ISMA and OMA DCF. The README says the SDK relies on no external library.

## Install

```
brew install bento4
# the formula depends on python@3.15; no account or hardware needed
```

## Try this

```
mp4info --help
```
Lists the options for the tool that summarizes tracks and codecs in an MP4 file.

```
mp4dump --help
```
Shows how to print the full atom/box structure of an MP4 file.

```
mp4dash --help
```
Shows the options for building a DASH presentation from MP4 input.

## What's unique

It covers the whole MP4 stack in one self-contained library, from box-level inspection to DASH and HLS packaging and several encryption schemes. Most similar tools do only one of those jobs.

## Caveats

The README marks its SCons build as deprecated, and no release dates were visible, so how recently it has been updated is unclear.

## Links

- [Bento4 homepage](https://www.bento4.com/)
- [GitHub repository (axiomatic-systems/Bento4)](https://github.com/axiomatic-systems/Bento4)
