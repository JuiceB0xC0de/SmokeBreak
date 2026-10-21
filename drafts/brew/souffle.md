---
name: souffle
title: Soufflé
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, datalog, declarative, logic-programming, static-analysis]
homepage: https://souffle-lang.github.io
scout_score: 5
status: draft
---

# Soufflé

**TLDR;** Soufflé is a Datalog-style logic language that compiles analysis rules into parallel C++, built for questions like points-to and taint analysis over large programs.

Soufflé is a language and tool for static analysis. You write rules as logic: facts go in, relations are derived from them, and the tool works out how to compute the answer. The README describes the language as "similar to Datalog (but has terms known as records)", and says it is frequently used as a domain-specific language for analysis problems.

The tool can run a program through an interpreter or compile it into parallel C++. The homepage credits Futamura projections and partial evaluation for the compile step, with specialized data structures for relations. The README adds de-specialization for efficient interpretation and optimal index selection. It also lists an extended I/O system for relations, including SQLite3 interfaces, plus C++ and SWIG interfaces for embedding. Provenance, debugging and profiling tools are described as built in.

The idea underneath is that many analysis problems, such as which pointers can reach which objects or where tainted data can flow, are recursive queries over relations. If you state the rules and leave out the evaluation strategy, you can try design variations quickly. The README pitches it as "rapid-prototyping for your analysis problems with logic", yet it is meant to scale to large programs, such as Java points-to analysis.

The language extends classic Datalog, for example with unbounded recursion over numbers and terms, so it is not pure Datalog.

## Install

```
brew install souffle
# The README does not mention macOS or Homebrew; it points to packaged releases for Ubuntu, Fedora and Oracle Linux, or a source build (git clone https://github.com/souffle-lang/souffle.git, then follow souffle-lang.github.io/build).
```

## Try this

```
souffle --help
```
Lists the command-line options, including how to run a program in the interpreter or compile it.

```
souffleprof --help
```
Shows the options for the profiler that ships with Soufflé.

## What's unique

Soufflé both interprets Datalog-style programs and compiles them to parallel C++ through partial evaluation, rather than being only an interpreter or a query engine.

## Caveats

The brief could not confirm current maintenance or build complexity, and code written for older versions may need the --legacy flag or a legacy pragma.

## Links

- [Homepage](https://souffle-lang.github.io)
- [Documentation](https://souffle-lang.github.io/docs.html)
- [GitHub repository](https://github.com/souffle-lang/souffle)
- [Publications](https://souffle-lang.github.io/publications)
