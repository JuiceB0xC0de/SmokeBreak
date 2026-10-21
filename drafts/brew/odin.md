---
name: odin
title: Odin
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, data-oriented, graphics, language, systems]
homepage: https://odin-lang.org/
scout_score: 7
status: draft
---

# Odin

**TLDR;** A compiled systems language that calls itself 'the C alternative for the Joy of Programming', with data-oriented features and graphics bindings built in.

Odin is a general-purpose compiled language. You write `.odin` files, the Odin compiler turns them into native programs, and a core library (fmt, simd and others) comes with it. A separate vendor library ships official bindings for SDL2, GLFW, raylib, microui and miniaudio, plus graphics APIs such as Vulkan, Metal, Direct3D and WebGL.

The stated principles are simplicity, performance and support for modern hardware. In the project's words: "Simplicity is complicated to get right, clear is better than clever." Performance comes from low-level control over memory layout and custom allocators. The README also describes it as "The Data-Oriented Language for Sane Software Development".

The idea underneath is data-oriented design: think first about how your data sits in memory, then write the code around it. Odin puts that into the language itself. Bit sets, enumerated arrays, SOA (struct-of-arrays) layout, SIMD vectors and component-wise array math with swizzles are built-in features, not libraries. The homepage examples also show `defer` for cleanup at scope exit, multiple return values, labelled control flow and inline assembly.

A program starts with `package main`, imports what it needs (for example `core:fmt`), and has a `main :: proc()` entry point. The homepage showcase lists many programs and Steam games written in Odin, which is a good place to see what people actually build with it.

## Install

```
brew install odin
```

## Try this

```
odin --help
```
Lists the compiler's commands and flags, so you can see how to build and run a .odin file.

## What's unique

Data-oriented features like SOA layout, bit sets and array programming are part of the language, and official graphics bindings come in the box, which is unusual for a young language.

## Caveats

The README warns that 'The Odin compiler is still in development', so expect the language and its tooling to keep changing.

## Links

- [Odin homepage](https://odin-lang.org/)
- [Getting Started / install docs](https://odin-lang.org/docs/install)
- [Package documentation (core and vendor)](https://pkg.odin-lang.org/)
- [GitHub repository](https://github.com/odin-lang/Odin)
