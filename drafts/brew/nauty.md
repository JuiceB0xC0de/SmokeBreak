---
name: nauty
title: nauty
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, combinatorics, graphs, math, science]
homepage: https://pallini.di.uniroma1.it/
scout_score: 7
status: draft
---

# nauty

**TLDR;** Research-grade software that finds the symmetries of graphs, plus about fifty tools that generate every non-isomorphic graph of a given size.

nauty and Traces are C programs that compute the automorphism group of a graph or digraph, meaning every way of relabelling its vertices that leaves it unchanged. They can also produce a canonical labelling: a standard form of the graph, so two graphs are the same shape exactly when their canonical forms match. That is the practical route to the graph isomorphism problem.

The package also ships gtools, a suite of about fifty command-line programs. Some generate graphs (geng, genbg, gentreeg, gentourng), some change them (addedgeg, deledgeg, complg, linegraphg), and some convert or filter them (dimacs2g, listg, pickg, shortg, labelg). They pass graphs along as plain text, so they chain together in pipes. The project's own description: "geng can generate non-isomorphic graphs very quickly." Interactive work happens in dreadnaut.

The design goes back to Brendan McKay's 1981 paper "Practical Graph Isomorphism". The current algorithms are described in McKay and Piperno, "Practical Graph Isomorphism, II" (J. Symbolic Computation, 2013). Traces builds on Piperno's work on contracting the search space during canonical labelling.

The door it opens is combinatorics: counting and listing graphs up to symmetry, checking whether two networks are secretly the same, and generating test cases for graph theory conjectures. The brief's description comes from a mirror of the docs, so details of the search algorithm are in the papers, not here.

## Install

```
brew install nauty
```

## Try this

```
geng --help
```
Prints the options for the fast generator of non-isomorphic graphs.

```
dreadnaut --help
```
Shows how to start the interactive program for automorphism groups and canonical labelling, if it supports that flag; otherwise run dreadnaut directly.

```
listg --help
```
Shows how to print graphs in a readable form, to inspect what geng produces.

## What's unique

It is the long-standing research reference for graph automorphisms and canonical labelling, with a full set of pipeable graph generators and filters included.

## Caveats

The official homepage was unreachable when this was written, the docs come from an ANU mirror, and the licence is a mix of authors' terms with 'absolutely no guarantees or warranties'.

## Links

- [Homepage](https://pallini.di.uniroma1.it/)
- [ANU mirror of nauty and Traces docs](https://users.cecs.anu.edu.au/~bdm/nauty/)
- [McKay and Piperno, Practical Graph Isomorphism II (2013)](https://doi.org/10.1016/j.jsc.2013.09.003)
