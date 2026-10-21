---
name: recoverpy
title: recoverpy
source: brew
category: take-things-apart
commitment: quick
tags: [disk, forensics, linux, python, quick, tui]
homepage: https://github.com/PabloLec/recoverpy
scout_score: 5
status: draft
---

# recoverpy

**TLDR;** A terminal tool that scans a raw disk for a string you remember, then lets you walk the surrounding blocks to recover deleted text by hand.

RecoverPy opens a partition or disk image read-only and streams through it in fixed-size chunks, looking for a byte string you type. Chunks overlap slightly so a match that straddles a boundary is not missed. Each hit is recorded by its absolute offset on the device. You open a match, step through the neighbouring blocks, select the part you want, and save it.

The idea underneath is the one in the README: when a file is deleted, its metadata goes first, while the data blocks often stay put until something else reuses them. RecoverPy ignores the filesystem entirely. It does not rebuild files, guess where they end, or restore names. It shows you what bytes are physically there and lets you read them.

That makes it a small door into how storage works. You learn that a delete is mostly bookkeeping, that offsets matter more than paths, and that a distinctive search string beats a common word. The README suggests a unique identifier, a configuration key, or a sentence fragment. The scan is streaming and memory-bounded, so the full partition is never loaded into RAM.

## Install

```
uv tool install recoverpy
# or: python -m pip install recoverpy
# Linux only, Python 3.9+. Reading raw block devices needs sudo. Homebrew's formula pulls in Python as a dependency.
```

## Try this

```
sudo uvx recoverpy
```
Runs the TUI once without a permanent install, with sudo for raw block device access.

```
sudo recoverpy
```
Starts the TUI after installing. Pick a partition, type a search string, and start the scan.

```
recoverpy --help
```
Prints the command-line help for the executable.

## What's unique

It does no filesystem parsing or signature carving. You search the raw device for any string you choose, then reassemble fragments by walking the adjacent blocks yourself.

## Caveats

Linux only, needs sudo, and cannot recover blocks that have been overwritten; results may be partial, and the output is raw content with no filenames.

## Links

- [Homepage and README (GitHub)](https://github.com/PabloLec/recoverpy)
