---
name: sleuthkit
title: The Sleuth Kit
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cli, disk-images, file-systems, forensics, reverse-engineering]
homepage: https://www.sleuthkit.org/
scout_score: 7
status: draft
---

# The Sleuth Kit

**TLDR;** A set of small command-line tools that take a raw disk image apart layer by layer, showing partitions, file names, inodes, and deleted files.

The Sleuth Kit (TSK) is a collection of command-line forensic tools and a C library for analyzing disk images and file systems. You give it a raw image, such as one made with dd, and it lets you inspect partitions, file system structures, files, deleted content, and hashes. It also powers Autopsy, a GUI front end.

The tools are organized in layers, and the first letter of each name tells you which layer it works on. `f` tools deal with file names (fls, ffind). `i` tools deal with metadata structures such as inodes (ils, istat, icat, ifind). `blk` tools deal with content units (blkls, blkcat, blkcalc, blkstat). Learning the naming scheme is also a quick way to learn how a file system is put together.

In the README's words, "These tools are low-level and each performs a single task. When used together, they can perform a full analysis." Timelines, for example, come from body files produced by fls and ils and fed to mactime. hfind does fast hash-set lookups, including against the NSRL.

The code descends from The Coroner's Toolkit file system tools by Wietse Venema and Dan Farmer, modified for platform independence and extended with NTFS and FAT support. The project says being open source lets investigators verify what the tools do, which is the point of using it over a closed suite.

## Install

```
brew install sleuthkit
```

## Try this

```
fls -rm dir
```
Lists allocated and unallocated file names in body-file format, the first step of a mactime timeline (the README's example; add an image path after the options).

```
ils -m
```
Lists unallocated inodes in body-file format, to be combined with fls output for a timeline.

```
fls --help
```
Prints the usage and options for the file-name layer tool, a good place to start learning the layers.

## What's unique

Each tool does one narrow job and is meant to be piped and combined, closer to Unix philosophy than to a monolithic forensic suite. Its lineage runs back to the Coroner's Toolkit.

## Caveats

It works on raw or file system images rather than live devices, its results should be re-created with a second tool to verify them, and the file type detection mostly checks only the first bytes of a file.

## Links

- [Homepage](https://www.sleuthkit.org/)
- [GitHub repository and README](https://github.com/sleuthkit/sleuthkit)
- [TSK wiki (tool overview and docs)](http://wiki.sleuthkit.org/index.php?title=Main_Page)
- [Autopsy (GUI built on TSK)](http://www.sleuthkit.org/autopsy)
