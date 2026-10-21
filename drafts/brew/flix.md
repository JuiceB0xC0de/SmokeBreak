---
name: flix
title: Flix
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, datalog, effects, functional, jvm, language]
homepage: https://flix.dev/
scout_score: 6
status: draft
---

# Flix

**TLDR;** A statically typed JVM language where side effects are tracked in the type system and Datalog constraints are ordinary values you can pass around.

Flix compiles .flix source files to JVM bytecode. The compiler comes with a build tool, package manager, test runner, REPL and language server, so there is no separate toolchain to assemble. It can call Java and Maven libraries directly, and the homepage describes it as a whole-program optimizing compiler.

The central idea is that effects are part of the type. Every expression carries an effect set, such as pure or IO, and the compiler infers and tracks it, including through higher-order functions. Library effects like Clock, Http and Logger have default handlers, so programs run without boilerplate. You can also define your own effects and handlers, which lets you write your own control structures. Per the homepage: "The Flix compiler provides an ironclad guarantee that if an expression is pure then it cannot have side-effects and it is referentially transparent."

The second door is logic programming. Datalog constraints are first-class values that can be stored, composed and solved inside an ordinary functional program, which suits fixpoint and graph-reachability problems. Region-based local mutation lets a function like sort use mutable arrays internally and still be typed pure.

Flix is developed at Aarhus University with contributors from Waterloo, Tübingen and Copenhagen. It is a research language that you can run on a normal afternoon.

## Install

```
brew install flix
Requires a Java runtime; the formula depends on openjdk. The homepage names no minimum version.
```

## Try this

```
flix init
```
Writes the first flix.toml manifest for a new project.

```
flix build
```
Builds the project to JVM bytecode, which you can then inspect with javap.

```
flix test
```
Runs every function marked @Test using the built-in test framework.

## What's unique

Effects are tracked in the type system, and Datalog constraints are first-class values inside a functional language. Build, test, REPL and language server are part of the compiler itself.

## Caveats

It is a niche language with a small ecosystem, and homepage code examples differ from the docs in places, so check snippets against the current standard library at api.flix.dev.

## Links

- [Flix homepage](https://flix.dev/)
- [Programming Flix (docs book)](https://doc.flix.dev/)
- [Standard library API reference](https://api.flix.dev/)
