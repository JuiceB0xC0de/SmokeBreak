---
name: vampire
title: Vampire
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, formal-methods, logic, math, smt, theorem-proving]
homepage: https://vprover.github.io/
scout_score: 5
status: draft
---

# Vampire

**TLDR;** A research-grade automated theorem prover: give it a logical problem in TPTP format and it tries to prove it, refute it, or build a model.

Vampire is an automated theorem prover, a program that tries to prove logical statements without a human steering it. Its main focus is first-order logic. It can also disprove non-theorems, build finite models, and reason with theories such as arithmetic, arrays, and datatypes. It reads problems in TPTP format, or SMT-LIB since it can act as an SMT solver, and prints a verdict. On request it also prints a detailed proof or a finite model.

The project's homepage says development began in 1994. It describes the superposition calculus as "one of the most advanced and elegant theories in computer science", and presents Vampire as a way to turn that theory into practical tools. The uses it lists are software and hardware verification, knowledge representation, the Semantic Web, algebra, and mathematics. It also supports inductive reasoning over algebraic data types, and the homepage says higher-order logic is increasingly handled.

The door into something larger is the idea of a portfolio. No single proof strategy works on every problem, so the `casc` mode tries many strategies, and the README says it often beats the default. The default mode runs with a 60 second time limit. Reading the proof output, then switching modes to see how the verdict changes, is a hands-on way into automated reasoning.

## Install

```
brew install vampire
# Pre-built binaries are also on the GitHub releases page. Problems must be written in TPTP format (see tptp.org).
```

## Try this

```
vampire problem.p
```
Runs Vampire in its default mode on a TPTP problem file, with a 60 second time limit.

```
vampire --mode casc problem.p
```
Runs portfolio mode, which tries many strategies and often does better than the default.

```
vampire --mode casc_sat problem.p
```
Uses a portfolio variant tuned for satisfiable problems, handy when you suspect the problem has a model.

## What's unique

One binary covers first-order proving, model finding, SMT-LIB input, and induction over datatypes. It comes from a prover with competition awards at CASC and SMT-COMP, and portfolio mode gives one-command access to many strategies.

## Caveats

It expects TPTP-formatted input and its appeal is niche and academic, so you will need to write or fetch a problem file before anything interesting happens.

## Links

- [Vampire homepage](https://vprover.github.io/)
- [GitHub repository](https://github.com/vprover/vampire)
- [Releases (pre-built binaries)](https://github.com/vprover/vampire/releases)
- [Source build wiki for users](https://github.com/vprover/vampire/wiki/Source-Build-for-Users)
- [TPTP problem format](https://tptp.org)
