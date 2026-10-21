---
name: bitwise
title: bitwise
source: brew
category: fundamentals
commitment: quick
tags: [bits, calculator, embedded, ncurses, quick, tui]
homepage: https://github.com/mellowcandle/bitwise
scout_score: 5
status: draft
---

# bitwise

**TLDR;** A terminal calculator that shows one number in every base at once and lets you toggle individual bits, with datasheet-style bit-field selects.

bitwise is a small C program on ncurses. Give it a number or a C-style expression and it prints the value as signed and unsigned decimal, hex, octal and binary, with a labelled bit grid. It also shows human-readable sizes, IPv4 in both byte orders, ASCII and Radix64. Run it with no arguments, or with `-i`, and you get a full-screen mode: edit any field and the others update, walk a cursor along the binary row to flip single bits, and switch the width between 8, 16, 32 and 64 bits. Pressing `:` opens an expression prompt, much like vim's command line.

The README aims it at "anyone who spends their day staring at a register dump wondering which bit is set." The point is to save a lookup for each representation when you are reading hardware registers, kernel flags or driver code.

The interesting design choice is the bit select. `v[msb:lsb]` and `v[bit]` come from Verilog, and the result is right-aligned, so `0xdeadbeef[31:16]` gives `0xdead` and not a masked `0xdead0000`. That matches how datasheets describe fields. It departs from C on purpose, since in C `v[3]` is array indexing. Everything else follows C's operator precedence, so expressions pasted from source evaluate the way you expect.

Base is detected from the prefix: `0x` for hex, a leading `0` for octal, `b` for binary, otherwise decimal.

## Install

```
brew install bitwise
```

## Try this

```
bitwise '0x875423[31:23]'
```
Extracts bits 31 down to 23 of the value and shows the field right-aligned in every base.

```
bitwise '0x875423[15]'
```
Returns the single value of bit 15.

```
bitwise -- '-5'
```
Shows a negative number in all bases; the `--` stops the leading minus being read as an option.

## What's unique

Verilog-style right-aligned bit-field selects sit alongside C-precedence expressions, so datasheet field notation and source-code arithmetic work in the same calculator.

## Caveats

Changing the bit width masks the number to the new width and can silently drop high bits, and comparison, logical, ternary and exponent operators are not supported.

## Links

- [GitHub repository and README](https://github.com/mellowcandle/bitwise)
- [vim-bitwise editor plugin](https://github.com/mellowcandle/vim-bitwise)
- [Latest release](https://github.com/mellowcandle/bitwise/releases/latest)
