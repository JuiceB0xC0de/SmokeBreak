---
name: dislocker
title: dislocker
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, bitlocker, encryption, filesystems, fuse, reverse-engineering]
homepage: https://github.com/Aorimn/dislocker
scout_score: 6
status: draft
---

# dislocker

**TLDR;** A FUSE driver that unlocks Windows BitLocker volumes on Linux, exposing the decrypted disk as a virtual NTFS file you can mount.

Dislocker opens BitLocker-encrypted Windows volumes without Windows. You give it a partition, or a BitLocker To Go USB stick, plus key material such as a password or recovery key. It hands back the decrypted contents. Its README says it "has been designed to read BitLocker encrypted partitions under a Linux system."

There are two routes. `dislocker-fuse` decrypts on demand: once the keys unlock, a file named `dislocker-file` appears in the mount point. That file is a virtual NTFS partition you can mount normally, and writes to it go through to the real BitLocker volume. `dislocker-file` instead decrypts the whole volume into a separate flat image. That copy is detached from the original and as large as the volume, so it can take a while to make.

Underneath is the interesting part: an encrypted on-disk format that someone had to understand well enough to reimplement. The README covers volumes from Vista through Windows 10, with AES-CBC or AES-XTS at 128 or 256 bits, with or without the Elephant diffuser. BitLocker To Go adds a twist. A FAT32 filesystem and an encrypted volume share one partition, and dislocker treats the whole partition as the BitLocker volume, so one tool handles internal drives and USB sticks.

It is built as a library with several binaries on top, which makes it a readable way into how full-disk encryption layers sit between a block device and a filesystem.

## Install

```
brew install dislocker
# Needs FUSE (libfuse is a dependency). Mounting needs a BitLocker volume and its password, recovery key or key file. The README describes building from source with cmake and make; see INSTALL.md.
```

## Try this

```
dislocker --help
```
Prints the options for unlocking a volume, including the ways of supplying key material.

```
dislocker-fuse --help
```
Shows the options for the on-demand FUSE mount, which exposes the decrypted disk as a virtual NTFS file.

```
dislocker-metadata --help
```
Shows how to inspect the BitLocker metadata of a volume.

## What's unique

The FUSE route gives a live, writable view of the decrypted disk without making a full copy, while the flat-file route gives a safe detached image. One tool handles both internal BitLocker drives and BitLocker To Go sticks.

## Caveats

Writing through dislocker-fuse changes the real BitLocker volume, dislocker-file needs free space equal to the volume size, and the README itself says "There may be bugs."

## Links

- [GitHub repository (homepage)](https://github.com/Aorimn/dislocker)
- [Issues](https://github.com/Aorimn/dislocker/issues)
- [CI tests workflow](https://github.com/Aorimn/dislocker/actions/workflows/tests.yml)
