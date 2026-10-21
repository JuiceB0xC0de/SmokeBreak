---
name: qbe
title: QBE
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, backend, compiler, intermediate-language, ssa]
homepage: https://c9x.me/compile/
scout_score: 6
status: draft
---

# QBE

**TLDR;** A hobby-scale compiler backend that turns a small SSA intermediate language into assembly, showing in a few thousand lines of C how real compilers lower code.

QBE is a compiler backend written in C. You give it code in its own intermediate language, a typed, SSA-based text format, and it emits assembly for amd64 (Linux and macOS), arm64, or riscv64. The homepage example is a short `.ssa` file that defines an add function, calls it, and calls `printf`. QBE turns that into `out.s`, and the system `cc` assembles and links it into an ordinary binary against the local libc.

The author's stated goal is to provide "70% of the performance of industrial optimizing compilers in 10% of the code." The size budget is deliberate. It keeps the project focused on the essentials and away from endless diminishing returns. The page says the codebase is "intended to remain hobby-scale and pleasant to hack on." Those performance figures are the author's framing and were not checked here.

Inside, the same IL is used at every stage. Front ends emit it, and the backend runs passes such as copy elimination, sparse conditional constant propagation, and dead instruction elimination, then register allocation. The page describes a split spiller and allocator working in SSA form, which it calls simpler and faster than graph coloring. It uses a linear allocator with hinting and a loop-aware spilling heuristic.

The idea underneath is that a new language does not need a huge toolchain. Write a front end that prints QBE IL, and you get native code and C interoperability. QBE implements the full C ABI, so your programs can call into C and be called from C. Reading the IL by hand is also a good way to see what a compiler does between source code and assembly.

## Install

```
brew install qbe
# the example also needs a system C compiler (cc) and libc to assemble and link the output
```

## Try this

```
qbe -o out.s file.ssa && cc out.s
```
Compiles a QBE IL file (for example the add and printf example from the homepage) to assembly, then assembles and links it into a runnable binary.

```
qbe --help
```
Prints the command-line options QBE accepts.

## What's unique

It is small on purpose, with a stated size budget, yet it implements the full C ABI. Its IL, optimizations, and register allocator can all be read in one compact codebase.

## Caveats

Only amd64, arm64, and riscv64 are targeted, and the homepage shows no release version or date, so the project's current activity is unknown.

## Links

- [QBE homepage](https://c9x.me/compile/)
