---
name: lunarml
title: LunarML
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, continuations, functional, javascript, lua, standard-ml]
homepage: https://github.com/minoki/LunarML
scout_score: 6
status: draft
---

# LunarML

**TLDR;** A Standard ML compiler that emits Lua or JavaScript, so a statically typed functional language can run inside Lua, LuaJIT, Node.js or a browser.

LunarML takes Standard ML source (`.sml`) or ML Basis project files (`.mlb`) and writes out a Lua or JavaScript program. Targets include Lua 5.3+, LuaJIT, Node.js as ES modules, and plain web JavaScript. You compile once, then run the output with whatever host runtime you picked.

The README gives no explicit motivation, but the shape of the project suggests one: Lua and JavaScript are everywhere, and Standard ML is a small, carefully specified language with a strong type system and pattern matching. LunarML lets you write in the second and ship to the first. It also advertises interfaces for calling into Lua and JavaScript.

The notable extra is continuations. Flags such as `--lua-continuations`, `--nodejs-cps` and `--webjs-cps` add one-shot or delimited continuations on those targets. Those are the kind of control-flow tools that language-design courses talk about and few mainstream runtimes expose. The README also says the Lua continuation mode supports deeply nested `handle`.

The compiler itself is built with MLton, so it is a native ML program that compiles ML. Some features follow Successor ML rather than strict SML '97, and Basis Library support is a subset.

## Install

```
brew install lunarml
# Homebrew also pulls in gmp. To run the output you need Lua 5.3+ (or LuaJIT) or a recent Node.js.
```

## Try this

```
lunarml compile example/hello.sml
```
Compiles the hello-world SML example from the repository into a Lua file.

```
lua example/hello.lua
```
Runs the compiled Lua output; the README shows it printing 'Hello world!'.

```
lunarml --help
```
Lists the compiler's options, including the target and continuation modes.

## What's unique

Standard ML aimed at both Lua and JavaScript from a single compiler is an uncommon pairing, and delimited continuations on those targets are rarer still.

## Caveats

The README warns that script-compiled LunarML is slow and says to use the native binary for serious use; the Basis Library is only a subset, and I could not confirm the project's recent activity.

## Links

- [GitHub repository (homepage)](https://github.com/minoki/LunarML)
- [Documentation (Read the Docs)](https://lunarml.readthedocs.io/en/latest/)
