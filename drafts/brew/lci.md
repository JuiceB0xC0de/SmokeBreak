---
name: lci
title: lci
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, functional, lambda-calculus, language, math]
homepage: https://www.chatzi.org/lci/
scout_score: 8
status: draft
---

# lci

**TLDR;** A command-line interpreter for the untyped lambda calculus, where integers, lists and operators are all built from nothing but functions.

LCI reads lambda terms, aliases and user-defined operators from a file or an interactive prompt, reduces them, and prints the result in readable form. Church numerals come back as plain numbers and lists as `[a,b,c]`, so you are not left squinting at nested lambdas.

The idea underneath is that the lambda calculus is a complete model of computation made from one thing: functions applied to functions. LCI does not add integers or lists as built-in primitives. A bundled `.lcirc` library defines them in pure lambda calculus. Integers use Church encoding by default, with Scott encoding available, and you can redefine the encoding or the operators to see how different choices change the system.

The homepage describes two evaluation strategies, call-by-name and call-by-value, which can coexist in one program. Recursion works by expanding self-referencing aliases while the program runs, or you can convert a recursive term into a non-recursive one with a fixed-point combinator. A `let x = M in N` form is parsed as `(\x.N) M`, and execution can be traced. An N-Queens example, `queens.lci`, is written in a Haskell-like style to show how far the bare calculus stretches.

The homepage also mentions running LCI in a browser through WebAssembly.

## Install

```
brew install lci
```

## Try this

```
lci --help
```
Prints the interpreter's usage and options, a starting point for running files or the interactive prompt.

## What's unique

Integers, lists and operators are not primitives. They are defined in pure lambda calculus in a library file you can edit, so the interpreter doubles as a lab for comparing encodings.

## Caveats

The homepage gives no release date or changelog, so how actively it is maintained is unknown, and its documentation was not checked.

## Links

- [LCI homepage](https://www.chatzi.org/lci/)
