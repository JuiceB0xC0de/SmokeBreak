---
name: ratarmount
title: ratarmount
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, archives, filesystem, fuse, python, sqlite]
homepage: https://github.com/mxmlnkn/ratarmount
scout_score: 5
status: draft
---

# ratarmount

**TLDR;** Mounts tar, zip, rar, 7z and other archives as read-only filesystems, using a SQLite index to jump straight to any file without extracting.

Ratarmount takes an archive, a folder, or a remote URI and exposes its contents as a FUSE mount point. You browse and read files with ordinary tools, and nothing is extracted to disk. It handles TAR (including compressed TAR), ZIP, RAR, 7z, SquashFS and AppImage, among others.

The README starts from a concrete problem: a 1.31TB TAR of ImageNet holding 14.2 million files. You may not have the disk space, the time, or a filesystem fast enough to unpack it. Earlier tools such as archivemount and tarindexer were slow to mount, handled random access poorly, or needed a database setup.

The idea underneath is the index. On first mount, ratarmount scans the archive and records every file's name, ownership, permissions and offset in an SQLite database stored next to the archive or in `~/.ratarmount/`. For gzip, bzip2, xz and zstd streams it also stores seek points, so decompression can resume near the requested byte instead of from the start. Later mounts reuse the index. In the README's words: "Ratarmount takes ~15min to create a ~150MB index and <1ms for opening an already created index (SQLite database) and mounting the TAR."

It also does some odd extras. It can mount archives nested inside archives, union several folders or archives under one mount point, and mount a remote folder over SSH. When a file appears several times in an archive, the older copies show up under a hidden `foo.versions/` folder.

## Install

```
brew install ratarmount
# Needs FUSE: macFUSE on macOS, fuse on Debian-like Linux. Alternatives: pip install ratarmount, conda install -c conda-forge ratarmount, or the AppImage from the releases page.
```

## Try this

```
ratarmount archive.tar.gz
```
Mounts the compressed archive at a folder named after it, so you can browse its contents without extracting.

```
ratarmount --recursive archive.tar mountpoint
```
Mounts the archive and every archive nested inside it under mountpoint.

```
ratarmount folder1 folder2 mountpoint
```
Union-mounts two folders so both appear under mountpoint, with the rightmost source winning on conflicts.

## What's unique

It keeps a reusable SQLite index plus seek points for compressed streams, so reading one file in a huge archive does not mean decompressing everything before it. It can also mount archives recursively and union them with folders.

## Caveats

Needs FUSE and works on Linux and macOS only; it is read-only by default, ordinary xz and zstd files are not truly seekable, and the README's install examples lag behind the 1.x releases.

## Links

- [Homepage / README (GitHub)](https://github.com/mxmlnkn/ratarmount)
- [Releases](https://github.com/mxmlnkn/ratarmount/releases)
- [Command-line help text](https://raw.githubusercontent.com/mxmlnkn/ratarmount/master/tests/ratarmount-help.txt)
