---
name: judy
title: Judy
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, data-structures, library]
homepage: https://judy.sourceforge.net/
scout_score: 6
status: draft
---

# Judy

**TLDR;** A C library for a sparse dynamic array that starts as a null pointer, grows only as you fill it, and claims to replace hash tables and trees.

Judy is a C library that implements a sparse dynamic array. You declare a Judy array with a null pointer. It uses memory only for elements you have populated, and it can grow to use all available memory if you let it. The API is small: insert, retrieve, and delete calls, with sort, search, count, and sequential access built in.

The homepage pitches it as a single structure that can stand in for arrays, sparse arrays, hash tables, B-trees, binary trees, linear lists, skiplists, and some sort, search, and counting code. The goal is a dynamically sized, associative array that is fast and memory-efficient, without reworking code when the data grows or shrinks.

The unusual part is the design stance. In the project's words, "Tuning and configuring are not required (in fact not even possible)." There are no knobs to turn, so the library has to pick good behavior on its own. The scout's notes call the design trie-based, but the homepage the brief draws on does not confirm that. The site links to technical descriptions, a 10-minute version and a 3-hour version, which are the obvious next step if you want to see how it works.

The library installs no executables. It is something to link against and write small C programs with, so the payoff comes from reading the docs and trying it on your own data.

## Install

```
brew install judy
# Installs the C library only, with no command-line tools. You need a C compiler to use it.
```

## Try this

## What's unique

One structure aims to cover the jobs of hash tables, trees, and skiplists, and it deliberately offers no tuning parameters.

## Caveats

The homepage footer reads 'Modified: 11/10/04' and '© 2004 Judy Team', so the project is old and quiet, and the 'state-of-the-art' claim is a 2004 one.

## Links

- [Judy Arrays homepage](https://judy.sourceforge.net/)
