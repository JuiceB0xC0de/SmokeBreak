---
name: bitwuzla
title: Bitwuzla
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bit-vectors, floating-point, logic, smt, solver, verification]
homepage: https://bitwuzla.github.io
scout_score: 5
status: draft
---

# Bitwuzla

**TLDR;** An SMT solver that decides whether logical formulas over bit-vectors, floating-point numbers and arrays can be satisfied, the engine behind much program verification.

Bitwuzla is a Satisfiability Modulo Theories (SMT) solver. You give it a logical formula over fixed-size bit-vectors, floating-point arithmetic, arrays and uninterpreted functions, or combinations of those, and it decides whether any assignment of values makes the formula true. It ships as a command-line program called `bitwuzla`, and it also has C, C++, Python and OCaml APIs.

The idea underneath is that a lot of questions about programs can be turned into logic. Can this integer addition overflow? Can this float computation produce a NaN? Is there an input that reaches this branch? Formulate the question as a formula and a solver answers it exactly, not by testing. That is the work of verification and symbolic execution tools, and this is the kind of engine they call underneath.

The project is clear about its niche: bit-precise and floating-point reasoning, not a general-purpose tool. The homepage mentions a CAV 2024 paper titled 'Scalable Bit-Blasting with Abstractions', which hints that bit-blasting, reducing bit-level operations to pure boolean logic, is part of the approach. The name comes from an Austrian dialect expression meaning 'someone who tinkers with bits'. The docs include a pronunciation guide.

The homepage credits a CAV 2023 Distinguished Paper Award and a string of SMT-COMP division wins, so the specialists consider it a serious solver.

## Install

```
brew install bitwuzla
```

## Try this

```
bitwuzla --help
```
Prints the command-line options, a first look at what the solver accepts and how you can steer it.

## What's unique

It is a competition-winning solver focused on bit-precise and floating-point reasoning, with bindings for C, C++, Python and OCaml as well as the CLI.

## Caveats

This is a specialist tool, and the brief did not cover its input format, so expect to read the Command Line Interface docs before getting an answer out of it.

## Links

- [Homepage](https://bitwuzla.github.io)
- [Documentation](https://bitwuzla.github.io/docs)
- [GitHub repository](https://github.com/bitwuzla/bitwuzla)
- [CAV 2023 system description (PDF)](https://bitwuzla.github.io/data/NiemetzP-CAV23.pdf)
