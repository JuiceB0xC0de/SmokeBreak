---
name: form
title: FORM
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, math, physics, symbolic-algebra, term-rewriting]
homepage: https://www.nikhef.nl/~form/
scout_score: 7
status: draft
---

# FORM

**TLDR;** A symbolic algebra system from high-energy physics that rewrites huge expressions by pattern matching and keeps them on disk instead of in RAM.

FORM reads a program from a text file, holds symbolic expressions, and applies rewrite rules to them until nothing more matches. You declare symbols and functions, define a Local expression, then write statements such as `id` that say what pattern to replace with what. The result is printed as text in mathematical notation.

It was written by Jos Vermaseren at NIKHEF, the Dutch institute for subatomic physics. The README says it has been "essential for many state-of-the-art computations in High Energy Physics." Those calculations can produce expressions with millions of terms, which is why the landmark feature is that expression size is "only limited by the available disk space and not by the available RAM."

The idea underneath is term rewriting: algebra as a set of pattern-matching rules applied repeatedly. The README's examples show this directly. A repeat loop rewrites x^10 into 34 + 55*x, and a pattern reorders the arguments of f(1,2,x,3,4) to give f(3,4,1,2). It reads more like a small rule-based language than a calculator, and that is the door into computer algebra for physics.

The executables are `form` and `tform`. The brief does not say what distinguishes them, so check the manual.

## Install

```
brew install form
# Optional libraries gmp, mpfr, zstd, zlib and flint improve performance. Arbitrary-precision floats need both gmp and mpfr.
# A precompiled binary is also on PyPI as form-bin.
```

## Try this

```
form --help
```
Lists the command-line options for running a FORM program file.

```
tform --help
```
Shows the options for the second installed executable, so you can compare it with form.

## What's unique

Expression size is bounded by disk space rather than RAM, which is unusual for a symbolic algebra tool. It comes from particle physics practice rather than general-purpose math software.

## Caveats

The brief could not confirm recent release dates, and the official homepage was unreachable when it was checked, so the GitHub README and online manual are the reliable sources.

## Links

- [Official homepage (unreachable at fetch time)](https://www.nikhef.nl/~form/)
- [GitHub repository (form-dev/form)](https://github.com/form-dev/form)
- [Latest reference manual](https://form-dev.github.io/form-docs/stable/manual/)
- [PyPI precompiled binary (form-bin)](https://pypi.org/project/form-bin/)
