---
name: retdec
title: RetDec
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binaries, decompiler, llvm, reverse-engineering]
homepage: https://github.com/avast/retdec
scout_score: 8
status: draft
---

# RetDec

**TLDR;** A decompiler from Avast that turns compiled executables for many architectures and file formats back into readable C, a hands-on way into reverse engineering.

RetDec takes an executable or raw machine code and produces high-level output: C, or a Python-like language. It reads ELF, PE, Mach-O, COFF, AR archives, Intel HEX and raw code, for x86, x86-64, ARM, ARM64, MIPS, PIC32 and PowerPC. Besides decompiling, it can detect compilers and packers, disassemble, and produce call and control-flow graphs and statistics.

The README describes it as a decompiler that is "not limited to any particular target architecture, operating system, or executable file format". It is built on LLVM, so one pipeline covers many binary types instead of one tool per platform. The project comes from Avast, and the README credits research funding from the Technology Agency of the Czech Republic.

The idea underneath is that a compiler throws information away, and decompiling is the work of guessing it back. The README mentions several of the steps: decoding instructions, stripping statically linked library code by signature, using DWARF and PDB debug info when present, reconstructing instruction idioms, and recovering C++ class hierarchies from RTTI and vtables. Optional UPX unpacking runs first. Reading its C output next to the original binary shows how much structure survives compilation and how much is inferred.

The brew formula also installs a set of helper tools: a file inspector (`retdec-fileinfo`), an unpacker, and utilities for building signature and YARA patterns. These are worth browsing once the main decompiler works.

## Install

```
brew install retdec
# An installed copy needs roughly 5 to 6 GB of disk. UPX and Graphviz are optional extras.
```

## Try this

```
retdec-decompiler --help
```
Lists the decompiler's options so you can see what it can be told to do.

```
retdec-fileinfo --help
```
Shows the options of the file inspector, which reports on a binary's format, compiler and packer.

```
$RETDEC_INSTALL_DIR/bin/retdec-decompiler test.exe
```
Decompiles the binary test.exe into C. The README's example uses this path after a manual install; with brew, run retdec-decompiler directly.

## What's unique

It handles many formats and architectures in one tool and outputs C rather than assembly-like pseudocode. It also rebuilds C++ class hierarchies from RTTI and vtables, and has separate plugins for IDA and radare2.

## Caveats

The project is in limited maintenance mode, so issues may wait a quarter and development is minimal. The install is large, and the README warns that nightly builds may regress.

## Links

- [Homepage / GitHub repository](https://github.com/avast/retdec)
- [Project site](https://retdec.com/)
- [Wiki (in progress)](https://github.com/avast/retdec/wiki)
