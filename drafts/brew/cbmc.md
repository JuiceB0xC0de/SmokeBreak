---
name: cbmc
title: CBMC
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, formal-methods, math, model-checking, verification]
homepage: https://www.cprover.org/cbmc/
scout_score: 7
status: draft
---

# CBMC

**TLDR;** A bounded model checker for C and C++ that turns your program into a logic equation and searches for inputs that break your assertions.

CBMC reads C or C++ source and checks it for memory safety, array bounds, pointer misuse, various undefined-behaviour cases, and assertions you write yourself. When it finds a violation, it reports it. It can also check C or C++ for I/O equivalence against other languages such as Verilog.

The method is the interesting part. CBMC unwinds the program's loops up to a fixed bound and turns the result into a logical equation. That equation goes to a decision procedure: by default a built-in bit-vector solver based on MiniSat, or an external SMT solver such as Boolector, CVC5 or Z3. In the project's words: "The verification is performed by unwinding the loops in the program and passing the resulting equation to a decision procedure." A solver answering yes or no replaces a test suite sampling a few inputs.

The word bounded matters. CBMC covers loop iterations only up to the unwinding limit, so a clean result is a proof about that bound, not about every possible run. That is the trade that makes this kind of checking practical on real code.

The package installs a whole family of tools: goto-cc compiles to a goto-program form, goto-instrument and goto-analyzer work on it, and jbmc is the Java bytecode variant. The README points to TOOLS_OVERVIEW.md for what each does. The reference paper, 'A Tool for Checking ANSI-C Programs', dates from around 2000 and is still widely cited. The work was sponsored by SRC, NSF, ONR, NRL, DARPA and ARO.

## Install

```
brew install cbmc
# macOS needs the Xcode Command Line Tools. External solvers (Boolector, CVC5, Z3) are optional and installed separately.
```

## Try this

```
cbmc --help
```
Lists the checks and options, including the unwinding bound and the version 6 switches like --no-standard-checks.

```
goto-cc --help
```
Shows the compiler front end that turns C into goto-programs for the other tools in the family.

```
jbmc --help
```
Shows the Java bytecode sibling of CBMC and its options.

## What's unique

It reaches further than most C checkers: C++, I/O equivalence against languages like Verilog, and a set of companion tools for analysing compiled goto programs. It has also been around for over twenty years.

## Caveats

Results hold only up to the loop unwinding bound, and version 6 changed defaults: undefined-behaviour checks are on, malloc may return NULL, and calls to bodiless functions fail verification.

## Links

- [CBMC homepage](https://www.cprover.org/cbmc/)
- [CPROVER documentation (manual, tutorial, properties checked)](https://diffblue.github.io/cbmc/)
- [GitHub repository](https://github.com/diffblue/cbmc)
