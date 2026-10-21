---
name: ntfs2btrfs
title: ntfs2btrfs
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, btrfs, filesystems, ntfs, risky, storage]
homepage: https://github.com/maharmstone/ntfs2btrfs
scout_score: 6
status: draft
---

# ntfs2btrfs

**TLDR;** Converts an NTFS volume into Btrfs on the same disk, with no copy-off and restore, and keeps the original as a reflink image you can roll back to.

Ntfs2btrfs takes an NTFS volume and rewrites it as Btrfs in place. On Windows you give it a drive letter, on Linux a device such as /dev/sda1. When it finishes, the disk holds a Btrfs filesystem with your files in it. The README says it is modelled on btrfs-convert, which does the same job for ext2.

The original NTFS image is kept as a reflink copy at image/ntfs.img inside the new filesystem, so the change can be rolled back. Once you are happy with the result you delete that image to get the space back. The reflink is the trick that makes this cheap: the old and new structures share the same data blocks instead of duplicating them.

The door here is how filesystems are laid out on disk. Converting in place means reading one format's metadata (NTFS's records, attributes and runs) and building another format's trees around data that stays where it is. The README also credits Eric Biggers's reverse-engineering of Windows 10 'WOF compressed data' and reuses his code for that part. The README says little more about the mechanism, so the source is the place to read on.

The author also maintains WinBtrfs, a Btrfs driver for Windows, and Quibble, a bootloader. The README says that with Quibble, Windows can boot from Btrfs: 'Yes, if the stars are right.'

## Install

```
brew install ntfs2btrfs
# Needs root on Linux (or an Administrator prompt on Windows) to run. Building from source on Linux needs a recent GCC (15 or later) and CMake.
```

## Try this

```
ntfs2btrfs --help
```
Prints the tool's usage and options without touching any disk.

```
ntfs2btrfs /dev/sda1
```
Run as root on Linux, converts that NTFS partition to Btrfs in place. Use a spare or backed-up partition, and swap in your own device name.

```
ntfs2btrfs.exe D:\
```
On Windows, from an Administrator command prompt, converts the D: drive.

## What's unique

It converts a real NTFS volume in place and keeps the original as a reflink image, so the change can be undone. It also reuses reverse-engineered Windows WOF compression code.

## Caveats

The author says 'I take no responsibility if something goes awry!'; it will not work on a boot drive or a drive with an active pagefile, and encrypted files and cluster sizes over 1MB are unsupported.

## Links

- [Project homepage (GitHub)](https://github.com/maharmstone/ntfs2btrfs)
- [WinBtrfs (Btrfs driver for Windows)](https://github.com/maharmstone/btrfs)
- [Quibble (booting Windows from Btrfs)](https://github.com/maharmstone/quibble)
