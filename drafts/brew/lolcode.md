---
name: lolcode
title: LOLCODE
source: brew
category: languages-and-oddities
commitment: quick
tags: [esoteric, interpreter, jit, language, quick]
homepage: http://www.lolcode.org/
scout_score: 8
status: draft
---

# LOLCODE

**TLDR;** An esoteric programming language written in lolspeak, with lci, a real interpreter that includes a bytecode VM, a JIT, and even a small language model library.

LOLCODE is a programming language whose syntax is internet lolspeak. The homepage's hello-world is `HAI 1.3`, `CAN HAS STDIO?`, `VISIBLE "HAI WORLD!!!1!"`, `KTHXBYE`. The joke is the vocabulary. The interpreter underneath, lci, is a C program that takes a .lol file and runs it.

The README describes lci as "designed to be correct, portable, fast, and precisely documented", and the engineering backs that up. Programs run in up to three stages: a tree-walking interpreter that defines the semantics, a register machine that compiles the parse tree to bytecode, and a JIT that emits AArch64 or x86-64 machine code. The JIT only takes a procedure when a dataflow pass proves every value in it is an integer or boolean. Otherwise it falls back a stage.

That makes it a small, readable tour of how language implementations are layered. Because LOLCODE is dynamically scoped, a whole-program analysis has to decide which names can safely become registers. The README's own benchmark, run by the author on an Apple M2 Max, shows fib(30) at about 5.4 ms on the JIT against about 1,682 ms in the tree-walker.

The standard libraries are loaded with `CAN HAS`. They cover file I/O (STDIO), TCP sockets (SOCKS), strings (STRING), random numbers (STDLIB), and BRAINZ, a character-level transformer language model that trains from inside LOLCODE.

## Install

```
brew install lolcode
# installs the `lci` interpreter
```

## Try this

```
lci --help
```
Shows the interpreter's usage and options.

```
CAN HAS STDIO?
```
Not a shell command: the LOLCODE line that loads the file I/O library, which the README's examples begin with. Put it in a .lol file between HAI and KTHXBYE.

## What's unique

A joke language with a serious, staged implementation: tree-walker, bytecode VM, and a conditional JIT. It also ships a transformer library written for it.

## Caveats

The homepage names v1.3 as current while README examples use HAI 1.4, and the JIT only runs on AArch64 and x86-64 for integer and boolean procedures.

## Links

- [Homepage](http://www.lolcode.org/)
- [lci GitHub repository (README)](https://github.com/justinmeza/lci)
- [lci v1.3 tag (spec implementation)](https://github.com/justinmeza/lci/tree/v1.3)
- [lollm (LOLCODE language model built on BRAINZ)](https://github.com/justinmeza/lollm)
