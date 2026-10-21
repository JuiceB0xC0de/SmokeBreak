---
name: wabt
title: wabt
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary-format, compiler-toolchain, disassembler, reverse-engineering, webassembly]
homepage: https://github.com/WebAssembly/wabt
scout_score: 6
status: draft
---

# wabt

**TLDR;** A suite of command-line tools that turns WebAssembly binaries into readable text and back, with byte-exact round-trips, so you can see what a .wasm file contains.

WABT (pronounced "wabbit") is a set of separate executables built from one C/C++ codebase. `wat2wasm` assembles WebAssembly's text format into a binary, and `wasm2wat` goes the other way. `wasm-objdump` and `wasm-stats` inspect a binary, `wasm-validate` checks it, `wasm-strip` removes sections, and `wasm-interp` runs it. `wasm2c` converts a binary to C source, and `wast2json` converts spec test files to JSON.

The project says its tools are "intended for use in (or for development of) toolchains or other systems that want to manipulate WebAssembly files." That is the practical reason it exists, but it also works as a way to look inside WebAssembly. WebAssembly is a compact stack-machine binary format, and `wat2wasm` with `-v` prints the meaning of every byte as it writes the file. Writing a few lines of text, assembling them, and reading the bytes shows how the format is laid out.

The design goal is fidelity rather than cleverness. The README says: "Unlike Binaryen these tools do not aim to provide an optimization platform or a higher-level compiler target; instead they aim for full fidelity and compliance with the spec (e.g. 1:1 round-trips with no changes to instructions)." So a binary converted to text and back should keep its instructions intact, which makes the output trustworthy for inspection.

The project has also been compiled to JavaScript with emscripten to power online demos, so you can try some of the conversions in a browser first.

## Install

```
brew install wabt
# Linux (apt): sudo apt install wabt
# Prebuilt binaries are also on the GitHub releases page.
```

## Try this

```
wat2wasm test.wat
```
Parses the text file test.wat and writes a binary test.wasm next to it.

```
wat2wasm spec-test.wast -v
```
Parses a spec-test file and prints verbose output, including the meaning of every byte.

```
wasm2wat test.wasm -o test.wat
```
Reads the binary and writes its text form to test.wat.

## What's unique

It aims for spec fidelity and instruction-preserving round-trips rather than optimization, which separates it from Binaryen. A proposal table lists which WebAssembly features each tool supports.

## Caveats

Several proposals, including threads, are not on by default, and some are not supported by every tool; if you build from source, the top-level Makefile may fail on macOS, so use CMake directly.

## Links

- [GitHub repository (homepage)](https://github.com/WebAssembly/wabt)
- [Online demos index](https://webassembly.github.io/wabt/demo/)
- [wasm-objdump man page](https://webassembly.github.io/wabt/doc/wasm-objdump.1.html)
