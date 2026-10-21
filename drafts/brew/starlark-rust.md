---
name: starlark-rust
title: starlark-rust
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, bazel, buck2, embeddable, language, rust, starlark]
homepage: https://github.com/facebook/starlark-rust
scout_score: 5
status: draft
---

# starlark-rust

**TLDR;** A Rust implementation of Starlark, the deterministic Python-like language behind Bazel and Buck2 builds, with a REPL, linter and language server.

Starlark is a small configuration language that looks like Python but is deliberately restricted. It is the language behind Bazel, Buck and Buck2. This project is a Rust implementation of it: an evaluator, a standard library, debugger support, a linter and an LSP server. Buck2 depends on this library.

The repo is split into crates. `starlark` is the main library, `starlark_syntax` holds the parser and AST, `starlark_derive` supplies proc macros, `starlark_map` provides memory-efficient maps and sets, `starlark_lsp` is the language server, and `starlark_bin` is the command-line binary. The project began in google/starlark-rust and moved to Meta at version 0.4.0. Java and Go implementations of Starlark also exist.

The idea underneath is the embeddable language: a host program exposes its own types and functions to a restricted, deterministic script language. The README says projects that embed Starlark are expected to write their own binary on top of the library. Frozen values are `Send` and `Sync` while non-frozen values are not, which is a Rust-shaped way to make that safe.

Used on its own, the REPL only knows standard Starlark. That makes it more a way to see how a build-config language is put together than a tool for daily work.

## Install

```
brew install starlark-rust
# The README gives no Homebrew steps. To run from source instead: install Rust with rustup, clone the repo, and run `cargo run`.
```

## Try this

```
starlark --help
```
Lists the options of the installed binary. The README does not say outright that this is the same program as its starlark_bin crate.

```
cargo run
```
From a clone of the repo, starts the Starlark interpreter at a prompt.

```
$> 1+2
```
Typed at the REPL prompt, evaluates the expression. The README shows the output as 3.

## What's unique

It is built as an embeddable language core rather than just an interpreter, shipping an LSP, a DAP debugger adapter, optional runtime-checked types and OSS-Fuzz fuzzing.

## Caveats

The README says it does not aim for API stability between releases, bytes are not yet supported, circular data structures may overflow the stack, and the bin is best treated as a test-bed.

## Links

- [GitHub repo (homepage)](https://github.com/facebook/starlark-rust)
- [crates.io: starlark](https://crates.io/crates/starlark)
- [docs.rs: starlark](https://docs.rs/starlark/)
- [Meta blog post on the library](https://developers.facebook.com/blog/post/2021/04/08/rust-starlark-library/)
