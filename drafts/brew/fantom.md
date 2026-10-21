---
name: fantom
title: Fantom
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [actors, afternoon, jvm, language, object-oriented]
homepage: https://fantom.org/
scout_score: 5
status: draft
---

# Fantom

**TLDR;** Fantom is a Java-flavoured object-oriented language that runs on the JVM and in browsers, with closures, immutability and actor concurrency built in.

Fantom is a programming language with a familiar, Java-like syntax. Its homepage describes it as "a portable language that runs on the JVM and modern web browsers." The pitch is one language that can target more than one runtime, instead of a separate language for each.

The language mixes static and dynamic typing and ships with a system library. It also has closures, immutability and actor-based concurrency. The homepage's Hello World is a plain Java-style class with a static main method, so a Java developer can read it on sight.

The Homebrew package installs a whole toolchain: `fan` (the launcher), `fanc`, `fanp`, `fanr`, `fansh`, `fant`, `flux`, `jstub` and others, plus Windows `.bat` variants. The brief did not confirm what each tool does. The names suggest a compiler, a test runner, a shell and a package manager, but that is inference. The homepage also points to Eggbox, a repository of libraries.

The interest here is in the design question: what do you keep, and what do you change, if you redo Java's ideas with portability across runtimes as a goal from the start? Fantom is a small, quiet answer to that question.

## Install

```
brew install fantom
# depends on openjdk, which Homebrew installs for you
```

## Try this

```
fan --help
```
Prints usage for the main Fantom launcher, a first look at how the toolchain is driven.

## What's unique

One language aimed at both the JVM and the browser, with a Java-like surface and built-in actor concurrency and immutability.

## Caveats

The brief only covers the homepage; docs and download pages weren't reachable, and the project's current activity level is unknown.

## Links

- [Fantom homepage](https://fantom.org/)
