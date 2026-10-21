---
name: mdk
title: mdk
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, ancient, assembly, education, emulator, knuth, scheme]
homepage: https://www.gnu.org/software/mdk/mdk.html
scout_score: 8
status: draft
---

# mdk

**TLDR;** An emulator, assembler and debugger for MIX, the imaginary computer from Knuth's The Art of Computer Programming, so you can step through its assembly.

MDK emulates MIX, the made-up machine Donald Knuth invented for The Art of Computer Programming, and MIXAL, its assembly language. `mixasm` turns MIXAL source into binaries, and the virtual machines run them. The emulated machine includes registers, memory cells, an overflow toggle, comparison flags, I/O devices and the binary instruction set.

There are two front ends for the VM. `mixvm` is a command-line debugger built on readline, and `gmixvm` is a GTK+ graphical one. Both support breakpoints, conditional breakpoints, step execution, timing statistics and instruction tracing. You can inspect or change registers, flags and memory at any step. I/O is simulated through standard output and the file system.

The fourth executable, `mixguile`, is a Guile interpreter with a MIX VM embedded in it, so the machine can be driven and scripted from Scheme. The kit also ships Emacs modes for editing MIXAL and running the VM.

The idea underneath is that a deliberately simplified machine is a good place to learn how real ones work. The project's own words: "The MIX computer is a simplified version of real CISC computers, and its assembly language closely resembles real ones." Since the book's programs are written for MIX, this lets you run them and watch the state change instruction by instruction.

## Install

```
brew install mdk
```

## Try this

```
mixvm --help
```
Lists the options of the command-line MIX debugger, the quickest way to see what the VM can do.

```
mixasm --help
```
Shows how to assemble a MIXAL source file into a binary the VM can run.

```
gmixvm --help
```
Shows the options for the graphical MIX VM, which needs GTK+.

## What's unique

It is a faithful emulator of a textbook machine, with a Scheme-scriptable VM (`mixguile`) alongside the debugger front ends.

## Caveats

The brief gives no worked example commands, so you will need Knuth's book or the bundled manual to know what MIXAL to write.

## Links

- [GNU MDK homepage](https://www.gnu.org/software/mdk/mdk.html)
- [Source repository (git, Savannah)](git://git.sv.gnu.org/mdk.git)
