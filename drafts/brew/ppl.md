---
name: ppl
title: ppl
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [c++, days-off, library, math, polyhedra, verification]
homepage: https://www.bugseng.com/ppl
scout_score: 5
status: draft
---

# ppl

**TLDR;** A C++ library for convex polyhedra and other numerical abstractions, with exact linear programming and a few demo tools you can run from the shell.

The Parma Polyhedra Library, or PPL, is a C++ library for working with (not necessarily closed) convex polyhedra. A polyhedron here is a set of points described by rational linear equalities and strict or non-strict inequalities. It also covers simpler shapes: boxes, bounded difference shapes, octagonal shapes, and grids, which are sets of congruence relations. Finite powersets and products of these can be built too.

Beyond the shapes, the library solves linear programs with an exact-arithmetic primal simplex, solves parametric integer programming problems, and synthesizes linear ranking functions for termination analysis. The README does not give a motive. The program verification framing comes from the Homebrew description, not from the README text the brief was based on.

The idea underneath is the abstract domain. Instead of tracking every value a program variable can take, you track a simplified geometric shape that contains them all. Boxes are cheap and crude, octagons are tighter, and polyhedra are tighter still and more expensive. PPL puts these trade-offs in one library, so you can see how precision and cost move against each other.

The README says you write constraints the way you would on paper, such as `x + 2*y + 5*z <= 7`, and that dimensions are limited only by available virtual memory. The brew package installs `ppl-config` and two demo-style executables, `ppl_lcdd` and `ppl_pips`. The source tree also has a demo called `ppl_lpsol`. Most of the real use is through the library, with optional interfaces for C, Java, OCaml, and several Prolog systems.

## Install

```
brew install ppl
# depends on gmp, which brew pulls in. The executables are small utilities; the library itself is for C++ programs.
```

## Try this

```
ppl-config --help
```
Prints the options for the config tool, which reports how the installed library was built and where it lives.

```
ppl_lcdd --help
```
Prints usage for the lcdd demo program.

```
ppl_pips --help
```
Prints usage for the parametric integer programming solver.

## What's unique

One library covers many abstract domains (polyhedra, grids, boxes, octagons, powersets) alongside exact LP, parametric integer programming, and ranking-function synthesis.

## Caveats

It is mostly a library, so the shipped executables are demos and utilities. The brief could not read the homepage (HTTP 403) or the full README, and found no runnable example commands.

## Links

- [Project homepage (returned 403 when checked)](https://www.bugseng.com/ppl)
- [Source repository and README](https://github.com/BUGSENG/ppl)
- [Product page cited in the README](http://bugseng.com/products/ppl/)
