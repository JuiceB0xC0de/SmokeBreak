---
name: cddlib
title: cddlib
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, geometry, library, linear-programming, math, polyhedra]
homepage: https://www.inf.ethz.ch/personal/fukudak/cdd_home/
scout_score: 6
status: draft
---

# cddlib

**TLDR;** A C library and set of command-line tools that convert convex polyhedra between inequalities and corner points, with exact rational arithmetic available.

cddlib implements the Double Description Method of Motzkin et al. Give it a polyhedron as a system of linear inequalities (b - A·x ≥ 0) and it lists every vertex and extreme ray. Give it vertices and rays and it runs the other way, returning the inequalities, which is the convex hull problem. It also solves linear programs over the polyhedron.

The idea underneath is that a polyhedron has two equally valid descriptions: the half-spaces that bound it, or the corners and directions that span it. The method keeps both lists in step and adds one constraint at a time, updating the generators as it goes. Moving between the two views is a basic operation in computational geometry, optimisation and combinatorics.

The library comes from Komei Fukuda's cdd family. The homepage calls it the only one still being updated, and the older cdd and cddplus programs are its predecessors. Arithmetic is either floating point, with a tolerance (dd_almostzero = 1.0E-6) that decides what counts as zero, or exact rational through GMP. The brew formula also installs command-line programs such as lcdd, scdd, cddexec, adjacency and fourier, each with a _gmp twin. The README does not document them, so expect to learn them from the manual or by experiment.

The README is candid about floating-point danger. Its advice: "When some strange behavior is observed, it is always wise to create a rational approximation of the input (for example, one can replace 0.3333333 with 1/3) and to compute it with cddlib compiled with GMP Rational to see what a correct behavior should be."

## Install

```
brew install cddlib
# depends on gmp, which brew pulls in. The _gmp executables use exact rational arithmetic.
```

## Try this

```
lcdd --help
```
Prints usage for lcdd, one of the command-line converters between inequality and vertex representations.

```
scdd --help
```
Prints usage for scdd, the other representation-conversion program.

```
cddexec --help
```
Prints usage for cddexec, the general-purpose cdd driver.

## What's unique

It treats floating-point failure as something to debug: rerun the same input in exact rational arithmetic and compare. It also handles awkward cases such as polyhedra that are not full-dimensional or have no vertices.

## Caveats

Floating-point results can be wrong on sensitive inputs, the documentation is incomplete, and the manual sits on an old ETH FTP link.

## Links

- [cdd, cddplus and cddlib homepage (Komei Fukuda)](https://www.inf.ethz.ch/personal/fukudak/cdd_home/)
- [cddlib GitHub repository and README](https://github.com/cddlib/cddlib)
- [cddlib manual (ETH FTP, incomplete)](ftp://ftp.math.ethz.ch/users/fukudak/cdd/cddlibman/cddlibman.html)
- [cddlib releases page](https://github.com/cddlib/cddlib/releases)
