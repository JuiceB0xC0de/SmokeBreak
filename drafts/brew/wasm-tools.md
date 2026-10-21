---
name: wasm-tools
title: wasm-tools
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary-formats, reverse-engineering, rust, wasm, webassembly]
homepage: https://github.com/bytecodealliance/wasm-tools
scout_score: 6
status: draft
---

# wasm-tools

**TLDR;** A single Rust binary that validates, prints, parses, mutates and generates WebAssembly, so you can read a .wasm file as text and rebuild it.

wasm-tools is the Bytecode Alliance's command-line toolkit for WebAssembly. Its subcommands take a binary `.wasm` file or a `.wat` text file and do one job each: validate it, print it as text, parse text back to binary, dump its sections, strip or demangle names, or build and inspect components and WIT interface files.

Each subcommand wraps a library in the same repository: wasmparser for validate, wat for parse, wasmprinter for print, wasm-smith for smith, wasm-mutate for mutate. The commands share conventions. They read stdin when no file is given, write to stdout unless you pass `-o`, and pipe into each other. A line like `wasm-tools demangle foo.wasm | wasm-tools strip | wasm-tools objdump` works as a small pipeline over a binary.

The idea underneath is that WebAssembly is a real, specified binary format with a readable text twin, and you can move between the two by hand. That makes the format easy to take apart. It also includes tools for test-case work: wasm-smith generates valid modules from a seed, wasm-mutate perturbs existing ones, and wasm-shrink reduces failing cases. The README says the repository "strives to implement any standardized proposal to WebAssembly", and a `--features` flag switches proposals on and off.

## Install

```
brew install wasm-tools
# alternatives: cargo install --locked wasm-tools (needs a Rust toolchain), or cargo binstall wasm-tools for precompiled binaries
```

## Try this

```
wasm-tools print foo.wasm -o foo.wat
```
Converts a binary module to WebAssembly text format and writes it to foo.wat, where you can read it.

```
wasm-tools parse foo.wat -o foo.wasm
```
Turns the text file back into a binary module.

```
wasm-tools mutate foo.wasm --seed 192 | wasm-tools validate
```
Produces a mutated module from a fixed seed and pipes it into validate to check that it is still valid.

## What's unique

One binary covers reading, writing, validating and fuzzing WebAssembly, and its subcommands pipe into one another. It also generates and mutates modules, not just inspects them.

## Caveats

Only the wasm-tools CLI and the wat crate are considered API-stable; the other crates are 0.X.Y and may break on each release, and `wasm-tools compose` is deprecated.

## Links

- [GitHub repository (homepage)](https://github.com/bytecodealliance/wasm-tools)
- [Precompiled release artifacts](https://github.com/bytecodealliance/wasm-tools/releases)
- [Online playground: parse (text to binary)](https://bytecodealliance.github.io/wasm-tools/parse)
