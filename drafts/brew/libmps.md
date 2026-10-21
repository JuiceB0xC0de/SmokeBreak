---
name: libmps
title: libmps (Memory Pool System)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, c, garbage-collection, library, memory-management]
homepage: https://www.ravenbrook.com/project/mps/
scout_score: 5
status: draft
---

# libmps (Memory Pool System)

**TLDR;** A C memory management library, in development since 1994, that lets you mix manual allocation and incremental generational garbage collection through swappable pool classes.

The Memory Pool System (MPS) is a C library from Ravenbrook Limited. It ships as the MPS Kit: source, a manual, and design documentation. You compile one file, mps.c, into an object file and link it into your own program, which then requests memory through the MPS allocation interfaces. The brew package installs no executables, so this is a library for people writing runtimes, not a command-line tool.

The central idea is that memory management is a set of policies rather than one allocator. The MPS provides pool classes, each implementing a different policy, and you combine them within one program. Manual and automatic management live in the same framework. The README lists in-line allocation, finalization, weakness, and multiple concurrent cooperating incremental generational garbage collections.

The project was started in 1994 and has been in commercial products since 1997. In its own words: "Bugs are almost unknown in production." That is the authors' claim, not something verified here. It is old, and the age is part of the appeal: the design documents and manual record decades of thinking about how collectors and allocators fit together.

The README's worked example is a Scheme interpreter in the example/scheme directory. That is a good place to see what it looks like to build a language runtime on top of a collector you did not write. The README calls reading the manual essential before programming against the MPS.

## Install

```
brew install libmps
# Installs a library only, no executables. The MPS Kit is source-only and must be built: cd code, then compile mps.c. See manual/build.txt in the repository for configuration, tests and the manual. Needs a C compiler (Xcode command line tools on macOS).
```

## Try this

```
cd code
```
Moves into the code directory of the MPS Kit, where the library source lives.

```
cc -O2 -c mps.c
```
Compiles the whole library into one object file (Unix or macOS) that you link into your own program.

```
cl /O2 /c mps.c
```
The same single-file compile on Windows with the Microsoft compiler.

## What's unique

It is a framework for memory management policies, not a single allocator or collector. You pick and combine manual and automatic pools, including incremental generational collection, in one program.

## Caveats

Source-only with a build step, and the listed platforms are narrow (macOS x86-64 only, no ARM listed); the homepage returned 503 when checked, and the repository was not checked for recent commits.

## Links

- [Project homepage (returned 503 when checked)](https://www.ravenbrook.com/project/mps/)
- [Manual (Read the Docs)](https://memory-pool-system.readthedocs.io/)
- [GitHub repository](https://github.com/Ravenbrook/mps)
