---
name: hfsutils
title: hfsutils
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, ancient, filesystems, hfs, macintosh, retro, reverse-engineering]
homepage: https://www.mars.org/home/rob/proj/hfs/
scout_score: 7
status: draft
---

# hfsutils

**TLDR;** Command-line tools that read and write classic Macintosh HFS disks and image files from a modern shell, in the spirit of mtools for DOS floppies.

hfsutils is a package for working with volumes in HFS, the Hierarchical File System that classic Macintoshes used before HFS+ replaced it. Point it at a floppy, SCSI disk, CD-ROM, Zip disk, partitioned medium, or an image file, and it can read files off or write files onto the volume without a Mac in the room. The page names tools such as hformat, hmount, hls, and hcopy.

The author's stated goal is to manipulate Macintosh volumes from UNIX and other systems. The command-line programs are meant to work the way mtools does for MS-DOS disks: small commands that each do one job against a volume. The package also includes an X-based browser (xhfs), a Tcl package with a scriptable HFS shell, and a C library for low-level volume access. The page suggests the library could be linked into other programs, for example to build a Macintosh Resource Manager on top of it.

The door here is the filesystem itself. HFS is a dead format with its own ideas about catalogs, volumes, and how a Mac laid out data on disk. Having a small, readable toolkit for it is a way to get at old disk images and see how a format from the 1980s and 90s was put together. Homebrew lists one executable, hvol. The project page does not mention it, so check its --help before assuming what it does.

## Install

```
brew install hfsutils

The Tcl and X tools need Tcl and Tk libraries; the page asks for patched Tcl 7.6 and Tk 4.2 and warns other versions may not work. Those interfaces are optional. You need an HFS disk image or a physical Mac-format disk to do anything useful.
```

## Try this

```
hvol --help
```
Prints usage for the one executable Homebrew installs, so you can see what it does, since the project page does not describe it.

## What's unique

It treats a dead Macintosh disk format like a mtools-style toolkit, and it ships a Tcl shell and a linkable C library as well as the commands.

## Caveats

The page's dates run 1996-2000. It does not support HFS+ or the old 400K MFS format, and many PCs cannot read physical 800K Mac floppies, though disk images work.

## Links

- [HFS Utilities home page (Robert Leslie)](https://www.mars.org/home/rob/proj/hfs/)
