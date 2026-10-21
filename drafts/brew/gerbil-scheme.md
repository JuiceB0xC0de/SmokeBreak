---
name: gerbil-scheme
title: Gerbil Scheme
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, gambit, language, lisp, macros, scheme]
homepage: https://cons.io
scout_score: 7
status: draft
---

# Gerbil Scheme

**TLDR;** A Scheme dialect on the Gambit runtime that compiles to native code, with a full macro tower and a module system aimed at systems programming.

Gerbil Scheme is a dialect of Scheme built on Gambit, Marc Feeley's Scheme-to-C compiler. You can type expressions into an interactive interpreter (gxi) or write source files and compile them to native code with gxc. The distribution also ships a package tool (gxpkg), a test runner (gxtest), a profiler (gxprof), a tags generator (gxtags) and an HTTP server (gxhttpd).

The README describes it as "an opinionated, some might even say tendentious, dialect of Scheme designed for systems programming," and suggests thinking of it as "the C++ to Marc Feeley's C." The author says it began as his private Scheme and was released publicly at the prompting of friends.

The idea underneath is that the macro system is the compiler. Macros are based on quote-syntax, with a full meta-syntactic tower and a native syntax-case implementation. The whole system is self-hosted, bootstrapping from source on Gambit with a precompiled macro system and compiler. So Scheme is used to build Scheme.

The module system resembles Racket's, with one difference the README stresses: Gerbil modules are single-instantiation. That is what supports high-performance ahead-of-time compilation and compiled macros. The homepage also advertises actors, an integrated metaobject protocol, an FFI and static binaries, though the brief did not confirm these in detail.

## Install

```
brew install mighty-gerbils/gerbil/gerbil-scheme
# The formula lives in the mighty-gerbils tap, not Homebrew core. It pulls in openssl and gcc.
# On Linux, build from source: git clone, ./configure, make -j4, sudo make install (installs to /opt/gerbil; add /opt/gerbil/bin to PATH). On Ubuntu first: sudo apt install libssl-dev zlib1g-dev libsqlite3-dev
```

## Try this

```
gxi
```
Starts the Gerbil interactive interpreter, where you can type Scheme expressions and see results.

```
gxc
```
Runs the Gerbil compiler, which turns Gerbil source into native code.

```
gerbil --help
```
Lists what the main gerbil command can do, including its package and build tooling.

## What's unique

It pairs a Racket-style module system with single instantiation, built for ahead-of-time native compilation, and treats a self-hosted macro system as the heart of the compiler. It is a Lisp that aims at systems work rather than teaching or scripting.

## Caveats

The README says the documentation is a work in progress and the team is still porting batteries, so parts of the library may be incomplete; Linux needs a source build or a prebuilt release package.

## Links

- [Homepage](https://cons.io)
- [Guide: Introduction to Gerbil](https://cons.io/guide/intro.html)
- [Reference documentation](https://cons.io/reference/)
- [Source code on GitHub](https://github.com/mighty-gerbils/gerbil)
