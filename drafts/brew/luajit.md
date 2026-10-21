---
name: luajit
title: LuaJIT
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, jit, language, lua]
homepage: https://luajit.org/luajit.html
scout_score: 5
status: draft
---

# LuaJIT

**TLDR;** A Lua interpreter with a trace-compiling JIT and a built-in C FFI, a small VM with an unusually deep design.

LuaJIT runs Lua source or bytecode as a standalone interpreter. While it runs, it spots hot code paths and compiles them to machine code. It is API-compatible with Lua 5.1, so existing Lua 5.1 embeddings can usually switch to it by relinking.

The homepage pitches it as a fast, low-footprint way to run Lua, embedded in games, appliances, network and graphics apps, numerical simulations and trading platforms. It has been in continuous development since 2005. LuaJIT 2.0 was a rewrite of the whole VM, aimed at closing the performance gap between dynamic languages and offline static compilers.

The design is the interesting part. The interpreter is hand-written in assembler. The JIT is a trace compiler with SSA-based optimizations and tuned code generation backends, rather than the more common method-at-a-time JIT. It records the path a hot loop actually takes and compiles that. It also ships a bit.* module and an FFI for calling C directly from Lua, which most Lua-family runtimes do not include.

That makes it a good door into how JITs work, and into why a tiny language can be made very fast.

## Install

```
brew install luajit

The project itself ships only source code. The brew formula builds it for you, installing the luajit executable.
```

## Try this

```
luajit --help
```
Lists the command-line options for the interpreter.

## What's unique

A hand-written assembler interpreter paired with a trace compiler, plus a built-in C FFI. Few runtimes in the Lua family have either.

## Caveats

It targets Lua 5.1 semantics, not later Lua versions, and the JIT is disabled on iOS and consoles, which get only the interpreter.

## Links

- [LuaJIT homepage](https://luajit.org/luajit.html)
- [Installation guide](https://luajit.org/install.html)
