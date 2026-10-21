---
name: ats2-postiats
title: ATS/Postiats
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, dependent-types, language, linear-types, proofs, types]
homepage: https://www.cs.bu.edu/~hwxi/atslangweb/
scout_score: 8
status: draft
---

# ATS/Postiats

**TLDR;** A statically typed language where dependent types, linear types and proofs live in the same source file as the program, compiling to native code.

ATS (this is ATS2, implemented as ATS/Postiats) is a statically typed, call-by-value language with an ML-flavoured core. Its author describes it as a language that "unifies implementation with formal specification." The homepage shows small programs that print text, reject an out-of-bounds list subscript at compile time, reuse code through a template system, and solve N-Queens with combinators.

The idea underneath is the Applied Type System framework. Types can depend on values, so a type can say how long a list is, and the compiler can then check that an index stays in range. A subsystem called ATS/LF supports interactive theorem-proving, where proofs are written as total functions. Programming and proving sit in the same file instead of in separate tools.

Linear types track resources. The homepage credits them for a low memory footprint and for safe explicit memory management and pointer arithmetic. The author says the aim is to "enforce precision in practical programming" and to support refinement-based development, and ATS is also positioned as a way to teach type theory. The ATS2 compiler is itself written in ATS1 (ATS/Anairiats) and is over 180K lines.

The three installed executables (patscc, patsopt, myatscc) are compiler front ends. The homepage does not describe them.

## Install

```
brew install ats2-postiats
# depends on gmp, which brew installs for you. The homepage also offers an in-browser "Try ATS on-line" option that needs no install.
```

## Try this

```
patscc --help
```
Prints the options of the ATS-to-native compiler driver.

```
patsopt --help
```
Shows the options of the ATS compiler proper, the stage that checks types and proofs.

```
myatscc --help
```
Shows what this extra front end accepts; the homepage does not describe it.

## What's unique

Dependent types, linear types and theorem proving are in one language that compiles to efficient native code, rather than in a separate proof assistant. Proofs are ordinary total functions in the same file as the program.

## Caveats

The homepage calls ATS "feature-rich (like C++)" and says learning it takes a substantial amount of time; it is a personal academic site with no visible release date, so its maintenance status is unclear.

## Links

- [ATS homepage](https://www.cs.bu.edu/~hwxi/atslangweb/)
