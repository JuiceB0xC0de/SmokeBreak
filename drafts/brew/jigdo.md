---
name: jigdo
title: jigdo
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, checksums, downloads, iso, network, protocol]
homepage: https://www.einval.com/~steve/software/jigdo/
scout_score: 6
status: draft
---

# jigdo

**TLDR;** Jigsaw Download rebuilds a huge CD or DVD image byte for byte from small pieces scattered across mirrors, using a text file you can edit.

Jigdo, short for Jigsaw Download, is a toolkit for distributing very large files, mainly ISO9660 and UDF disc images. The publisher runs `jigdo-file` over the image and the set of files it was built from. That produces two things: a small, human-readable `.jigdo` file and a binary `.template` file. A user hands the `.jigdo` file to a download client, which fetches the pieces from one or more mirrors and reassembles the exact image.

The trick is in the template. `jigdo-file` scans the image with a rolling checksum inspired by rsync and finds regions that match known input files. Matched data is left out and replaced with a checksum reference. Unmatched data, such as directory structures, is compressed into the template. The `.jigdo` file is INI-style text mapping each part's checksum to labelled server locations, so adding a mirror means editing a text file, not rebuilding the image.

The homepage says it exists to make downloading very large images as easy as clicking a direct link in a browser, without the hosting problems such files cause server administrators. A CD-sized ISO can be assembled from an ordinary FTP tree of individual files. The pieces can be any size, as long as each is one contiguous region of the image.

The idea underneath is content-addressed transfer: name data by its checksum, and it no longer matters where it comes from. That is a door into rsync, package mirrors and reproducible images.

## Install

```
brew install jigdo
# The homepage says most Linux users should install from their distribution instead; Debian and Ubuntu package it.
```

## Try this

```
jigdo-file --help
```
Lists the commands: make-template builds the .jigdo and .template files, make-image rebuilds an image, verify checks one.

```
jigdo-file make-image
```
Reads a .template plus the files you have and builds the image, in several passes if needed, writing to imagename.tmp until complete.

```
jigdo-lite --help
```
Shows the options of the download front end that takes a .jigdo file and fetches the pieces.

## What's unique

The mirror layout is a plain text file you can edit without touching the image, and the image is rebuilt byte for byte from ordinary files on ordinary servers.

## Caveats

Slow-moving: the latest release noted is 0.8.2 from August 2023; the default MD5 checksums are called no longer secure by the author, and the SHA256 v2 format needs 0.8.0 or newer tools.

## Links

- [Project homepage (Steve McIntyre)](https://www.einval.com/~steve/software/jigdo/)
- [jigdo-file(1) man page (Debian unstable)](https://manpages.debian.org/unstable/jigdo-file/jigdo-file.1.en.html)
- [Source repository (git.einval.com)](https://git.einval.com)
