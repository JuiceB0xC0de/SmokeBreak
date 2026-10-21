---
name: unshield
title: unshield
source: brew
category: take-things-apart
commitment: quick
tags: [ancient, c, file-formats, installers, quick, reverse-engineering]
homepage: https://github.com/twogood/unshield
scout_score: 7
status: draft
---

# unshield

**TLDR;** Unshield lists and extracts files from InstallShield cabinets, opening up a 1990s Windows installer format that was never officially documented.

Unshield is a command-line tool and C library for InstallShield cabinet files, the data1.cab-style archives that InstallShield installers use to carry the files they install. Point it at a cabinet and it either lists the contents or writes the files to a directory you choose. The README says it extracts the Microsoft Cabinet Files nested inside, so what comes out is ordinary files you can use on any OS.

The author wanted to install Pocket PC applications from InstallShield installers on Linux or FreeBSD without Windows. The format is not officially documented, and the existing Windows tools, i5comp and i6comp, depended on InstallShield decompression code that was not open source. The README puts it this way: "I could have modified i5comp and i6comp to run on other operating systems than Microsoft Windows, but I preferred to use them as a reference for this implementation."

The underlying idea is reverse engineering an undocumented format by reading what already exists. The author used the older tools as a reference, and ran `strings` over InstallShield's decompression code to discover that it relied on zlib. Decompression therefore uses open source zlib, and the parsing is a clean reimplementation. The stated goals are MIT licensing, little-endian and big-endian support, a split between tool and library, InstallShield version 5 and later, and both listing and extraction.

It is a good small door into how installers package files, and into how a format gets worked out from the outside.

## Install

```
brew install unshield
```

## Try this

```
unshield -h
```
Prints the usage help; the README also points to a manual page for more options.

```
unshield l data1.cab
```
Lists the files inside an InstallShield cabinet without extracting anything.

```
unshield -d extracted x data1.cab
```
Extracts the cabinet's contents into a directory named 'extracted'.

## What's unique

It is a from-scratch, MIT-licensed reimplementation of an undocumented 1990s installer format, built by studying older Windows tools and the strings in InstallShield's binaries. The README is candid about that history and its limits.

## Caveats

You need an InstallShield cabinet of your own to try it; very old ones may need the -O flag, which picks a compression method rather than repairing damaged files, and support starts at InstallShield version 5.

## Links

- [GitHub repository and README (homepage)](https://github.com/twogood/unshield)
- [Releases](https://github.com/twogood/unshield/releases)
