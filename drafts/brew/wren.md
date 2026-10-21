---
name: wren
title: Wren
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, embeddable, fibers, language, scripting]
homepage: https://wren.io
scout_score: 6
status: draft
---

# Wren

**TLDR;** A tiny class-based scripting language with built-in fibers, made to embed in other programs, and described as Smalltalk in a Lua-sized package.

Wren is a scripting language meant to live inside a host application. It compiles source to bytecode in a single pass and runs it on its own VM, and a C API lets the host program drive it. It has no dependencies and a small standard library. The README says the VM implementation is under 4,000 semicolons.

The author's pitch is that many scripting languages have an unusual or missing object model, so Wren puts classes front and center. The README puts the idea as: "Think Smalltalk in a Lua-sized package with a dash of Erlang and wrapped up in a familiar, modern syntax."

The idea underneath is the fiber. Fibers are lightweight coroutines that are core to the execution model, so a program can be organized as, in the README's words, "an army of communicating coroutines." You create one with `Fiber.new`, start it with `call`, and hand values back with `Fiber.yield`. It is a small, readable way to see cooperative concurrency without threads.

The README also says the VM is small but not dense and is lovingly commented, which makes it a good candidate for reading as well as running. How the standalone command-line side works is unclear from the sources behind this entry.

## Install

```
brew install wren
# The formula lists no executables, so it may not provide a `wren` command. The README says Wren compiles as C99 or C++98 or later with no dependencies, but gives no build steps. The browser playground needs no install.
```

## Try this

## What's unique

Fibers are the core concurrency primitive in a very small embeddable language, and the object model is deliberately class-first. The codebase is also written to be read.

## Caveats

The Homebrew formula lists no executables, so it may not give you a command-line binary, and the project's release status and last activity could not be confirmed.

## Links

- [Homepage](https://wren.io)
- [GitHub repository (README)](https://github.com/wren-lang/wren)
- [Browser playground](http://ppvk.github.io/wren-nest/)
- [Getting started](http://wren.io/getting-started.html)
