---
name: fennel
title: Fennel
source: brew
category: languages-and-oddities
commitment: quick
tags: [compiler, language, lisp, lua, macros, quick, repl]
homepage: https://fennel-lang.org
scout_score: 7
status: draft
---

# Fennel

**TLDR;** A Lisp with macros that compiles to plain Lua, so it runs anywhere Lua does, with a REPL and a single-file compiler you can embed.

Fennel is a programming language written in Lisp syntax that compiles to Lua. You give it .fnl files or type into its REPL, and it produces ordinary Lua source. Per the homepage, it calls any Lua function or library, and Lua can call back into it.

The homepage pitches it as bringing together "the simplicity, speed, and reach of Lua with the flexibility of a lisp syntax and macro system." Macros run at compile time, so the Lua you ship has no runtime dependency on Fennel. The site says the compiled output should be as efficient as hand-written Lua.

The idea underneath is that a language can be a thin, inspectable layer over another one. The homepage has an in-browser REPL and a side-by-side viewer that shows how Fennel forms map to Lua, which makes the compile step easy to see. The compiler is a single file, fennel.lua, which you can drop into a Lua program for runtime extension and live development. TIC-80 has Fennel built in, and LÖVE can use it with some manual setup.

## Install

```
brew install fennel
# Homebrew pulls in lua as a dependency. Other routes: a single fennel script (needs an existing Lua or LuaJIT) or a prebuilt binary for GNU/Linux x86_64 and Windows.
```

## Try this

```
fennel --help
```
Lists the command-line options, including running a file, starting the REPL, and compiling.

```
./fennel --compile $< > $@
```
From a Makefile recipe, compiles each .fnl file ahead of time into a .lua file.

```
require("fennel").install().dofile("main.fnl")
```
In a Lua program, loads fennel.lua, installs its module searcher, and runs main.fnl as the entry point.

## What's unique

It is a Lisp whose output is ordinary Lua, and the whole compiler fits in one embeddable file. Because of that, you can add macros and a live REPL to any Lua host.

## Caveats

Likely maintained (releases up to v1.6.1), but the brief found no release or commit dates; prebuilt binaries cover only GNU/Linux x86_64 and Windows.

## Links

- [Homepage](https://fennel-lang.org)
- [Setting up Fennel](https://fennel-lang.org/setup)
- [Issue tracker](https://dev.fennel-lang.org)
