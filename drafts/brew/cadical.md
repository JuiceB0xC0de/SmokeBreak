---
name: cadical
title: CaDiCaL
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, library, logic, math, sat, solver]
homepage: https://fmv.jku.at/cadical/
scout_score: 5
status: draft
---

# CaDiCaL

**TLDR;** A readable, competition-winning SAT solver: hand it a Boolean formula in DIMACS format and it tells you whether any assignment satisfies it.

CaDiCaL is a SAT solver, a program that decides whether a Boolean formula can be made true by some assignment of its variables. It uses conflict-driven clause learning (CDCL). The input is a formula in DIMACS format, and the usage line from the README is `cadical [ dimacs [ proof ] ]`. The optional second file receives a proof of the result. It also builds as a C library, `libcadical.a`, with an API you can call from your own code.

The author's stated goal was a CDCL solver that is easy to understand and change, without being much slower than other state-of-the-art solvers. The README says the design was only partly simplified compared with Lingeling, but the code is much better documented. That makes it a reasonable place to read how a modern solver is put together.

The idea underneath is that a huge number of hard problems can be rewritten as one question: is this pile of true/false constraints satisfiable? Scheduling, puzzles, hardware verification and package dependency resolution all reduce to it. Solvers like this one chew through those encodings. CaDiCaL won first place in the SAT track of SAT Race 2019 and second overall.

## Install

```
brew install cadical
```

## Try this

```
cadical -h
```
Prints the other command-line options, a quick tour of what a modern solver lets you tune.

```
cadical --help
```
Prints the usage text, the same entry point for exploring the solver's options.

```
cadical [ dimacs [ proof ] ]
```
Runs the solver on a DIMACS formula file, with an optional second argument for writing a proof of the result.

## What's unique

It is built to be read and modified, a teaching-friendly alternative to heavier solvers that still keeps close to their speed.

## Caveats

The README is written for SAT researchers, and it says CaDiCaL lacks some preprocessing, mainly parity and cardinality constraint reasoning, which matters for certain instances.

## Links

- [Homepage (FMV, JKU Linz)](https://fmv.jku.at/cadical/)
- [GitHub repository and README](https://github.com/arminbiere/cadical)
- [CaDiCaL 2.0 paper (CAV'24)](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-CAV24.pdf)
