---
name: rizin
title: Rizin
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, binary-analysis, disassembler, reverse-engineering, tui]
homepage: https://rizin.re
scout_score: 8
status: draft
---

# Rizin

**TLDR;** A Unix-style reverse engineering toolkit: open a binary, firmware image or running program and read its disassembly from an interactive shell.

Rizin is a command-line reverse engineering framework. Point `rizin` at a binary, a firmware image or a disk file and it drops you into an interactive shell with a prompt like `[0x00000000]>`. From there you can disassemble code, analyse functions, debug, or use it as a scriptable hex editor. The same backend is also split into single-purpose tools: `rz-bin` for binary info, `rz-asm` for assembling and disassembling, `rz-hash` for hashing, `rz-diff` for comparing, and others.

It began as a fork of radare2, "with a focus on usability, features and cleanliness." The homepage describes a Unix-friendly approach: a shell-like environment "without unnecessary weight" that GUIs and scripts can build on. The Cutter GUI sits on the same backend. The shell was rebuilt on Tree-sitter for parsing, with commands registered in YAML files that also drive the help text.

The idea underneath is that a compiled program is just data you can query. When a binary is stripped of names, Rizin can match unnamed functions against FLIRT signatures from sigdb, so common library code gets labelled automatically. Scripting goes through rzpipe, which the README says supports Python, Haskell, OCaml, Ruby, Rust and Go.

## Install

```
brew install rizin
# plugins, extras and bindings install under $HOMEBREW_PREFIX/lib/rizin
# scripting from other languages needs the separate rzpipe library
```

## Try this

```
rizin --help
```
Lists the command-line options for the main shell.

```
rizin
```
Starts the interactive shell with a banner and a prompt like [0x00000000]>.

```
rz-bin --help
```
Shows what the standalone binary-inspection tool can report about an executable.

## What's unique

Its shell is built on Tree-sitter with YAML-defined commands, and it auto-labels library functions in stripped binaries using FLIRT signatures. It is also a young, cleaner fork of radare2.

## Caveats

Some features are still early: the project save/load format is beta and the rz-pm plugin manager is in early development.

## Links

- [Homepage](https://rizin.re)
- [Official Rizin book (docs)](https://book.rizin.re)
- [Install instructions](https://rizin.re/install/)
- [GitHub repository](https://github.com/rizinorg/rizin)
