---
name: rdb
title: rdb
source: brew
category: take-things-apart
commitment: quick
tags: [binary-format, flame-graph, go, quick, redis, reverse-engineering]
homepage: https://github.com/HDT3213/rdb/
scout_score: 5
status: draft
---

# rdb

**TLDR;** A Go tool that opens Redis RDB snapshot files and turns them into JSON, memory reports, biggest-key lists, or a flame graph of key prefixes.

An RDB file is the binary snapshot Redis writes to disk: every key, its type, its expiry, packed into a compact format. Normally you never look at it. `rdb` reads one and streams out each object (strings, lists, sets, hashes, sorted sets, streams, functions) so you can see what a running database actually holds.

One binary, several views of the same file. `-c json` dumps every key. `-c memory` writes a CSV of per-key sizes. `-c bigkey` lists the largest keys. `-c aof` converts the snapshot into a stream of RESP commands. `-c flamegraph` splits keys on a separator such as `:`, groups them by shared prefix, and serves a flame graph on a local port, so a key naming scheme turns into a picture of where the memory went.

The README calls it "a golang implemented Redis RDB parser for secondary development and memory analysis" and credits redis-rdb-tools as the inspiration. It also works as a Go package: you can walk objects in code and write new RDB files. Sizes are estimates based on the RDB-encoded size of each key, not Redis's live allocator numbers, so read them as a guide to proportions rather than exact bytes.

## Install

```
brew install rdb
# or, with the Go toolchain: go install github.com/hdt3213/rdb@latest
# You need an .rdb file: a dump from your own Redis, or the samples in the repo's cases/ directory.
```

## Try this

```
rdb
```
Prints the built-in manual listing the -c modes and options.

```
rdb -c bigkey -n 5 cases/memory.rdb
```
Lists the five largest keys in the sample file by estimated size.

```
rdb -c flamegraph -port 16379 -sep : dump.rdb
```
Serves a flame graph of memory by key prefix on local port 16379, splitting keys on ':'.

## What's unique

One binary covers JSON export, memory report, bigkey and hotkey lists, prefix breakdown and flame graph from the same snapshot, and the Go API can also write RDB files.

## Caveats

The hotkey mode only works on files from Redis instances using an LFU eviction policy, and support is stated only up to RDB version 12 (Redis 7.2), so newer dumps may not parse.

## Links

- [GitHub repository (homepage)](https://github.com/HDT3213/rdb/)
- [Go package reference](https://pkg.go.dev/github.com/hdt3213/rdb)
- [Releases (prebuilt binaries)](https://github.com/HDT3213/rdb/releases)
