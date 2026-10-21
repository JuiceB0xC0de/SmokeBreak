---
name: zpaq
title: zpaq
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, archiver, cli, compression, journaling]
homepage: https://mattmahoney.net/dc/zpaq.html
scout_score: 6
status: draft
---

# zpaq

**TLDR;** A journaling command-line archiver that keeps every version of your files and compresses with a context-mixing model you can reconfigure.

zpaq is an archiver that never overwrites. Each time you add files, it appends a new version to the archive, so you can roll back to how a directory looked at an earlier date. Per the Homebrew description, it is incremental and journaling.

It is written by Matt Mahoney, whose homepage is the project page. His name is tied to the PAQ family of context-mixing compressors, which trade speed for very tight compression. The scout notes that zpaq pairs this with a configurable model language, so the compression method can be described rather than hardcoded. The brief did not confirm further details, so treat that as a lead to follow on the homepage.

The idea underneath is that an archive format can describe its own decompressor. That makes zpaq a door into how compression models predict data, and into how journaled, versioned storage works.

## Install

```
brew install zpaq
```

## Try this

```
zpaq --help
```
Prints the list of commands and options, a good first look at what the archiver can do.

## What's unique

Most archivers overwrite or rebuild; zpaq appends versions, and its compression model is configurable rather than fixed.

## Caveats

The brief was thin, so details beyond the project description and homepage are unverified here.

## Links

- [Homepage](https://mattmahoney.net/dc/zpaq.html)
