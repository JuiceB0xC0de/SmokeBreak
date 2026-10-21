---
name: quickjs
title: QuickJS
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, compiler, embeddable, interpreter, javascript, quick]
homepage: https://bellard.org/quickjs/
scout_score: 6
status: draft
---

# QuickJS

**TLDR;** A complete JavaScript engine in a few C files, small enough to embed anywhere, that can also compile scripts into standalone executables.

QuickJS is a JavaScript engine written in C by Fabrice Bellard, with copyright shared with Charlie Gordon. It targets the ES2025 specification. The `qjs` command runs JavaScript through an interpreter, and `qjsc` compiles a script into a standalone executable with no external dependencies.

It exists for places where a full JavaScript runtime is too heavy. The homepage pitches it as small and easily embeddable, with very low startup time. It cites 367 KiB of x86 code for a hello world program and a full runtime lifecycle under 300 microseconds. Those figures are the author's own.

The interesting idea is how little a spec-complete language implementation needs. Memory is managed by reference counting with cycle removal, which the author says keeps memory use down and makes behavior deterministic. The interpreter's contextual colorization is written in JavaScript. The regex, Unicode and dtoa pieces (libregexp, libunicode, dtoa) are separate C libraries that can be reused on their own. The author also reports that the TypeScript and Babel compilers have been built to run on it.

It is a good project to read as well as run. The engine is compact enough that you can plausibly follow how a modern JavaScript implementation fits together.

## Install

```
brew install quickjs
```

## Try this

```
qjs --help
```
Lists the interpreter's options, including how to run a script, evaluate an expression, or start the interactive REPL.

```
qjsc --help
```
Shows how to compile a JavaScript file into a standalone executable or C output.

## What's unique

It is a nearly complete modern JavaScript engine that stays tiny, and it can turn scripts into self-contained binaries. Its regex, Unicode and number-formatting libraries can be lifted out and reused separately.

## Caveats

The 2025-04-26 release removed the bignum extensions and the qjscalc app, and the speed and conformance figures are the author's own claims.

## Links

- [QuickJS homepage](https://bellard.org/quickjs/)
