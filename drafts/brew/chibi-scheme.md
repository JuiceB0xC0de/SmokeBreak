---
name: chibi-scheme
title: Chibi-Scheme
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c, embedding, language, r7rs, scheme]
homepage: https://github.com/ashinn/chibi-scheme
scout_score: 6
status: draft
---

# Chibi-Scheme

**TLDR;** A very small Scheme interpreter built to be embedded in C programs, with R7RS, a full numeric tower, and Unicode, and a REPL to try it.

Chibi-Scheme is a Scheme implementation shipped as a small C library, libchibi-scheme, plus a sample command-line REPL called `chibi-scheme`. It has no external dependencies. The README describes it as "intended for use as an extension and scripting language in C programs."

Despite the size, the default language is not a toy subset. It includes the R7RS small bindings, a full numeric tower with rationals and complex numbers, Unicode, hygienic macros, and an extensible module system. The README says it "attempts to do The Right Thing." The language is built in layers, and the manual explains how to compile with fewer features or ask for a smaller language at startup.

The idea underneath is embedding: instead of writing a config format or a one-off scripting syntax for your program, you drop in a small, real language. Each VM runs in its own isolated heap, so several VMs can run side by side in different OS threads. That makes it a useful way to see what a language runtime looks like when it is meant to live inside another program.

The Homebrew formula also installs `chibi-ffi`, `chibi-doc`, and the `snow-chibi` package tool. The brief does not describe what those do, so check their `--help`.

## Install

```
brew install chibi-scheme
```

## Try this

```
chibi-scheme --help
```
Lists the options of the sample REPL so you can see how to start it and run scripts.

```
chibi-ffi --help
```
Shows the usage for the foreign function interface tool that ships with it.

```
snow-chibi --help
```
Shows the package manager's commands.

## What's unique

It is a real R7RS Scheme with numeric tower, Unicode, and hygienic macros, designed to be dropped into a C project as a library. Each VM gets an isolated heap, so several can run in parallel OS threads.

## Caveats

The brief could not confirm how actively the project is maintained, and native Windows desktop support is described as basic.

## Links

- [GitHub repository](https://github.com/ashinn/chibi-scheme)
- [Online manual](http://synthcode.com/scheme/chibi/)
- [R7RS small specification](https://small.r7rs.org/)
