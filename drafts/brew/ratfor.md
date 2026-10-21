---
name: ratfor
title: ratfor
source: brew
category: languages-and-oddities
commitment: quick
tags: [ancient, fortran, language, preprocessor, quick]
homepage: http://www.dgate.org/ratfor/
scout_score: 6
status: draft
---

# ratfor

**TLDR;** A preprocessor that turns Rational Fortran, Fortran with structured control flow, into plain FORTRAN 77, a working piece of the Software Tools era.

Ratfor is short for Rational FORTRAN. The `ratfor` command reads source written in that dialect and writes FORTRAN 77, which you then hand to a separate compiler such as GNU Fortran. It is a translator, not a compiler.

The idea is to write Fortran with saner control structures than the language itself offered, and let a small tool produce the verbose output. The project page notes that Ratfor was used in Kernighan and Plauger's Software Tools. That is the door into something larger: a language grown as a thin layer over another language, and the long tradition of preprocessors that fix a host language's rough edges.

This version is derived from public domain ratfor 1.0 and is still being patched. The latest release, 1.07, is dated 2025-01-13, and the recent changes are bug fixes and buffer-overrun hardening rather than new features. The README does not explain how the translation works internally, so reading the generated FORTRAN 77 for yourself is the way to see it.

## Install

```
brew install ratfor
# You also need a FORTRAN 77 compiler to build the output, such as GNU Fortran from GCC. Homebrew's gcc is listed as a dependency.
```

## Try this

```
ratfor --help
```
Prints the tool's usage, a quick check that it installed and which options it accepts.

## What's unique

It is a preprocessor from the Software Tools era that is still being patched, with its public-domain lineage spelled out on the project page.

## Caveats

Output is FORTRAN 77 only, so you need a separate compiler, and the README does not describe the full Ratfor syntax.

## Links

- [Linux Ratfor homepage](http://www.dgate.org/ratfor/)
