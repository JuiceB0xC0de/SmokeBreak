---
name: pari
title: PARI/GP
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, cas, language, math, number-theory]
homepage: https://pari.math.u-bordeaux.fr/
scout_score: 6
status: draft
---

# PARI/GP

**TLDR;** A number theory calculator with its own small language, built in Bordeaux since the early 1980s, for factoring, elliptic curves and other exact arithmetic.

PARI/GP is a free computer algebra system aimed at fast computation in number theory: factorization, algebraic number theory, elliptic curves, modular forms, L-functions. It also handles matrices, polynomials, power series and many transcendental functions, plus numerical summation and integration.

You mostly meet it through `gp`, an interactive shell where you type expressions and get results back. The same shell runs scripts written in GP, the project's own small language. Underneath is PARI, a C library that does the heavy arithmetic, and `gp` is a front end exposing those functions.

The University of Bordeaux has developed it since the early 1980s. The homepage describes it as built for speed in number theory while also being free software under the GPL. That focus is the idea worth poking at: it is not trying to be a general symbolic algebra system, but a fast tool for working with integers, number fields and curves.

For scripts that need more speed, there is gp2c, a compiler from GP to C that loads the compiled functions back into `gp`. The homepage says compiled scripts typically run 3 or 4 times faster, though gp2c only understands a subset of GP.

## Install

```
brew install pari
# Graphical plotting needs X11 on macOS: brew install --cask xquartz
```

## Try this

```
gp
```
Starts the interactive shell, where you can type number theory expressions and see results.

```
gphelp --help
```
Shows the options for the built-in help lookup tool that documents GP functions.

```
gp --help
```
Lists the command-line options for the shell.

## What's unique

It is a research-grade system focused on fast number theory rather than symbolic breadth, with a C library, a GP-to-C compiler and its own compact language.

## Caveats

Graphical plotting needs X11 (XQuartz on macOS), gp2c covers only a subset of GP, and the formula's versioned binary is gp-2.17 while the homepage announces 2.19.0, so check which version you get.

## Links

- [PARI/GP homepage](https://pari.math.u-bordeaux.fr/)
- [Documentation page (user's guide PDFs, reference cards, tutorials)](https://pari.math.u-bordeaux.fr/doc.html)
