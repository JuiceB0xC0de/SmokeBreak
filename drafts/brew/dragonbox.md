---
name: dragonbox
title: Dragonbox
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, algorithms, c++, floating-point, library, math]
homepage: https://github.com/jk-jeon/dragonbox
scout_score: 5
status: draft
---

# Dragonbox

**TLDR;** A C++ library that finds the shortest decimal string a float will read back as exactly, with a published proof of why it works.

Dragonbox converts a nonzero finite float or double into a decimal significand and exponent. The digits are the shortest ones that still round-trip to the same number. Among the shortest candidates, it picks the correctly rounded one. A companion `to_chars` function turns those integers into text, so 1.234 comes out as `1.234E0`.

It exists because printing floats is harder than it looks. The number you typed, 0.3, is not the number stored in the machine. Printing the stored value naively gives a long tail of digits, and printing too few digits gives back a different number. Dragonbox is the author's successor to Schubfach by Raffaello Giulietti, and it is inspired by Grisu and Grisu-Exact. The name nods to the pigeonhole principle, which Schubfach calls the drawer principle and which is also known as Dirichlet's box principle. Dragonbox keeps the box and adds Grisu's dragon.

The repository is a good door into how numbers become text. The README points to a paper, `other_files/Dragonbox.pdf`, that explains the algorithm and includes a mathematical proof. It says the proof was checked with verification programs in the test and meta directories. The main implementation is, in the author's words, "riddled with template indirections obscuring the core logic of the algorithm." For reading, the README points to a simpler version in `subproject/simple`.

The string step is not officially part of the algorithm. The README says the fmt library uses an almost identical implementation.

## Install

```
brew install dragonbox
# Installs headers only, with no executables. It is a C++11 or later library; every function is constexpr since C++20. Header-only use needs just dragonbox.h. For string output, add dragonbox_to_chars.h and dragonbox_to_chars.cpp.
```

## Try this

```
git clone https://github.com/jk-jeon/dragonbox
```
Fetches the source, including the paper in other_files and the simpler implementation in subproject/simple.

```
cmake .. -DDRAGONBOX_ENABLE_SUBPROJECT=On
```
Run from a build directory, this configures the test, benchmark, common and meta subprojects so you can build them from the root.

```
ctest .
```
Runs the test suite once the test subproject is built.

## What's unique

It guarantees the shortest, correctly rounded string that round-trips, and the README presents it as a tie-break-aware refinement of Schubfach. Sign handling, trailing zeros, rounding mode and cache size are all compile-time policies.

## Caveats

to_decimal is undefined for infinities, NaN and zero, each policy combination creates its own template instantiation which can bloat binaries, and the README gives no release version or last-commit date (its benchmarks are dated 03/30/2024).

## Links

- [GitHub homepage and README](https://github.com/jk-jeon/dragonbox)
- [Simpler reference implementation in subproject/simple](https://github.com/jk-jeon/dragonbox/tree/master/subproject/simple)
- [Drachennest, a fairer benchmark cited by the author](https://github.com/abolz/Drachennest)
