---
name: fpart
title: fpart
source: brew
category: languages-and-oddities
commitment: quick
tags: [backup, bin-packing, c, cli, migration, quick, rsync]
homepage: https://www.fpart.org/
scout_score: 5
status: draft
---

# fpart

**TLDR;** Crawls a file tree and sorts it into similar-sized bags, as lists of file names, so huge copies can be split and run in parallel.

Fpart walks directories and divides what it finds into a set number of partitions. You can ask for a partition count, a maximum file count, or a maximum size per partition. It aims for partitions of similar size and file count, using bin packing. The output is just lists of paths, written to stdout or to numbered files, and other programs consume them. In the README's words: "Fpart does NOT split or modify your data in any way."

The idea underneath is that moving a very large tree is a scheduling problem. If you can cut the tree into balanced pieces, you can hand each piece to its own rsync, tar, or cpio process. Live mode (`-L`) emits each partition as soon as it fills, and hooks (`-w` before, `-W` after) run a shell command with variables like `FPART_PARTFILENAME`. A transfer can therefore start while the crawl is still running.

The companion script fpsync, which the README calls a demonstration, builds on this. It runs the transfer jobs in parallel, including the final `rsync --delete` pass. The author says it helped move over 400 TB at work. Fpart also accepts piped input from `find` or `du`, so it can pack lists it did not crawl itself. The scout framed it as splitting backups onto media, which is one of the examples, but the README leans toward data migration.

## Install

```
brew install fpart
```

## Try this

```
fpart -n 3 -o var-parts /var
```
Splits /var into 3 partitions of roughly equal size and file count, written to var-parts.1 through var-parts.3.

```
du * | fpart -n 2 -a
```
Builds two partitions from du output without re-crawling the filesystem; -a accepts arbitrary values.

```
fpart -L -f 1 -o /tmp/part.out -W 'echo == ${FPART_PARTFILENAME} == ; cat ${FPART_PARTFILENAME}' foo/
```
Live mode with one file per partition; a hook prints each partition's file name and contents as it completes.

## What's unique

It only reads the filesystem and emits lists, so it slots into any copy tool. Live mode with hooks lets a transfer begin before the crawl finishes.

## Caveats

It never splits files, so a tree mixing tiny and huge files, or one giant file, cannot be balanced; it also does not deduplicate overlapping input paths.

## Links

- [Fpart.org homepage](https://www.fpart.org/)
- [Fpart documentation (what it is, examples, live mode, migration)](https://www.fpart.org/fpart/)
- [Changelog](https://www.fpart.org/changelog/)
- [Source on GitHub](https://github.com/martymac/fpart)
