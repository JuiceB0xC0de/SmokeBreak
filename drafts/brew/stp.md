---
name: stp
title: STP
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bitvectors, logic, smt, solver, symbolic-execution]
homepage: https://stp.github.io/
scout_score: 6
status: draft
---

# STP

**TLDR;** A constraint solver that takes logical puzzles about bitvectors and answers satisfiable or not, the same engine that sits under symbolic-execution bug finders like KLEE.

STP is an SMT solver: you describe a set of constraints over fixed-width integers (bitvectors), arrays, and floating-point numbers, and it tells you whether any assignment of values can satisfy all of them. If one exists, it prints a model. If none does, it says unsat. You hand it a problem as an SMT-LIB2 file or on standard input.

The reason this matters is that a lot of program analysis reduces to exactly this question. Can this input make that branch execute? Can this arithmetic overflow? Can this hash collide? The homepage lists program analysis tools, theorem provers, automated bug finders, cryptographic algorithms, intelligent fuzzers and model checkers as users. It is also the solver underneath KLEE, EXE, and several other symbolic-execution tools.

Inside, STP does word-level preprocessing in repeated passes until it reaches a fixed point, then translates what is left into SAT and hands it to a SAT solver. The backend can be CryptoMiniSat, CaDiCaL, MiniSat, or optionally Incremental Kissat. It also has C, C++, and Python APIs if you want to embed it rather than feed it files.

The door here is the idea of asking a machine to search for inputs that satisfy logic, instead of writing the search yourself. Once you can write a few small bitvector constraints, a lot of reverse engineering and verification papers start to read differently.

## Install

```
brew install stp
```

## Try this

```
stp --help
```
Lists the command-line options, including the choice of SAT backend.

```
stp problem.smt2
```
Runs STP on an SMT-LIB2 file and prints sat or unsat, with a model when satisfiable.

```
stp < problem.smt2
```
Same thing, with the problem piped in on standard input.

## What's unique

STP is a long-running academic solver with several first-place finishes in the QF_BV category at SMT-COP from 2006 to 2023, and unusually detailed docs on its architecture and SAT tuning.

## Caveats

You need to write SMT-LIB2 by hand, only a subset of that language is supported, and the homepage and README disagree on the default SAT backend; I could not confirm what the stp_simple executable does.

## Links

- [Homepage](https://stp.github.io/)
- [Documentation: overview, build, usage, and SMT-LIB2 pages](https://stp.github.io/stp/)
- [Source code on GitHub](https://github.com/stp/stp)
