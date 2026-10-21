---
name: algol68g
title: Algol 68 Genie
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, algol, ancient, interpreter, language]
homepage: https://algol68genie.nl/en/algol-68-genie/
scout_score: 8
status: draft
---

# Algol 68 Genie

**TLDR;** A from-scratch interpreter for Algol 68, the 1968 language with a two-level grammar, runtime checks, a debugger and arbitrary-precision arithmetic.

Algol 68 Genie (`a68g`) runs programs written in Algol 68, a historical language whose influence shows up in later languages but which few people have ever written in. You hand it source code and it interprets it. While it runs it checks for uninitialised objects, out-of-range subscripts or values, and dangling references. A GDB-style debugger is available during execution. It also offers arbitrary-precision integer, real and complex arithmetic.

The project exists to preserve the language for educational and scientific-historical reasons. It is a recent implementation written from scratch, shipped with a Revised Report, a programming guide and example programs. The author wants people to be able to study the language and its context-dependent two-level grammar, and also to use it for medium-sized programming tasks.

The door it opens is the grammar. Algol 68 is defined by a two-level van Wijngaarden grammar (the W-grammar), which is unlike the grammars most developers meet. The homepage says the interpreter's hand-coded parser for it is the basis of ga68, an experimental Algol 68 front-end merged into GCC 16.1.

The interpreter adds one extension to the language: Charles Lindsey's 1976 partial parametrization proposal, which gives the imperative language a functional sub-language. On Linux and FreeBSD, well-debugged code can optionally be partially precompiled to object code that is linked in at runtime.

## Install

```
brew install algol68g
# installs the a68g executable; depends on readline
```

## Try this

```
a68g --help
```
Prints the interpreter's command-line options, a first look at what it can do.

## What's unique

It is one of the most complete Algol 68 implementations, written from scratch rather than derived from an older compiler, and its parser is the basis of the Algol 68 front-end in GCC.

## Caveats

The project aims to preserve the original language, not modernise it, and the optional precompilation works only on Linux and FreeBSD.

## Links

- [Algol 68 Genie project homepage](https://algol68genie.nl/en/algol-68-genie/)
