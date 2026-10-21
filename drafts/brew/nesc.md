---
name: nesc
title: nesC
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, deprecated, embedded, language, quick, tinyos]
homepage: https://github.com/tinyos/nesc
scout_score: 6
status: draft
---

# nesC

**TLDR;** nesC is a C dialect that builds TinyOS's event-driven, component-wiring model into the language, for sensor nodes with a few hundred bytes of RAM.

nesC (pronounced "NES-see") is an extension to C. Its README says it is "designed to embody the structuring concepts and execution model of TinyOS". TinyOS is an event-driven operating system for sensor network nodes with very limited resources. The README's example is 8K bytes of program memory and 512 bytes of RAM.

Instead of leaving the structure of the system to convention, nesC puts it in the language. A program is built from components that are wired together, and the execution model is event-driven. The Homebrew description calls it a language for deeply networked systems, which is broader than the README's TinyOS framing. The README itself stays with TinyOS.

The install ships four executables: `nescc`, the compiler driver, plus `nescc-mig`, `nescc-ncg` and `nescc-wiring`. The README does not describe their inputs and outputs, and points to the `nescc` man page for usage. It is a small door into an older way of thinking about concurrency, where the compiler knows the whole shape of the program because the components are declared and wired explicitly.

## Install

```
brew install nesc

The formula is marked deprecated and pulls in emacs as a dependency. No hardware or account is needed to install it. Building from source needs automake, autoconf, gperf, bison and flex as well.
```

## Try this

```
man nescc
```
Opens the nescc man page, which the README names as the place to learn how to use the compiler.

```
nescc --help
```
Prints the compiler driver's usage summary.

## What's unique

It bakes TinyOS's event-driven, component-wiring model into a C extension, aimed at severely memory-constrained sensor nodes rather than general networked applications.

## Caveats

The upstream repository is archived and read-only, the README has no tutorial or examples, and building from source is picky about autoconf and emacs versions.

## Links

- [Homepage (GitHub repository)](https://github.com/tinyos/nesc)
- [Releases (shows archive banner and v1.3.6 notes)](https://github.com/tinyos/nesc/releases)
