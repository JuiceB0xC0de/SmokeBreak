---
name: mlton
title: MLton
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, functional, language, standard-ml]
homepage: http://mlton.org
scout_score: 6
status: draft
---

# MLton

**TLDR;** A whole-program optimizing compiler for Standard ML that turns an entire program into one small native executable, with its own lexer, parser and profiler tools.

MLton compiles Standard ML, an old and carefully specified functional language, into standalone native executables. You hand it SML source, plus ML Basis files if you use libraries, and it produces a binary. The homepage describes the results as small and fast: "MLton generates small executables with excellent runtime performance."

The idea underneath is whole-program compilation. Most compilers handle one module at a time and link the pieces afterwards. MLton sees the entire program at once, so it can optimize across module boundaries. The README credits untagged and unboxed native integers, reals and words, unboxed native arrays, and GMP-based arbitrary-precision arithmetic. It also offers several selectable code generation and garbage collection strategies. The README does not go into more detail on the optimization pipeline.

The package also installs a small toolbox for SML work: mllex (a lexer generator), mlyacc (a parser generator), mlprof (a source-level profiler) and mlnlffigen (a generator for foreign-function-interface bindings to C). It supports full SML97 and ships the Basis Library. That makes it a practical way to see what a statically typed functional language looks like when compiled ahead of time as a whole.

## Install

```
brew install mlton
# Depends on gmp, which brew installs for you. Building from source also needs a C compiler with -std=gnu11 support and an existing Standard ML compiler to bootstrap.
```

## Try this

```
mlton --help
```
Prints the compiler's options, including the code generation and optimization switches.

```
mlprof --help
```
Shows how to use the source-level profiler on programs built with profiling enabled.

```
mllex --help
```
Shows the lexer generator's usage, the first step toward writing a parser in SML.

## What's unique

Most SML implementations favor interactive use or quick compilation. MLton compiles the whole program together to get small, fast native binaries, and bundles a lexer generator, parser generator, profiler and C FFI generator.

## Caveats

Building from source needs GMP, a gnu11 C compiler and an existing SML compiler to bootstrap, and the optional docs need a heavy TeX and AsciiDoctor toolchain.

## Links

- [MLton homepage](http://mlton.org)
- [MLton GitHub repository (README)](https://github.com/MLton/mlton)
