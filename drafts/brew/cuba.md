---
name: cuba
title: Cuba
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, integration, library, math, monte-carlo, physics, science]
homepage: https://feynarts.de/cuba/
scout_score: 5
status: draft
---

# Cuba

**TLDR;** A library from particle physics that integrates functions over many dimensions, with four different algorithms behind one calling interface so you can cross-check answers.

Cuba is a library for multidimensional numerical integration, usable from C/C++, Fortran and Mathematica. You hand it an integrand and bounds. It returns the integral, an error estimate, and a \u03c7\u00b2-probability that says how far to trust that error estimate. It can also integrate vector-valued integrands and parallelizes the sampling on its own in Fortran and C/C++.

It was written by Thomas Hahn at the Max Planck Institute for Physics in Munich for particle physics, where integrals over many variables are routine and no single method suits every integrand. So Cuba ships four: Vegas, Suave, Divonne and Cuhre. Vegas, Suave and Divonne are Monte Carlo or stratified-sampling methods that draw quasi-random or pseudo-random points. They use importance sampling, globally adaptive subdivision, or partitioning guided by numerical optimization. Cuhre is deterministic. It applies a cubature rule to subregions and repeatedly halves the one with the largest error.

The idea underneath is that a numerical answer is only worth something alongside an honest estimate of its error, and that the best check on an integral is a different algorithm. The four routines share nearly identical calling conventions, so switching is a matter of changing a routine name. In the project's words: "Cuhre is quite powerful in moderate dimensions, and is usually the only viable method to obtain high precision, say relative accuracies much below 1e\u20133."

The homepage also answers its most common question, which is how to use bounds other than the unit hypercube. You do not change the bounds. You scale the integrand by the Jacobian, and the page shows this in a short Fortran snippet.

## Install

```
brew install cuba
# Cuba is a library with no executables. You write a C, C++ or Fortran program that calls it and link against it. The homepage notes the source compiles with gcc.
```

## Try this

## What's unique

Four quite different integration algorithms sit behind one calling interface, so cross-checking an integral is a one-word change. It also reports a \u03c7\u00b2-probability for how reliable its own error estimate is.

## Caveats

It is a library with no command-line tool, so you have to write your own integrand code. The last release, 4.2.2, is from February 2022, and native Windows is unsupported because it uses fork(2).

## Links

- [Cuba homepage](https://feynarts.de/cuba/)
- [Cuba paper, Comput. Phys. Commun. 168 (2005) 78](https://arxiv.org/abs/hep-ph/0404043)
- [Parallel features paper, Comput. Phys. Commun. 207 (2016) 341](https://arxiv.org/abs/1408.6373)
