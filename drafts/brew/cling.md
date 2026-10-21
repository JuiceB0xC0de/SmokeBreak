---
name: cling
title: cling
source: brew
category: languages-and-oddities
commitment: quick
tags: [c++, clang, interpreter, jupyter, llvm, quick, repl]
homepage: https://root.cern/cling/
scout_score: 7
status: draft
---

# cling

**TLDR;** An interactive C++ interpreter from the ROOT project at CERN, built on Clang and LLVM, that lets you type C++ at a prompt and run it immediately.

Cling takes a language that normally means write, compile, link, run, and gives it a prompt. You type C++ at the command line, or pass it as arguments, and each piece is parsed by Clang, compiled just-in-time by LLVM, and executed inside the interpreter process. Compiler errors come back in Clang's own diagnostic style.

It began in the ROOT project as a replacement for CINT, the first C++ interpreter there. The homepage describes the goal as a contemporary, high-performance alternative, with backward compatibility with CINT as a major priority. The idea underneath is that a REPL for a compiled language does not need a separate toy implementation. If you embed the real compiler front end and a JIT, the interpreter accepts what the compiler accepts.

Beyond plain C++, there is a set of dot-prefixed metaprocessor commands. They load source files and libraries, add include paths, and show the abstract syntax tree after each processed entity. There is also a Jupyter kernel, so C++ can run in notebooks. On startup it pulls in several headers and its own runtime universe, so you begin with a minimal working environment.

## Install

```
brew install cling
# Jupyter support is a separate install: see tools/Jupyter in the repository README, and keep cling on PATH when jupyter starts.
```

## Try this

```
cling '#include <stdio.h>' 'printf("Hello World!\n");'
```
Runs the README's Hello World: the include and the printf are each compiled and executed on the spot, with no separate build step.

```
cling --help
```
Lists the command-line options.

```
.printAST
```
Typed at the cling prompt, turns on display of the abstract syntax tree after each entity you enter, so you can see how Clang reads your code.

## What's unique

It is a REPL built on the real Clang front end, so it accepts C++ and reports errors as the compiler does. The dot-commands and the CINT-compatibility goal set it apart from simpler C++ REPLs.

## Caveats

The README warns that "some of the resources are rather old and most of the stated limitations are outdated", and I could not confirm recent activity. It documents building Clang and LLVM from source since nightly binaries are unavailable, but the Homebrew formula spares you that.

## Links

- [Cling homepage](https://root.cern/cling/)
- [GitHub repository](https://github.com/root-project/cling)
- [CHEP 2012 paper (DOI)](https://doi.org/10.1088/1742-6596/396/5/052071)
