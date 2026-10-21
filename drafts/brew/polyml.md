---
name: polyml
title: Poly/ML
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, functional, language, repl, standard-ml]
homepage: https://www.polyml.org/
scout_score: 6
status: draft
---

# Poly/ML

**TLDR;** A Standard ML implementation with a REPL, a native-code compiler and multicore threads, used to run large theorem provers like Isabelle and HOL.

Poly/ML takes Standard ML source and either runs it interactively or compiles it. On x86 (32- and 64-bit) and 64-bit ARM it generates native code. On other architectures it falls back to an interpreted byte-code, which the download page says will be slower. The README says it has been fully compatible with the ML97 standard since version 4.0.

It began life written in an experimental language called Poly, and the project still describes its approach as conservative: in its own words, "Poly/ML takes a conservative approach to the Standard ML language and avoids incompatible extensions." What it adds are library extensions, such as a thread library with a simplified POSIX-threads-style interface adapted for Standard ML. Programs can use multiple cores, and the garbage collector is parallelised. The homepage also advertises an interactive debugger.

The door it opens is the ML family itself: a statically typed functional language with type inference, pattern matching and a formal specification. The README calls Poly/ML the "Preferred implementation for large projects such as Isabelle and HOL", so it is a way to see the language that serious proof assistants are built on, not just a teaching toy.

## Install

```
brew install polyml
# Upstream's documented route is a source build: ./configure, make, make install. No accounts or extra runtimes are mentioned.
```

## Try this

```
poly --help
```
Prints the command-line options for the Poly/ML interpreter. Run plain `poly` to get the interactive prompt.

```
polyc --help
```
Shows the options for the compiler wrapper that builds Standard ML programs into executables.

```
polyimport --help
```
Shows the options for the import tool, which loads exported Poly/ML heap data.

## What's unique

It is one of the few Standard ML systems that advertises a parallelised garbage collector and multicore threads, and it is tied to Isabelle and HOL.

## Caveats

Native code exists only on x86 and 64-bit ARM, other platforms get a slower byte-code interpreter, and the executable names come from Homebrew metadata rather than the project pages.

## Links

- [Poly/ML homepage](https://www.polyml.org/)
- [GitHub repository](https://github.com/polyml/polyml)
- [Download page](http://www.polyml.org/download.html)
- [Basis library documentation](http://www.polyml.org/documentation/Reference/Basis.html)
