---
name: io
title: Io
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, language, prototype-based, repl, smalltalk, webassembly]
homepage: http://iolanguage.com/
scout_score: 8
status: draft
---

# Io

**TLDR;** A small prototype-based language where everything is a message send and objects are made by cloning, in the Smalltalk and Self family.

Io is a dynamic, prototype-based programming language. The README places it alongside Smalltalk and Self and puts the whole model in one line: "Everything is a message send from one object to another." You type expressions into a REPL or run a script, and it prints values back, so `1 + 1` gives `==> 2` and `List clone append(30, 10, 5, 20) sort` gives `list(5, 10, 20, 30)`.

There are no classes. You make a new object by cloning an existing one, then add slots at runtime, as in `Contact := Object clone` followed by `Contact fullAddress := method(...)`. That is the idea underneath it: if objects, methods and data are all slots on cloned objects, a lot of what other languages treat as separate machinery falls away. It is a compact way to see a different model of programming.

The current master branch targets WebAssembly. It builds a single WASI binary, `io_static`, that runs under wasmtime, Node or browsers, and it ships with a browser REPL. A bidirectional bridge lets Io code call JavaScript functions and JavaScript call Io methods. The older native build, with its addon system, now lives on a separate branch.

## Install

```
brew install io
# The brew formula installs `io` and `io_static`. It may be the older native build rather than the WASI build the current README describes, so check which one you get.
# To build current master from source: git clone --recursive https://github.com/IoLanguage/io.git && cd io && make
# The source build needs wasi-sdk (default ~/wasi-sdk, override with WASI_SDK=/path) and wasmtime.
```

## Try this

```
wasmtime build/bin/io_static -e '"hello" println'
```
Runs a one-line Io expression under wasmtime, after building from source.

```
wasmtime build/bin/io_static
```
Starts the Io REPL, where you can try cloning objects and adding slots.

```
io --help
```
Shows the options of the installed executable.

## What's unique

Io pushes the prototype idea to its minimum: no classes, only messages and clones. Its current build targets WebAssembly with a JavaScript bridge and a browser REPL, an unusual home for a language like this.

## Caveats

The README describes two builds and the brew formula may point at the older native one; the current build needs wasi-sdk and wasmtime, has no native addon system, and I could not confirm how recently master changed.

## Links

- [Homepage](http://iolanguage.com/)
- [Repository](https://github.com/IoLanguage/io)
- [Guide](https://iolanguage.org/docs/Guide)
- [Wikipedia overview](https://en.wikipedia.org/wiki/Io_(programming_language))
