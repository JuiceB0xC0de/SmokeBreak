---
name: minuit2
title: Minuit2
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, library, math, science, statistics]
homepage: https://root.cern.ch/doc/master/Minuit2Page.html
scout_score: 5
status: draft
---

# Minuit2

**TLDR;** CERN's C++ function minimizer, descended from 1970s Fortran MINUIT, that fits parameters and reports asymmetric errors for chi-square and likelihood fits.

Minuit2 is a C++ library for finding the minimum of a function of many parameters. You write a function, usually a chi-square or a negative log-likelihood, and hand over starting values with rough uncertainties. The minimizer searches for the best-fit values, then reports parameter errors and correlations. It can also compute MINOS asymmetric errors and CONTOURS, which returns (x,y) points. It does no histogramming, data handling or graphics.

It was written at CERN for experimental data analysis. It is an object-oriented rewrite of the original Fortran MINUIT, written around 1975-1980 by Fred James and M. Winkler, and keeps the numerical behavior while adding single-sided parameter limits and the FUMILI least-squares algorithm. Its README describes it as especially suited to "difficult problems, including those which may require guidance in order to find the correct solution."

The idea underneath is that a fit is not just a best value, it is the shape of the function around the minimum. The error matrix is twice the inverse of the second-derivative matrix, scaled by an error definition: 1.0 for chi-square, 0.5 for negative log-likelihood. MINOS walks away from the minimum to find errors that include non-linearity and parameter correlations. The README calls it probably the first generally available program to do so.

Parameters with limits are mapped into an unbounded internal space with a non-linear transform, sine-based for double-sided limits. That is a neat trick, and also the reason the README advises avoiding limits unless you need them.

## Install

```
brew install minuit2
# This is a library with no executables. You compile your own C++ program against it. Needs a C++ compiler and CMake.
```

## Try this

```
Quad4FMain
```
The README's post-install test program. It minimizes a test function and should print that Minuit did successfully converge, after about 74 function calls. You may need to build it from the source tree, since brew installs no executables.

## What's unique

It is the actual minimizer lineage used in high-energy physics fits, with MINOS asymmetric errors and contour finding rather than just a best-fit point.

## Caveats

It is a library, not an application: there is no interactive mode, you write and compile C++ with an FCNBase subclass, and the README puts the practical limit around 15 free parameters.

## Links

- [Minuit2 reference guide (homepage)](https://root.cern.ch/doc/master/Minuit2Page.html)
- [DEVELOP.md: ROOT Minuit2 build and standalone install instructions](https://github.com/root-project/root/blob/master/math/minuit2/DEVELOP.md)
