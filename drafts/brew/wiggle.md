---
name: wiggle
title: wiggle
source: brew
category: take-things-apart
commitment: quick
tags: [c, diff, merge, patch, quick]
homepage: https://github.com/neilbrown/wiggle
scout_score: 5
status: draft
---

# wiggle

**TLDR;** Wiggle applies patches that GNU patch rejects, matching word by word instead of line by line so drifted context still lands.

Wiggle is a small C program for the moment when `patch` gives up. A hunk's surrounding lines have changed since the patch was made, so a line-based tool cannot find where it belongs and writes it to a reject file. Wiggle compares at the level of words, which lets it place many of those hunks anyway. Where it cannot, it marks the conflict in the output.

It does four things: merge (the default), diff, extract and browse. Merge takes a file and a patch, or three files, and produces a three-way merge with word-level comparison. Diff reports word-wise or line-wise differences in a unified-diff style. Extract pulls one branch out of a patch or merge file. Browse is an interactive mode for stepping through a set of patches, and its help text says it 'will eventually allow limited editing'.

The idea underneath is that a diff does not have to be a list of lines. Change the unit of comparison from lines to words and a whole class of conflicts shrinks or disappears. The source tree has files named bestmatch.c, merge2.c and patch_depends.c, which hint at how the matching works, but the README does not explain the algorithm, so reading the source is the way in.

## Install

```
brew install wiggle
```

## Try this

```
wiggle --help
```
Prints the overview of the four functions: merge, diff, extract and browse.

```
wiggle --diff --help
```
Shows detailed help for the diff function. A function must be selected before its help can be requested.

```
wiggle --merge --help
```
Shows the options for merge, the default function that applies a patch to a file with word-level wiggling.

## What's unique

Most patch tools match whole lines. Wiggle matches words, so it can apply a hunk whose context has changed slightly and still produce a three-way merge with word-level conflict markers.

## Caveats

Maintained slowly and niche; browse mode editing is unfinished, and the README is mostly help text rather than an explanation of how it works.

## Links

- [GitHub repository (homepage)](https://github.com/neilbrown/wiggle)
- [Author's project page and tarball index](https://neil.brown.name/wiggle/)
