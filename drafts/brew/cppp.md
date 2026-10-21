---
name: cppp
title: cppp
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, cli, legacy-code, preprocessor, quick]
homepage: https://www.muppetlabs.com/~breadbox/software/cppp.html
scout_score: 5
status: draft
---

# cppp

**TLDR;** A partial C preprocessor that resolves only the #ifdef-style conditionals you name and leaves everything else untouched, for cleaning old code.

cppp reads C source on input and writes C source on output. You tell it which macros are defined (-D) or undefined (-U), and it resolves the conditionals that test them: #ifdef, #ifndef, #if, #elif, #elifdef and #elifndef. Branches that can no longer be taken are removed, and the surviving branch is kept without its directive lines. It does not expand macros or do any of the preprocessor's other work.

The interesting part is what it does with questions it cannot answer. A macro it has not been told about is treated as indeterminate, and the conditional that tests it passes through. If an #if expression is only partly decided, cppp rewrites it to keep just the undecided part. Numeric constants given with -D, such as MYLIB_VERSION=0x0102, can be used in integer comparisons, so a version check like `MYLIB_VERSION >= ((1 << 8) | 13)` gets evaluated and one side of it disappears.

The author, Brian Raiter, wrote it for legacy codebases where #ifdef statements have piled up over time and hurt legibility. He first wrote it as a learning exercise, then said it later saved him from a tedious and error-prone cleanup. The idea underneath is partial evaluation: decide what you can, leave the rest alone. It is a good way to see how the preprocessor's conditional logic works, since you can feed it a file and watch exactly which parts collapse.

## Install

```
brew install cppp
```

## Try this

```
cppp -DFOO
```
Treats FOO as defined, so the FOO branch is kept and the #else branch is dropped.

```
cppp -UFOO -UBAZ
```
Treats FOO and BAZ as undefined, so the #ifdef FOO branch is removed and the #ifndef BAZ branch is kept.

```
cppp -DMYLIB_VERSION=0x0102
```
Assigns a numeric value, so a test like MYLIB_VERSION >= ((1 << 8) | 13) evaluates to false and the older API branch is kept.

## What's unique

It is deliberately partial: it resolves only what it is told about and passes everything else through unchanged, rather than doing a full preprocessing pass like the standard preprocessor.

## Caveats

The homepage gives no release date or commit history, so maintenance status is unknown, and the author warns the source is messy: "Use the program, not the source."

## Links

- [cppp homepage (Brian Raiter)](https://www.muppetlabs.com/~breadbox/software/cppp.html)
