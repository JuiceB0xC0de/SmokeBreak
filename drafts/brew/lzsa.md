---
name: lzsa
title: lzsa
source: brew
category: take-things-apart
commitment: quick
tags: [6502, 8-bit, compression, formats, quick, retro, z80]
homepage: https://github.com/emmanuel-marty/lzsa
scout_score: 7
status: draft
---

# lzsa

**TLDR;** A byte-aligned compression format and packer built so 8-bit CPUs like the Z80 and 6502 can unpack data fast, with tiny decompressors.

LZSA is a family of lossless compression formats, plus a packer called `lzsa` that produces them. It splits input into blocks of up to 64 KB, lets matches reach back up to 64 KB, and writes a packed file that decompresses to the original. The decompressors are not part of the brew install. The README points to assembly routines for Z80, 6502, 6809, 8088, i8080, PDP-11, MC68000 and Game Boy, many contributed by other people.

The design goal is the unusual part. On an 8-bit machine, the cost of unpacking matters as much as the size of the result, and the decompressor itself has to fit in a few bytes. The README frames LZSA1 as a replacement for LZ4 and LZSA2 as a replacement for ZX7 in these scenarios. It cites a 67-byte size-optimized Z80 decompressor for LZSA1.

The tricks are about what a tiny CPU does badly. LZSA2 avoids slow bit-packing and uses byte alignment and nibbles instead. It encodes offsets of 5, 9, 13 and 16 bits, and supports rep-matches. The encoding avoids 16-bit arithmetic on the decoder side. The optimizer searches for the command sequence that gives the smallest output while keeping decompression fast, and the match-finder and optimizer cooperate to prefer 8-bit match offsets.

That makes it a good door into compression tradeoffs: ratio versus speed versus decoder size, and how format design follows the hardware. The format docs are linked below if you want to read the bit layouts.

## Install

```
brew install lzsa
```

## Try this

```
lzsa --help
```
Prints the packer's usage, since the README shows no command lines of its own.

## What's unique

Most compressors chase ratio. This one is shaped around what a Z80 or 6502 can unpack quickly, and the optimizer is tuned for decoder speed as well as output size.

## Caveats

The README gives no usage steps, the maintenance status is unclear from the brief, and the decompressors are assembly meant for the target machines, not for your laptop.

## Links

- [Project homepage (GitHub)](https://github.com/emmanuel-marty/lzsa)
- [Stream format doc](https://github.com/emmanuel-marty/lzsa/blob/master/StreamFormat.md)
- [Block format for LZSA1](https://github.com/emmanuel-marty/lzsa/blob/master/BlockFormat_LZSA1.md)
- [The Hollow demo on Pouet (uses LZSA on Z80)](https://www.pouet.net/prod.php?which=81909)
