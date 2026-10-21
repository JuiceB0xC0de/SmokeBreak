---
name: metalang99
title: Metalang99
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, functional, header-only, library, metaprogramming, preprocessor]
homepage: https://metalang99.readthedocs.io/en/latest/
scout_score: 6
status: draft
---

# Metalang99

**TLDR;** A functional programming language that runs inside the C preprocessor, with lists, pattern matching and recursion, shipped as plain header files.

Metalang99 is a header-only library for C99 (and C++11 onward). You include metalang99.h and write metaprograms as ML99_EVAL or ML99_call expressions. At compile time an interpreter built from macros reduces them to plain C text: static arrays, struct initializers, overloaded macros. The standard library supplies lists, tuples, choice types, naturals, booleans and assertions. The README also lists algebraic data types, pattern matching, currying and collections.

The author, Hirrolot, argues that C metaprogramming is crippled. The preprocessor has no control flow, integers, unbounded sequences or compound data. Recursion limits in Boost/Preprocessor made his earlier Poica project unmaintainable. Metalang99 is his attempt to give pure C a proper paradigm for metaprograms. It also underpins Datatype99 and Interface99, and the README says it is used at OpenIPC as an indirect dependency.

The underlying idea is the interesting part. Preprocessor macro recursion is prohibited, so the library builds an ad-hoc recursion engine that defers expansions and passes continuations. A continuation-passing-style interpreter sits on top of that and reduces language expressions to final results. The standard library is ordinary metafunctions written in that core language. A fixed number of reduction steps bounds every metaprogram, so in practice it is not Turing-complete.

There is a tutorial book and a formal specification PDF if you want to see how the interpreter is defined. A built-in syntax checker turns many macro mistakes into readable static assertion messages, which is unusual for this kind of code.

## Install

```
brew install metalang99
# Header-only: there is no executable. Add metalang99/include to your include path.
# GCC: add -ftrack-macro-expansion=0. Clang: add -fmacro-backtrace-limit=1. Both avoid useless macro-expansion errors.
# With CMake, the recommended route is FetchContent from the GitHub release tarball, then link the metalang99 target.
```

## Try this

```
gcc playground.c -Imetalang99/include -ftrack-macro-expansion=0
```
Compiles a file of ML99_EVAL lines with GCC's macro backtraces off, so the built-in syntax checker's error messages stay readable.

```
./scripts/bench.sh
```
Run from the repository root, it executes the benchmarks the FAQ points to when asking about compile times.

## What's unique

It treats the preprocessor as an interpreted functional language with a real recursion engine, partial application and ML99_abort/ML99_fatal for debugging macros. Libraries like Boost/Preprocessor instead copy-paste recursive definitions up to a fixed depth.

## Caveats

The README says it is for syntax transformation only, not CPU-bound work. Recursion is bounded by a reduction-step limit, and error messages can still be obscure. I could not confirm a last-commit date, though the docs show version 1.13.5.

## Links

- [Homepage (standard library reference)](https://metalang99.readthedocs.io/en/latest/)
- [GitHub repository](https://github.com/Hirrolot/metalang99)
- [Tutorial book](https://hirrolot.gitbook.io/metalang99/)
- [Specification PDF](https://github.com/hirrolot/metalang99/blob/master/spec/spec.pdf)
