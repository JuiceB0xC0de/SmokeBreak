---
name: woxi
title: Woxi
source: brew
category: languages-and-oddities
commitment: quick
tags: [interpreter, jupyter, language, quick, repl, rust, wolfram]
homepage: https://github.com/ad-si/Woxi
scout_score: 6
status: draft
---

# Woxi

**TLDR;** A from-scratch Rust interpreter for a subset of the Wolfram Language, so you can run symbolic one-liners and scripts without a Wolfram kernel or license.

Woxi evaluates Wolfram Language source from the command line. You can pass a single expression to `woxi eval`, run a script file with `woxi run`, or open a REPL where definitions and `%` / `Out[]` history persist between inputs. It also provides a Jupyter kernel, an LSP server for editors, a WebAssembly build with npm and Python bindings, and a notebook editor called Woxi Studio.

It is an independent reimplementation, not a wrapper around Wolfram's kernel. The README says the aim is CLI scripting and notebooks, and it claims Woxi runs faster than WolframScript because "there is no overhead of starting a kernel and verifying its license."

The interesting idea is how it keeps itself honest. The CLI tests in `tests/cli` define the supported behaviour, and the README says "All tests must pass with Woxi and WolframScript." A `functions.csv` file tracks the implementation status of each function. The language server draws hover docs and completions from the same symbol registry as the interpreter, and it warns about symbols the interpreter does not implement.

The Wolfram Language treats everything as symbolic expressions that get rewritten by rules. A small open interpreter is a convenient way to see that model at work, and to find out which parts of it you can run outside the commercial system.

## Install

```
brew install woxi
# alternatives: cargo install woxi, pip install woxi, npm install woxi-wasm
# Jupyter use needs: woxi install-kernel
```

## Try this

```
woxi eval "1 + 2"
```
Evaluates one expression and prints 3.

```
woxi eval 'StringJoin["Hello", " ", "World!"]'
```
Calls a string function and prints Hello World!.

```
woxi repl
```
Opens an interactive session where definitions and output history persist across inputs.

## What's unique

It is an independent reimplementation of the Wolfram Language rather than a wrapper, tested against WolframScript for matching output. It also runs in many places: native CLI, WASM, Python, Jupyter, a browser demo, and an LSP server.

## Caveats

Only a subset of the Wolfram Language is implemented (functions.csv shows what), .nb notebook files cannot be run directly, and the brief could not confirm how recently the project has been updated.

## Links

- [Homepage (GitHub repository)](https://github.com/ad-si/Woxi)
- [Official documentation](https://woxi.ad-si.com/docs/)
- [JupyterLite demo (runs in browser)](https://woxi.ad-si.com/jupyterlite/lab/index.html?path=showcase.ipynb)
- [Function implementation status (functions.csv)](https://github.com/ad-si/Woxi/blob/main/functions.csv)
