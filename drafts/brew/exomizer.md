---
name: exomizer
title: Exomizer
source: brew
category: take-things-apart
commitment: quick
tags: [8-bit, compression, demoscene, quick, retro]
homepage: https://bitbucket.org/magli143/exomizer/
scout_score: 6
status: draft
---

# Exomizer

**TLDR;** A file compressor built so the compressed data can be unpacked quickly on 8-bit machines, a small door into retro constrained-machine engineering.

Exomizer is a file compressor. Its Homebrew description says it is optimized for decompression in 8-bit environments. The formula installs two executables: `exomizer` and `exobasic`.

The idea underneath it is an asymmetry. Compression can run on a modern laptop and take as long as it likes. Decompression has to run on a machine with a few kilobytes of free memory and a CPU that does one simple thing at a time. A compressor tuned for that case trades effort at pack time for a small, cheap unpacker on the target.

The brief could not read the project's own pages, so details are thin. What the inputs and outputs look like, what `exobasic` does, and which target machines are supported were not visible. The scout links it to the retro demoscene, where squeezing programs and data into tiny machines is a craft. Start with `--help` and let the tool describe itself.

## Install

```
brew install exomizer
```

## Try this

```
exomizer --help
```
Prints the tool's usage and lists its modes, the best way to see what it can do.

```
exobasic --help
```
Prints usage for the second executable, whose purpose the brief could not confirm.

## What's unique

Most compressors optimize for ratio or speed on modern hardware. This one is aimed at making decompression practical on 8-bit machines.

## Caveats

The project's homepage returned no readable content, so status, platform support, and what exobasic does are unverified.

## Links

- [Homepage (Bitbucket, returned no project content)](https://bitbucket.org/magli143/exomizer/)
