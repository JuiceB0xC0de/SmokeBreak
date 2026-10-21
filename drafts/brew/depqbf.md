---
name: depqbf
title: DepQBF
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c-library, complexity, logic, math, qbf, solver]
homepage: https://lonsing.github.io/depqbf/
scout_score: 6
status: draft
---

# DepQBF

**TLDR;** A research solver for quantified boolean formulae: SAT with 'for all' and 'exists' bolted on, a step up the complexity ladder you can run on a file.

DepQBF reads a quantified boolean formula in prenex CNF, usually a QDIMACS file, and says whether it is true or false. It reports through exit codes in the SAT-competition style: 10 for satisfiable, 20 for unsatisfiable, anything else means it did not solve the instance. With `--qdo` it prints a partial assignment for the outermost quantifier block, and with `--trace` it dumps every resolution step in QRP format.

A QBF is an ordinary SAT problem where each variable is either 'there exists a value' or 'for all values'. That alternation is what takes the problem from NP-complete to PSPACE-complete. It is a compact way to ask questions like 'is there a move such that for every reply there is a move...', so game-like and planning problems map onto it naturally.

Under the hood it is a search-based solver using conflict-driven clause learning plus solution-driven cube learning (QCDCL). It computes a standard dependency scheme, a graph of which variables really depend on which, to find variables that can be decided more freely. Since version 5.0 it also runs dynamic blocked clause elimination during the search, and since 6.0 it calls PicoSAT and Nenofex as oracles.

It comes out of Florian Lonsing's research group and exists to implement and test ideas from their papers. It can also be used as a C library (`libqdpll.a`, `qdpll.h`) with an incremental push/pop API, and through a Java wrapper, DepQBF4J.

## Install

```
brew install depqbf
# Upstream is source-only: unpack the archive and run ./compile.sh (needs network access and a C toolchain, since it downloads and builds PicoSAT and Nenofex).
# You also need a QDIMACS file to feed it; the brief does not name a bundled example.
```

## Try this

```
depqbf -h
```
Prints usage and the command-line options, the README's suggested way to learn the configuration.

```
depqbf input-formula.qdimacs; echo $?
```
Solves a QDIMACS file, then prints the exit code: 10 means satisfiable, 20 means unsatisfiable.

```
depqbf --trace input-formula.qdimacs > trace.qrp
```
Writes every resolution step of the proof to trace.qrp in QRP format, for certificate extraction with other tools.

## What's unique

Few solvers expose the standard dependency scheme and dynamic blocked clause elimination. DepQBF also ships an incremental API, unsat-core extraction and certificate output.

## Caveats

Quiet project: the last release, 6.03, is from August 2017; input must be prenex CNF, and tracing does not work in incremental mode.

## Links

- [Homepage](https://lonsing.github.io/depqbf/)
- [GitHub repository (README)](https://github.com/lonsing/depqbf)
- [Nenofex, the QBF solver bundled as an oracle since 6.0](https://github.com/lonsing/nenofex)
