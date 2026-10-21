---
name: one-ml
title: 1ML
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, functional, language, ml, research, type-systems]
homepage: https://people.mpi-sws.org/~rossberg/1ml/
scout_score: 6
status: draft
---

# 1ML

**TLDR;** An experimental ML dialect where modules are ordinary values and the core and module languages collapse into one, from Andreas Rossberg's research.

Standard ML and OCaml have two languages stacked together. The core language has expressions and types. On top sits a separate module language with structures, signatures and functors. The two duplicate much of each other's syntax and semantics, and the split has a cost: you cannot pick a module based on a runtime decision, because modules are not ordinary values.

1ML removes the split. In the project's words, "functions, functors, and even type constructors are one and the same construct; likewise, no distinction is made between structures, records, or tuples." Modules become first-class, and the whole thing is meant to be one small, consistent language.

The design claim underneath is that this does not need dependent types. Its type structure can be expressed in plain System Fω, a variation on the author's earlier F-ing modules approach. The author describes 1ML either as one language where everything is a mode of use of modules, or as a friendlier surface syntax for System Fω. The tool installed here is a simple prototype interpreter, version 0.1, for running small examples. It is best read next to the papers, which the homepage lists (ICFP 2015, a 2015 extended version, JFP 2018, and WadlerFest 2016).

## Install

```
brew install one-ml
# the executable is named 1ml. Upstream says building from source needs OCaml 4.02 and Make.
```

## Try this

```
1ml --help
```
Prints the interpreter's usage, since the brief gives no other documented commands. The README in the GitHub repository has the basic documentation.

## What's unique

It argues that ML's core/module split is unnecessary, and it fits the whole system into plain System Fω without dependent types.

## Caveats

It is a research prototype, version 0.1, with a copyright line of 2015-2017; type inference for the implicitly typed version is incomplete, and the effect polymorphism extension from the latest paper is not implemented.

## Links

- [1ML project homepage](https://people.mpi-sws.org/~rossberg/1ml/)
