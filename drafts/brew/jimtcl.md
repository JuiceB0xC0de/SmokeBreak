---
name: jimtcl
title: Jim Tcl
source: brew
category: languages-and-oddities
commitment: quick
tags: [c, embeddable, interpreter, language, quick, tcl]
homepage: https://jim.tcl.tk/index.html
scout_score: 5
status: draft
---

# Jim Tcl

**TLDR;** A from-scratch Tcl interpreter in about 14k lines of C, small enough to embed inside another program as its scripting language.

Jim is a small implementation of the Tcl language, written from scratch. It runs ordinary Tcl scripts through the `jimsh` shell. It can also be built into a larger C application so that the application can be scripted in Tcl. The README says it covers many Tcl 8.5 and 8.6 features, such as `{*}`, `dict`, `lassign` and `tailcall`. It leaves out others, including traces and Tk.

The author started it in January 2005 to "vent my need to hack on Tcl". The pitch is Tcl's familiar syntax and tooling in a footprint small enough to ship inside a program or an embedded system. The README puts a build with default extensions at about 130k with `-Os`, or about 85k with no extensions. Extensions load dynamically and some are written in pure Tcl, which keeps the base interpreter small.

The idea underneath is that a scripting language can be a component you carry with your program instead of a system you depend on. Tcl's syntax is regular enough that the whole core fits in roughly 14k lines. Values are dual-ported objects, so a value's string form and its internal form can both be used without converting back and forth. The README also says arrays act as sugar over dicts, and the interpreter has its own garbage collection for lambdas and references. The core is small enough to read, and the README invites you to hack on it for your own application.

The Homebrew package also installs `jimdb`, a debugger, and `build-jim-ext`, a helper for building extensions. The README does not describe either, so check their `--help` output.

## Install

```
brew install jimtcl
```

## Try this

```
jimsh --help
```
Shows how to start the Jim shell and what options it accepts.

```
./configure --help
```
From a source checkout, lists the optional extensions you can enable at build time.

```
jimdb --help
```
Shows usage for the bundled debugger.

## What's unique

It is a full Tcl dialect in a tiny C interpreter, not a new little language. The README says so itself: "Jim is not the next 'little language', but it's a Tcl implementation."

## Caveats

Traces and Tk are not implemented and probably never will be, and the README says speed is faster than Tcl 7.6p2 but slower than Tcl 8.4.

## Links

- [Homepage](https://jim.tcl.tk/index.html)
- [Source repository and README](https://github.com/msteveb/jimtcl)
