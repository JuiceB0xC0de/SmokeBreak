---
name: janet
title: Janet
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, bytecode-vm, embeddable, language, lisp, peg]
homepage: https://janet-lang.org
scout_score: 7
status: draft
---

# Janet

**TLDR;** A small Lisp-style scripting language with a bytecode VM, built-in PEG parsing, green threads and networking, all under 1MB and embeddable via two C files.

Janet is a dynamic language that mixes functional and imperative styles, with Lisp-style prefix syntax. It is mostly standard C99. You can type into its REPL or run a script with `janet myscript.janet`. Source is read, compiled to bytecode and run on a VM, and the compiler can also write an image file with `--compile`.

The homepage pitches it two ways: as a system scripting language, and as a language to embed in other programs. Embedding means adding `janet.c` and `janet.h` to a C project. Most embeddable languages ship lean and leave you to bolt on the rest. Janet instead includes threads, networking, an event loop, subprocess handling and Parsing Expression Grammars in the core. The homepage says the whole thing (core library, interpreter, compiler, assembler, PEG) is "less than 1MB".

The door it opens is how much language fits in a small, readable C codebase. PEGs are built into the core, so you can write real parsers as ordinary data structures in a few lines. The docs also describe first-class green threads and Erlang-style supervision trees. The companion build tool `jpm` can export a project as a standalone executable.

## Install

```
brew install janet
# the latest git version: brew install --HEAD janet
# jpm, the project manager, is a separate install: run `janet bootstrap.janet` from a cloned jpm repository
```

## Try this

```
janet
```
Starts the REPL. The homepage example types (+ 1 2 3) and gets 6 back.

```
(doc)
```
Typed inside the REPL, lists every macro, function and constant. (doc defn) shows a single docstring.

```
janet -h
```
Prints usage, including the -e, -c, -i, -k, -l and -b options.

## What's unique

It is a full language with an event loop, networking, PEG and Erlang-style supervision trees in under 1MB, and it embeds by dropping in two C files.

## Caveats

Homebrew's uninstall leaves files behind: you must manually delete $HOMEBREW_PREFIX/lib/janet, $HOMEBREW_PREFIX/bin/jpm and the jpm man page.

## Links

- [Janet homepage](https://janet-lang.org)
- [Janet documentation (installation and language guide)](https://janet-lang.org/docs/index.html)
- [Janet Zulip community](https://janet.zulipchat.com)
