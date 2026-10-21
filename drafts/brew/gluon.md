---
name: gluon
title: Gluon
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, embeddable, functional, language, rust, type-inference]
homepage: https://gluon-lang.org
scout_score: 6
status: draft
---

# Gluon

**TLDR;** A small, statically typed, type-inferred functional language written in Rust, designed to be embedded in other programs the way Lua is.

Gluon is a functional language meant to live inside a host application. The README frames it as 'designed for application embedding' and 'similar to Lua': you include it in your program so users or developers can script behaviour. Its stated inspirations are Lua, Haskell and OCaml.

The twist is the type system. Gluon uses a Hindley-Milner based type system with some extensions, so types are rarely written out. In the project's words: 'Type inference ensures that types rarely have to be written explicitly giving all the benefits of static types with none of the typing.' Most embeddable languages are dynamically typed, which is what makes this one uncommon.

The library is split into a parser, a type checker, and a virtual machine plus compiler, and each can be used on its own. Rust functions can be passed straight into Gluon with little marshalling code, and each executing Gluon thread gets its own garbage-collected heap. The homepage example imports std.json, derives Serialize and Deserialize on a record, parses a JSON string, updates the record and prints it back as pretty JSON.

The REPL is the quickest way in. It can tell you the type of an expression, describe a name, load files and tab-complete identifiers. The examples include a parser-combinator library and a 24 game written in Gluon itself.

## Install

```
brew install gluon
# The README's own routes are prebuilt binaries from GitHub releases, or: cargo install gluon_repl (needs a recent Rust toolchain)
```

## Try this

```
gluon --help
```
Lists the options of the executable, including -i for interactive mode.

```
:t expression
```
Inside the REPL, shows the inferred type of any expression you type.

```
:i std.prelude.List
```
Inside the REPL, prints information about a name, here the List type from the standard prelude.

## What's unique

It pairs Hindley-Milner type inference with a Lua-style embedding goal, so a host Rust program gets a statically typed scripting language with little marshalling code.

## Caveats

Recent activity is unconfirmed, the C API is described as 'rudimentary', parallel execution 'may still have issues such as deadlocks', and the Brew-installed executable may differ from the README's gluon_repl.

## Links

- [Homepage](https://gluon-lang.org)
- [GitHub repository and README](https://github.com/gluon-lang/gluon)
- [The Gluon Book](https://gluon-lang.org/doc/crates_io/book/index.html)
