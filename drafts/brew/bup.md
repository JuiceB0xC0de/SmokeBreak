---
name: bup
title: bup
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, backup, deduplication, git, python, storage]
homepage: https://bup.github.io/
scout_score: 6
status: draft
---

# bup

**TLDR;** A backup tool that cuts files into chunks with a rolling checksum and stores them as git packfiles, so repeated backups only add what changed.

bup is a command-line backup program written mostly in Python with some C. You give it files, it splits them into chunks using a rolling checksum similar to rsync's, and it writes the chunks into a git-format repository, by default in ~/.bup. Before writing a chunk it checks existing packfiles, so data it has already seen is not stored again. Each named backup becomes a git branch, and 'git diff' is useful on the results.

It exists for large files that change a little at a time, such as VM disk images, databases and XML files. Per the README, it aims to back these up incrementally without using much disk space for each version. It also aims to avoid git's slow repacking step and to scale to millions of filenames and hundreds or thousands of gigabytes.

The idea underneath is content-defined chunking. Chunk boundaries come from the data itself, not from fixed offsets, so inserting a few bytes near the start of a file shifts only nearby chunks and the rest still match. Deduplication then works across every backup at once, with no need to track which backup is based on which. An incremental backup also looks like a full backup when restored.

bup writes packfiles with its own code instead of calling git's, but the format is git's. In the project's words, "you can access the stored data even if you don't like bup's user interface." Remote backups go over ssh to a server that only needs bup installed.

## Install

```
brew install bup
# optional: install par2 if you want 'bup fsck -g' to generate recovery data
```

## Try this

```
bup init
```
Creates the default repository at ~/.bup.

```
bup index /etc && bup save -n local-etc /etc
```
Indexes /etc, then saves it as a named backup called local-etc. Running it again stores only new data.

```
bup restore -C ./dest local-etc/latest/etc
```
Restores the latest saved copy of /etc into ./dest.

## What's unique

It reuses git's packfile format as the storage layer but does rolling-hash chunking and deduplication across all backups. Every save restores like a full backup while storing only the new chunks.

## Caveats

The README says bup is 'not remotely as well tested as something like tar' and may 'eat your data', and metadata support is immature on some platforms, for example no ACLs on macOS.

## Links

- [Homepage](https://bup.github.io/)
- [GitHub repository and README](https://github.com/bup/bup)
- [Releases and tags](https://github.com/bup/bup/tags)
