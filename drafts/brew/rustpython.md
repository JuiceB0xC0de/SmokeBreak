---
name: rustpython
title: RustPython
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, interpreter, python, rust, wasi, webassembly]
homepage: https://rustpython.github.io
scout_score: 5
status: draft
---

# RustPython

**TLDR;** A Python 3 interpreter written from scratch in Rust, embeddable in Rust programs and compilable to WebAssembly to run Python in a browser.

RustPython runs Python source the way `python` does: a `-c` one-liner, a script, or an interactive `>>>` prompt. It is not a wrapper around CPython and has no CPython bindings. The whole interpreter is a fresh implementation in Rust, aiming for what the README calls a "clean implementation and no compatiblity hacks."

The idea is the one behind Jython and IronPython: put Python on top of another host runtime. The homepage says: "We want to unlock the same possibilities that Jython and IronPython enable, but for the Rust programming language." Rust's minimal runtime also makes WebAssembly builds practical, so the same interpreter can run in a browser tab, under a WASI runtime like Wasmer, or as a scripting engine inside a Rust program.

Under the hood, the standard library's Python files live in `Lib/` and are wired in by symlinks. For WASI builds the stdlib can be frozen into the binary. The README points to an architecture document for the component layout, which makes this a readable way to see how a Python interpreter is put together. There is also a very experimental JIT that compiles Python functions to native code.

## Install

```
brew install rustpython
# Alternative: cargo install --git https://github.com/RustPython/RustPython rustpython
# pip and HTTPS need a build with the ssl feature.
```

## Try this

```
rustpython --help
```
Lists the interpreter's command-line options.

```
rustpython -c 'print("Hello, RustPython!")'
```
Runs a one-line Python program on the Rust interpreter.

```
rustpython -m venv <your_env_name>
```
Creates a virtual environment, which the README says is the easiest route to using pip.

## What's unique

It is a full Python 3 interpreter in Rust rather than a binding to CPython, and it runs in a browser through WebAssembly. Ruff is cited as a downstream user.

## Caveats

The README says it is in development and "not totally production-ready"; docs are early-stage, the JIT is very experimental, and the homepage and README disagree on the target CPython version (3.11 vs 3.15).

## Links

- [Homepage](https://rustpython.github.io)
- [Online demo (WebAssembly)](https://rustpython.github.io/demo/)
- [User guide](https://rustpython.github.io/docs/)
- [GitHub repository](https://github.com/RustPython/RustPython)
