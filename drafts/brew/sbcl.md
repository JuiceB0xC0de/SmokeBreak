---
name: sbcl
title: SBCL
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, common-lisp, compiler, language, lisp, repl]
homepage: https://www.sbcl.org/
scout_score: 6
status: draft
---

# SBCL

**TLDR;** A fast, free Common Lisp compiler with a live interactive environment, debugger and profiler built in: a door into one of the oldest programming traditions.

SBCL (Steel Bank Common Lisp) is a compiler and runtime for ANSI Common Lisp. Its homepage calls it "a high performance Common Lisp compiler", open source with a permissive license. It runs on Linux, several BSDs, macOS, Solaris and Windows.

Beyond compiling, it ships an interactive environment. In the homepage's words: "a debugger, a statistical profiler, a code coverage tool, and many other extensions." The brief does not describe the REPL in detail, but an interactive environment is the core of how Lisp is normally used: you start it, type expressions, and define things in a running system instead of running a compile-edit-run loop.

That is the larger idea underneath. Common Lisp is an old, standardised language built around a live, changeable program, and SBCL is one of the most widely used implementations of it. Poking at it shows what programming looked like when the running image was the workspace, and why people still prefer it.

## Install

```
brew install sbcl
```

## Try this

```
sbcl --help
```
Prints the runtime's command-line options, a safe first look at what the binary accepts.

## What's unique

It is a native compiler that also provides a live interactive environment, with a debugger and a statistical profiler included in one free package.

## Caveats

The brief could not read the Getting Started, Download or Documentation pages (404s), so usage details beyond the homepage are unverified.

## Links

- [SBCL homepage](https://www.sbcl.org/)
