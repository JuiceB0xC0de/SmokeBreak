---
name: fplll
title: fplll
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, cryptography, lattices, library, math]
homepage: https://github.com/fplll/fplll
scout_score: 5
status: draft
---

# fplll

**TLDR;** A lattice reduction toolkit: feed it a matrix of integer vectors and it returns a better basis, or solves shortest and closest vector problems.

fplll is a C++ library with two command-line programs. `fplll` reads a lattice basis, written as integer row vectors, from stdin or a file and prints a reduced basis. It runs LLL, BKZ, HKZ, slide, self-dual BKZ and HLLL reduction. It can also solve the shortest vector problem (SVP) and the closest vector problem (CVP). `latticegen` prints random test lattices of several kinds (knapsack, NTRU-like, q-ary and others) so there is something to feed it.

The name comes from LLL, the Lenstra-Lenstra-Lovász algorithm, which is central to the code. The README describes floating-point LLL variants 'offering different speed/guarantees ratios'. Exact integer arithmetic for this work is slow, so fplll does the orthogonalization in floating point (double, long double, dd, qd, dpe or MPFR) and still tries to state what is guaranteed about the output. A 'wrapper' picks 'the estimated best sequence of variants in order to provide a guaranteed output as fast as possible', so you do not have to choose.

The idea underneath is that a lattice has many bases, and some are far nicer than others: short, nearly orthogonal vectors instead of long skewed ones. Finding a good basis turns out to matter in number theory, integer programming and cryptanalysis, and it is the hard problem that lattice-based cryptography leans on. BKZ here includes the BKZ-2.0 improvements, and SVP uses Kannan-Fincke-Pohst enumeration. Playing with it is a hands-on way into why that problem is hard.

## Install

```
brew install fplll
# Debian/Ubuntu: sudo aptitude install fplll-tools
# conda: conda install fplll
# Homebrew pulls in gmp and mpfr as dependencies.
```

## Try this

```
./latticegen r 10 1000 | ./fplll
```
Generates a 10-dimensional knapsack-style matrix with 1000-bit entries and LLL-reduces it.

```
./latticegen r 30 3000 | ./fplll -a svp
```
Solves the shortest vector problem on a random 30-dimensional lattice.

```
echo "[[17 42 4][50 75 108][11 47 33]][100 101 102]" | ./fplll -a cvp
```
Finds the lattice vector closest to the target [100 101 102] for a small inline basis.

## What's unique

Most lattice tools expose one algorithm. fplll's wrapper chooses the LLL variant itself, and latticegen supplies the standard test lattices from the literature, so you can experiment right away.

## Caveats

It is mostly a library for specialists; the README warns that the 'n' NTRU-like generator does not produce a genuine NTRU lattice, and the brief could not confirm recent activity.

## Links

- [fplll GitHub repository and README](https://github.com/fplll/fplll)
- [API documentation](https://fplll.github.io/fplll/annotated.html)
- [fpylll, Python interface](https://github.com/malb/fpylll)
