---
name: sollya
title: Sollya
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, floating-point, libm, math, numerical-analysis]
homepage: https://www.sollya.org/
scout_score: 6
status: draft
---

# Sollya

**TLDR;** A scripting environment for building floating-point math functions with proven error bounds, the kind of work that sits underneath every libm.

Sollya is both a tool environment and a library for safe floating-point code development. It has its own scripting language, aimed at analysing numerical programs the way a computer algebra system analyses equations. The homepage says it is "particularily targeted to the automatized implementation of mathematical floating-point libraries (libm)."

The pieces are concrete. It computes "a certified infinity (supremum) norm for computing safe approximation error bounds", runs a fast Remez algorithm to find minimax polynomials, and evaluates composed expressions in multi-precision with faithful rounding, building on MPFR. A polynomial implementer can then emit CRlibm-style C code along with a matching Gappa proof.

The idea underneath is that when you write `sin` or `exp` for a computer, you replace a function with a polynomial and a rounding scheme. Normally you test it and hope. Sollya is for the other way: bound the approximation error rigorously, then show the final code respects that bound. It is a door into how real math libraries are made, and into the gap between an estimated error and a certified one.

The brief does not show command syntax, so the language itself is something to learn from the documentation, which is linked from the homepage as online pages and a PDF.

## Install

```
brew install sollya
# installs the `sollya` executable; Gnuplot is optional but recommended for the plot commands
```

## Try this

```
sollya --help
```
Prints the command-line options of the Sollya interpreter, a first look before opening the documentation.

## What's unique

It is a numerical-analysis language rather than a library you merely call from C: you script the search for an approximation, certify its error, and have it emit C code plus a Gappa proof.

## Caveats

The site warns it can be complicated to use and is aimed at developers and experienced professionals; the last stable release listed is 8.0 from March 2022, and recent activity could not be confirmed.

## Links

- [Sollya homepage](https://www.sollya.org/)
