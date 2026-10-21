---
name: bic
title: bic
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, api, c, interpreter, libc, repl]
homepage: https://github.com/hexagonal-sun/bic
scout_score: 7
status: draft
---

# bic

**TLDR;** A C interpreter with a REPL prompt that lets you #include real system headers and call actual libc functions, no main() required.

bic gives C a read-eval-print loop. You get a `BIC>` prompt, type C statements, and see the result of each expression printed back. You can `#include` system headers and call real library functions such as `fopen` and `fputs` straight away, without wrapping anything in `main()`. It can also run a whole file with `-s file.c`, which calls that file's `main()`.

The README says it exists to let developers explore and test C APIs with a REPL. Most C REPLs give you a sandboxed language. bic reaches into the real shared libraries on your machine. A `?name` inspector in the REPL prints type and variable details, such as size and where something was declared. The README also describes a `-l` option for loading other libraries such as Capstone, though the example is missing from the text.

Under the hood, bison and flex generate two parsers, one for REPL input and one for C files. Programs become generic tree objects defined in a lisp-like `c.lang` file, and the evaluator walks that tree recursively. To call external functions, bic marshals arguments into registers following the calling convention and branches to the function. That code is written separately for x86_64 and aarch64, which is the door into ABIs and how a call actually happens.

On first launch bic reads `~/.bic` if it exists and evaluates it as startup code, which is handy for defining functions you use often.

## Install

```
brew install bic
# runtime needs GNU Readline and GMP (gmp is pulled in as a dependency); only x86_64 and aarch64 are supported
```

## Try this

```
bic --help
```
Lists the command-line options, including the ones for running a file and loading libraries.

```
bic -s test.c
```
Evaluates test.c by calling its main(); the README's example prints "Factorial of 4 is: 24".

## What's unique

Most C REPLs hand you a language sandbox. bic lets you include real system headers and call into the actual libc or other shared libraries, and it can report declarations and sizes with `?name`.

## Caveats

Only x86_64 and aarch64 are supported because external calls are written per architecture, and the brief could not confirm recent commit activity.

## Links

- [GitHub repository and README](https://github.com/hexagonal-sun/bic)
- [doc directory in the repo](https://github.com/hexagonal-sun/bic/tree/master/doc)
