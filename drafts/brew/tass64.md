---
name: tass64
title: 64tass
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [6502, afternoon, assembler, c64, macro-assembler, retro]
homepage: https://tass64.sourceforge.net/
scout_score: 6
status: draft
---

# 64tass

**TLDR;** A command-line macro assembler for the 6502 family that turns assembly source into binaries for C64-era machines, with an unusually rich expression language.

64tass reads an assembly source file for a 65xx processor (6502, 65C02, 65816, 65CE02, 45GS02 and others) and writes a binary. Hex and S-record text output are also available. It makes multiple passes over the source to resolve forward references and to pick addressing modes, which it chooses from the instruction and the `.dpage`, `.databank` and program counter settings.

It exists as a portable, modern tool whose syntax is familiar to people who used Omicron TASS and TASM. That makes it a bridge between old C64-era source and today's editors and build systems. The source can be written in any text editor, and the manual's Makefile example feeds the output to a cruncher (pucrunch, a separate tool) to produce a PRG file for a real or emulated machine.

The door it opens is writing machine code for chips from the 1970s and 80s, where every byte and every addressing mode matters. The manual is long, but it says the assembler can be used with just basic 6502 knowledge, like any other assembler. The long part is for when you want more.

That extra part reads like a small language: lists and tuples, dictionaries usable as enumerations, bit-string and byte-string slicing, and a `binary()` function that pulls files such as SID music straight into source. It also has macros, structures, unions, scopes, sections with a built-in linker, and assembly and label listings.

## Install

```
brew install tass64
```

## Try this

```
64tass --help
```
Lists the command-line options, including output format and case-sensitivity switches.

```
64tass -a src.asm
```
Assembles src.asm as ASCII/Unicode source. The manual recommends -a for such files.

```
64tass -C -a -B -i source.asm -o demo.tmp
```
The manual's Makefile recipe: builds source.asm into an intermediate file, demo.tmp, ready for a cruncher.

## What's unique

Its expression language goes far beyond a typical assembler, with element-wise list arithmetic, dictionaries, and the ability to read binary files into source. It also stays compatible with the old Omicron TASS workflow.

## Caveats

The manual calls this a development version (v1.60 r3243) and warns that syntax may change in rare non-backwards-compatible ways.

## Links

- [Homepage / reference manual (v1.60 r3243)](https://tass64.sourceforge.net/)
- [SourceForge project page (downloads, tracker, reviews)](https://sourceforge.net/projects/tass64/)
