---
name: patchutils
title: patchutils
source: brew
category: take-things-apart
commitment: quick
tags: [ancient, cli, diff, patch, quick]
homepage: https://cyberelk.net/tim/software/patchutils/
scout_score: 5
status: draft
---

# patchutils

**TLDR;** Two dozen small commands that treat patch files as data you can list, filter, split, merge and repair instead of just applying.

Patchutils is a collection of command-line programs that read patch (diff) files and write new ones. The input is a patch; the output is another patch or a listing. `lsdiff` lists the files a patch touches, `filterdiff` keeps or drops parts of a patch by file wildcard, and `splitdiff` breaks a multi-file patch into one patch per file.

The more unusual tools work on relationships between patches. `interdiff` takes two patches against the same source and produces the incremental patch between them. `combinediff` goes the other way: it merges two incremental patches into one, so that "the resulting patch file only alters each file once." `rediff` compares an original patch with a hand-edited copy and fixes the offsets and line counts.

The homepage describes the tools by job rather than by mission. Its examples are practical repairs: correcting output from `cvs diff`, fixing patches edited by hand, and reviewing or merging pre-patches against one source tree. The idea underneath is that a patch is a structured document with hunks, offsets and counts, and once you see that, you can edit it with tools instead of by hand.

The executables list also includes helpers such as `gitdiff`, `gitshow`, `svndiff`, `patchview` and `move-to-front`. The brief does not describe them, so check their `--help` output.

## Install

```
brew install patchutils
```

## Try this

```
lsdiff --help
```
Shows the options for listing the files a patch file affects.

```
filterdiff --help
```
Shows how to include or exclude parts of a patch by file pattern.

```
interdiff --help
```
Shows how to produce the incremental patch between two patches made against the same source.

## What's unique

It treats a patch as plain data you can split, merge, filter and repair, rather than something you only apply. Merging incremental patches so each file appears once, and splitting a patch into per-file pieces, are the less common operations.

## Caveats

The homepage shows no release date, version, supported platforms or known limitations, so how actively it is maintained is unconfirmed.

## Links

- [Homepage](https://cyberelk.net/tim/software/patchutils/)
- [Signed stable release tarballs](https://cyberelk.net/tim/data/patchutils/stable/)
