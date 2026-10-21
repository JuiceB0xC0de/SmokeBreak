---
name: cbmbasic
title: cbmbasic
source: brew
category: languages-and-oddities
commitment: quick
tags: [basic, commodore, language, quick, retro, scripting]
homepage: https://github.com/mist64/cbmbasic
scout_score: 8
status: draft
---

# cbmbasic

**TLDR;** Commodore 64 BASIC V2 reimplemented in native C, so you can type line numbers at a prompt or run BASIC files as Unix scripts.

cbmbasic is an interpreter for Commodore BASIC V2, the Microsoft-derived dialect that greeted every Commodore 64 owner. Start it with no arguments and you get the interactive prompt. Pass it a plain-text BASIC file and it runs the program. Put `#!/usr/bin/env cbmbasic` on the first line, set the executable bit, and the file runs like any other Unix script.

It does not emulate a 6502. The interpreter core in `cbmbasic.c` is native C, written to be independent of platform, endianness and bitness. The README says this makes it about 1000x the speed of a 1 MHz 6502 on a 1 GHz CPU, and calls it 100% compatible with the original.

The underlying idea is the boundary between a language and its machine. On the C64, BASIC talked to the outside world through KERNAL routines such as CHRIN and CHROUT. Here, all I/O goes through `runtime.c`, and anything the core cannot handle is routed through `kernal_dispatch()`, a switch statement that calls C functions standing in for those routines. Replace that one file and the same interpreter can live somewhere else entirely.

There is also an optional extension layer. `SYS 1` turns on a plugin system that adds statements like `LOCATE` and `SYSTEM`, and `SYS 0` turns it off. The extended `WAIT` implements a Bill Gates easter egg, which the README links to.

## Install

```
brew install cbmbasic
```

## Try this

```
cbmbasic
```
Starts the interactive Commodore BASIC V2 prompt, where you can type line-numbered programs.

```
cat hello.bas
```
Shows the README's example script: a `#!/usr/bin/env cbmbasic` line followed by `PRINT"HELLO WORLD!"`.

```
./hello.bas
```
With the executable bit set, runs the BASIC file directly as a Unix script and prints HELLO WORLD!.

## What's unique

Rather than emulating a 6502 and a ROM, it reimplements the BASIC interpreter in portable C and treats the KERNAL as a thin, swappable I/O layer. That is what lets a BASIC file serve as a shell script.

## Caveats

The codebase looks mid-2000s (the README lists Mac OS X 10.4/10.5, Debian Etch, GCC 3.3 to 4.1) and its maintenance status is unclear; runtime.c does not implement every KERNAL function, so LOAD, SAVE, OPEN and SETTIM may be incomplete.

## Links

- [GitHub repository (homepage)](https://github.com/mist64/cbmbasic)
- [Bill Gates easter egg reference (pagetable.com)](http://www.pagetable.com/?p=43)
