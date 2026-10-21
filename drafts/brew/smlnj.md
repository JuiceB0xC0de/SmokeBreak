---
name: smlnj
title: SML/NJ
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, functional, language, ml]
homepage: https://www.smlnj.org/
scout_score: 6
status: draft
---

# SML/NJ

**TLDR;** A maintained compiler and interactive REPL for Standard ML, a statically typed functional language with a long academic history, plus its own parser and lexer generators.

Standard ML of New Jersey is a compiler for Standard ML '97. You can type expressions into its interactive top level, started with `sml`, or compile whole programs. The homepage describes it as free, open source software, and the brief gives no further statement of motive.

The distribution is more than a bare compiler. It includes ml-yacc and ml-ulex (parser and lexer generators), ml-antlr, ml-burg, a compilation manager driven through ml-build, ml-makedepend for dependencies, asdlgen, and heap2exec for turning a saved heap image into an executable. That makes it a small, self-contained environment for writing language tools in a language designed for exactly that.

The project is old but alive. The README says the code generator moved from MLRISC to LLVM in the 2021 release, and the homepage lists development releases as recent as 2026.3 and a PLDI 2026 paper on a new closure converter. It runs two tracks: a stable legacy 110.99.x line and a 20xx.x development line. The README recommends the legacy version for production and says the development line can still be used day to day.

The larger idea is the ML family itself: algebraic data types, pattern matching, type inference, and a module system. Many later languages borrowed from it. SML/NJ is one of the places to see those ideas in their original form.

## Install

```
brew install smlnj
```

## Try this

```
sml
```
Starts the interactive top level, where you can type Standard ML expressions and see inferred types.

```
ml-yacc --help
```
Shows usage for the bundled parser generator.

```
ml-build --help
```
Shows usage for the tool that builds a heap image from a project using the compilation manager.

## What's unique

It is a long-running Standard ML compiler that ships its own lexer and parser generators and a compilation manager, and it is still actively developed on two release tracks.

## Caveats

The development line is described by its README as not stable and supports only AMD64 and Arm64 on Linux or macOS; the legacy 110.99.9 line is recommended for production.

## Links

- [SML/NJ homepage](https://www.smlnj.org/)
- [Development repository (GitHub)](https://github.com/smlnj/smlnj)
- [Legacy 110.99.x repository (GitHub)](https://github.com/smlnj/legacy)
