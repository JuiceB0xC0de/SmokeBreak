---
name: umka-lang
title: Umka
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, embeddable, language, quick, scripting, static-typing]
homepage: https://github.com/vtereshkov/umka-lang
scout_score: 7
status: draft
---

# Umka

**TLDR;** A small statically typed scripting language with Go-like syntax, built to be embedded in C programs and run on a bytecode VM.

Umka compiles source to bytecode and runs it on a virtual machine with garbage collection. The interpreter is written in C99 and can be linked into a host application as a static or dynamic library with a simple C API. The host program loads Umka code and calls into it. The `umka` executable is the command-line front end to the same compiler and VM.

The README sets Umka against Go. Go is a compiled systems language with a complex runtime and large output binaries. Umka aims to be the small, easy-to-embed counterpart, with compile-time type checking instead of the usual dynamic typing of scripting languages. Its guiding principle is "Explicit is better than implicit."

The syntax is Go-flavoured but makes some unusual choices. Pointer dereference is Pascal-style `p^`, and `*` is repurposed as the export mark, as in Oberon. Declarations use a `:` separator, closures take explicit capture lists, and there is a ternary operator that Go leaves out. There is no separate slice type. Dynamic arrays are declared like Go's slices and initialized with `make()`. Multitasking uses fibers (lightweight threads) instead of goroutines and channels.

The README lists real projects built with it, including games, a finite element demo and a text editor port. The idea underneath is a scripting layer you can type-check, which is what makes it a way into language design and embedding.

## Install

```
brew install umka-lang
# No install needed to try it: the browser playground is at https://vtereshkov.github.io/umka-lang
# The C+Umka 3D example additionally needs raylib.
```

## Try this

```
umka --help
```
Prints the command-line usage, so you can see how to run a .um script, since the README shows no quick-start command.

## What's unique

It pairs Go-like syntax and static typing with a tiny C99 embeddable VM, and adds Oberon and Pascal quirks such as `p^` dereference and `*` as the export mark.

## Caveats

The README shows no quick-start command, so you will likely need the language docs to run a first script, and the benchmark chart comes from old hardware.

## Links

- [Homepage (GitHub repository)](https://github.com/vtereshkov/umka-lang)
- [Playground](https://vtereshkov.github.io/umka-lang)
- [Language documentation](https://github.com/vtereshkov/umka-lang/blob/master/doc/lang.md)
- [Embedding API](https://github.com/vtereshkov/umka-lang/blob/master/doc/api.md)
