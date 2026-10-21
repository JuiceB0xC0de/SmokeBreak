---
name: fatsort
title: fatsort
source: brew
category: take-things-apart
commitment: quick
tags: [c, exfat, fat, filesystems, mp3, quick]
homepage: https://fatsort.sourceforge.io/
scout_score: 5
status: draft
---

# fatsort

**TLDR;** A small C tool that reorders the directory entries on FAT and exFAT volumes, so dumb players and car stereos play files in the order you want.

FATSort sorts the directory entries of FAT12, FAT16, FAT32 and exFAT partitions. It reads the volume's boot sector, walks the directory structure recursively, and rewrites the entries in sorted order. It handles long file name entries, and it runs on Linux, BSD and other UNIX systems, and macOS.

The author wrote it to organize MP3 files on a hardware player that could not sort them itself. Such devices often play files in the order they sit in the directory table, not alphabetically. A FAT directory is just a list of entries in whatever order files were written, so copying files over in the wrong order gives a wrong playlist. Sorting the table directly fixes that.

That is the door it opens: a filesystem is a data structure, and the order you see is a property of bytes on disk, not of the files. The changelog shows some care about this. Entries are only written back when reordering actually happened, and the tool checks that all copies of the FAT match before it sorts.

It has been around since 2004, with exFAT support added in 2019 and a v1.7 release in November 2025.

## Install

```
brew install fatsort
# From source instead: download the tarball from SourceForge, run `make` in the fatsort directory, then `make install`. Needs a C toolchain.
```

## Try this

```
fatsort --help
```
Prints the usage summary and the available options.

```
make
```
Builds the fatsort executable from source when run in the fatsort directory, per the homepage.

```
make install
```
Installs the built FATSort, per the homepage.

## What's unique

It changes the on-disk order of directory entries rather than anything a file manager shows, which is what simple hardware players actually read.

## Caveats

It rewrites directory order on the volume itself, so back up first; the changelog records past bugs with endianness and multi-byte names, and there is no Windows support.

## Links

- [Homepage](https://fatsort.sourceforge.io/)
- [SourceForge downloads and changelog](https://sourceforge.net/projects/fatsort/files/)
