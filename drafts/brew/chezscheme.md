---
name: chezscheme
title: Chez Scheme
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, language, lisp, repl, scheme]
homepage: https://cisco.github.io/ChezScheme/
scout_score: 7
status: draft
---

# Chez Scheme

**TLDR;** A Scheme implementation that compiles everything, even what you type at the prompt, straight to optimized native machine code.

Chez Scheme is both a programming language and an implementation of it, with supporting tools and documentation. It is a superset of R6RS and includes first-class procedures, proper tail calls, continuations, records, libraries, exceptions, and hygienic macros. The homepage presents it as a full compiler, run-time system, and programming environment, not just an interpreter.

The unusual part is that the compiler lives inside the run-time system. In the project's words: "Although an interpreter is available, all code is compiled by default." Code loaded from a file or typed into the shell becomes machine code on the fly, so programs can generate and compile more programs while running. That dynamically compiled code is reclaimed by the generational garbage collector like any other allocation.

Files can be precompiled to stored binaries, and precompiled files are recompiled automatically when their dependencies change. The compiler optimizes across separately compiled library boundaries. Whole-program compilation can reduce a program and its libraries to a single binary.

The tools around it include a multi-line expression editor called expeditor and a source-level debugger. It also offers extensive C and foreign-language interop, multithreading on multiple cores, and non-blocking I/O. For a curious developer, it is a good place to see what a serious, compiled Lisp-family language looks like up close.

## Install

```
brew install chezscheme
# installs three executables: chez, petite, scheme-script
```

## Try this

```
chez --help
```
Lists the command-line options for the full Chez Scheme REPL, which has the compiler built in.

```
petite --help
```
Shows the options for Petite Chez Scheme, the variant that works as an interpreter-style REPL.

```
scheme-script --help
```
Shows how to run a Scheme file as a script.

## What's unique

Everything is compiled to native code by default, even expressions typed at the shell, and whole-program compilation can merge a program and its libraries into one binary.

## Caveats

I could not confirm a last-release date, though the homepage lists release notes through 10.4.0, and its community section still points to a freenode channel that may be out of date.

## Links

- [Chez Scheme project homepage](https://cisco.github.io/ChezScheme/)
- [The Chez Scheme User's Guide (html)](https://cisco.github.io/ChezScheme/csug/csug.html)
- [GitHub repository](https://github.com/cisco/ChezScheme)
