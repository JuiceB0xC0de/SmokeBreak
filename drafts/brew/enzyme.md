---
name: enzyme
title: Enzyme
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, automatic-differentiation, compilers, llvm, math]
homepage: https://enzyme.mit.edu
scout_score: 6
status: draft
---

# Enzyme

**TLDR;** An LLVM plugin that computes derivatives of existing compiled code, so C, Rust, Julia or Fortran functions get gradients without being rewritten.

Enzyme takes code as LLVM IR and produces the derivative or gradient of a function you choose. You mark the function by calling `__enzyme_autodiff` on it. When the Enzyme pass runs, that call is replaced with generated derivative code. The homepage lists C, C++, Swift, Julia, Rust, Fortran and TensorFlow as sources of IR, and the README says Julia, Rust and Fortran bindings exist.

The project exists so that people can get gradients of existing source code without rewriting it for a machine learning framework. Working at the LLVM level means one tool can serve many languages and reuse LLVM's optimizer.

The underlying idea is to differentiate after optimization instead of before. In the project's words: "By differentiating code after optimization, Enzyme is able to create substantially faster derivatives than existing tools that differentiate programs before optimization." That speed claim comes from the authors and their papers. The pipeline has an optional preprocessing phase, a type analysis that deduces what lives in each memory location, an activity analysis that works out which values can affect the derivative, and a pass that emits the derivative functions.

This is a door into compilers and automatic differentiation: what a derivative of a program even means, why types and memory matter, and what changes when the optimizer runs first. The README says it also handles GPU and parallel code, including OpenMP, MPI and Julia tasks.

## Install

```
brew install enzyme
# Pulls in llvm as a dependency. Enzyme installs no executables; it is a plugin loaded into LLVM tooling.
# Also packaged for Spack (spack install enzyme) and Nix (nix-shell -p enzyme).
```

## Try this

```
brew install enzyme
```
Installs the Enzyme plugin and the LLVM it depends on. There is no command to run afterwards.

```
cmake -G Ninja .. -DLLVM_DIR=/path/to/llvm/lib/cmake/llvm -DLLVM_EXTERNAL_LIT=/path/to/lit/lit.py
```
Configures a source build from a checkout, pointing at your LLVM CMake directory and the lit test runner. Run it inside a build directory, then run ninja.

## What's unique

Most automatic differentiation tools work on source code or a high-level IR before optimization. Enzyme differentiates already-optimized LLVM IR, so one implementation covers many languages.

## Caveats

It only handles statically analyzable code, it has no command-line tool to try, and the brief did not confirm a first-run workflow, so expect to read the getting started guide and match LLVM versions.

## Links

- [Enzyme homepage](https://enzyme.mit.edu)
- [GitHub repository (EnzymeAD/Enzyme)](https://github.com/EnzymeAD/Enzyme)
- [SC '21 paper on GPU kernel AD (DOI)](https://doi.org/10.1145/3458817.3476165)
