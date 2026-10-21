---
name: sdcc
title: SDCC
source: brew
category: take-things-apart
commitment: afternoon
tags: [8051, afternoon, c, compiler, microcontrollers, retro, simulator, z80]
homepage: https://sdcc.sourceforge.net/
scout_score: 7
status: draft
---

# SDCC

**TLDR;** A C compiler for tiny chips like the 8051, Z80, STM8 and 6502, bundled with assemblers, a debugger and simulators so you can run the result without hardware.

SDCC is a retargetable, optimizing C compiler suite for small microcontrollers and 8-bit CPUs. It takes standard C (the homepage lists C89 through C23) and emits machine code for Intel MCS51 parts, the Maxim DS80C390, Freescale HC08/S08, the Zilog Z80 family, Padauk, STM8, MOS 6502 and WDC 65C02. Several other targets are listed as experimental or in progress.

The suite is more than a compiler. It includes an assembler and linker (sdas and sdld, derived from ASXXXX), a preprocessor, a source-level debugger (sdcdb), archive tools derived from GNU Binutils, and about a dozen ucsim simulators. That means you can compile a C program for a chip from the 1970s or 80s and run it in a simulator on your laptop, with no board or programmer needed.

The interesting part is what C has to do on these machines. They have a handful of registers, tiny memory and no stack in the modern sense, so the compiler needs MCU-specific language extensions, a global register allocator and a rule-based peephole optimizer. Looking at the assembly it generates shows how a high-level language gets squeezed onto very small hardware.

The project says it is "primarily developed by unpaid volunteer work" and has lived on SourceForge since 1999. It is still active: version 4.6.0 was released in June 2026.

## Install

```
brew install sdcc
No hardware is needed to compile or to run code in the bundled ucsim simulators. The homepage notes that distro packages are often outdated; source and binaries are on the SourceForge releases page.
```

## Try this

```
sdcc -v
```
Prints the compiler version and build date, a quick check that the toolchain is installed.

```
sdcc --help
```
Lists the compiler options, including the choice of target architecture.

```
ucsim_z80 --help
```
Shows how to start the Z80 simulator, one of the bundled ucsim simulators.

## What's unique

It is a full modern C compiler for a long list of retro and small-MCU families, and it ships simulators for most of them in the same tree.

## Caveats

The PIC16 and PIC18 targets are unmaintained, some other targets are experimental, and the project is mostly unpaid volunteer work.

## Links

- [SDCC homepage](https://sdcc.sourceforge.net/)
- [SDCC file releases (SourceForge)](http://sourceforge.net/projects/sdcc/files/)
