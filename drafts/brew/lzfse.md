---
name: lzfse
title: lzfse
source: brew
category: take-things-apart
commitment: quick
tags: [apple, c, codec, compression, library, quick]
homepage: https://github.com/lzfse/lzfse
scout_score: 5
status: draft
---

# lzfse

**TLDR;** Apple's open-sourced LZFSE compressor in plain C, pairing Lempel-Ziv matching with Finite State Entropy coding for zlib-like ratios at higher speed.

lzfse is the reference C implementation of the compressor Apple introduced in its Compression library with OS X 10.11 and iOS 9. It ships as a small library (`liblzfse.a` and `lzfse.h`) plus a command-line tool called `lzfse`. The README calls LZFSE "a Lempel-Ziv style data compression algorithm using Finite State Entropy coding" and says it targets "similar compression rates at higher compression and decompression speed compared to deflate using zlib."

The idea underneath is the two-stage split common to modern compressors. First, an LZ pass finds repeated byte sequences and replaces them with references. Then an entropy coder squeezes the result. Here the entropy stage is Finite State Entropy, a table-driven coder that stands in for the Huffman step used in deflate. That pairing is how the design aims for zlib-level ratios at better speed.

The source tree is small enough to read in an afternoon, and it is laid out to show the seams. `lzfse_encode*.c` and `lzfse_decode*.c` hold the LZFSE entry points, `lzfse_fse.c` holds the entropy coder, and `lzvn_encode_base.c` and `lzvn_decode_base.c` hold LZVN, a separate codec that lives in the same tree. Most people meet zlib or zstd; this is a rare chance to read a production codec that came out of Apple.

## Install

```
brew install lzfse
```

## Try this

```
lzfse --help
```
Prints the tool's usage. The README shows no input and output syntax, so this is the way to find the options.

## What's unique

It is an Apple-authored codec released as a clean C reference, in a field where most people only ever meet zlib or zstd. LZVN, a second Apple codec, sits in the same source tree.

## Caveats

The README is brief, with no CLI examples or benchmarks, and its build notes are old (tested on Ubuntu 15.10 with gcc 5.2.1), so the project's current maintenance status is unclear.

## Links

- [LZFSE GitHub repository](https://github.com/lzfse/lzfse)
- [Python bindings: dimkr/pylzfse](https://github.com/dimkr/pylzfse)
- [Apple Compression library reference (old URL, may no longer resolve)](https://developer.apple.com/library/mac/documentation/Performance/Reference/Compression/index.html)
