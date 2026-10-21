---
name: erg
title: Erg
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, language, python, type-system]
homepage: https://github.com/erg-lang/erg
scout_score: 5
status: draft
---

# Erg

**TLDR;** A statically typed language that runs on Python, with refinement types that catch out-of-range indexes and unit mismatches at compile time.

Erg is a programming language whose compiler checks `.er` source files before anything runs. Its type system includes dependent and refinement types, so mistakes like indexing past the end of a list or mixing up units are reported at compile time. It also ships a REPL and an optional language server, ELS, behind a feature flag.

The README pitches it at two groups. One wants Rust-like robustness without Rust's verbose type annotations and memory management. The other is frustrated with Python but cannot throw away its Python code. The README also names an ML-style simplicity goal and a Scala-style mix of object-oriented and functional programming.

Erg is described as internally compatible with Python. Python modules come in through the `pyimport` keyword, which the README says works "at zero cost". Side effects are marked with a trailing `!` on names and methods, and the compiler rejects calling a procedural method inside a function. The README says error messages are a priority, with hints such as pointing you to the mutable variant of a method.

The idea underneath is that a type system can carry more than "this is an int". Ranges, units and purity become things the compiler checks. Erg lets you try that on top of an ecosystem you already know.

## Install

```
brew install erg
# A Python 3 interpreter is required (README says 3.7 to 3.11).
# From source instead: cargo install erg (needs the Rust toolchain). Optional feature flags include els, full-repl, and full.
```

## Try this

```
erg --help
```
Lists the available commands and options for the compiler.

```
erg
```
With no arguments, the README's REPL is the place to try expressions and see type errors immediately.

## What's unique

Most languages that target Python bolt types on afterward. Erg builds refinement and dependent types, compile-time index and unit checks, and a `!` marker for side effects into a Python-compatible language.

## Caveats

The README says some features are not yet implemented, it requires Python 3.7 to 3.11 at runtime, and it gives no release or last-commit date, so maintenance state is unclear.

## Links

- [Homepage (GitHub repository)](https://github.com/erg-lang/erg)
- [Project site](https://erg-lang.org/)
- [Web IDE playground](https://erg-lang.org/web-ide/)
- [Discord](https://discord.gg/zfAAUbgGr4)
