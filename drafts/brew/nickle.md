---
name: nickle
title: Nickle
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, arbitrary-precision, calculator, language]
homepage: https://www.nickle.org/
scout_score: 7
status: draft
---

# Nickle

**TLDR;** A C-like desk calculator language with exact rationals and arbitrary precision numbers, built as a fuller replacement for bc, dc and expr.

Nickle is a small programming language aimed at numeric work. Its syntax looks like C, but the numbers behave differently: integers have no size limit, rationals are exact, and floating-point reals carry a precision you choose. Arrays, strings, structures, tagged unions and pointers sit alongside them.

The homepage says it was built to provide the functionality of UNIX bc, dc and expr "in much-improved form". It is meant to fill the gap between a calculator and a full language, and to cover what AWK and Perl handle poorly in numeric work. It can run scripts, or it can be used as a prototyping environment for numeric ideas.

Under the calculator surface is a real language. The homepage describes optional static type checking backed by full run-time type checking, typed exceptions, first-class functions, continuations, and a simple thread model with semaphores and mutexes. It says these ideas are drawn from Modula 3, ML and Java.

The design is described in a 2001 Usenix paper. Keith Packard also used Nickle's foreign function interface to build a Cairo binding, cairo-5c. It is an old, quiet corner of language design that is still pleasant to type into.

## Install

```
brew install nickle
```

## Try this

```
nickle --help
```
Prints the interpreter's command-line options so you can see how to start it and run scripts.

## What's unique

It combines exact rationals and unbounded-precision reals with a C-like syntax and a real type system, instead of bc's terse calculator dialect.

## Caveats

The homepage was last updated in 2005 and may not match the current release; it says parametric polymorphism and fuller ADT support are still unimplemented.

## Links

- [Nickle homepage](https://www.nickle.org/)
