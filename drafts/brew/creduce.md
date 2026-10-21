---
name: creduce
title: C-Reduce
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, c++, compilers, debugging, llvm, test-case-reduction]
homepage: https://github.com/csmith-project/creduce
scout_score: 6
status: draft
---

# C-Reduce

**TLDR;** Give it a huge C or C++ file and a test script, and it shrinks the file to a tiny program that still does the same thing.

C-Reduce takes a large C or C++ program that has some property of interest, such as triggering a compiler bug, and automatically produces a much smaller program with the same property. You supply the property as an "interestingness test", a script that exits successfully when the file still shows the behaviour. The tool tries smaller variants, keeps the ones that still pass, and repeats.

It exists for people who find and report bugs in compilers and other tools that process C/C++. A bug report that says "this 20,000-line file crashes the compiler" is hard to act on. A ten-line file is easy. Doing that shrinking by hand is tedious, so C-Reduce does it for you.

The idea underneath is test-case reduction: define a property as a yes/no question, then search for the smallest input that still answers yes. The README does not detail the reduction passes, but INSTALL.md mentions an internal tool, clang_delta, built against LLVM/Clang. Each run of your test happens in a fresh temporary directory holding a copy of the file being reduced, which keeps test scripts simple.

The README also says it does a pretty good job on languages other than C/C++, such as JavaScript and Rust, even though it was built for C.

## Install

```
brew install creduce
# Homebrew pulls in astyle and llvm@21 as dependencies. You also need your own interestingness test script.
```

## Try this

```
creduce --help
```
Lists the options and shows how to pass in your interestingness test and the file to reduce.

```
creduce --n 1
```
Runs on a single core so it never kills a running compiler instance, which avoids leaking files into /tmp. Add your test script and source file as arguments.

## What's unique

It turns "make this bug report smaller" into an automated search driven by a script you write. Its README also claims it handles JavaScript and Rust reasonably well despite being built around C.

## Caveats

Homebrew marks the formula deprecated, though the README I read does not say so, and the install docs pin old LLVM and FreeBSD versions. The README also warns that running on more than one core can leak space in /tmp.

## Links

- [GitHub repository (homepage)](https://github.com/csmith-project/creduce)
- [INSTALL.md](https://github.com/csmith-project/creduce/blob/master/INSTALL.md)
