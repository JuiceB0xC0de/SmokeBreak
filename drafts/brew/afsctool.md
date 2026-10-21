---
name: afsctool
title: afsctool
source: brew
category: take-things-apart
commitment: quick
tags: [apfs, compression, filesystems, macos, quick, zfs]
homepage: https://brkirch.wordpress.com/afsctool/
scout_score: 5
status: draft
---

# afsctool

**TLDR;** A macOS command-line tool that applies, removes, and reports Apple's transparent filesystem compression on files Finder won't compress for you.

afsctool takes file or folder paths and either compresses them with Apple File System Compression, decompresses files that already use it, or prints statistics about what is compressed. The compression is transparent: files look and behave the same to applications, but take less space on disk. The original blog post describes it as working with HFS+ compression on Mac OS 10.6 or later. The RJVB fork, which is the README the brief was built from, adds APFS, LZVN and LZFSE support, and a second executable called zfsctool.

The author's stated motive is that Finder gives you no way to compress existing files this way. The blog's own example is a large World of Warcraft install. One commenter reports running it nightly from cron over mail and sync directories in ~/Library to save SSD space.

Per the fork README, it compresses by writing each file back in compressed form, with an undo path if something goes wrong and an optional backup. The -j and -J flags set a worker-thread count. -j parallelises only the compression step while disk I/O runs with exclusive access, and -J parallelises every step. Combining -S with -R compresses the largest files first, which limits free-space fragmentation.

zfsctool is the odd idea here. ZFS compression is set per dataset and there is no API to get or set it per file, so it recompresses by changing the dataset's compression property, rewriting the files, then resetting the property. That also affects other files written during the rewrite. It is a door into how filesystems store compressed data, and how much of it is hidden from ordinary tools.

## Install

```
brew install afsctool
# macOS only. The brief's README describes a CMake source build (needs zlib 1.2.8+, google-sparsehash, cmake, pkgconfig, and git clone --recurse-submodules). zfsctool needs OpenZFS on OS X at runtime.
```

## Try this

```
afsctool --help
```
Prints the usage text and the list of flags.

```
zfsctool --help
```
Prints usage for the ZFS companion tool.

```
sudo afsctool -cv expansion4.MPQ
```
Compresses one large file verbosely. In a blog comment this particular run reported 'Unable to compress file.' so expect some files to refuse.

## What's unique

It exposes Apple's built-in transparent compression, which Finder doesn't offer on existing files, and adds parallel compression modes. zfsctool tries the same trick on ZFS by flipping a dataset property and rewriting.

## Caveats

macOS only. Maintenance status is unclear, the brief found no release or commit dates, and zfsctool is early work that only prints statistics.

## Links

- [Homepage (brkirch blog)](https://brkirch.wordpress.com/afsctool/)
- [RJVB fork on GitHub](https://github.com/RJVB/afsctool)
- [LZFSE reference implementation](https://github.com/lzfse/lzfse)
