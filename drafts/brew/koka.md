---
name: koka
title: Koka
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, effect-types, functional, language, research]
homepage: http://koka-lang.org
scout_score: 7
status: draft
---

# Koka

**TLDR;** A research functional language that tracks side effects in its types and compiles to C without a garbage collector, using effect handlers for exceptions and async.

Koka is a strongly typed, functional-style language and its compiler. You write `.kk` files and the compiler turns them, by default through generated C, into runnable programs. The README also mentions JavaScript and WebAssembly backends. Its central habit is that every function's type records its side effects, so pure and effectful code are visibly different.

The idea underneath is effect handlers. Instead of building exceptions, async/await, and probabilistic programming into the language as separate features, Koka offers one general mechanism. Those control abstractions can then be written as ordinary libraries. The compiler implements this with evidence passing.

The other half is memory. Koka uses Perceus, a compiler analysis for reference counting, which lets it emit C with no garbage collector or runtime system. Perceus also does reuse analysis: functional-style code that builds a new structure can often update the old memory in place. The README says benchmarks against OCaml, GHC, Swift, Java and C++ show Koka is competitive, though it calls them not a precise head-to-head.

It comes from Daan Leijen and collaborators as a research language. The README states plainly: "Koka v3 is a research language that is currently under development and not quite ready for production use."

## Install

```
brew install koka
```

## Try this

```
koka --version
```
Checks that the installed compiler runs and prints its version.

```
koka --help
```
Lists the compiler's options, including the backends and output choices.

```
koka --fprofile -e myprogram.kk
```
Compiles and runs a Koka program of your own with GCC profiling instrumentation, for use with gprof.

## What's unique

Few languages compile to C without a garbage collector while also tracking effects in the type system. Perceus reference counting with in-place reuse, plus handlers as the single mechanism for exceptions and async, sets it apart.

## Caveats

It is a research language, not ready for production by the README's own words, with package management still on the to-do list and only basic parallel task support.

## Links

- [Homepage (redirects)](http://koka-lang.org)
- [Koka book: language tour and specification](https://koka-lang.github.io/koka/doc/book.html)
- [Library documentation](https://koka-lang.github.io/koka/doc/toc.html)
- [GitHub repository](https://github.com/koka-lang/koka)
