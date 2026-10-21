---
name: inko
title: Inko
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [actors, afternoon, concurrency, language, llvm, ownership]
homepage: https://inko-lang.org/
scout_score: 6
status: draft
---

# Inko

**TLDR;** A statically typed language that compiles to native code, with Erlang-style lightweight processes and Rust-style ownership but no garbage collector.

Inko is an object-oriented language for concurrent software. Source files ending in .inko are compiled to native machine code through LLVM and linked against a small runtime written in Rust. That runtime handles process scheduling and non-blocking IO, so the program itself does not manage threads.

The homepage says it exists to make concurrent software easy to build "without having to worry about unpredictable performance, unexpected runtime errors, data races, and type errors." The README positions it as an alternative to Ruby, Erlang, and Go. It says it does not aim to compete with C and Rust on performance.

The idea underneath is single ownership. Values start out owned and are dropped when they go out of scope, with no garbage collector. They can be moved, or borrowed with `ref` (read-only) or `mut` (mutable), and the compiler checks every use. Concurrency uses lightweight isolated processes, declared as `async` types, that talk by sending messages. The compiler requires data sent between processes to be unique (`uni`), so it is moved rather than deep-copied. The project describes this as inspired by Erlang and Pony.

Errors are handled with Result values and `try` and `throw`, rather than hidden exceptions. Together this makes Inko a compact way to see how ownership and message passing fit into one design.

## Install

```
brew install inko
# Brew pulls in llvm as a dependency. The README gives no install steps and points to the manual's installation guide, which I did not confirm.
```

## Try this

```
inko --help
```
Lists the subcommands and options of the inko executable, the place to start since the brief shows no other commands.

## What's unique

It combines ownership with move semantics and borrowing, Erlang-style isolated processes, and no garbage collector, in a language aimed at Ruby and Go users rather than systems programmers.

## Caveats

The README shows no version or release date, so the language may still change, and some homepage snippets deliberately contain errors and will not run as written.

## Links

- [Inko homepage](https://inko-lang.org/)
- [Inko manual](https://docs.inko-lang.org/manual/main)
- [GitHub repository](https://github.com/inko-lang/inko)
