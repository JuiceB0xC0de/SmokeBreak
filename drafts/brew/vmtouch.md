---
name: vmtouch
title: vmtouch
source: brew
category: take-things-apart
commitment: quick
tags: [cli, filesystem, memory, page-cache, quick, unix]
homepage: https://hoytech.com/vmtouch/
scout_score: 6
status: draft
---

# vmtouch

**TLDR;** vmtouch shows which pages of a file are sitting in the operating system's page cache, and lets you load, evict or lock them yourself.

vmtouch takes files or directories and reports how many of their pages are currently resident in memory, as page counts and percentages. Point it at /bin/ and the README's example reports 348 of 1307 pages cached, 26.6%. With -v it draws a per-page progress bar for a single file, so you can see which parts of the file are in RAM.

It does more than look. -t touches a file to pull it into cache, -e evicts it, and -l locks it into physical memory so the OS won't evict it. -d runs it as a daemon. The README lists uses such as finding out which files the OS is caching, preserving a virtual memory profile when failing over servers, keeping a hot-standby file server, and maintaining "soft quotas" of cache usage.

The idea underneath is that file reads on Unix go through a page cache, so the same read can be fast or slow depending on what happened earlier. Normally that is invisible. Here you can run tail on the end of a big file, check again, and watch only the last pages light up. Then you can touch the whole file and watch the bar fill. The README's own example took about 12 seconds to load a large file.

The homepage and README do not describe the internals, and they point to a separate TUNING.md for system tuning parameters.

## Install

```
brew install vmtouch
# documented upstream route, from source: git clone https://github.com/hoytech/vmtouch.git && cd vmtouch && make && sudo make install
```

## Try this

```
vmtouch /bin/
```
Prints a summary of files, directories and how many pages of /bin/ are resident in cache.

```
vmtouch -v big-dataset.txt
```
Shows a per-page progress bar of which parts of the file are cached. Use any large file you have.

```
vmtouch -vt big-dataset.txt
```
Touches every page to load the file into memory, with an animated progress bar showing the cache filling.

## What's unique

It makes the page cache visible and steerable from one small command, down to which pages of a specific file are resident. The homepage links an Instagram architecture write-up that used it in real work.

## Caveats

The README gives no release date, and its copyright line reads 2009-2017 with a travis-ci.org badge, so the project may be quiet; it also names no specific supported platforms beyond 'unix and unix-like systems'.

## Links

- [Homepage](https://hoytech.com/vmtouch/)
- [Online manual (vmtouch.pod)](https://github.com/hoytech/vmtouch/blob/master/vmtouch.pod)
- [System tuning parameters (TUNING.md)](https://github.com/hoytech/vmtouch/blob/master/TUNING.md)
- [GitHub repository](https://github.com/hoytech/vmtouch)
