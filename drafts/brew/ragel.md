---
name: ragel
title: Ragel
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, code-generation, compilers, parsing, regex, state-machines]
homepage: https://www.colm.net/open-source/ragel/
scout_score: 6
status: draft
---

# Ragel

**TLDR;** Ragel compiles regex-like machine descriptions with embedded code actions into dependency-free C, C++ or assembly state machines, a hands-on way to see how parsers work.

Ragel is a state machine compiler. You write a machine description that mixes regular-expression operators (union, concatenation, Kleene star) with embedded actions, which are small blocks of host-language code attached to points in the machine. Ragel turns that into C, C++, or x86_64 GNU assembly that runs the machine with no runtime dependencies. It can also draw the machine with Graphviz.

The idea underneath is that a regular expression is a deterministic finite automaton in disguise. Ragel compiles your expressions to a DFA and attaches your actions to its transitions, so your code runs at exact points during recognition rather than after a match is complete. The generated code can be table-driven or built from gotos, and the machine can be minimized with Hopcroft's algorithm.

The homepage positions it for protocol implementations, data format parsing, lexical analysis of programming languages, and input validation. It also has operators for controlling non-determinism, building scanners, and statechart-style machines, plus jumping or calling into other parts of a machine from inside an action.

In the project's words: "Ragel compiles executable finite state machines from regular languages." Reading the goto-based output for a small number grammar is a direct look at what a parser actually is once the notation is gone.

## Install

```
brew install ragel
# Homebrew installs a packaged release. The upstream project builds Ragel 7 from the Colm Suite with autogen.sh, configure, make, and make install. No accounts or hardware needed beyond a build toolchain.
```

## Try this

```
ragel --help
```
Lists the options, including the choices of output language and code generation style.

## What's unique

Ragel embeds actions at arbitrary points in a regular language without breaking its syntax, and the generated code has no dependencies and no license requirement on its output. Its Graphviz visualization and statechart support set it apart from simpler regex engines.

## Caveats

Generated assembly targets only GNU, x86_64, System V ABI, and Ragel 6 (GPL v2) and Ragel 7 (MIT) carry different licenses.

## Links

- [Ragel homepage](https://www.colm.net/open-source/ragel/)
- [Colm Suite repository (GitHub)](https://github.com/adrian-thurston/colm-suite)
