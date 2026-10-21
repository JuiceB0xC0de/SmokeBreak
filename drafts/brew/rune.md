---
name: rune
title: Rune
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, async, embeddable, language, rust, scripting]
homepage: https://rune-rs.github.io
scout_score: 5
status: draft
---

# Rune

**TLDR;** Rune is a small dynamic scripting language written for embedding inside Rust programs, with async built in from the start.

Rune is a scripting language that lives inside Rust. You write scripts with functions, structs, enums, pattern matching, template literals and async code. Then you run them with the bundled `rune` command, or load them from a Rust program through the `rune` crate.

Under the hood, source text is compiled into a compact form and run on a stack-based virtual machine. The Rust host builds a context, loads sources, prepares a VM, and calls script functions by name, for example `vm.call(["add"], (10i64, 20i64))`. Results come back into Rust through `rune::from_value`. Memory safety comes from reference counting, and each call gets its own stack frame.

The idea underneath is the embedded scripting layer: a compiled host program that stays fast and typed, with a looser language on top that can change without a rebuild. Games, tools and servers have long used this split. Rune aims to offer it to Rust programs without leaving Rust.

The homepage puts async first: "Rune prioritized excellent support for async with support for async functions, closures, blocks, and generators." It also shows a native `select` expression that races futures, and a const-evaluation example that runs a loop at compile time.

## Install

```
brew install rune
# The README only documents building from source: cargo run --bin rune
# To embed it in a Rust program, add the `rune` crate (and `termcolor` for coloured diagnostics).
```

## Try this

```
rune --help
```
Lists the subcommands and options of the bundled command-line tool.

```
cargo run --bin rune -- run scripts/hello_world.rn
```
From a checkout of the repo, compiles and runs the hello world script.

```
cargo run --bin rune -- run scripts/hello_world.rn --dump --trace
```
Runs the same script and prints detailed diagnostics about the compiled program and its execution.

## What's unique

It is a scripting language designed around Rust hosts, with async functions, generators and a `select` expression for racing futures built into the language itself.

## Caveats

The fetched pages show no release date, platform list or stability statement, so how actively it is maintained and how production-ready it is are unconfirmed.

## Links

- [Homepage](https://rune-rs.github.io)
- [Book](https://rune-rs.github.io/book/)
- [GitHub repository](https://github.com/rune-rs/rune)
- [Rust docs (docs.rs)](https://docs.rs/rune)
