---
name: coccinelle
title: Coccinelle
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, linux-kernel, ocaml, refactoring, source-transformation]
homepage: https://coccinelle.gitlabpages.inria.fr/website/
scout_score: 7
status: draft
---

# Coccinelle

**TLDR;** Coccinelle rewrites C code by matching its structure instead of its text, using semantic patches the Linux kernel community relies on for large API changes.

Coccinelle is a program matching and transformation engine for C. You write a semantic patch in SmPL (Semantic Patch Language), a file ending in `.cocci` that describes a piece of C code and the edit to make to it. Then you run `spatch` over C source files, and it produces rewritten C. The README describes the result as style-preserving source-to-source transformation, so the output keeps the formatting of the original.

It began with a Linux problem. Per the homepage, it was "initially targeted towards performing collateral evolutions in Linux": when a library API changes, every piece of client code has to change with it. That might mean renaming a function, adding an argument that depends on context, or reorganizing a data structure. Doing that by hand across thousands of files is error-prone, and a regular expression can't tell what the code means.

The idea underneath is that a change to code can itself be written as a patch-like description, matched against program structure rather than characters. The same mechanism is also used, in the homepage's words, "for finding and fixing bugs in systems code." The homepage says semantic patches for Linux live in the kernel's scripts directory, so this is part of how kernel changes actually get made.

The package installs two executables, `spatch` and `spgen`. The brief does not explain what `spgen` does, so start with `spatch`.

## Install

```
brew install coccinelle
# Optional: OCaml scripting in SmPL needs an OCaml install; Python scripting needs Python development files. No account needed.
```

## Try this

```
spatch --help
```
Lists the options spatch accepts, a first look at how it is driven.

```
spatch --sp-file demos/simple.cocci demos/simple.c -o /tmp/new_simple.c
```
Runs the README's demo: applies the semantic patch simple.cocci to demos/simple.c and writes the rewritten C to /tmp/new_simple.c. Run it from a checkout of the source repository, which contains the demos folder.

## What's unique

It matches C by structure rather than text and rewrites in place while keeping the original formatting. It is also a tool the Linux kernel actually uses for sweeping changes.

## Caveats

Maintenance status is unclear: the GitHub page is a mirror of the Inria repository and the brief could not confirm a recent commit or release date.

## Links

- [Coccinelle homepage](https://coccinelle.gitlabpages.inria.fr/website/)
- [Downloads (precompiled binaries and distro packages)](https://coccinelle.gitlabpages.inria.fr/website/download.html)
- [GitHub mirror (source and README)](https://github.com/coccinelle/coccinelle)
