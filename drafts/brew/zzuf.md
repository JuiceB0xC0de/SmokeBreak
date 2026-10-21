---
name: zzuf
title: zzuf
source: brew
category: take-things-apart
commitment: quick
tags: [fuzzing, quick, reverse-engineering, security, testing]
homepage: http://caca.zoy.org/wiki/zzuf
scout_score: 5
status: draft
---

# zzuf

**TLDR;** A fuzzer that sits under any program and flips random bits in the data it reads, so you can watch software break on malformed input.

zzuf runs a target program and corrupts what that program reads. It intercepts file and network operations and flips random bits in the input. The program is not modified or recompiled. It simply receives damaged data, and the crashes or memory faults that follow are the output.

The author's motivation is that much of the data applications handle comes from untrusted sources on the Internet, and corrupting it is a cheap way to find bugs. The homepage is modest about it: "zzuf is not rocket science: the idea of fuzzing input data is barely new, but zzuf's main purpose is to make things easier and automated."

The idea underneath is deterministic fuzzing. zzuf's behaviour is deterministic, so a bug found with a given seed can be reproduced. That turns random breakage into something you can investigate. The homepage lists three uses: quality assurance and test suites, security work (segfaults and memory corruption as possible holes), and code coverage analysis.

It is aimed at real-world targets such as media players, image viewers and web browsers, not only unit tests. The homepage says CERT's Basic Fuzzing Framework (BFF) is based on it. Two executables are installed: zzuf, and zzat.

## Install

```
brew install zzuf
```

## Try this

```
zzuf --help
```
Lists the options for controlling how input is corrupted and how the target is run.

```
zzat --help
```
Shows the usage for the second installed tool, zzat.

## What's unique

It is transparent: the target program is untouched because zzuf intercepts its I/O, and runs are seeded so any crash can be reproduced.

## Caveats

The homepage wiki was last modified in 2015, the tutorial is marked work in progress, and the author warns the code is full of black magic and hard to hack on.

## Links

- [Homepage (Caca Labs wiki)](http://caca.zoy.org/wiki/zzuf)
- [GitHub repository](https://github.com/samhocevar/zzuf)
- [Releases](https://github.com/samhocevar/zzuf/releases)
