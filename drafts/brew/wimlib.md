---
name: wimlib
title: wimlib
source: brew
category: take-things-apart
commitment: quick
tags: [archives, compression, deduplication, file-formats, quick, wim, windows]
homepage: https://wimlib.net/
scout_score: 5
status: draft
---

# wimlib

**TLDR;** Read, build, and modify Windows Imaging (WIM) archives from any OS, with content deduplicated by hash and compressed with Microsoft's own formats.

WIM is the archive format Windows uses for install media and system images. It resembles ZIP but holds several images in one file, keeps Windows metadata such as ACLs and named streams, and stores each distinct file content only once. wimlib is a C library that reads and writes these files, along with ESD archives, which are WIM files using solid LZMS compression. The brew package installs its command-line frontend as a set of separate tools: wimcapture, wimapply, wimdir, wiminfo, wimverify and more.

The deduplication is the interesting part. Each file's content is identified by its SHA-1 digest and stored once per archive, however many images, duplicate files, hard links or data streams point at it. wimlib does this automatically when it creates or updates an archive. It implements XPRESS, LZX and LZMS compression, with LZX as the default, and has a solid mode.

It exists as a free, cross-platform alternative to Microsoft's WIMGAPI, ImageX and DISM, so non-Windows systems can work with these files. The homepage says it can deploy Windows from Linux, including capturing NTFS block devices through NTFS-3G. It also says its LZX and LZMS compressors typically beat Microsoft's own, and offers them as standalone libraries. In the project's words, they are "independent, high quality open source compressors and decompressors for several compression formats used by Microsoft which are not as well known as more open formats."

That makes it a handy way to look inside a Windows install image without Windows, and a small lesson in content-addressed storage along the way.

## Install

```
brew install wimlib
```

## Try this

```
wimlib-imagex --help
```
Lists the subcommands (capture, apply, dir, info, verify and others) that the separate wim* tools wrap.

```
wiminfo --help
```
Shows how to print the images, sizes and metadata stored in a WIM file.

```
wimdir --help
```
Shows how to list the files inside an image in a WIM without extracting it.

## What's unique

It gives non-Windows systems a full read and write path for WIM and ESD files, including NTFS-correct metadata, and ships LZX and LZMS compressors as reusable libraries.

## Caveats

Mounting a WIM (wimmount, wimmountrw) is Linux-only and needs FUSE, and wimlib cannot decrypt Microsoft's partially encrypted ESD archives.

## Links

- [wimlib homepage](https://wimlib.net/)
- [GitHub mirror of source](https://github.com/ebiggers/wimlib)
