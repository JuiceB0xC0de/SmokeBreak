---
name: bsc
title: bsc
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, hardware, haskell, language, verilog]
homepage: https://github.com/B-Lang-org/bsc
scout_score: 7
status: draft
---

# bsc

**TLDR;** A compiler that turns Bluespec, a high-level hardware description language with a Haskell-style syntax, into plain Verilog, so you can design circuits as rules instead of wiring.

bsc is the Bluespec Compiler. It reads Bluespec source in one of two interchangeable syntaxes, a SystemVerilog-style one (BSV) or a Haskell-style one (BH, also called Bluespec Classic), and emits standard Verilog that any synthesis toolchain can take. The repository also ships a simulator called bluesim, a standard library, and bluetcl, a Tcl scripting shell.

The central idea is Guarded Atomic Actions. Instead of describing every signal and clock edge by hand, you write a module as a set of rules, each with a condition (the guard) and an action that happens atomically. You state the invariants of the design, and the compiler works out how to schedule the rules into hardware. The README describes Bluespec as a high-level language with a type system that can catch errors before synthesis.

It is not a toy. The README says the toolchain was developed by Bluespec Inc for almost 20 years and has been used in production designs such as the Flute, Piccolo, and Shakti processor cores. The compiler itself is written in Haskell, with some libraries in C and C++, and it uses an SMT solver (Yices by default, or STP) at runtime.

For a developer who has never touched hardware design, it is a view of chip design from the language-and-types side: rules, scheduling, and a compiler that does the hard part, rather than a pile of always blocks.

## Install

```
brew install bsc
# pulls in gmp, icarus-verilog and tcl-tk as dependencies; no hardware needed
```

## Try this

```
bsc -help
```
Lists the command-line options of the compiler, including flags for emitting Verilog or targeting bluesim.

```
bsc -help-hidden
```
Shows additional flags the README says are intended for developers of the compiler.

```
bluetcl --help
```
Shows how to use the Tcl scripting shell that ships with the toolchain.

## What's unique

One language with two interchangeable syntaxes, one Haskell-flavoured and one SystemVerilog-flavoured, where guarded atomic actions let the compiler choose the scheduling. The output is plain Verilog, so it fits into ordinary synthesis flows.

## Caveats

Homebrew installs it for you, but building from source is heavy (GHC 9.6.7, several Haskell libraries, optional LaTeX and SMT solver builds), and you will need the user guide or tutorials to write your first design.

## Links

- [GitHub repository (homepage)](https://github.com/B-Lang-org/bsc)
- [BSC User Guide (PDF, latest release)](https://github.com/B-Lang-org/bsc/releases/latest/download/bsc_user_guide.pdf)
- [BSVLang training and tutorials](https://github.com/BSVLang/Main)
