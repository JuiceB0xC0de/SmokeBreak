---
name: spim
title: SPIM
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, assembly, cpu, mips, old, simulator, teaching]
homepage: https://spimsimulator.sourceforge.net/
scout_score: 7
status: draft
---

# SPIM

**TLDR;** A MIPS32 simulator that runs assembly source in your terminal, so you can step through how a simple processor executes code.

SPIM reads MIPS32 assembly language source, runs it, and gives you a simple debugger plus a minimal set of operating system services, such as printing and reading. It does not run compiled binaries. The input is assembly text and the output is whatever the program does inside the simulator. The `spim` command is the terminal interface. QtSpim, xspim and PCSpim are windowed front ends, though only the terminal program is installed by the Homebrew formula.

It was written by James Larus, and the copyright line runs from 1990 to 2023. The README gives no motivation beyond describing it as a simulator. Tools like this are widely used for teaching, because a small, regular instruction set is a good way to see what a compiler eventually produces: registers, loads and stores, branches, and system calls.

The idea underneath is that a processor is just a loop that fetches an instruction and does what it says. With a simulator you can write that instruction stream by hand and watch the machine state change, without hardware or a cross-compiler. It covers almost the whole MIPS32 assembler-extended instruction set, which is enough to write real small programs.

The project is old and says so. The author writes: "Spim is no longer supported. The code has been stable for many years, with a few occasional bugs." He invites people to fork it.

## Install

```
brew install spim
```

## Try this

```
spim --help
```
Lists the command-line options of the terminal simulator, including how to load an assembly file.

## What's unique

It is a small, self-contained simulator that runs MIPS32 assembly source directly, with a built-in debugger and basic OS services, and ships with full source and documentation.

## Caveats

The author says SPIM is no longer supported, it only runs assembly source rather than compiled binaries, and it omits most floating point comparisons, rounding modes and memory page tables.

## Links

- [SPIM homepage](https://spimsimulator.sourceforge.net/)
- [QtSpim downloads (SourceForge)](https://sourceforge.net/projects/spimsimulator/files/)
- [Qt framework downloads](http://qt-project.org/downloads)
