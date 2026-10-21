---
name: unuran
title: UNU.RAN
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c-library, math, random-numbers, statistics]
homepage: https://statmath.wu.ac.at/unuran/
scout_score: 6
status: draft
---

# UNU.RAN

**TLDR;** A C library that draws random numbers from almost any probability distribution, including truncated and empirical ones, and refuses methods that don't fit.

UNU.RAN, short for Universal Non-Uniform RAndom Number generator, is a C library for generating random variates from a distribution you choose, rather than from the plain uniform distribution. You describe the distribution, pick a sampling method, and get back a generator object that produces samples. The library ships with standard distributions, and you can also build custom, truncated, empirical or multivariate ones.

It was written by the ARVAG project group in Vienna, and the homepage lists Josef Leydold as author. It is meant for cases where a non-standard or truncated distribution is needed, where you want to experiment with different distribution types, where variance reduction techniques need variates, or where you need fast generators of predictable quality. In the homepage's words: "Originally designed as a library for so called black-box or universal algorithms its interface is different from other libraries."

The idea underneath is that sampling is a separate problem from the distribution. Distribution objects, parameter objects, generator objects and uniform random number sources are independent pieces, so you can swap a distribution without rewriting the sampler. If the chosen method does not suit the distribution, or the distribution object carries too little information, initialization fails with an error instead of quietly returning wrong samples. That makes it a good door into how random variate generation actually works, a field most people never see behind a call to a normal-distribution helper.

The library is also bundled inside ROOT, the R package Runuran, and SSJ, so you may meet it there first.

## Install

```
brew install unuran
# C library only, no executables. Depends on gsl. You supply a uniform random number source; the homepage suggests Otmar Lendl's PRNG library.
```

## Try this

## What's unique

Instead of one sampler per distribution, it separates distribution, method and generator into objects, and the initializer rejects mismatched methods. It is a black-box toolkit for arbitrary or empirical distributions, not a set of normal and gamma helpers.

## Caveats

The homepage is dated 2009 and current maintenance is unconfirmed; it is a C library with no command-line tool, and the GPL applies to anything you link it into.

## Links

- [UNU.RAN homepage (ARVAG, WU Vienna)](https://statmath.wu.ac.at/unuran/)
