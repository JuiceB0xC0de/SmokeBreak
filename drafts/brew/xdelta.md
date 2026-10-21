---
name: xdelta
title: xdelta3
source: brew
category: take-things-apart
commitment: quick
tags: [binary, compression, diff, patching, quick, vcdiff]
homepage: https://github.com/jmacd/xdelta
scout_score: 6
status: draft
---

# xdelta3

**TLDR;** A binary diff tool that writes the smallest recipe for turning one file into another, using the VCDIFF standard (RFC 3284).

Given an old file and a new file, xdelta3 writes a small delta that describes how to rebuild the new one from the old. Given the old file and the delta, the decoder reproduces the new file. The command line is modelled on gzip, so it reads stdin, writes stdout, and takes a few flags.

Underneath, the encoder matches strings between source and target and emits two kinds of instruction: copy this range from the source, or insert these literal bytes. An optional secondary compressor (LZMA, DJW or FGK, where compiled in) can then squeeze the result. The idea is that an update is mostly the old version, so you only need to ship what changed. That is the principle behind software patches, game updates and backup systems.

The delta is not a black box. The printhdr, printhdrs and printdelta commands dump a delta's headers, windows and instructions as readable text, so you can see which parts of a file were copied and which were new. Armor mode, on by default when compiled in, embeds BLAKE3 digests of the source and target and checks them when decoding. The merge command collapses a chain of deltas (1 to 2, 2 to 3, 3 to 4) into a single 1 to 4 delta.

## Install

```
brew install xdelta
# the executable is xdelta3; prebuilt binaries for Linux, macOS and Windows are also on GitHub Releases
```

## Try this

```
xdelta3 -e -s old-file new-file update.vcdiff
```
Writes a delta that turns old-file into new-file.

```
xdelta3 -d -s old-file update.vcdiff reconstructed-file
```
Applies the delta to old-file and rebuilds the new file.

```
xdelta3 -J -d -s old-file update.vcdiff
```
Decodes and verifies the delta without writing any output, to check that it is valid.

## What's unique

It uses an open standard (VCDIFF, RFC 3284) rather than a private format, so other implementations can decode its deltas. Armor mode adds whole-file BLAKE3 verification, and deltas can be merged into one.

## Caveats

LZMA-compressed deltas need a decoder built with liblzma, so the docs suggest -S none for compatibility with older or reduced builds, and in armor mode an already-applied patch exits with status 2, which scripts must handle.

## Links

- [Homepage (GitHub repository)](https://github.com/jmacd/xdelta)
- [Full documentation](https://jmacd.github.io/xdelta/)
- [Command-line reference](https://jmacd.github.io/xdelta/commandline/)
- [GitHub Releases](https://github.com/jmacd/xdelta/releases)
