---
name: ponyc
title: Pony
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [actors, afternoon, compiler, concurrency, language, type-system]
homepage: https://www.ponylang.io/
scout_score: 7
status: draft
---

# Pony

**TLDR;** A compiled actor-model language whose type system checks at compile time that concurrent programs cannot have data races, with no locks.

Pony is an object-oriented language that compiles ahead of time to native code, with no interpreter or virtual machine. The `ponyc` executable is the compiler. The Homebrew package also installs `pony-doc`, `pony-lint`, `pony-lsp`, `pony-dep` and `pony-agent-server`. Programs can call C libraries through a foreign function interface.

The unit of concurrency is the actor. Actors talk by sending asynchronous messages, and a behaviour is declared with `be` and called like a method on another actor. The homepage frames the goals in order: correctness first, performance second, simplicity third.

The idea underneath is reference capabilities. These are labels on data that say how it may be shared. In the project's words: "Share only immutable data. Exchange only isolated data. The compiler enforces both. No locks needed." The compiler checks the labels, and the project claims this rules out data races without locks or atomic operations.

Most languages that prevent races use locks, a borrow checker, or runtime checks. Pony moves the sharing rules into the type system, which makes it a way into a different style of concurrent design.

## Install

```
brew install ponyc
# depends on openssl@4, which brew installs
# Linux needs kernel 5.3 or newer; Windows needs Windows 11 or Server 2022
```

## Try this

```
ponyc --help
```
Lists the compiler's options so you can see what it can build and how.

```
pony-doc --help
```
Shows the options for the documentation generator that ships with the compiler.

```
pony-lint --help
```
Shows the options for the linter included in the package.

## What's unique

Data-race freedom comes from reference capabilities checked at compile time, not from locks, a borrow checker or runtime checks. The README says the language has no locks or atomic operations at all.

## Caveats

Pony is pre-1.0 and "semi-regularly introduces breaking changes", the library ecosystem is small, there is no IDE, and the homepage says it is not the right choice yet for projects needing a large ecosystem and stable APIs.

## Links

- [Pony homepage](https://www.ponylang.io/)
- [Source repository (README)](https://github.com/ponylang/ponyc)
- [Learn Pony (tutorial, reference capabilities, install)](https://www.ponylang.io/learn/)
- [Try Pony in the browser playground](https://playground.ponylang.io)
