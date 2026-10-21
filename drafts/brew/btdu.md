---
name: btdu
title: btdu
source: brew
category: take-things-apart
commitment: quick
tags: [btrfs, disk-usage, filesystem, quick, sampling, tui]
homepage: https://github.com/CyberShadow/btdu
scout_score: 7
status: draft
---

# btdu

**TLDR;** A btrfs disk usage profiler that samples random points on the disk and asks the filesystem who owns them, so answers appear instantly and sharpen over time.

btdu is a terminal disk usage tool for btrfs, written in D. Where ncdu walks every file and adds up sizes, btdu picks a random point in the used part of the disk, works out which path owns that point, and adds it to a tree. You browse that tree interactively while it fills in. It can also run headless, print a tree to stdout, and export results to `.btdu` or `.json` files.

The README says btrfs makes classic analyzers unreliable: subvolumes, cloned files and extents, and compression all break the idea that a file's size is the space it takes. Sampling sidesteps the problem by asking the filesystem directly what sits at each point. In the README's words, "btdu needs to collect only 100 samples to achieve a ~1% resolution", and "Though it works by taking random samples, it is 'eventually' accurate."

The idea underneath is that a statistical question can be easier than an exact one. When an extent is shared by several files or snapshots, btdu assigns it to the shortest path, with ties broken lexicographically, so each extent is counted once. A side effect is that a snapshot's size reads as the amount of new data in it. It can also estimate "dark matter", space held by unreachable parts of extents, which the README calls unique to btdu.

You can save a run and compare it against a baseline later, which turns it into a way to see what changed between two points in time.

## Install

```
brew install btdu
# Needs root, and a mounted btrfs filesystem. The path must be the top-level subvolume (or remount with -o subvol=/,subvolid=5).
```

## Try this

```
btdu --help
```
Lists the options, including headless mode, export, import and compare.

```
sudo btdu --headless --max-time=30s /mnt/btrfs
```
Samples for 30 seconds without the TUI, then prints a tree of items over 1% of total space.

```
sudo btdu --headless --export=results.json --max-time=10m /mnt/btrfs
```
Samples for ten minutes and saves the results, which you can later open with `btdu --import results.json`.

## What's unique

It answers the question with random sampling instead of a full scan, so it handles snapshots, reflinks and compression without special cases. It also estimates the dark-matter space that file-walking tools cannot see.

## Caveats

It needs root and a btrfs filesystem, analyses only whole filesystems, and early numbers are wildly off until enough samples accumulate.

## Links

- [Homepage / repository](https://github.com/CyberShadow/btdu)
- [Releases](https://github.com/CyberShadow/btdu/releases)
- [CONCEPTS.md (size metrics and btrfs concepts)](https://github.com/CyberShadow/btdu/blob/master/CONCEPTS.md)
