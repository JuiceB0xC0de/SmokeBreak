---
name: staq
title: staq
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, compilers, openqasm, quantum, science]
homepage: https://iopscience.iop.org/article/10.1088/2058-9565/ab9359/pdf
scout_score: 5
status: draft
---

# staq

**TLDR;** A command-line toolkit that compiles and transforms quantum circuits by editing the OpenQASM syntax tree directly, so the output still reads like your source.

staq is a C++17 library and a set of command-line tools for synthesizing, transforming, optimizing and compiling quantum circuits. The main input is OpenQASM 2.0 source. The output is a transformed circuit, or a translation into another circuit language or library. The brew formula installs separate tools for mapping onto a device, estimating resources, inlining, simplifying, optimizing rotations and emitting other targets, plus a top-level `staq` command.

The design is the interesting part. Most compilers lower code into an intermediate representation, and the original source is gone by the end. staq is inspired by Clang and works on the OpenQASM 2.0 syntax tree itself. In the README's words, this is "rather than through an intermediate representation which makes retrieving the original source code impossible." A circuit can be changed in place and, in most cases, still look like what you wrote.

That makes it a good way to see what a quantum compiler pass does. You can run a transformation and compare the result against your input, line by line, instead of decoding a lowered form. Translating to another circuit language is easier to follow for the same reason. Logic synthesis is handed to the EPFL logic synthesis libraries, and the parser was adapted from Bruno Schmitt's tweedledum.

There is also a header-only C++ library for parsing and manipulating OpenQASM 2.0, and a Python 3 wrapper called pystaq.

## Install

```
brew install staq
# no accounts or hardware needed; the formula depends on gmp
```

## Try this

```
staq --help
```
Lists the main staq options and the transformations it can apply to an OpenQASM 2.0 circuit.

```
staq_resource_estimator --help
```
Shows how to ask for a resource count on a circuit.

```
staq_mapper --help
```
Shows the options for mapping a circuit onto a device layout.

## What's unique

Most quantum compiler toolkits go through an intermediate representation. staq keeps the OpenQASM syntax tree as its working form, so edited circuits still resemble the original source.

## Caveats

It reads OpenQASM 2.0, so you need a circuit in that format to do anything interesting; activity looks quiet, with the README at version 3.5 dated March 2024, though that is tentative.

## Links

- [Homepage (IOP paper, may be blocked by captcha)](https://iopscience.iop.org/article/10.1088/2058-9565/ab9359/pdf)
- [GitHub repository and README](https://github.com/softwareQinc/staq)
- [Project wiki](https://github.com/softwareQinc/staq/wiki)
- [INSTALL.md](https://github.com/softwareQinc/staq/blob/main/INSTALL.md)
