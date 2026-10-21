---
name: klee
title: KLEE
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, llvm, research, symbolic-execution, testing]
homepage: https://klee-se.org
scout_score: 7
status: draft
---

# KLEE

**TLDR;** KLEE runs programs with unknown inputs instead of fixed ones, then works out concrete inputs that reach each path through the code.

KLEE is a symbolic virtual machine built on the LLVM compiler infrastructure. It executes LLVM bitcode, but inputs can be marked as unknowns rather than fixed data. The homepage calls it "a dynamic symbolic execution engine built on top of the LLVM compiler infrastructure." The brew description adds that it finds inputs that drive programs down hidden paths. That matches the general idea of symbolic execution, though the pages read for this entry do not put it in those words.

It also ships a POSIX/Linux emulation layer, aimed at uClibc, so parts of the operating system environment can be symbolic too. Files, command-line arguments and environment variables can all be treated as unknowns. Replay tools can then take the computed inputs and run them on native programs, setting up files, pipes, environment variables and arguments.

The idea underneath is a different way of thinking about testing. Instead of asking what a program does on this input, you ask what inputs make it do each of the things it can do. The homepage cites the OSDI 2008 paper as the reference for what KLEE is and can do. The project still holds an international workshop, with a fifth one announced for October 2026 in Munich.

The formula installs nine executables: kleaver, klee, klee-exec-tree, klee-replay, klee-stats, klee-zesti, ktest-gen, ktest-randgen and ktest-tool. The pages read for this entry do not explain what each one does.

## Install

```
brew install klee
# KLEE works on LLVM bitcode, so you also need a compiler that emits it, such as clang. The Getting Started page also lists Docker, Snap, Nix and other routes.
```

## Try this

```
klee --help
```
Prints the options for the main engine, a first look at what can be tuned.

```
ktest-tool --help
```
Shows how to read the saved test-case files KLEE produces.

```
klee-replay --help
```
Shows how computed inputs can be replayed against a native program.

## What's unique

Beyond analysing bitcode, it models parts of the operating system as symbolic and replays the generated inputs on native binaries. KLEE Web also lets you try small examples in a browser first.

## Caveats

It works on LLVM bitcode, not arbitrary binaries, and the docs recommend building from source against LLVM 18, so setup may be fiddly; the brief found no command-line examples and no clear release status.

## Links

- [Homepage](https://klee-se.org)
- [GitHub repository](https://github.com/klee/klee)
- [Getting Started](https://klee.github.io/getting-started/)
