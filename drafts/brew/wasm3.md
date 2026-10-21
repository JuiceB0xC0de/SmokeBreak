---
name: wasm3
title: wasm3
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, embedded, interpreter, virtual-machine, webassembly]
homepage: https://twitter.com/wasm3_engine
scout_score: 6
status: draft
---

# wasm3

**TLDR;** A WebAssembly interpreter in C, small enough for microcontrollers, that runs portable bytecode directly instead of compiling it to native code.

Wasm3 takes a WebAssembly module and executes it directly, without generating machine code at runtime. It is written in C and also ships as a library, with bindings listed for Python, Rust, Go, Zig, .NET and Arduino. The README gives a minimum footprint of about 64 KB of code and 10 KB of RAM, and lists platforms from Linux and macOS to routers, single-board computers and microcontrollers.

The README calls it a research project. The question it asks is whether WebAssembly can be a portable, sandboxed alternative to Lua, JS, Python or Lisp on small devices, for things like plugin systems, edge computing and IoT rules. Its argument for an interpreter over a JIT is that size, memory, startup latency, portability and security often matter more than raw speed. A JIT also cannot run at all on some platforms, such as iOS or inside a browser.

The idea underneath is that bytecode is just a program for a small virtual machine, and this one is small enough to read. The architecture is described in docs/Interpreter.md. The feature list also includes gas metering, suspend and resume snapshots, a deterministic profile and structured execution tracing, which are unusual for an interpreter this size.

## Install

```
brew install wasm3
# Prebuilt static binaries are also on the GitHub releases page (on Linux, run chmod +x on the .elf file).
# You need a .wasm module to run; the Homebrew formula depends on uvwasi.
```

## Try this

```
wasm3 --help
```
Prints the interpreter's command-line options, which is the quickest way to see what it can do with a module.

```
pip3 install pywasm3
```
Installs the Python binding so you can load and call WebAssembly modules from a Python script.

```
chmod +x wasm3-linux-x64.elf
```
Makes the prebuilt Linux binary from the releases page executable, with nothing else to install.

## What's unique

One small C engine spans desktop binaries down to microcontrollers with a few KB of RAM, and still offers gas metering, snapshots and execution tracing.

## Caveats

The README says the project is in minimal maintenance with no new features planned, it is slower than JIT runtimes, and the listed homepage is a login-walled X profile rather than a project site.

## Links

- [Homepage (X profile)](https://twitter.com/wasm3_engine)
- [GitHub repository and README](https://github.com/wasm3/wasm3)
- [Installation instructions](https://github.com/wasm3/wasm3/blob/main/docs/Installation.md)
- [Interpreter architecture](https://github.com/wasm3/wasm3/blob/main/docs/Interpreter.md)
