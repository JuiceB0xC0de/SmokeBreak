---
name: pbc
title: PBC
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c, cryptography, elliptic-curves, library, math]
homepage: https://crypto.stanford.edu/pbc/
scout_score: 5
status: draft
---

# PBC

**TLDR;** A C library for pairing-based cryptography, written for a degree and now openly 'frozen in amber', with a door into bilinear maps on elliptic curves.

PBC (Pairing-Based Cryptography) is a free C library built on GMP. It handles the math underneath pairing-based cryptosystems: generating elliptic curves, doing arithmetic in their groups, and computing the pairing itself. It also ships example programs for several such systems.

Ben Lynn wrote it so that these cryptosystems could share a common base, with speed and portability as goals. The API is abstract enough that a programmer needs only an elementary understanding of pairings, without much elliptic curve or number theory. In his words: "The PBC library is designed to be the backbone of implementations of pairing-based cryptosystems, thus speed and portability are important goals."

The idea underneath is the bilinear map: a function that takes two points on a curve and returns a value in another group, in a way that lets you move exponents around between the inputs. That one property makes possible things ordinary elliptic curve cryptography cannot do, and the examples are a practical way to see how those schemes are put together. The manual has an internals chapter covering the curve types, labelled Type A through Type I.

The author is candid about the library's age: "I started the PBC library decades ago, for a degree. I also graduated decades ago, and as a result, the library is almost frozen in amber." He recommends MIRACL Core for new work. Read this one as a teaching artifact and a readable piece of history.

## Install

```
brew install pbc
# Installs the C library and headers; it depends on gmp, which brew pulls in. There is no command-line executable, so you need a C compiler to use it.
```

## Try this

## What's unique

The author's own homepage tells readers to use a newer library instead, and explains how his hash-to-curve approach differs from the RFC 9380 standard. Few projects point users to their successor this plainly.

## Caveats

It is a library with no executables, the manual is dated 2006, the benchmarks come from a 1GHz Pentium III, and the author recommends MIRACL Core for anything new.

## Links

- [PBC homepage](https://crypto.stanford.edu/pbc/)
- [Downloads page](https://crypto.stanford.edu/pbc/download.html)
- [PBC Library Manual 1.0.0](https://crypto.stanford.edu/pbc/manual/)
