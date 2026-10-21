---
name: futhark
title: Futhark
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, functional, gpu, language, parallel]
homepage: https://futhark-lang.org/
scout_score: 6
status: draft
---

# Futhark

**TLDR;** A small functional array language from the University of Copenhagen that compiles to GPU code, so you write ML-style array functions instead of CUDA or OpenCL.

Futhark is a statically typed, purely functional array language in the ML family. You write functions over arrays, and an ahead-of-time optimising compiler turns them into GPU code through CUDA, HIP or OpenCL, or into multi-threaded CPU code. The homepage example is a one-line average: `def average (xs: []f64) = reduce (+) 0 xs / f64.i64 (length xs)`.

It exists because, in the project's words, "it's nicer than writing CUDA or OpenCL by hand!" It is not meant to replace general-purpose languages. The intended use is a small, compute-heavy piece of a larger application. The compiler can emit plain C that any language with a basic FFI can call, or a Python module that drives PyOpenCL.

The idea underneath is that parallel programs are easier to optimise when the language rules out the things that make them hard. Everything is pure, yet the language still offers imperative-style in-place array updates, which it keeps safe through alias analysis and consumption effects. It supports nested data-parallelism and automatic differentiation. It is developed at DIKU, and the project calls itself a research project that is also quite usable for real programming.

## Install

```
brew install futhark
# Running GPU output needs your own C compiler plus OpenCL or CUDA libraries and GPU drivers, installed separately.
```

## Try this

```
futhark --help
```
Lists the compiler's subcommands, including the backends you can target.

## What's unique

It is a research-grade ML-style language that compiles high-level array code to several GPU backends, plain C and Python modules, while keeping purity intact through alias analysis.

## Caveats

Windows support is partial and the multicore backend does not work there; running GPU output needs separately installed drivers and OpenCL or CUDA libraries.

## Links

- [Homepage](https://futhark-lang.org/)
- [GitHub repository](https://github.com/diku-dk/futhark)
- [User's guide (Read the Docs)](http://futhark.readthedocs.io)
