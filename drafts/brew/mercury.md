---
name: mercury
title: Mercury
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, functional, language, logic-programming]
homepage: https://mercurylang.org/
scout_score: 6
status: draft
---

# Mercury

**TLDR;** A compiled logic/functional language built for large programs, with static analysis that catches errors before anything runs.

Mercury is a declarative programming language that mixes logic and functional programming. Its homepage describes it as combining "the clarity and expressiveness of declarative programming with advanced static analysis and error detection features." Programs are compiled by the Mercury toolchain, and the homepage claims the execution is highly optimized, far faster than older logic programming systems and close to conventional ones.

The project's stated aim is scale. The about text calls it "a general purpose language intended to support the creation of large, reliable and efficient applications," and the homepage points to modularity, separate compilation, and optimization trade-offs. That is a different goal from most logic languages, which tend to live in research or small scripts.

The compiler is written in Mercury itself, so building it from git requires an existing Mercury install. There are two kinds of backend: a low-level one that goes through C with GCC or Clang, and high-level ones targeting C#, Java, and C. The long list of executables Homebrew installs (mmc, mmake, mdb, mdprof and others) suggests a full toolchain with a debugger and profilers, though the brief did not confirm what each does.

The door here is a paradigm: describing what is true about a problem and letting the compiler check your description, instead of spelling out steps. If you have only seen Prolog in passing, a compiled and statically analysed relative is a different experience.

## Install

```
brew install mercury
# Homebrew lists openjdk as a dependency. Source and Debian packages are on the download page.
```

## Try this

```
mmc --help
```
Prints the options of the Mercury compiler, the main entry point to the toolchain.

```
mmake --help
```
Shows the Mercury-aware make wrapper that drives builds.

```
mdb --help
```
Shows usage for the Mercury debugger.

## What's unique

It is a logic/functional language that is compiled, statically analysed, and aimed at large programs rather than being purely academic.

## Caveats

The documentation link on the homepage returned a 404 when fetched, and the GitHub README points to a LIMITATIONS.md listing where the implementation falls short of its goals.

## Links

- [Homepage](https://mercurylang.org/)
- [Download page](https://mercurylang.org/download.html)
- [GitHub repository](https://github.com/Mercury-Language/mercury)
