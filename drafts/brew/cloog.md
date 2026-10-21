---
name: cloog
title: CLooG
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, compiler, library, loops, math, polyhedral]
homepage: https://github.com/periscop/cloog
scout_score: 5
status: draft
---

# CLooG

**TLDR;** CLooG takes a polyhedron described as affine inequalities and prints the nested for-loops that visit every integer point inside it exactly once.

CLooG, the Chunky Loop Generator, is a command-line tool and C library that generates loop code for scanning the integer points of one or more parametrized polyhedra, or a union of them. You give it affine inequalities that define the shapes, plus an optional context stating what is known about the parameters, in a file. It prints pseudo scanning code, and the README says several options help make that code close to compileable.

The README's own example is a 2D polygon with parameters n and m. The output is nested loops where the inner bound is something like min(m,-i+n+2). That one line shows the idea: a geometric description of which iterations exist becomes loop bounds, with no wasted checks inside the loop body.

It was built as a standalone piece of the Chunky project, an automatic loop optimizer for data locality. The wider idea is polyhedral compilation: treat loop iterations as integer points in a shape, transform the shape (skew it, tile it, reorder it), then turn it back into code. CLooG is the last step of that pipeline. The README says it is designed to avoid control overhead and produce very efficient code, and every function the program uses is also callable from the library. It can use either PolyLib or isl as its backend.

## Install

```
brew install cloog
# pulls in gmp and isl; no hardware or account needed
```

## Try this

```
cloog -h
```
Prints brief help listing the options.

```
cloog -v
```
Prints the version line, which the README asks for in bug reports.

```
cloog
```
Runs CLooG; give it an input file name to generate loops from a polyhedron description. The README points to test/readme.cloog in the source for the real input syntax.

## What's unique

It is the classic code generator for polyhedral loop nests: a shape and a context go in, and loops with min/max bounds come out.

## Caveats

The README is old, dating from 2002, and partly stale, with PostScript manual references and PolyLib options; the input format is only shown by example in the source's test files.

## Links

- [Homepage / repository](https://github.com/periscop/cloog)
- [Releases](https://github.com/periscop/cloog/releases)
