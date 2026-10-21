---
name: crcany
title: crcany
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, algorithms, c, checksums, crc, math]
homepage: https://github.com/madler/crcany
scout_score: 6
status: draft
---

# crcany

**TLDR;** Computes and generates C code for any CRC from its parameters, showing the same checksum done bit by bit, byte by byte and word by word.

crcany is a small C suite that treats a CRC as one parameterized algorithm. You give it a CRC definition in the Greg Cook / Ross Williams parameter model, either by catalogue name or as raw parameters, and it computes the checksum. It can also combine two CRCs: given the CRC of each block and the length of the second, it produces the CRC of the concatenation without re-reading the data. A companion tool writes .c and .h files for one or many CRC definitions.

The interesting part is how the three algorithms relate. The bit-at-a-time version behaves like a hardware shift register. The byte-at-a-time version builds a 256-entry table by running the bit-at-a-time routine on every byte value. The word-at-a-time version expands that table into n-1 more tables, where n is the word size in bytes, with separate little-endian and big-endian flavors.

The README states the goal plainly: "Provide once and for all a definitive reference for how to compute and combine any CRC with any of bit, byte, or word-at-a-time algorithms, on any big or little-endian architecture." It is written by Mark Adler, so it is a reference you can read to see why table-driven CRCs work, not just a tool to run.

The door it opens is the family of CRC variants: why CRC-32 and CRC-16 flavors differ in polynomial, bit order, initial value and final XOR, and how fast implementations are derived from the slow, obvious one.

## Install

```
brew install crcany
```

## Try this

```
crcany --help
```
Prints whatever usage the binary offers; the README documents no syntax for it, so this is the way in.

```
make
```
If building from source, compiles the crcany, crctest, crcall, crcadd and mincrc executables from the repository root.

```
make test
```
Checks CRC calculation and the generated C code against the full list of catalogued CRCs.

## What's unique

Rather than hard-coding one polynomial, it generates code for any CRC up to 64 bits in bit, byte and word-at-a-time forms, and includes CRC combination.

## Caveats

The README documents no usage syntax for the crcany binary, code generation stops at 64 bits, and the brief shows no version or commit dates.

## Links

- [GitHub repository (homepage)](https://github.com/madler/crcany)
- [Greg Cook's CRC catalogue](https://reveng.sourceforge.io/crc-catalogue/all.htm)
- [Ross Williams CRC tutorial](http://zlib.net/crc_v3.txt)
