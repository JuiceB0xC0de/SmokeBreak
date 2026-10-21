---
name: yices2
title: Yices 2
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, formal-methods, library, logic, math, smt, solver]
homepage: https://yices.csl.sri.com/
scout_score: 5
status: draft
---

# Yices 2

**TLDR;** An SMT solver from SRI that takes logical and arithmetic constraints and returns either a satisfying assignment or a verdict that none exists.

Yices 2 decides satisfiability of formulas that mix logic with other theories: uninterpreted functions with equality, linear and nonlinear real and integer arithmetic, bitvectors, scalar types and tuples. You declare variables, assert constraints, call `check-sat`, and then `get-model`. If a solution exists, you get concrete values. If not, you get `unsat`.

Input can be written in SMT-LIB (versions 2.0 and 1.2) or in Yices' own specification language, which adds tuples and scalar types. The README's examples show a linear real problem coming back with x = 2.0 and y = -1.0, and a bitvector problem returning two 32-bit values. It is also a library with a C API, with bindings for Java, Python, Go and OCaml.

It comes from SRI's Computer Science Laboratory, a formal-methods group, with funding from SRI, NSF, NASA and DARPA. The idea underneath is that many hard questions, such as whether a piece of code can overflow, whether a schedule is feasible, or whether two circuits are equivalent, can be rewritten as 'is there an assignment that makes this formula true?' A solver like this answers that mechanically. Learning to phrase problems that way opens up program verification, symbolic execution, and automated planning.

The repository also includes a script that runs several Yices configurations in parallel on one file and reports whichever finishes first.

## Install

```
brew install yices2
# The README's MCSAT-enabled build (nonlinear arithmetic) comes from SRI's tap: brew install SRI-CSL/sri-csl/yices2
# Depends on gmp, which brew pulls in. No account or runtime needed.
```

## Try this

```
yices-smt2 --help
```
Lists the options for the SMT-LIB 2 front end, the one most people will use.

```
yices-smt2 lra.smt2
```
Runs the solver on a linear real arithmetic file (you write it yourself, following the README's example). The README shows it printing sat and a model with x = 2.0 and y = -1.0.

```
yices-smt2 bv.smt2
```
Runs a bitvector problem; the README shows sat with two 32-bit model values.

## What's unique

It is a full SMT solver that accepts standard SMT-LIB and also has its own richer specification language, with bindings for several languages. It comes from a formal-methods lab that has worked on this for years.

## Caveats

Licensed GPLv3. Nonlinear arithmetic (MC-SAT) is not in a default source build and needs libpoly and CUDD, and the library is not thread-safe unless built with --enable-thread-safety.

## Links

- [Yices homepage](https://yices.csl.sri.com/)
- [GitHub repository (source, README, examples)](https://github.com/SRI-CSL/yices2)
- [Yices C API header](https://github.com/SRI-CSL/yices2/blob/master/src/include/yices.h)
