---
name: math-comp
title: Mathematical Components (math-comp)
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [coq, days-off, formal-verification, library, math, proof-assistant, rocq]
homepage: https://math-comp.github.io/math-comp/
scout_score: 5
status: draft
---

# Mathematical Components (math-comp)

**TLDR;** A large library of machine-checked mathematics for the Coq/Rocq proof assistant, behind formal proofs of the Four Colour and Feit-Thompson theorems.

Mathematical Components, or math-comp, is a library of formalized mathematics for the Coq proof assistant, now called Rocq. It is written in the SSReflect proof language. You feed it Coq source files and it checks them, so what you get is verified theorems and definitions, not program output. The README describes it as "an extensive and coherent repository of formalized mathematical theories."

The theories run from everyday data structures such as lists, prime numbers and finite graphs up to advanced algebra. The repository is a tree of `.v` files, for example `ssreflect/seq.v` and `ssreflect/prime.v`, and it is split into opam packages like `rocq-mathcomp-boot`, `rocq-mathcomp-algebra` and `rocq-mathcomp-field`.

It exists to support very large formal proofs. The README points to two: the foundations for a formal proof of the Four Colour Theorem, and a mechanization of the Odd Order Theorem (Feit-Thompson), a landmark result in finite group theory that uses the library extensively.

The idea underneath is that a proof can be a program a computer checks, and that a big proof needs a well-organised standard library the way big software does. Reading the library shows how mathematicians' definitions get shaped so a machine can verify them. There is also a Mathematical Components Book linked from the project if you want a guided route in.

## Install

```
opam repo add rocq-released https://rocq-prover.org/opam/released
opam install rocq-mathcomp-boot
# Requires a fresh or up-to-date opam 2 and a working Rocq/Coq installation, both obtained through opam. A Homebrew formula also exists (brew install math-comp), which pulls in rocq and related dependencies, but the README documents the opam route.
```

## Try this

```
opam repo add rocq-released https://rocq-prover.org/opam/released
```
Adds the Rocq released opam repository so the MathComp packages can be found.

```
opam install rocq-mathcomp-boot
```
Installs the base MathComp package; rocq-mathcomp-algebra and rocq-mathcomp-field install the same way.

## What's unique

Few formal libraries have carried results as heavy as the Four Colour Theorem and the Feit-Thompson Odd Order Theorem. This one is built around that kind of use.

## Caveats

It is a proof library, not a tool: you need to know Coq/Rocq and SSReflect to do anything with it, and upgrades between versions may need work because of deprecation warnings.

## Links

- [Homepage](https://math-comp.github.io/math-comp/)
- [HTML documentation of the last version](https://math-comp.github.io/htmldoc/libgraph.html)
- [Mathematical Components Book](https://math-comp.github.io/mcb/)
