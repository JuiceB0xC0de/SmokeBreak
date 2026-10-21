---
name: trealla-prolog
title: Trealla Prolog
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, constraints, embeddable, interpreter, logic-programming, prolog]
homepage: https://github.com/trealla-prolog/trealla-prolog
scout_score: 7
status: draft
---

# Trealla Prolog

**TLDR;** A compact ISO Prolog interpreter in plain C that gives you logic programming, tabling and constraint solving from one small tpl binary.

Trealla Prolog is an ISO Prolog interpreter written in C99 and built with a plain Makefile. You run `tpl` with source files or a goal, or start it with no goal and get a REPL with history. Prolog programs state facts and rules, then you ask questions and the engine searches for answers by backtracking.

The README describes it as a compact, efficient interpreter that runs on very many platforms, including bare boards and bare metal. The feature list is long for something small: unbounded integers and rationals, UTF-8 atoms and strings, DCGs, freeze/dif/when, CLP(B) and CLP(Z) constraint solvers, threads, engines, actors, sockets, and SQLite through an FFI-backed module. It can also be embedded in C programs, built to WebAssembly, and used from Jupyter.

The idea underneath is declarative programming. Tabling memoizes each call variant, so left-recursive predicates that would loop forever in plain Prolog terminate. Tables can be declared incremental or mode-directed (min/max). Double-quoted text is a packed UTF-8 byte array that behaves like a char list, and a file opened with mmap can be read as a Prolog string. This gives you a small, readable system for exploring how logic languages work.

## Install

```
brew install trealla-prolog
# Apple Silicon and Linux get prebuilt bottles; an Intel Mac builds from source.
# Depends on openssl; building by hand needs a C99 compiler and make.
```

## Try this

```
tpl --help
```
Prints the usage line and options such as -g goal, -l file, -t trace and -q quiet.

```
tpl
```
Starts the REPL with history, where you can consult files and type queries.

```
tpl -g test2,halt samples/sieve
```
Runs the goal test2 from the sieve sample in the source repository, then exits. You need a clone of the repository for the samples.

## What's unique

One small C binary covers tabling, delimited continuations, engines, actors and constraint solving. It also has a freestanding profile that boots on a Raspberry Pi 4 and an Arduino Nano ESP32 with no operating system.

## Caveats

Unbounded integers work for arithmetic only, rational trees, some FFIs and the Python bridge are marked experimental, and the Raspberry Pi bare-metal port is only a proof of concept.

## Links

- [Homepage / README (GitHub)](https://github.com/trealla-prolog/trealla-prolog)
- [Source repository for the interpreter](https://github.com/trealla-prolog/trealla)
- [Jupyter kernel for Logtalk (runs with Trealla)](https://github.com/LogtalkDotOrg/logtalk-jupyter-kernel#readme)
