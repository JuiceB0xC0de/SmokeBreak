---
name: lfe
title: LFE (Lisp Flavoured Erlang)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, beam, erlang, language, lisp, macros, repl]
homepage: https://lfe.io/
scout_score: 6
status: draft
---

# LFE (Lisp Flavoured Erlang)

**TLDR;** A Lisp with Erlang's data types that compiles to BEAM bytecode, so you can write macros and call OTP's concurrency machinery in s-expressions.

LFE is a Lisp-syntax front-end to the Erlang compiler. You type LFE into a REPL, save it as a script, or compile it as a module. What comes out is ordinary BEAM code that Erlang modules can call and be called by. The data types are Erlang's own: lists, tuples, maps, atoms and binaries, with strings as lists of integers.

The homepage tagline is "Taking the syntax out of distributed systems programming". The idea is to put a Lisp surface on Erlang/OTP's concurrency, distribution and fault-tolerance machinery. Behaviours such as gen_server and supervisors are used directly from LFE syntax.

The design choices are worth reading about. It is a Lisp-2, with separate function and variable namespaces, and `defun` arguments use Erlang-style pattern matching. Macros are compile-time only, except in the REPL. They are unhygienic but scoped, and there is no gensym. The author says gensym would be unsafe for code shared with remote nodes. A macro like `mean` can also take any number of arguments, which works around Erlang's lack of variadic functions.

## Install

```
brew install lfe
# Pulls in Erlang/OTP as a dependency. Docker is an alternative: docker pull lfex/lfe
```

## Try this

```
lfe
```
Starts the REPL, where you can call Erlang modules directly.

```
lfe> (* 2 (lists:foldl #'+/2 0 (lists:seq 1 6)))
```
Calls into Erlang's lists module from Lisp and returns 42.

```
lfe> (mean 1 2 3 4 5 6 42 108)
```
Runs the homepage's variadic-style macro example and returns 21.375. It needs the `mean` macro defined first; the homepage shows it as `(defmacro mean args ...)`.

## What's unique

It is a Lisp whose macros and pattern-matching function heads work directly with OTP, and it gives up gensym and macro hygiene on purpose because code may run on remote nodes.

## Caveats

It needs a working Erlang/OTP install, macros are unhygienic so safety is on you, and the README gives no Windows instructions. Homebrew also ships lfeexec, lfe-test and lfe-first-try, which the README does not document.

## Links

- [Homepage](https://lfe.io/)
- [Source repository and README](https://github.com/lfe/lfe)
- [Quick Start (gitbook)](https://lfe.gitbooks.io/quick-start/content/)
