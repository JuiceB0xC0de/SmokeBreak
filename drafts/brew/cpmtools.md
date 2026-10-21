---
name: cpmtools
title: cpmtools
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, cp/m, disk-images, file-systems, retro, z80]
homepage: https://www.moria.de/~michael/cpmtools/
scout_score: 8
status: draft
---

# cpmtools

**TLDR;** Command-line tools that list, copy, create and check files inside CP/M disk images, so 8-bit era floppies can be handled from a modern shell.

Cpmtools is a set of small programs for working with CP/M file systems, the disk format of many 8-bit computers. `cpmls` lists a directory, `cpmcp` copies files in and out, `cpmrm` deletes, `cpmchmod` and `cpmchattr` change permissions and attributes, and `mkfs.cpm` makes a fresh file system. `fsck.cpm` checks and repairs one, and `fsed.cpm` lets you view it.

The author built it for file exchange with a Z80-PC simulator. It is modelled on mtools, which does the same job for MS-DOS file systems. The homepage says it also works on floppy devices, not only image files.

The idea underneath is that an old file system is just a layout of bytes: a directory area, allocation blocks, and some attribute bits. Once a tool understands the layout, you can put files into and take them out of an image without booting a guest operating system. It is a practical way to see how a very small file system was organised.

A couple of details show the era. Password protection is ignored, but a pseudo-file `[passwd]` exposes the stored passwords. The disk label appears as a pseudo-file `[label]`.

## Install

```
brew install cpmtools
# pulls in libdsk as a dependency. You need a CP/M disk image to work with, or make one with mkfs.cpm.
```

## Try this

```
cpmls --help
```
Prints usage for the directory lister, the quickest way to see how you point the tools at an image and a disk format.

```
mkfs.cpm --help
```
Shows the options for creating a new empty CP/M file system.

```
cpmcp --help
```
Shows how to copy files between your host file system and a CP/M image.

## What's unique

It does for CP/M what mtools does for MS-DOS, handling old disk images from a modern shell with no emulated guest OS. It also exposes pseudo-files like [passwd] and [label].

## Caveats

The homepage gives version 2.23 but no release date, so maintenance status is unclear, and fsck.cpm only repairs simple errors so far.

## Links

- [Cpmtools homepage](https://www.moria.de/~michael/cpmtools/)
