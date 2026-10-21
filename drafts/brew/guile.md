---
name: guile
title: Guile
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compilers, embeddable, gnu, language, lisp, scheme]
homepage: https://www.gnu.org/software/guile/
scout_score: 6
status: draft
---

# Guile

**TLDR;** GNU's Scheme implementation, built to be embedded in other programs as an extension language and able to host other languages on its compiler.

Guile is a Scheme implementation with a compiler and a bytecode virtual machine. You can run it standalone for scripts, or embed it in a C or C++ application so the people using that application can extend it. It supports the Revised5 Scheme report, most of the Revised6 report, and many SRFIs. Its module library includes an HTTP server and client, XML parsing, and object-oriented programming.

The name says what it is for: GNU Ubiquitous Intelligent Language for Extensions. The homepage calls it "the official extension language of the GNU project" and says it is designed so applications "can be extended by users or other programmers with plug-ins, modules, or scripts." The idea is that end users can share features as scripts instead of patches.

The door into something larger is the compiler. Guile compiles Scheme to bytecode, and its parsing and compiling tools are exposed as ordinary modules. That means new source languages can be added without writing C. Front-ends already exist for ECMAScript and Emacs Lisp, and Lua support is described as underway. A Scheme runtime that doubles as a small language workbench is a good reason to spend an afternoon with it.

## Install

```
brew install guile
# Homebrew caveats: add these to your .bashrc or equivalent to install Guile libraries into the Homebrew prefix:
export GUILE_LOAD_PATH="$HOMEBREW_PREFIX/share/guile/site/3.0"
export GUILE_LOAD_COMPILED_PATH="$HOMEBREW_PREFIX/lib/guile/3.0/site-ccache"
export GUILE_SYSTEM_EXTENSIONS_PATH="$HOMEBREW_PREFIX/lib/guile/3.0/extensions"
```

## Try this

```
guile --help
```
Lists the interpreter's options, including how to run a script or start the REPL.

```
guild --help
```
Shows the subcommands of guild, the tool that ships alongside the interpreter.

```
guile-config --help
```
Shows how to query the installed Guile's build and configuration details.

## What's unique

It is a general-purpose Scheme designed from the start to be embedded, and its compiler tooling is open enough that other languages like ECMAScript and Emacs Lisp run on it.

## Caveats

The brief's examples are all Scheme and do not cover embedding in C, and the Homebrew paths and environment variables are specific to the 3.0 series.

## Links

- [Guile homepage](https://www.gnu.org/software/guile/)
