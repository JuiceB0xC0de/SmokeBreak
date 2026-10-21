---
name: dwarfs
title: DwarFS
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, archive, compression, deduplication, filesystem, fuse]
homepage: https://github.com/mhx/dwarfs
scout_score: 6
status: draft
---

# DwarFS

**TLDR;** A read-only compressed filesystem that packs a directory into one image, clusters similar files together, and mounts it instantly as a normal folder.

mkdwarfs takes a directory and writes a single .dwarfs image. The dwarfs driver mounts that image as an ordinary folder, so there is no full extraction and no temporary files. dwarfsextract unpacks it to real files when you need them, and dwarfsck lists contents or prints per-file checksums.

The author, Marcus Holland-Moritz, started it in 2013 to store several hundred Perl versions, about 30 GB, in far less space. In his telling, cromfs compressed well but was slow to build and often crashed, and SquashFS never reached the same compression rates. DwarFS aims for fast random reads and large space savings together.

The idea underneath is that where a file sits in an archive matters. According to the README, DwarFS uses a similarity hash to cluster similar files, so redundancy across file boundaries can be exploited. A categorization framework lets different kinds of content be handled differently, for example skipping compression on incompressible files or using FLAC for PCM audio. The tools are highly multi-threaded.

That makes it a good door into how block-based, deduplicated storage works. The image format is documented in a dwarfs-format man page if you want to see what is actually on disk.

## Install

```
brew install dwarfs
# Homebrew installs mkdwarfs, dwarfsck and dwarfsextract. For the FUSE driver on macOS: brew tap gromgit/homebrew-fuse && brew install dwarfs-fuse-mac (needs macFUSE). On Linux, the FUSE driver needs the fuse3 tools installed separately.
```

## Try this

```
mkdwarfs -i /path/to/input/dir -o /path/to/image.dwarfs
```
Packs a directory into a single compressed DwarFS image.

```
dwarfsck /path/to/image.dwarfs -l
```
Lists the files inside the image without mounting or extracting it.

```
mkdwarfs --man
```
Prints the manual page, which covers the compression and clustering options.

## What's unique

It clusters files by similarity and handles file types differently, which the README says gets far past SquashFS-style ratios. For example, a Perl corpus came out at 0.310 GiB with lzma against 12.17 GiB for tar.gz, though those are the author's own benchmarks.

## Caveats

On macOS the FUSE driver comes from a third-party tap and needs macFUSE; Windows support is labelled experimental, extended attributes are not preserved, there is no built-in recovery data, and there are no API stability guarantees before 1.0.0.

## Links

- [Project homepage (GitHub)](https://github.com/mhx/dwarfs)
- [mkdwarfs manual](https://github.com/mhx/dwarfs/blob/main/doc/mkdwarfs.md)
- [DwarFS file system format (dwarfs-format(5))](https://github.com/mhx/dwarfs/blob/main/doc/dwarfs-format.md)
- [Releases (prebuilt binaries)](https://github.com/mhx/dwarfs/releases)
