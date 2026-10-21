---
name: qd
title: qd
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, fortran, library, math, precision]
homepage: https://www.davidhbailey.com/dhbsoftware/
scout_score: 5
status: draft
---

# qd

**TLDR;** A C++ and Fortran-90 library that swaps ordinary floating-point numbers for double-double (~31 digits) and quad-double (~62 digits) types, from David H. Bailey's lab.

QD is an extended-precision arithmetic package written by David H. Bailey with Xiaoye Li and Yozo Hida at Lawrence Berkeley National Laboratory. It provides two number types: double-double, at about 31 digits, and quad-double, at about 62 digits. Through its high-level C++ and Fortran-90 interfaces, a program can use these types in place of plain `double` values and get results with far more correct digits.

The homepage does not explain the internals or the original motivation. It sits in Bailey's directory of high-precision software, where it is labelled "An older quad-double package". New users are pointed to DQFUN, QXFUN or DDFUN. It is a library, not a tool: the Homebrew formula installs only `qd-config`, a helper for finding compile and link settings, and you write your own program against it.

The idea underneath is that ordinary 64-bit floats run out of digits quickly, and many numerical problems need more. Rounding error can swamp a result, or you may want a constant to dozens of places. Between hardware doubles and arbitrary-precision libraries there is a middle tier, and QD occupies it with fixed, fairly small types. It is a door into why precision is a design choice rather than a given.

The homepage quote that sums up its niche: "It is not thread-safe, but, unlike MPFUN2020, is available with both a Fortran-90 and a C++ high-level interface."

## Install

```
brew install qd
# Library only. Needs a C++ or Fortran compiler (Homebrew pulls in gcc) and your own code to link against it.
```

## Try this

```
qd-config --help
```
Prints the options of the helper that reports how to compile and link a program against QD.

## What's unique

It offers two precision tiers, double-double and quad-double, behind both C++ and Fortran-90 interfaces. Its newer siblings target Fortran-2008 compilers.

## Caveats

The homepage calls QD older and recommends DQFUN, QXFUN or DDFUN instead; it is not thread-safe, and commercial use requires contacting Lawrence Berkeley National Laboratory.

## Links

- [High-Precision Software Directory (homepage)](https://www.davidhbailey.com/dhbsoftware/)
