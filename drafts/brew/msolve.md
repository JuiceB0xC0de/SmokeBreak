---
name: msolve
title: msolve
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, computer-algebra, groebner-bases, math, polynomials, science]
homepage: https://msolve.lip6.fr
scout_score: 6
status: draft
---

# msolve

**TLDR;** A command-line solver that finds exact solutions to systems of polynomial equations using Groebner bases, returning rational boxes instead of floating-point guesses.

msolve reads a plain text file describing a system of multivariate polynomials and solves it with computer algebra rather than numerical approximation. You list the variables, give a field characteristic (0 for rationals, or a prime), then write out the polynomials. It can compute Groebner bases, work out whether the system has finitely many complex solutions, and isolate the real solutions. Results go to an output file.

The idea underneath is that a polynomial system can be rewritten into a form that makes its structure readable. A Groebner basis is that form: from its leading monomials you can read off the dimension and degree of the solution set. msolve's core uses the F4 algorithm and changes of monomial ordering. When the system has finitely many complex solutions and rational coefficients, it isolates real roots as rational boxes. Over prime fields it computes a parametrization of the solutions.

The output is exact. A real root comes back as an interval with rational endpoints that provably contains one root, not a decimal that might be off. The README says multi-threading is applied to the linear algebra for prime-field Groebner bases, to multi-modular real solving, and to real root isolation.

It is also embedded in Oscar, SageMath (via Variety) and Macaulay2, so you can meet it through those systems first. Running the binary directly is a good way to see what they are doing underneath.

## Install

```
brew install msolve
```

## Try this

```
msolve -f in.ms -o out.ms
```
Reads the system from in.ms, detects whether it is zero-dimensional, then isolates real roots (rational coefficients) or computes a parametrization (prime field), writing to out.ms.

```
msolve -g 2 -f in.ms -o out.ms
```
Writes the full reduced Groebner basis in graded reverse lexicographic order.

```
msolve -v 2 -t 4 -f in.ms -o out.ms
```
Runs on 4 threads with verbosity 2, so you can watch what it is doing.

## What's unique

Most solvers hand back approximate numerical roots. msolve returns exact encodings: rational isolating boxes and rational parametrizations.

## Caveats

Real root isolation only applies to systems with finitely many complex solutions and rational coefficients, prime-field Groebner computations need characteristic below 2^31, and repeating a monomial within a polynomial gives undefined parser behaviour.

## Links

- [Homepage](https://msolve.lip6.fr)
- [Tutorial (PDF)](https://msolve.lip6.fr/downloads/msolve-tutorial.pdf)
- [GitHub repository (README)](https://github.com/algebraic-solving/msolve)
- [ISSAC 2021 paper (PDF)](https://hal.sorbonne-universite.fr/hal-03191666v2/file/main.pdf)
