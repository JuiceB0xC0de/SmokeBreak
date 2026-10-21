---
name: esbmc
title: ESBMC
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, bug-finding, c, formal-verification, model-checking, python, smt]
homepage: https://esbmc.github.io/
scout_score: 6
status: draft
---

# ESBMC

**TLDR;** A model checker that turns C, C++ or Python code into SMT formulas and either proves assertions hold within a bound or hands back a concrete failing trace.

ESBMC reads a source file, unwinds its loops to a bound, and encodes every possible execution up to that bound as a logic formula. An SMT solver (Bitwuzla, Z3 or Boolector) then decides whether any input can break an assertion or trigger a runtime error such as an out-of-bounds access, pointer misuse or overflow. The answer is VERIFICATION SUCCESSFUL, VERIFICATION FAILED with a counterexample trace, or a result saying the budget ran out.

The homepage calls it push-button: no pre- or postconditions are required. You write the program, optionally add assertions, and run one command. It covers C and C++ through Clang, and also Python, Java/Kotlin, Rust, Solidity, CUDA and others. For threaded programs it explores interleavings under a context bound, so it can find race-dependent bugs that testing rarely hits.

The idea underneath is that a bug search can be a satisfiability question. Bounded checking is complete only up to the bound, but k-induction can turn some of those checks into unbounded proofs. The tool is a fork of CBMC v2.9 (2008) that the homepage says has diverged substantially. It is a practical way into formal verification, and it works on ordinary code.

## Install

```
brew install esbmc
```

## Try this

```
esbmc file.c --incremental-bmc
```
Unwinds loops step by step in a C file, and reports a counterexample trace if it finds a violation such as a NULL dereference.

```
esbmc main.py
```
Verifies a type-annotated Python file; the README's example finds a division-by-zero counterexample.

```
esbmc file.c --floatbv --k-induction
```
Checks a floating-point C program with bit-vector float semantics and tries to prove it by k-induction.

## What's unique

It aims for proofs rather than only bug-finding, combining incremental BMC, k-induction and interval analysis. It also covers Python, Solidity and Kotlin/Java alongside C and C++, and its --all-witnesses mode lists every failing input vector rather than just one.

## Caveats

Results are bounded by default, so unbounded proofs depend on k-induction converging, and the Python frontend's README example uses type annotations.

## Links

- [Homepage](https://esbmc.github.io/)
- [GitHub repository and README](https://github.com/esbmc/esbmc)
- [Usage docs](https://esbmc.github.io/docs/usage/)
