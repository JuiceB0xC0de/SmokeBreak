---
name: picoc
title: picoc
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, interpreter, language, quick]
homepage: https://gitlab.com/zsaleeba/picoc
scout_score: 7
status: draft
---

# picoc

**TLDR;** A very small C interpreter that runs C source directly, with no separate compile step, so C works a bit like a scripting language.

picoc is described on its project page as "A very small C interpreter." Homebrew's description says it is for scripting: you hand it C source and it runs the program directly, without a separate compile-and-link step.

C is the language people assume must be compiled ahead of time. An interpreter turns that around. The same syntax you would normally feed to a compiler is read and executed on the spot, which makes C feel closer to a shell script or a Python file.

The brief could not read the README, so what follows is unconfirmed: which parts of C are supported, what the standard library coverage looks like, and how it is meant to be embedded or used day to day. Treat the first session as exploration. The project page shows a creation date of June 2018, and the installed executable is named picoc.

## Install

```
brew install picoc
```

## Try this

```
picoc --help
```
Prints the usage text, which is the quickest way to learn how picoc expects to be given a C file.

## What's unique

It treats C as a language you can run directly, without a compile step. That is an odd stance for a language usually tied to compilers.

## Caveats

The README did not load when this was researched, so supported C features, platform notes, and whether the project is still maintained are all unconfirmed.

## Links

- [Project homepage (GitLab)](https://gitlab.com/zsaleeba/picoc)
