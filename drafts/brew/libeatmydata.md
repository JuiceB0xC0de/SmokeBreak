---
name: libeatmydata
title: libeatmydata
source: brew
category: take-things-apart
commitment: quick
tags: [fsync, ld_preload, linux, quick, syscalls, testing]
homepage: https://www.flamingspork.com/projects/libeatmydata/
scout_score: 7
status: draft
---

# libeatmydata

**TLDR;** A tiny LD_PRELOAD library that makes any program's fsync calls do nothing, so it runs faster and stops being crash-safe.

libeatmydata is a small shared library plus a wrapper script called `eatmydata`. You run a command through the wrapper, and the fsync family of calls, including `open(O_SYNC)`, return without flushing anything to disk. The program being run is not modified and does not know.

The author built it to speed up database test runs and similar workloads where synchronous disk writes dominate the runtime. The homepage benchmark runs a MySQL InnoDB test suite in about 3m36s normally and about 2m10s under the library, which the author describes as saving "about a third of the total runtime." That is one test run, not a general promise.

The trick underneath is `LD_PRELOAD`. The dynamic linker loads the library ahead of the C library, so its versions of the calls are found first. The wrapper sets this up so you do not have to set the variable by hand. It is a compact example of how much a program trusts the layer below it, and how easily that layer can lie. Programs that care about durability ask the OS to confirm data is on disk, and here the answer is always yes.

The name is a warning. The homepage says: "DO NOT use libeatmydata on software where you care about what it stores."

## Install

```
brew install libeatmydata
```

## Try this

```
eatmydata --help
```
Shows how the wrapper is invoked.

```
eatmydata foo
```
Runs the program foo with its fsync calls turned into no-ops. Replace foo with any command that writes data.

## What's unique

It speeds up unmodified software by lying at the system-call boundary instead of changing the program or its configuration. The whole idea fits in one preload library.

## Caveats

Not crash-safe by design, so use it only on throwaway data such as test runs and disposable databases; the author mainly uses it on Linux, with macOS and some other platforms reported to work.

## Links

- [Project homepage](https://www.flamingspork.com/projects/libeatmydata/)
- [GitHub repository](https://github.com/stewartsmith/libeatmydata)
