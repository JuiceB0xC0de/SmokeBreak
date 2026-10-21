---
name: t2sz
title: t2sz
source: brew
category: take-things-apart
commitment: quick
tags: [compression, file-formats, quick, seekable, tar, zstd]
homepage: https://github.com/martinellimarco/t2sz
scout_score: 5
status: draft
---

# t2sz

**TLDR;** Compresses a tar archive into a seekable zstd file, one frame per member, so a reader can pull out one file without unpacking the rest.

t2sz writes ordinary zstd output, but it splits the input into many independent frames instead of one long stream. In its default tar mode, each file in the archive gets its own frame. For anything that is not a tar, or with `-r`, it runs in raw mode and cuts the input into fixed-size blocks.

The idea underneath is that a compressed stream does not have to be all-or-nothing. A normal `.tar.gz` or `.tar.zst` must be decompressed from the start to reach a file near the end. If the compressor ends a frame at each file boundary and writes a seek table, a reader can jump to the right frame and decompress only that. The README puts it this way: "This allows fast seeking and extraction of a single file without decompressing the whole archive."

The output stays compatible. The README says any Zstandard tool, including `zstd`, can decompress it, so nothing is lost by using it. The `-s` and `-S` options tune the trade: pack small files together until a block reaches a size, or split large files into fixed-size blocks. Bigger frames usually compress better, smaller ones seek more finely.

t2sz only writes the file. Seeking is done by separate projects the README links: libzstd-seek for C and C++, indexed_zstd for Python, and ratarmount, which mounts the archive through FUSE. Those are the next doors to open.

## Install

```
brew install t2sz
```

## Try this

```
t2sz archive.tar
```
Compresses archive.tar to archive.tar.zst in tar mode, with each member in its own frame.

```
t2sz -s 10M any.file
```
Raw mode: compresses any.file to any.file.zst in blocks of 10M.

```
t2sz -o - archive.tar
```
Writes the seekable compressed result to standard output so you can pipe it.

## What's unique

Each tar member becomes its own zstd frame with a seek table, yet plain zstd tools still decompress the result. The -s and -S options let you tune archive size against seek granularity.

## Caveats

t2sz alone only writes the seekable file; seeking needs a separate reader library or a FUSE mount like ratarmount, and the brief could not confirm how recently the project was updated.

## Links

- [GitHub homepage and README](https://github.com/martinellimarco/t2sz)
- [ratarmount (FUSE mount for seeking)](https://github.com/mxmlnkn/ratarmount)
- [indexed_zstd (Python seeking library)](https://github.com/martinellimarco/indexed_zstd)
- [libzstd-seek (C/C++ seeking library)](https://github.com/martinellimarco/libzstd-seek)
