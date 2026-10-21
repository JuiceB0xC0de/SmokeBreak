---
name: lightning
title: GNU lightning
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, assembly, compilers, gnu, jit, library]
homepage: https://www.gnu.org/software/lightning/
scout_score: 6
status: draft
---

# GNU lightning

**TLDR;** A GNU library that emits native machine code at run-time from one RISC-style instruction set, so a JIT does not need a code generator per CPU.

GNU lightning is a library, not a command. A program calls it to write instructions into memory while running, and the library turns them into native code for the CPU it was built for. The caller writes against one standardized RISC instruction set, which the homepage says is "inspired by the MIPS and SPARC chips."

The reason for it, per the project page, is speed and portability. The library is described as "very fast, making it ideal for Just-In-Time compilers," and it spares clients from writing a separate code generator for each architecture. The homepage lists backends for aarch64, alpha, arm, hppa, ia64, loongarch, mips, powerpc, risc-v, s390, sparc and x86.

The idea underneath is how a JIT actually works: choose a simple intermediate instruction set, then map it onto each real processor. Lightning is a code generation layer rather than a compiler, so the rest is left to the caller. That makes it a small way to see how machine code gets emitted across many CPU families.

The homepage is thin. It gives no API details, examples or commands, so expect to read the documentation and source to learn how it is used.

## Install

```
brew install lightning
# This installs a library only: no executables. You will need a C compiler and your own program to call it. The homepage gives no build steps; releases are on ftp.gnu.org and the source is on git.savannah.gnu.org.
```

## Try this

## What's unique

It is a plain code generation library with a fixed RISC-style instruction set, and the caller handles everything else. Its backend list is long for a project this small.

## Caveats

The homepage has no README, examples or commands, and its activity level could not be confirmed, so you will be reading docs and source to get started.

## Links

- [GNU lightning homepage](https://www.gnu.org/software/lightning/)
- [Git repository (Savannah)](git.savannah.gnu.org)
- [Releases (GNU FTP)](ftp.gnu.org)
