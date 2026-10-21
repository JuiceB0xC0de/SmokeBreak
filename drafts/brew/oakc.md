---
name: oakc
title: oakc
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, intermediate-representation, language, rust]
homepage: https://github.com/adam-mcdaniel/oakc
scout_score: 6
status: draft
---

# oakc

**TLDR;** Oak is a small Rust-flavoured language that compiles down to a 17-instruction intermediate representation, so porting it to a new target means implementing a handful of operations.

Oak (the repo is called oakc) has a high-level frontend with Rust-like syntax and a deliberately tiny backend. The `oak` compiler reads `.ok` source files, lowers them into an intermediate representation of just 17 instructions, and then assembles that IR for a target. The README lists C, Go, and TypeScript backends.

The design goal is stated plainly: "The goal of oak is to be as high level as possible in the frontend, but as small and low level as possible in the backend." The README also describes oak as a more robust, higher-level version of the author's earlier project, `free`.

The interesting part is the machine underneath. Every IR instruction works on a single memory tape of double-precision floats that serves as both stack and heap. Variables become fixed offsets from a per-function base pointer. Struct methods are flattened into plain functions that take a pointer to the struct. A backend implements the instructions through a `Target` trait in Rust. The README claims the C backend fits in under 100 lines and compares the instruction count to brainfuck: "That's on par with brainfuck!"

It is a good door into how compilers separate a friendly frontend from a minimal target, and why a small IR makes a language easy to carry to new places. The compiler also has a `doc` subcommand that generates documentation from `#[doc(...)]` attributes.

## Install

```
brew install oakc
# The README's own routes use the Rust toolchain: cargo install -f oakc
# Targeting a backend needs that toolchain separately: a C99 GCC, Go 1.14, or TypeScript 3.9. No accounts or hardware needed.
```

## Try this

```
oak --help
```
Lists the compiler's subcommands and options, including the documentation generator.

```
git clone https://github.com/adam-mcdaniel/oakc
```
Fetches the repository, which includes the examples directory used in the next step.

```
oak c examples/hello_world.ok -c
```
Compiles the hello world example through the C backend; the README shows the output as main.exe.

## What's unique

The whole backend contract is 17 instructions over one float tape, so adding a target is a small job rather than a project. Few languages put their portability argument that bluntly.

## Caveats

The README is the only source read, it gives no release dates or stability statement, and the portability and 100-line claims are the author's own; some of its compile-process examples are illustrative pseudocode.

## Links

- [Project homepage (GitHub)](https://github.com/adam-mcdaniel/oakc)
- [crates.io package](https://crates.io/crates/oakc)
- [Predecessor project 'free'](https://github.com/adam-mcdaniel/free)
