---
name: librsync
title: librsync
source: brew
category: fundamentals
commitment: quick
tags: [backup, checksums, delta, library, quick, rsync]
homepage: https://librsync.github.io/
scout_score: 5
status: draft
---

# librsync

**TLDR;** The rsync delta algorithm as a C library, plus rdiff, a tool that makes a patch from a tiny checksum file instead of the old file itself.

librsync packages the core trick of rsync as an API that other programs can call. The `rdiff` tool that comes with it exposes three operations: make a signature of a file, make a delta from that signature and a newer file, and apply the delta to the old file to rebuild the new one.

The unusual part is the first step. The signature is a set of checksums, one per block of the old file. To compute a delta, the other side needs only that signature and the new file. In the README's words, "The rsync algorithm is different from most differencing algorithms because it does not require the presence of the two files to calculate the delta." The two machines never need to see each other's whole file.

The sender scans the new file and looks for blocks whose checksums match the signature, at any byte offset. Matches are likely identical and become references to the old file. The leftover bytes are the difference. That idea sits under backup tools and binary patch distribution. The README says Dropbox, rdiff-backup and Duplicity use it. It began as part of rproxy, an experiment in delta compression for HTTP.

The scope is deliberately narrow. It works on byte streams only, with no filenames, permissions, directories, network code or rsync wire protocol. That leaves the algorithm easy to see by itself.

## Install

```
brew install librsync
```

## Try this

```
rdiff --help
```
Lists the tool's operations and options, including the signature, delta and patch steps.

## What's unique

It is the rsync algorithm on its own, as a reusable library with no wire protocol, SSH or file metadata. That makes it a way to study the delta idea and to build your own sync or backup tool.

## Caveats

It does not talk to an rsync server, and it handles only byte streams, not filenames, permissions or directories; the homepage shows version 2.3.4 with docs generated in February 2023.

## Links

- [librsync homepage](https://librsync.github.io/)
- [Original project site (sourcefrog)](http://librsync.sourcefrog.net/)
