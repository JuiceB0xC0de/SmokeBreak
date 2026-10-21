---
name: ancient
title: ancient
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, amiga, atari, compression, file-formats, retro, reverse-engineering]
homepage: https://github.com/temisu/ancient
scout_score: 7
status: draft
---

# ancient

**TLDR;** A command-line decompressor for dead Amiga and Atari compression formats like ByteKiller, PowerPacker and Pack-Ice, rewritten cleanly and tested on about 10,000 real files.

Ancient is a C++ library with a small command-line tool on top. You give it a file packed by one of dozens of old formats, mostly from Amiga and Atari machines in the 1980s and 1990s, and it detects the format in most cases and writes out the decompressed data. The list includes ByteKiller, Pack-Ice, PowerPacker, StoneCracker, DMS and XPK wrappers, plus Unix compress/pack, gzip and bzip2.

The reason it exists is that many of these algorithms can still be found, but the originals were written for the machines they ran on. Some ports are incomplete or poor, and some are direct translations of M68K assembly. Licensing is often unclear or missing. The author's answer is clean modern implementations under a BSD-style license, tested against a cache of roughly 10k real files. In the author's words: "The code is no good if it does not work properly and the old code have a lot of corner cases."

The idea underneath is that a compression format is a small, complete piece of reverse engineering. Each one is a tight bit of design shaped by the memory and CPU limits of its machine. Detection is not always reliable, because the old formats had weaknesses, which shows how little these files said about themselves. Some formats, such as DMS and PowerPacker PX20, have weak password protection that the code can bypass. The project says it does not do real cryptography.

It does not handle archives or self-extracting executables. Zip and LZH exist only as backends, not as usable archive readers.

## Install

```
brew install ancient
```

## Try this

```
ancient --help
```
Prints the tool's usage, which is the place to start since the README shows no example commands.

## What's unique

It covers a large number of obscure Amiga and Atari formats in one tool, many of which exist nowhere else as clean modern code. It was also rewritten under BSD-style terms to settle the unclear licensing of the originals.

## Caveats

The README has no build or usage instructions, detection is unreliable for some formats, several formats are marked 'verification missing', and archives and self-extracting executables are not supported.

## Links

- [GitHub repository (homepage)](https://github.com/temisu/ancient)
