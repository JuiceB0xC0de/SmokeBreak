---
name: primecount
title: primecount
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [library, math, number-theory, openmp, primes, quick]
homepage: https://github.com/kimwalisch/primecount
scout_score: 6
status: draft
---

# primecount

**TLDR;** Counts the primes up to 10^31 without listing them, using the combinatorial algorithms behind prime counting world records.

primecount takes a number like `1e14` and prints pi(x), the count of primes less than or equal to it. Sieving every number up to x would take far too long at that size. primecount never enumerates the primes. It reduces the count to a sum of phi function values plus a few correction terms, evaluated over a much smaller sieve bound.

It implements the lineage of these formulas: Legendre, Meissel, Lehmer, Lagarias-Miller-Odlyzko, Deleglise-Rivat and Gourdon. Gourdon's is the default, and flags such as `--meissel` let you run the older ones on the same input. The README says it holds the first open source implementations of Deleglise-Rivat and of Xavier Gourdon's algorithm, in its words "(that works)". It is parallelized with OpenMP and uses a custom load balancer that the README says scales to hundreds of cores.

It also does related things. `--nth-prime` finds the nth prime by estimating it with the inverse Li or inverse Riemann R function, counting primes up to that guess, then running a segmented sieve forward to the exact answer. It can approximate pi(x) with Riemann R or Li, and evaluate phi(x, a). It is also a C/C++ library, with bindings for Python, Julia, Rust, Haskell, Lua and Common Lisp.

The door here is analytic number theory. Counting primes without finding them is a real research problem, and the project says it has been used to compute several prime counting world records.

## Install

```
brew install primecount
# depends on primesieve and libomp, which brew pulls in. No account or hardware needed.
```

## Try this

```
primecount 1e14
```
Prints the number of primes up to 10^14.

```
primecount 2**32 --meissel
```
Counts primes up to 2^32 using Meissel's older algorithm instead of the default Gourdon.

```
primecount 1e14 --nth-prime --threads=4 --time
```
Finds the 10^14th prime on 4 threads and prints the elapsed seconds.

## What's unique

It packages the full lineage of combinatorial prime counting algorithms in one tool, including open source Deleglise-Rivat and Gourdon implementations, and lets you switch between them on the same input.

## Caveats

Maximum input is 10^31, and very large inputs like 1e20 are a serious computation. The README gives no release or commit date, though CI, 2025 benchmarks and distro packages suggest it is maintained.

## Links

- [primecount homepage (GitHub)](https://github.com/kimwalisch/primecount)
- [C and C++ API documentation](https://github.com/kimwalisch/primecount/blob/master/doc/libprimecount.md)
- [World records](https://github.com/kimwalisch/primecount/blob/master/doc/Records.md)
