---
name: snobol4
title: SNOBOL4
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, language, pattern-matching, strings]
homepage: https://www.regressive.org/snobol4/
scout_score: 8
status: draft
---

# SNOBOL4

**TLDR;** A string-processing language from Bell Labs where patterns are first-class values and matching backtracks. Odd, old, and a good way to see another model of text handling.

SNOBOL4 (StriNg Oriented and symBOlic Language) is a language for text processing, pattern matching, and much more. Its homepage says it was first designed and implemented at Bell Telephone Laboratories in the 1970s. The Homebrew description says 1960s, and the page does not settle the difference. The language itself is older than most tools you use.

This formula installs `snobol4` along with `sdb` and `snopea`, which look like a debugger and a companion tool. The brief could not confirm which implementation it builds. The likeliest match is Phil Budne's CSNOBOL4, described on the homepage as a port of the original Bell Labs Macro SNOBOL4 for machines with a C89 compiler. Treat that as an inference, not a fact. You feed it a SNOBOL4 program, and it prints or computes whatever the program says.

The idea underneath is that matching is a core part of the language rather than a library bolted on. The scout's notes point to a model of pattern matching with backtracking. The homepage itself does not explain the mechanism, so read the manuals it links to for the details. If you have only met regular expressions as strings inside another language, this is a different way to think about the problem.

The homepage is also a preservation project. It collects implementations for IBM System/360, PDP-10, VAX and CDC 6600 machines, plus books, mailing lists, and In Memoriam notes for Ralph and Madge Griswold. It is a decent starting point for the language's history.

## Install

```
brew install snobol4
```

## Try this

```
snobol4 --help
```
Prints the interpreter's usage and options, which is the safest way to see what this build supports.

```
sdb --help
```
Shows usage for the sdb executable, which appears to be a debugger.

```
snopea --help
```
Shows usage for the snopea executable, a companion tool whose purpose the brief could not confirm.

## What's unique

Pattern matching is built into the language itself, and the homepage doubles as an archive of implementations from mainframes to modern C ports.

## Caveats

The homepage is a resource index, not a README for this package, so the exact implementation, version, and the purpose of sdb and snopea are unverified, and many of its links are old FTP links.

## Links

- [SNOBOL4 Resources homepage (Phil Budne)](https://www.regressive.org/snobol4/)
