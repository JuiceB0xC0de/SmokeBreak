---
name: libcello
title: Cello
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, experiment, generics, library, macros]
homepage: https://libcello.org/
scout_score: 6
status: draft
---

# Cello

**TLDR;** A C library that bolts generics, type classes, exceptions, reflection and optional garbage collection onto plain C, as an experiment in how far the language can be pushed.

Cello is a runtime system layered on standard C. A program includes one header, Cello.h, and gets objects with constructors and destructors, polymorphic functions, interfaces (type classes), exceptions, reflection and optional garbage collection. Stack objects are made with `$(Type, value)`, heap objects with `new(Type, ...)`, and collections can be walked with `foreach`. The result is an ordinary C program linked against libCello.a.

Daniel Holden made it, in his words, "as a fun experiment to see what C looks like hacked to its limits." It is not a new compiler or a preprocessor dialect. As the README puts it: "Although Cello does not look like it - it is just a C library."

The idea underneath is the fat pointer: values carry extra type information alongside them, so the runtime can dispatch on type, check it and inspect it. The README does not explain the mechanism itself. It points to the article "A Fat Pointer Library" and says the source is fairly readable. Reading how macros and header tricks can imitate a higher-level language is the real payoff, whether or not you ever ship code with it.

## Install

```
Not in a brew-first workflow: download the source tarball from libcello.org, unpack it, then run `make` and `make check`. Optionally `make install`. Needs a gnu99-compatible C compiler: gcc on Linux, Xcode command line tools on Mac, MinGW64 or Cygwin on Windows.
```

## Try this

```
gcc --version
```
Confirms you have a C compiler before building.

```
make
```
Compiles the library and should produce libCello.a.

```
make check
```
Builds and runs the test suite to confirm the build works.

## What's unique

It makes C feel like a higher-level language without a new compiler or syntax: the code is ordinary C including one header. The author openly calls it a hack.

## Caveats

The author calls it a hack with "its fair share of oddities and pitfalls", recommends it for hobby projects, and says it is too big a dependency for portable new C projects; no release date was visible.

## Links

- [Homepage](https://libcello.org/)
- [Installation guide](http://libcello.org/learn/installation)
- [A Fat Pointer Library (how it works)](http://libcello.org/learn/a-fat-pointer-library)
- [GitHub repository](https://github.com/orangeduck/libCello)
