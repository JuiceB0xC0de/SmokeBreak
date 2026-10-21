---
name: gecode
title: Gecode
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, constraint-programming, math, minizinc, solver]
homepage: https://www.gecode.dev/
scout_score: 6
status: draft
---

# Gecode

**TLDR;** A C++ constraint solver: you describe variables and rules, and it searches for assignments that satisfy them, with MiniZinc front ends installed alongside.

Gecode is an open source C++ toolkit for building constraint-based systems. You declare variables over integers, Booleans, sets, or floats, then state constraints between them. The search engines look for assignments that satisfy every constraint. Puzzles, scheduling, and timetabling are typical problems for this style.

The idea underneath is constraint programming. Instead of writing the algorithm that finds an answer, you write down what a valid answer looks like and let the solver propagate, branch, and backtrack. Gecode lists branching heuristics such as accumulated failure count and activity, restarts with no-goods, automatic symmetry breaking, and parallel search across cores.

The homepage says it is built to be extended: new constraints, branching strategies, search engines, and variable domains can be programmed to run as efficiently as the built-in ones. It also reports winning every gold medal at the MiniZinc Challenges from 2008 to 2012.

The brew formula installs two executables, fzn-gecode and mzn-gecode. Going by their names, these are FlatZinc and MiniZinc front ends, and the homepage says MiniZinc is supported. The pages read for this entry do not describe the executables, so check their --help output before relying on that guess.

## Install

```
brew install gecode
# Depends on qtbase. The upstream 6.4.0 release is source-only; the formula builds it for you.
```

## Try this

```
mzn-gecode --help
```
Prints the options of the MiniZinc-facing executable, a way to see what the front end accepts.

```
fzn-gecode --help
```
Prints the options of the FlatZinc solver executable.

## What's unique

The solver is meant to be embedded and extended, so you can add your own constraints and search strategies at the same efficiency as the built-in ones. It also comes with a test suite of more than 50000 cases.

## Caveats

This is mainly a C++ library, not a command-line app, so the upstream docs show little to run and the two executables are not described in the pages read.

## Links

- [Homepage](https://www.gecode.dev/)
- [GitHub repository](https://github.com/Gecode/gecode)
- [Documentation (tutorial and reference)](https://gecode.github.io/documentation.html)
- [Download page](https://gecode.github.io/download.html)
