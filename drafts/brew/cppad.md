---
name: cppad
title: CppAD
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, automatic-differentiation, c++, library, math]
homepage: https://cppad.readthedocs.io/latest/
scout_score: 5
status: draft
---

# CppAD

**TLDR;** A C++ template library that turns any function you can write in C++ into one that also gives exact derivatives, with no formulas worked out by hand.

CppAD implements Algorithmic Differentiation. You write a function using its `AD` scalar type instead of `double`. As the function runs, operator overloading records each arithmetic operation. The recording is stored in an `ADFun` object, which can then report function values and derivatives of any order, plus Jacobians, Hessians, and sparsity patterns.

The docs describe the core idea as "the automatic creation of an algorithm that computes derivative values from an algorithm that computes function values." This differs from symbolic algebra and from finite differences. The derivatives come from the exact sequence of operations your code performed, so they are not approximations.

Beyond the basics, the docs describe optimizing the recorded sequence, dynamic parameters that are not differentiated, and atomic functions where you supply your own derivative. They also cover sparse Jacobians and Hessians driven by sparsity patterns, and multi-threading through OpenMP, Boost, or POSIX threads. The docs say all the examples double as correctness tests.

The idea underneath is the door: differentiation is a mechanical transformation of a program. The same idea sits behind optimization solvers and machine learning frameworks. CppAD is a place to see it in plain C++.

## Install

```
brew install cppad
# Library only: Homebrew installs no executables. You use it from your own C++ code.
# From source, the README says the preferred build uses cmake; the autotools path is deprecated.
```

## Try this

## What's unique

It differentiates ordinary C++ you already have through operator overloading, and goes deep with sparse derivatives, user-defined atomic functions, and checkpointing.

## Caveats

It is a library with no executables, so there is nothing to run from a shell after installing; you need to write C++ to use it.

## Links

- [Homepage (User's Manual)](https://cppad.readthedocs.io/latest/)
- [Get started example](https://cppad.readthedocs.io/latest/get_started.cpp.html)
- [Install instructions](https://cppad.readthedocs.io/latest/Install.html)
- [Git repository (coin-or/CppAD)](https://github.com/coin-or/CppAD)
