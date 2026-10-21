---
name: e2fsprogs
title: e2fsprogs
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, ancient, debugfs, ext4, file-formats, filesystems]
homepage: https://e2fsprogs.sourceforge.net/
scout_score: 5
status: draft
---

# e2fsprogs

**TLDR;** The reference toolkit for ext2, ext3 and ext4 filesystems, including debugfs and dumpe2fs for looking at on-disk structures directly.

e2fsprogs is the set of userland utilities for the ext family of Linux filesystems. It makes filesystems (`mke2fs`), checks and repairs them (`e2fsck`), resizes them (`resize2fs`), and labels them (`e2label`). Each tool takes a block device or an image file and works on its on-disk structures. It is maintained by Theodore Ts'o.

The interesting part for a curious reader is the inspection side. `dumpe2fs` prints superblock and block group information. `debugfs` is an interactive tool for looking inside a filesystem. `e2image` saves filesystem metadata to a file, and `e2undo` can roll back some changes. `filefrag`, `e2freefrag`, `lsattr` and `chattr` show how files are laid out and what attributes they carry. Together they turn a filesystem from a black box into something you can read.

The idea underneath is that a filesystem is just a data format on a block device, and an image file works as well as a disk. You can build one in a regular file, poke at it, and break it with no risk to real data. The brief does not include usage examples, so the commands below are a starting point, not a tour.

The project's own words are modest: "From time to time, I release new versions of e2fsprogs, to fix bugs and to make the utilities more robust."

## Install

```
brew install e2fsprogs
```

## Try this

```
mke2fs --help
```
Prints the usage text for the tool that creates ext2, ext3 and ext4 filesystems.

```
debugfs --help
```
Shows the options for the interactive filesystem debugger.

```
dumpe2fs --help
```
Shows how to dump superblock and block group information from a device or image.

## What's unique

It is the long-standing reference userland for the ext family, and one package covers creating, repairing, resizing and inspecting a filesystem at the structure level.

## Caveats

The README has no usage examples, and the homepage's last-modified date (2010) conflicts with its 1.47.4 release notice, so recency is unclear.

## Links

- [Homepage](https://e2fsprogs.sourceforge.net/)
- [GitHub mirror (README)](https://github.com/tytso/e2fsprogs)
- [Git repository (development sources)](git://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git)
