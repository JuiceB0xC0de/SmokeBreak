---
name: httm
title: httm
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, backup, btrfs, rust, snapshots, tui, zfs]
homepage: https://github.com/kimono-koans/httm
scout_score: 6
status: draft
---

# httm

**TLDR;** A fast command-line Time Machine that lists every unique past version of a file across ZFS, btrfs and other snapshots, and can restore any of them.

httm takes file paths and prints each distinct version of those files found on snapshots, with size, date and location. It deduplicates by modify time and size, or by checksum if you ask for stricter verification. The output can be plain lines, null or tab delimited, JSON or CSV, so it fits into pipes. It also has interactive modes to browse, select, prune and restore.

The problem it addresses is that ZFS, btrfs and NILFS2 snapshots are taken per dataset, not per file. Asking 'what did this one file look like last month?' means digging through snapshot directories by hand. httm does that search for you, and it can reach files behind deleted directories and list deleted files. It also works with Restic repositories and Time Machine backups, and with rsync-ed copies on ext4, XFS or NTFS.

The idea underneath is that a snapshot is just a directory tree frozen in time, so a file's history is already on disk, waiting for a tool to line it up. Once it is lined up, you can diff it, restore it or build something on it. The install also brings small wrapper scripts. `ounce` snapshots a file before a command like rm runs, `bowie` diffs snapshot versions against the live file, and `nicotine` builds a git history from the versions. `equine` is needed for Time Machine support on macOS.

The README says httm 'might change the way you use snapshots'. That depends on whether you already keep snapshots, and the author has a guide to making them.

## Install

```
brew install httm
# Needs a filesystem with snapshots (ZFS, btrfs, NILFS2, Restic or Time Machine) to show anything.
# btrfs, NILFS2 and Restic may need sudo. bowie is required for the default --preview behaviour.
```

## Try this

```
httm --json ~/.histfile
```
Prints every unique snapshot version of your history file as formatted JSON.

```
httm -b -R ~
```
Opens an interactive browser over your home directory, recursively, with unique versions from local snapshots.

```
httm -d=only -b -a -R ~
```
Browses files deleted from your home directory, including versions on alternative replicated snapshot datasets.

## What's unique

It lists unique versions of a file rather than every snapshot, and it reaches into deleted directories, replicated datasets and Time Machine backups. The wrapper scripts show uses beyond browsing, such as snapshotting before an rm.

## Caveats

It needs snapshots to be useful, some modes need root, Restic and Time Machine need extra flags, and the brief could not confirm whether it is currently maintained.

## Links

- [httm on GitHub (homepage and README)](https://github.com/kimono-koans/httm)
- [Asciicast demo](https://asciinema.org/a/637475)
- [A Somewhat Opinionated Guide to Effective ZFS Snapshots](https://kimono-koans.github.io/opinionated-guide/)
