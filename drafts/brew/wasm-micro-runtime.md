---
name: wasm-micro-runtime
title: WAMR (WebAssembly Micro Runtime)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, embedded, jit, runtime, wasi, webassembly]
homepage: https://github.com/bytecodealliance/wasm-micro-runtime
scout_score: 5
status: draft
---

# WAMR (WebAssembly Micro Runtime)

**TLDR;** A small WebAssembly runtime that runs .wasm files outside the browser, with an interpreter, ahead-of-time compiler and JIT tiers to compare.

WebAssembly Micro Runtime, or WAMR, loads Wasm modules and runs them. Its command-line tool, iwasm, takes a .wasm file, or an AOT file made by the separate wamrc compiler, and runs it with WASI support. The core is also meant to be embedded as a C/C++ library, with Python, Go and Rust bindings.

The README describes it as a runtime for applications "from embedded, IoT, edge to Trusted Execution Environment (TEE), smart contract, cloud native and so on". Small footprint and high performance are the stated goals. It is not only for microcontrollers: it also covers Linux, macOS, Windows and Android.

The interesting part is that one project offers several ways to execute the same bytecode: a fast interpreter, a classic interpreter, AOT, LLVM JIT, Fast JIT, and a multi-tier mode. Multi-tier starts a module on Fast JIT immediately, compiles hot functions with LLVM on background threads, and switches over as they finish. Comparing these modes on one module is a hands-on way to learn the tradeoffs between interpreting, compiling ahead of time and compiling while running.

The README also gives size figures measured on a Cortex-M4F: about 21.4K for the WASI libc and 3.7K for the builtin libc. That shows how small a Wasm runtime can be made.

## Install

```
brew install wasm-micro-runtime
# installs iwasm and a versioned iwasm-2.4.5. The brief does not explain the versioned name, and the README documents building from source rather than brew.
# You need a .wasm file of your own to run. The default build has the interpreter, AOT and WASI but no JIT. wamrc must be built from source.
```

## Try this

```
iwasm --help
```
Lists the runtime's options so you can see what the command-line tool can do.

```
iwasm <wasm file>
```
Runs a WebAssembly module with the default fast interpreter.

```
wamrc -o <AOT file> <WASM file>
```
Compiles a Wasm file ahead of time into an AOT file; wamrc has to be built from the source tree first. Run the result with iwasm <AOT file>.

## What's unique

One runtime offers an interpreter, AOT and two JIT tiers, including a Fast JIT that hands off to LLVM JIT while the program runs. The README documents per-component sizes down to a few kilobytes.

## Caveats

Making full use of it means building from source (LLVM JIT needs a long LLVM build), and the brief shows no dated release signal, though the README suggests ongoing upkeep.

## Links

- [GitHub repository (homepage)](https://github.com/bytecodealliance/wasm-micro-runtime)
- [WAMR guide (GitBook)](https://wamr.gitbook.io/)
- [WAMR website](https://bytecodealliance.github.io/wamr.dev)
