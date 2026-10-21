---
name: alive2
title: Alive2
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, compilers, formal-verification, llvm, optimization, smt, z3]
homepage: https://github.com/AliveToolkit/alive2
scout_score: 7
status: draft
---

# Alive2

**TLDR;** Alive2 uses an SMT solver to check whether an LLVM optimization preserves a program's meaning, and hands back a concrete counterexample when it does not.

Alive2 takes LLVM IR and asks whether a transformation is a valid refinement of the original. You give it a source and a target, either as two files or as two functions named src and tgt in one file. Or you give it one unoptimized file and it runs an -O2-like pipeline itself, without interprocedural passes. It then asks the Z3 solver whether the target can do anything the source could not. The answer is either "Transformation seems to be correct!" or a counterexample with concrete input values.

The idea underneath is translation validation. Alive2 does not prove that an optimizer is correct as a whole. It checks one run of it, after the fact, by comparing the IR before and after. That is a much easier problem, and it still finds real bugs. The project keeps a list of the LLVM bugs it has found in BugList.md, and the README says it is meant to make LLVM less buggy.

The checking is precise about undefined behaviour, which is where many compiler optimization bugs live. The README gives an example of removing nsw from an add, and another where it flags a bug in an LLVM 10.x release branch optimizer. Beyond alive-tv, it ships clang and opt plugins, alivecc and alive++ as drop-in compiler wrappers that validate every IR-level transformation in a build, and an experimental IR interpreter, alive-exec. The PLDI 2021 paper is the technical introduction.

## Install

```
brew install alive2
# Needs no account. To skip installing entirely, alive-tv runs in the browser at https://alive2.llvm.org/ce/
```

## Try this

```
alive-tv --help
```
Lists the options for the translation validator, the main tool.

```
alive-tv src.ll tgt.ll
```
Checks whether the target function refines the source function, and reports either a correct transformation or a counterexample.

```
alive-tv foo.ll
```
Runs the built-in -O2-like pipeline over one unoptimized IR file and validates the result.

## What's unique

It checks whether a specific optimizer transformation preserves meaning and returns a concrete counterexample when it does not, rather than trying to prove a whole compiler correct. It also works as a drop-in clang wrapper, so an entire build can be checked pass by pass.

## Caveats

It does not support interprocedural transformations and may give spurious counterexamples on them, and alive-exec is described as highly experimental.

## Links

- [GitHub repository (homepage)](https://github.com/AliveToolkit/alive2)
- [Online alive-tv (Compiler Explorer)](https://alive2.llvm.org/ce/)
- [PLDI 2021 paper: technical introduction](https://web.ist.utl.pt/nuno.lopes/pubs/alive2-pldi21.pdf)
