---
name: testdisk
title: TestDisk
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, data-recovery, filesystems, forensics, partitions, tui]
homepage: https://www.cgsecurity.org/wiki/TestDisk
scout_score: 6
status: draft
---

# TestDisk

**TLDR;** A terminal tool that reads a disk's raw partition tables and backup boot sectors to rebuild lost partitions, with PhotoRec to carve files from wrecks.

TestDisk works below the filesystem. It scans a physical disk, USB stick or disk image for partition structures and filesystem signatures, including backup boot sectors on FAT32 and NTFS and backup superblocks on ext2/3/4. It lists what it finds, and you choose which partitions to keep and write back to the partition table. A damaged boot sector can be repaired by copying the valid backup over it. It can also undelete files from FAT, exFAT, NTFS and ext2 and copy them out.

The wiki says it was designed to recover lost partitions and make non-booting disks bootable again when the cause is faulty software, certain viruses, or human error such as deleting a partition table. It also aims to help novices collect detailed information about a dead drive to send to a technician.

The package also installs PhotoRec, which takes a different approach. It ignores the filesystem and identifies files by their content signatures, which helps when the filesystem is too damaged to read. A third tool, fidentify, ships alongside them.

The idea underneath is that a disk is just numbered sectors with some structure laid on top, and that structure is often duplicated. Working through a recovery in the menus is a good way to see those raw structures.

## Install

```
brew install testdisk
# Working on physical devices needs root (sudo) or Administrator rights. On macOS, TestDisk restarts itself under sudo after you confirm.
```

## Try this

```
testdisk image.dd
```
Opens the menu-driven interface on a raw disk image, so you can practise partition recovery without touching a real drive.

```
testdisk image.E01
```
Opens an EnCase EWF image to recover files from it.

```
photorec --help
```
Shows the options of the signature-based file carver that ships with TestDisk.

## What's unique

It can often bring back a whole lost partition, not just individual files, and it pairs that with PhotoRec's signature carving for when the filesystem is beyond reading.

## Caveats

Physical-device work needs root or Administrator, and the step-by-step guide still shows older 6.13 paths even though the wiki lists 7.2 (February 2024) as the latest stable version.

## Links

- [TestDisk homepage (CGSecurity wiki)](https://www.cgsecurity.org/wiki/TestDisk)
- [TestDisk Step By Step recovery guide](https://www.cgsecurity.org/wiki/TestDisk_Step_By_Step)
- [TestDisk & PhotoRec forum](https://forum.cgsecurity.org/phpBB3/)
