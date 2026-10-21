---
name: srecord
title: SRecord
source: brew
category: take-things-apart
commitment: quick
tags: [cli, eprom, file-formats, firmware, quick, retro]
homepage: https://srecord.sourceforge.net/
scout_score: 6
status: draft
---

# SRecord

**TLDR;** A set of command-line tools for converting, filtering, comparing and generating EPROM and firmware load files across Intel hex, Motorola S-Record and many other formats.

SRecord is built around three programs. `srec_cat` reads one or more load files, optionally transforms them, and writes the result in another format. `srec_cmp` checks whether two files, or parts of them, hold the same data. `srec_info` prints a summary of a file. Load files are the text or binary images that were once fed to chip programmers, and they are still how a lot of firmware gets passed around.

The formats list is long: Intel hex, Motorola S-Record, TI-TXT and Verilog VMEM can be read and written. Some formats go one way only. C array, VHDL, BASIC DATA statements, ASM and Hexdump are output-only, so a firmware image can be turned into source code you could paste into a program.

The design idea is that any input can be replaced by a generator (constant, random, repeated data), and any input can be run through a chain of filters such as crc, checksum, crop, exclude, fill, offset and split. Because they sit on the same command line, you can describe a whole image-patching job as one pipeline instead of writing a one-off script.

The author, Peter Miller, wrote it because he could not find many programs for manipulating EPROM load files, and the ones he found only did a few of the things he needed. Formats and filters are C++ polymorphic classes, so adding new ones is relatively simple. The project also ships a shared library exposing the same formats and filters to other programs.

## Install

```
brew install srecord
```

## Try this

```
srec_cat --help
```
Prints usage for the main tool, a first look at the input, filter and output options.

```
srec_info --help
```
Shows how to get a summary of a load file's contents.

```
srec_cmp --help
```
Shows how to compare two load files, or portions of them, for equality.

## What's unique

Filters and generators can be chained onto any input in a single command line, and the format list is unusually long for a tool this small. It reads like a small language for firmware images.

## Caveats

The homepage calls itself 'very much a product of its time', and several formats are one-way only, so not every conversion works in both directions.

## Links

- [Homepage](https://srecord.sourceforge.net/)
- [Manual (single PDF, linked from homepage)](https://srecord.sourceforge.net/)
- [Manual pages as HTML (linked from homepage)](https://srecord.sourceforge.net/)
