---
name: objconv
title: objconv
source: brew
category: take-things-apart
commitment: quick
tags: [disassembler, elf, mach-o, object-files, quick, reverse-engineering, x86]
homepage: https://www.agner.org/optimize/#objconv
scout_score: 6
status: draft
---

# objconv

**TLDR;** A small converter that turns x86 object files and libraries between ELF, PE/COFF, OMF and Mach-O, and also disassembles them.

objconv reads object files, executables and function libraries for 32-bit and 64-bit x86 and writes them back out in another format. The supported formats are COFF/PE, OMF, ELF and Mach-O, so a library built for one platform's toolchain can be reshaped for another's. It can also rename symbols inside an object file, build and modify function libraries, and dump the contents of object and executable files.

It comes from Agner Fog's software optimization resources, which also include his manuals, a vector class library and an assembly function library. The page gives no explicit motive, but the placement suggests it serves programmers and tool makers who ship or consume low-level code across operating systems.

The idea underneath is that an object file is just a container. Machine code, symbol tables and relocations are the same ideas on every platform, and each OS wraps them differently. Converting between wrappers shows what each format actually carries. The bundled disassembler covers SSE4, AVX, AVX2, AVX512, FMA3, FMA4, XOP and Knights Corner instructions, so you can read the code inside the container too.

## Install

```
brew install objconv
```

## Try this

```
objconv --help
```
Prints the tool's usage summary and the options it supports for converting, renaming symbols and dumping files.

## What's unique

It combines format conversion, symbol renaming, library building and a disassembler with wide x86 instruction-set coverage in one small GPL tool.

## Caveats

It covers only 32-bit and 64-bit x86, so ARM and other architectures are out of scope, and the homepage describes it in one short paragraph with no usage examples.

## Links

- [objconv on Agner Fog's optimization resources](https://www.agner.org/optimize/#objconv)
