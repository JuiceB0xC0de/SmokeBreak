---
name: metis
title: METIS
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c, graphs, math, science, sparse-matrices]
homepage: https://papers.karypis.org/glaros/software/metis/overview.html
scout_score: 6
status: draft
---

# METIS

**TLDR;** Classic C programs that split big graphs and meshes into balanced pieces and reorder sparse matrices, the quiet machinery behind a lot of scientific computing.

METIS is a set of serial programs for partitioning graphs, partitioning finite element meshes, and producing fill-reducing orderings for sparse matrices. It comes from Karypis's lab and is written entirely in ANSI C, over 35,000 lines of it. The Homebrew formula installs six command-line tools: cmpfillin, gpmetis, graphchk, m2gmetis, mpmetis and ndmetis.

The homepage names the algorithm families behind it: multilevel recursive-bisection, multilevel k-way, and multi-constraint partitioning. The implied purpose is to cut a large unstructured graph or mesh into parts, so that work can be spread out, and to order the rows and columns of a sparse matrix so that factorizing it creates less fill-in. The homepage does not explain how the algorithms work. That is in the PDF manual shipped in the source distribution.

The idea underneath is that many problems, such as simulations, solvers and routing, are really graph problems. Where you cut a graph decides how fast everything downstream runs. METIS is a hands-on way to see that: you feed it a graph and watch how it divides it.

METIS sits in a family with ParMETIS (MPI, parallel), mt-metis (OpenMP) and hMETIS (hypergraph, aimed at VLSI). Those are separate downloads and not part of the brew formula.

## Install

```
brew install metis
```

## Try this

```
gpmetis --help
```
Prints usage for the graph partitioner, the main tool for splitting a graph into parts.

```
ndmetis --help
```
Prints usage for the nested dissection tool, which computes fill-reducing orderings for sparse matrices.

```
graphchk --help
```
Prints usage for the graph checker, a good first stop before feeding it your own data.

## What's unique

It is the reference implementation of multilevel graph partitioning, and the brew formula gives you six separate command-line tools rather than a single binary.

## Caveats

The stable release, 5.1.0, dates from 2013, and the homepage does not state a license for METIS itself, so check the distribution's terms before commercial use; the usage details live in the PDF manual.

## Links

- [METIS overview (homepage)](https://papers.karypis.org/glaros/software/metis/overview.html)
