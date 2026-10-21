---
name: primesieve
title: primesieve
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [c++, math, number-theory, primes, quick, stress-test]
homepage: https://github.com/kimwalisch/primesieve
scout_score: 6
status: draft
---

# primesieve

**TLDR;** A very fast prime number generator that counts or prints primes, twin primes and larger k-tuplets up to 2^64, and doubles as a CPU stress test.

primesieve is a command-line program and C/C++ library for generating prime numbers. Give it a limit and it counts the primes up to it. Ask it to print and it lists them. Ask for twin primes, or triplets, and it finds those instead, with k-tuplets up to 6 supported. Limits go as high as 2^64, and by default it uses every CPU core.

Underneath is the segmented sieve of Eratosthenes with wheel factorization. Run time is O(n log log n) and memory is O(sqrt n). The interesting engineering is about the machine rather than the maths: it detects your CPU's L1 and L2 cache sizes and sizes its main data structures to fit, and above 2^32 it switches to a bucket sieve to stay cache friendly. The sieve is old, and the speed comes from making it fit the hardware.

That same property gives it a second use. The built-in stress test counts primes over huge ranges, and every block has a known answer. A wrong count points to a hardware fault, so it works as a check on cooling and stability. It has a CPU mode and a RAM mode.

For a curious developer it is a door into number theory you can run at home: how dense primes get, how often twin primes appear, how counts behave at 10^10 and beyond. The library API is there if you want to build on it.

## Install

```
brew install primesieve
```

## Try this

```
primesieve 1e10
```
Counts the primes up to 10 billion across all CPU cores and prints the total.

```
primesieve 1000000 --print=2
```
Prints every twin prime pair up to one million.

```
primesieve 1e10 --dist=2^32 --count=3
```
Counts prime triplets in the interval from 1e10 to 1e10 plus 2^32.

## What's unique

It tunes its sieve to your CPU's measured cache sizes, and it ships a stress test that uses prime counting with known answers to catch hardware faults.

## Caveats

Printing runs single-threaded because output must be in order, and the stress test's default timeout is 24 hours, so set --timeout yourself.

## Links

- [Homepage / GitHub repository](https://github.com/kimwalisch/primesieve)
- [C API documentation](https://github.com/kimwalisch/primesieve/blob/master/doc/C_API.md)
- [C++ API documentation](https://github.com/kimwalisch/primesieve/blob/master/doc/CPP_API.md)
