---
name: dwarfutils
title: dwarfutils
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, compilers, debug-info, dwarf, elf, reverse-engineering]
homepage: https://www.prevanders.net/dwarf.html
scout_score: 6
status: draft
---

# dwarfutils

**TLDR;** dwarfdump prints the DWARF debug information inside compiled object files, showing how a compiler describes your program's types, functions and line numbers.

dwarfdump is the command-line tool that ships with libdwarf, a C library for reading DWARF debugging data. Point it at an object file and it prints the DWARF in readable form. It covers DWARF2, DWARF3, DWARF4 and some DWARF5. The Homebrew formula is called dwarfutils and installs the `dwarfdump` executable.

DWARF is the format compilers use to tell debuggers what the machine code means: which source line produced which instruction, what a struct looks like, where a variable lives. Reading it directly is a way to see what a debugger sees, and to see what your compiler recorded about your code.

The code comes from SGI's IRIX developer tools. libdwarf was open-sourced in 1994 and dwarfdump in 1999. The README states the goal as portable, ABI-independent access to the data that detects corruption and avoids crashes or leaks however corrupted the input is. The project backs this with roughly twenty thousand regression checks, fuzzing, Coverity scans, and a public vulnerability list.

The formula description mentions producing DWARF, but the homepage says the old producer interfaces were removed. Treat this as a reader and dumper. Also note that libdwarf reads files on disk, not running programs or running shared objects.

## Install

```
brew install dwarfutils
```

## Try this

```
dwarfdump --help
```
Lists the options for choosing which DWARF sections and details to print.

## What's unique

It is the reference-style DWARF reader descended from SGI's IRIX toolchain, built to survive corrupted input, with a public record of its testing and vulnerabilities.

## Caveats

The README gives build instructions but no dwarfdump usage examples, so expect to learn the options from --help and the documentation.

## Links

- [Homepage](https://www.prevanders.net/dwarf.html)
- [GitHub repository (libdwarf-code)](https://github.com/davea42/libdwarf-code)
- [libdwarf API documentation](https://www.prevanders.net/libdwarfdoc/index.html)
- [libdwarf.pdf](https://www.prevanders.net/libdwarf.pdf)
