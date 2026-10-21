---
name: msieve
title: msieve
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c, cryptography, factoring, math, number-theory]
homepage: https://sourceforge.net/projects/msieve/
scout_score: 6
status: draft
---

# msieve

**TLDR;** A public-domain C library and small command-line tool that factors big integers, from quick trial division up to the quadratic sieve and an unfinished number field sieve.

Msieve takes an integer, a file of integers one per line, or an arithmetic expression like `(10^53 - 1) / 9`, and returns the prime factors. Output goes to a logfile, with a summary on screen. The command-line program is a small demo of the library.

Inside, it runs cheap methods first and escalates. Trial division and Pollard rho run on every input. Then come P-1, P+1 and ECM, which need GMP-ECM. If those fail, the self-initializing quadratic sieve takes over. The number field sieve is also in the code for much larger inputs, but the README says it is for users who know what they are doing. Savefiles let an interrupted factorization restart.

The author, Jason Papadopoulos, describes it as the result of his efforts "to understand and optimize how integers are factored using the most powerful modern algorithms." It is a hobby project, released into the public domain.

The idea underneath is that factoring is a ladder of algorithms, each beating the last at a certain size, and the difficulty of the top rungs is why RSA works. Running msieve on numbers of growing length shows where one method gives way to the next. The README is candid that this is not a tutorial: "Do not expect to become a factoring expert just by reading it."

## Install

```
brew install msieve
```

## Try this

```
msieve -h
```
Prints the full list of command-line options for the demo program.

## What's unique

It is a complete factoring pipeline in one small, self-contained, public-domain C library. The author's FAQ suggests using GGNFS for the first stage of large jobs and msieve for the last part.

## Caveats

The README says it does not expect to complete factorizations above about 120 digits on its own, the quadratic sieve is 'not appropriate' above roughly 110 digits, and the NFS code is not finished; activity status is unclear.

## Links

- [Homepage (SourceForge)](https://sourceforge.net/projects/msieve/)
- [Source repository (GitHub mirror, with README)](https://github.com/radii/msieve)
- [Author's web page](http://www.boo.net/~jasonp/qs.html)
