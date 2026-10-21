---
name: swi-prolog
title: SWI-Prolog
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, language, logic-programming, prolog, repl]
homepage: https://www.swi-prolog.org/
scout_score: 6
status: draft
---

# SWI-Prolog

**TLDR;** A mature Prolog system where you state facts and rules, then ask questions at a `?-` prompt and let the engine search for answers.

SWI-Prolog is an open source implementation of Prolog, written in C and Prolog, with many extensions beyond the core language. You write facts and rules in a file, or type goals at the interactive top level, and the system works out which answers satisfy them. The prompt is `?-`.

The homepage says development has been driven by the needs of real-world applications since 1987, and pitches it as "Robust, mature, free. Prolog for the real world." The README lists uses such as business rule validation, natural language processing, software verification, network configuration, robotics, graph processing, machine learning and linked data (RDF).

The idea underneath is logic programming. Instead of writing the steps to compute a result, you describe relationships and let the engine search for solutions. That is a different way of thinking about programs, and it is the reason to poke at it on a break.

The system also has a built-in manual you can search from the prompt with `apropos` and `help`. A comprehensive build adds XPCE (a GUI toolkit that provides `swipl-win`), the PceEmacs editor, a source-level debugger and profiling tools. There is also a WASM build for browsers and Node, and a sandboxed online version called SWISH if you want to try it without installing anything.

## Install

```
brew install swi-prolog
# installs swipl, swipl-ld and swipl-win; no account or hardware needed
```

## Try this

```
swipl --help
```
Prints a summary of the most important command-line options.

```
swipl --version
```
Prints the version and architecture identifier, then exits.

```
swipl
```
Starts the interactive top level at the `?-` prompt. From there, `?- help(append/3).` shows the manual entry for a predicate and `?- apropos("query").` searches the manual.

## What's unique

It bundles a GUI toolkit (XPCE), an Emacs-style editor mode, a source-level debugger and a WASM build that can touch the browser DOM, which most Prolog systems do not. It is also long-running and widely used, with many libraries.

## Caveats

XPCE, swipl-win and PceEmacs need the comprehensive build, and the online SWISH version is sandboxed and lacks modules, threads and most interfaces.

## Links

- [Homepage](https://www.swi-prolog.org/)
- [Source repository (README)](https://github.com/SWI-Prolog/swipl-devel)
- [Command-line options (manual)](https://www.swi-prolog.org/pldoc/man?section=cmdline)
- [SWISH online version](https://swish.swi-prolog.org)
