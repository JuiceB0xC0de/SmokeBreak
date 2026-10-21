---
name: bsdiff
title: bsdiff
source: brew
category: take-things-apart
commitment: quick
tags: [binary-diff, compression, executables, patching, quick, suffix-array]
homepage: https://www.daemonology.net/bsdiff/
scout_score: 6
status: draft
---

# bsdiff

**TLDR;** A pair of tools that diff two binary files into a small patch and rebuild the new file from the old, using suffix sorting.

bsdiff takes an old file and a new file and writes a patch. Its companion bspatch takes the old file plus that patch and reconstructs the new file. It is aimed mainly at executables, where most bytes move around a little between versions rather than changing outright. The homepage claims patches 50-80% smaller than those from Xdelta.

The author wanted small binary updates for executables. The tools were first called bdiff and bpatch, but those names clashed with many other programs, so they became bsdiff and bspatch.

Underneath is a neat idea. bsdiff uses suffix sorting, specifically Larsson and Sadakane's qsufsort, to find long matching regions between the old and new files. It then stores the bytewise differences between those matched regions, which are mostly zeros and compress well with bzip2. The page credits this "bytewise subtraction" for the speed and small size. The algorithm is described in the author's unpublished paper "Naive differences of executable code", and a more sophisticated version, giving roughly 20% smaller patches, is in his doctoral thesis.

That makes it a small door into delta compression, the thing behind software updates that ship only what changed.

## Install

```
brew install bsdiff
bsdiff and bspatch use bzip2, which the homepage says it expects in /usr/bin by default.
```

## Try this

```
bsdiff --help
```
Prints usage for the bsdiff executable, which takes an old file, a new file and a patch file name.

## What's unique

It pairs a suffix-sorting search with bytewise subtraction tuned to how executables change, and the author documents the approach and its memory cost openly.

## Caveats

It is memory-hungry, needing roughly 17 times the old file size in the worst case, and the homepage benchmarks date from a 200MHz Pentium Pro and give no release date.

## Links

- [bsdiff homepage](https://www.daemonology.net/bsdiff/)
