---
name: prog8
title: Prog8
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [6502, afternoon, commander-x16, commodore-64, compiler, emulator, language, retro]
homepage: https://prog8.readthedocs.io
scout_score: 7
status: draft
---

# Prog8

**TLDR;** A structured, compiled language that turns readable source into native machine code for the 6502 chip inside the Commodore 64, Commander X16 and other 8-bit machines.

Prog8 is a compiler for the 6502 family of 8-bit CPUs, the chips behind many home computers of the late 1970s and 1980s. You write `.p8` source files using blocks and subroutines, and the `prog8c` compiler produces native machine code for a target such as the Commodore 64, Commodore 128, Commodore PET or Commander X16. There is also an experimental backend for the 32-bit Motorola 68000, used for Amiga targets.

The author's pitch is "all advantages of a higher level language over having to write assembly code manually", while staying low level enough for fast programs. The language adds things raw assembly lacks: structs, typed pointers, modules with private symbols, a `defer` statement, multiple return values, 2D array syntax and a `when` statement. The compiler hands the final assembly step to the external 64tass cross assembler.

The idea underneath is how much a compiler can do on a machine with a few dozen kilobytes of memory and a CPU with almost no registers. If a program sticks to the standard Kernal and Prog8 library routines, the same source can be rebuilt for a different machine by changing the target flag. After a successful build, the compiler can launch the result in the VICE emulator, so you can try it without owning any hardware.

## Install

```
brew install prog8
# Brew pulls in openjdk and tass64 (the 64tass assembler). To run programs you also need an emulator: VICE for the C64, or x16emu R42 or newer (Box16 is an alternative) for the Commander X16.
```

## Try this

```
prog8c --help
```
Lists the compiler's options, including how to choose a target machine and whether to launch an emulator after building.

## What's unique

It aims at the same space as C via cc65, but the author claims smaller and often faster output, with a benchmark linked from the README. Its language features go well beyond what raw assembly gives you.

## Caveats

The Amiga and 68000 targets and the optional `-newcodegen 6502` generator are experimental, most development centres on the Commander X16, and you need an emulator or real hardware to run anything.

## Links

- [Prog8 documentation](https://prog8.readthedocs.io)
- [GitHub repository and README](https://github.com/irmen/prog8)
- [Compiling from source instructions](https://prog8.readthedocs.io/en/latest/compiling.html)
