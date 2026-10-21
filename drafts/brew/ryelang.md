---
name: ryelang
title: Rye
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, go, homoiconic, language, rebol, repl]
homepage: https://ryelang.org/
scout_score: 7
status: draft
---

# Rye

**TLDR;** Rye is a small homoiconic scripting language where if, loop and fn are ordinary functions, and failures are values instead of null.

Rye is a dynamic language with a Go-based interpreter and a REPL. Programs are built from function calls and pipes, with no keywords. Most values are blocks, strings, numbers, tables or Failures. It runs script files, and it can be embedded in a Go program as a scripting or configuration language.

Its README says it is inspired by Rebol, Factor, Linux shells and Go. The homepage describes it as "designed for predictable, composable programs and interactive use." Everything is a function call, including `if`, `loop`, `fn` and `try`, so a user can inspect or replace them. Code is made of Rye values, so blocks can be passed around, stored, combined and examined.

The idea underneath is that control flow does not have to be built into the language. When `if` is just a function, you can write your own control structures, and the homepage shows an `if-joe` example. State is strict: names defined with a colon are constants, and mutation needs a mod-word (`::`) or a function whose name ends in `!`.

Failure is also a value. A failed lookup returns a Failure carrying a message, type and status, which you handle inline with `fix`, as in `person -> "surname" |fix { "Doe" } |print`. The binary bundles modules for HTTP, SQLite, JSON, CSV and regexp, plus dialects for validation, math, SQL and HTML.

## Install

```
brew install ryelang
# Other routes: curl -fsSL https://ryelang.org/install.sh | sh, or docker run -ti ghcr.io/refaktor/rye
# Building from source needs Go 1.21.5 or later.
```

## Try this

```
rye --help
```
Lists the options of the installed interpreter.

```
bin/rye
```
Starts the REPL when you have built from source, so you can try pipes and Failure handling interactively.

```
bin/rye script.rye
```
Runs a Rye script file.

## What's unique

Control flow is made of ordinary functions in a homoiconic language, so you can inspect or replace it. Explicit Failure values take the place of null, and one binary carries SQLite, HTTP and more.

## Caveats

The README labels it Beta and the homepage says active development, so the syntax and API may change, and its word-based pipes and set-words will feel unfamiliar.

## Links

- [Rye homepage](https://ryelang.org/)
- [Meet Rye (intro and interactive demos)](https://ryelang.org/meet_rye/)
- [GitHub repository](https://github.com/refaktor/rye)
