---
name: libchaos
title: libchaos
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, hashing, library, math, random]
homepage: https://github.com/maciejczyzewski/libchaos
scout_score: 5
status: draft
---

# libchaos

**TLDR;** A C++11 library that builds hash functions and random generators from chaotic systems, with time, space and key as the dials.

Libchaos is a C++ library for randomization, hashing and statistical analysis. It has two families of algorithms. The first is "chaos machines", which behave like a pseudo-random oracle: you push data in with `push` or `<<`, and pull blocks of output back out with `pull`. The second is a set of ordinary pseudo-random number generators, such as xoroshiro and KISS, used through `seed` and `next`.

The idea underneath is the chaos machine. The README says: "It turns out that a pseudo-random function can be easily enriched by a chaotic system, creating something completely new." A machine is controlled by three parameters: time (how long it runs), space (memory or period length) and an initial secret key. Turning those dials lets one scheme act as a hash, a pseudo-random function or an oracle. The theory is in an eprint paper linked below.

The headline entry point is `chaos::password`. It takes a password, a salt, and time, space and output-size parameters, and returns a hex string. That makes it a salted hash whose cost you tune, in the spirit of memory-hard password hashing.

The author wants a modern C++ toolkit for research on randomness and hashing, and says TestU01, Dieharder and Hashdeep are obsolete or stalled and that libchaos aims to replace them. That ambition is mostly still a plan. The statistical-test module and a Hashdeep fork are listed as in progress or TODO.

## Install

```
There is no Homebrew formula in the README, only a stated plan. Check `brew info libchaos` first. Otherwise build from source, which needs a C++11 compiler (g++ 4.7 or newer):
git clone git@github.com:maciejczyzewski/libchaos.git
cd libchaos && ./install.sh
```

## Try this

```
g++ -std=c++11 -lchaos example.cc
```
Compiles the README's example program against the installed library.

```
./a.out | xxd -l 1024
```
Runs the compiled example and hex-dumps the first 1024 bytes of its output.

```
cmake -DLIBCHAOS_ENABLE_TESTING=ON ..
```
Configures a build with the Google Test and Google Benchmark targets enabled, for contributors.

## What's unique

Chaos machines present hashing, pseudo-random functions and oracles as one scheme with tunable time, space and key. It is an unusual angle compared with the usual PRNG and hash libraries.

## Caveats

The README says the project is at an early stage, and many listed features are TODO. Its CI badge points to a retired service, so it looks quiet, and the benchmarks are the author's own.

## Links

- [Homepage (GitHub repository)](https://github.com/maciejczyzewski/libchaos)
- [Chaos machines theory (eprint paper)](https://eprint.iacr.org/2016/468)
- [Algorithms list (ALGORITHMS file)](https://github.com/maciejczyzewski/libchaos/blob/master/ALGORITHMS)
