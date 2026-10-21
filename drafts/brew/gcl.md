---
name: gcl
title: GCL (GNU Common Lisp)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, common-lisp, compiler, gnu, lisp, repl]
homepage: https://www.gnu.org/software/gcl/
scout_score: 5
status: draft
---

# GCL (GNU Common Lisp)

**TLDR;** GCL is the GNU project's Common Lisp, which turns Lisp into native code by handing it to your C compiler.

GNU Common Lisp is a free implementation of Common Lisp. You can type code at its REPL or feed it source files, and it compiles them to native object code by calling the system's C compiler. It can also save a custom Lisp image of your session with save-system.

It began as AKCL and was released as GCL in 1994. The homepage says it exists mainly to support free software built in Lisp, and names Maxima, ACL2 and Axiom. Maxima, a computer algebra system, was the original driver. Running GCL means touching the Lisp layer under those mathematics tools.

The design leans on existing tools instead of building a code generator of its own. The README credits the C compiler for good performance and easy portability. On most platforms it can load native object code modules straight into the running Lisp core, and those modules persist in saved images. Memory is managed by a stratified garbage collector that uses native page fault handling for recent allocations. The homepage claims a function call costs the same as a C function call through a pointer.

There is also a source-level debugger, dbl, for interpreted code, which works with an Emacs window. Some of the project's wording is old, from the era of the first Common Lisp standard, CLtL1. The homepage says ANSI compliance is a goal and can be enabled at compile time.

## Install

```
brew install gcl
# The formula pulls in gmp and libtirpc. The brief lists no executables for the brew package, so check what lands on your PATH after installing.
```

## Try this

## What's unique

Instead of a bespoke native code generator, GCL compiles Lisp through the host C compiler and uses a page-fault-based garbage collector. It is the GNU project's official Common Lisp and the long-time engine behind Maxima.

## Caveats

The brief lists no executables for the brew formula, so I cannot say what command starts it. The upstream 2.7.1 tarball needs manual errata patches before building, and ANSI compliance is still described as a goal.

## Links

- [GCL homepage](https://www.gnu.org/software/gcl/)
- [Git repository (from README)](git://git.sv.gnu.org/gcl.git)
