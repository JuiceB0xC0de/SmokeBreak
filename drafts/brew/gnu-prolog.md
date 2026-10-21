---
name: gnu-prolog
title: GNU Prolog
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, constraints, logic-programming, prolog]
homepage: http://www.gprolog.org/
scout_score: 7
status: draft
---

# GNU Prolog

**TLDR;** A Prolog compiler with a finite-domain constraint solver that turns logic programs into stand-alone native executables, the way gcc turns C into binaries.

GNU Prolog is a free Prolog system written by Daniel Diaz. You can use it two ways: as an interactive top-level with a debugger by running `gprolog`, or as a compiler with `gplc`, which turns Prolog and constraint programs into native binaries. The homepage describes the language side as ISO-conformant, with extensions such as global variables, DCGs, sockets and an OS interface.

The constraint solver works over finite domains. Instead of writing a search loop, you state that variables take values from a range and describe how they must relate, and the system finds assignments that satisfy it. Puzzles like scheduling, sudoku and the like become declarations rather than algorithms. The homepage says the solver defines all its high-level constraints in terms of a single low-level primitive, which makes constraints compilable and lets users define their own.

Under the hood it is built on the Warren Abstract Machine. A program is compiled to a WAM file, then to a machine-independent mini-assembly, then to the target machine's assembly, and finally to a native executable. The author's earlier system, wamcc, went through C and was slowed by gcc compile times, so this design generates assembly directly. Development began in January 1996 under the name Calypso. Unused built-in predicates are dropped at link time, which keeps executables small.

The other executables (`pl2wam`, `wam2ma`, `ma2asm`, `fd2c`, `hexgplc`) are the stages of that pipeline, which makes it a readable tour of how a logic language becomes machine code.

## Install

```
brew install gnu-prolog
```

## Try this

```
gprolog --version
```
Prints the installed GNU Prolog version, the same check the homepage asks for in bug reports.

```
gprolog
```
Starts the interactive top-level, where you can enter queries and use the debugger.

```
gplc --help
```
Shows the options of the compiler that builds native executables from Prolog source.

## What's unique

It compiles Prolog and constraint programs to native binaries without going through C, and its finite-domain solver is built on one primitive that users can extend.

## Caveats

The homepage shows no release date; it lists 1.5.0 as the current stable version, with a copyright line of 1999-2021.

## Links

- [GNU Prolog homepage](http://www.gprolog.org/)
- [Users mailing list archive and subscription](http://mail.gnu.org/mailman/listinfo/users-prolog)
- [Bug reports mailing list](http://mail.gnu.org/mailman/listinfo/bug-prolog)
