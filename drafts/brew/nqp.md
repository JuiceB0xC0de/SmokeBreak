---
name: nqp
title: NQP (Not Quite Perl)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compilers, language, moarvm, raku, virtual-machine]
homepage: https://github.com/Raku/nqp
scout_score: 6
status: draft
---

# NQP (Not Quite Perl)

**TLDR;** A deliberately tiny Raku-flavoured language, with Raku's object model and regex engine, built for writing compilers that run on virtual machines.

NQP stands for "Not Quite Perl". It is a small language and runtime that takes `.nqp` source files and runs them on a virtual machine. MoarVM is the main backend. JVM and JavaScript backends exist but are experimental. Run with no script, `nqp` drops into a small interactive mode.

It is not a general-purpose Raku. The README says it is "a tool for writing Raku compilers, not a low-level module for Raku programmers." It is meant to be "a very small environment (as compared with, say, raku or Rakudo)" while still giving you a Raku object model and a regular expression engine.

The idea underneath is bootstrapping. To build a high-level language you first need a smaller, high-level language to write its compiler in, one that already knows how to talk to the VM. NQP fills that role for Raku's compiler, and it can target several VMs from one source language. If you are curious how a language implementation is layered on a VM, this is a compact place to look. The repository has docs on opcodes and built-in routines, and an examples directory.

## Install

```
brew install nqp
# pulls in moarvm as a dependency. Homebrew installs two executables: nqp and nqp-m.
```

## Try this

```
nqp --help
```
Lists the command-line options of the NQP executable.

```
nqp
```
With no script, starts the small interactive mode where you can type NQP and see it run.

```
./nqp hello.nqp
```
Runs an NQP program file. The README shows this form from a source build directory, so with a Homebrew install use `nqp hello.nqp` instead.

## What's unique

It is a tiny language runtime whose job is to build other language implementations. It carries Raku's object model and regex engine without the weight of Rakudo.

## Caveats

The README says there is no end-user support and behaviour can change without notice; the JVM and JavaScript backends are experimental, and the README does not describe the nqp-m executable.

## Links

- [GitHub repository (homepage)](https://github.com/Raku/nqp)
- [Docs directory (opcodes and built-in routines)](https://github.com/Raku/nqp/tree/main/docs)
- [Examples directory](https://github.com/Raku/nqp/tree/main/examples)
