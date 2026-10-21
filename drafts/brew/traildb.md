---
name: traildb
title: TrailDB
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c-library, compression, database, events, time-series]
homepage: https://traildb.io/
scout_score: 5
status: draft
---

# TrailDB

**TLDR;** A C library and tool that packs per-user event histories into single immutable compressed files you can query without unpacking them.

TrailDB stores series of discrete events grouped by a primary key: a user's page views and checkouts, or the trades made by a trading algorithm. You hand the library events, and it encodes them into one file. That file is immutable and compressed, and it can be queried directly, decompressing only the parts you ask about.

It was created at AdRoll for event time series. The homepage says AdRoll has used it since 2014 to store and query tens of trillions of web events. The docs position it as a building block that sits beside relational databases and key-value stores, not in place of them.

The idea underneath is trading mutability for compression and simplicity. Because a TrailDB never changes after it is written, it can lean on the predictability of time-based data to compress harder. The docs put the ratio at about Gzip level. Distribution gets simple too: a producer writes a daily file to S3, and many consumers read it in parallel. In the project's words, "TrailDB's secret sauce is data compression."

The core is a C library with bindings for Go, Python, D, Haskell and R. The `tdb` command line tool ships alongside it. The pages read for this entry do not show how to use `tdb`, so expect to find your way with its help output.

## Install

```
brew install traildb
# Linux: the README says no binaries yet. Build from source with libarchive, Judy (libjudy) and pkg-config, then ./waf configure && ./waf install
```

## Try this

```
tdb --help
```
Prints the command line tool's usage, the way in since the README does not show how to use it.

```
traildb_bench --help
```
Shows what the bundled benchmark executable accepts; it is not described in the README or docs.

## What's unique

Most embedded stores optimize for mutable data. TrailDB gives up updates entirely, so each database is one immutable file you can copy, ship to S3 and inspect with ordinary filesystem tools.

## Caveats

Activity looks quiet since around 2021, Linux users must build from source with a picky Judy dependency, and the data cannot be updated or deleted once written.

## Links

- [Homepage](https://traildb.io/)
- [Getting Started guide](http://traildb.io/docs/getting_started/)
- [GitHub repository](https://github.com/traildb/traildb)
- [Docs introduction](https://traildb.io/docs/)
