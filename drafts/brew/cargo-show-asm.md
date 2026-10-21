---
name: cargo-show-asm
title: cargo-show-asm
source: brew
category: take-things-apart
commitment: quick
tags: [assembly, cargo, compiler, llvm, quick, rust]
homepage: https://github.com/pacak/cargo-show-asm
scout_score: 5
status: draft
---

# cargo-show-asm

**TLDR;** A Cargo subcommand that prints the assembly, LLVM-IR, MIR or WASM rustc produces for a single Rust function, so you can see what the compiler did.

cargo-show-asm adds a `cargo asm` command to Cargo (the binary is `cargo-asm`). Point it at a crate target, such as a lib, bin, example, test or bench, and it has rustc build an assembly file, then lists the functions it finds with their line counts. Give it a full name, a unique partial name or an index from the list, and it prints that one function's code.

The idea underneath is that reading source only tells you what you asked for, while the compiler's output tells you what you got. Output can be Intel or AT&T assembly, with Rust source interleaved if you want it. It can also show LLVM-IR, MIR, WASM, or llvm-mca analysis, so one function can be followed through several stages of compilation.

A few options turn it into an exploration tool. `--context N` pulls in the bodies of called functions recursively, and `--callers-of` takes a regex and filters functions by their call graph. For example, you can list every function that reaches `panic`.

There is a catch that teaches something itself. As the README puts it, `rustc` only generates code for your function "if it knows what type it is, including generic parameters and if it is exported (in case of a library) and not inlined". A function that vanishes from the listing is usually generic or inlined, and `#[inline(never)]` is the suggested fix.

## Install

```
brew install cargo-show-asm
# or: cargo install cargo-show-asm
# Needs a Rust project to inspect. --wasm needs the wasm32-unknown-unknown target installed; --file needs a build with the disasm feature.
```

## Try this

```
cargo asm
```
Run inside a Rust project with no parameters; it suggests how to narrow the search scope.

```
cargo asm --lib Debug
```
Lists only functions in the lib target whose names match the partial string Debug.

```
cargo asm --lib --callers-of panic
```
Lists functions that call something matching panic, which is a quick way to find code that can panic.

## What's unique

It works per function and can filter by call graph, for instance every function that can reach panic. It also covers asm, LLVM-IR, MIR, WASM and llvm-mca in one tool, where alternatives tend to cover only one.

## Caveats

Linux and macOS are supported, Windows only in a limited way; the default build is --release, and the brief could not confirm a recent release date or maintenance status.

## Links

- [Homepage / GitHub repository](https://github.com/pacak/cargo-show-asm)
- [Issue 247: context option discussion](https://github.com/pacak/cargo-show-asm/issues/247)
- [rust-lang PR 116505: inlining and codegen behaviour](https://github.com/rust-lang/rust/pull/116505)
