---
name: sparse
title: Sparse
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, linux-kernel, parsers, static-analysis]
homepage: https://sparse.wiki.kernel.org/
scout_score: 6
status: draft
---

# Sparse

**TLDR;** Linus Torvalds's semantic C checker, which uses annotations in ordinary C to catch mixups like kernel pointers passed where user-space pointers belong.

Sparse is a C parser that builds a full semantic parse tree for a source file, handling most of ANSI C and many GCC extensions. It ships with sample back ends, one of which is a static analyzer also called sparse. The brew formula installs two executables, `sparse` and `cgcc`; the brief does not verify what `cgcc` does.

The homepage says Linus Torvalds started it in 2003 to catch problems such as mixing pointers into user address space with pointers into kernel address space. Those two kinds of pointers look identical to a normal compiler. Sparse lets you label them in the source, then checks that the labels stay consistent.

That is the idea underneath: a set of annotations that carry meaning about types, such as which address space a pointer belongs to, or which locks a function acquires or releases. In the project's words: "Sparse provides a set of annotations designed to convey semantic information about types, such as what address space pointers point to, or what locks function acquires or releases." It is a way to see how the Linux kernel polices itself with extra type information layered on plain C.

Internally, the older GitHub README describes five phases: tokenizing the whole file, preprocessing, semantic parsing, lazy type evaluation, and inline function expansion with tree simplification. Types are only computed when a back end asks. The parser needs the whole file before it gives any result. The same README calls it a library with "one mission in life: create a semantic parse tree for some arbitrary user for further analysis."

## Install

```
brew install sparse
# needs a C build toolchain only if you build from source instead:
# git clone git://git.kernel.org/pub/scm/devel/sparse/sparse.git && cd sparse && make && make install
```

## Try this

```
sparse --help
```
Lists the analyzer's command-line options, including which warnings it can turn on or off.

```
cgcc --help
```
Shows the options for the second executable the formula installs.

## What's unique

It is a small, lazily typed parser built for analysis tools rather than a compiler, and its annotations let authors describe address spaces and locking in ordinary C.

## Caveats

The brief found no sample output, license text or platform list, and the GitHub mirror README is older and describes it differently from the homepage, so check the kernel.org docs for current status.

## Links

- [Sparse documentation homepage](https://sparse.wiki.kernel.org/)
- [GitHub mirror (lucvoo/sparse)](https://github.com/lucvoo/sparse)
- [Release tarballs and signatures (kernel.org)](https://www.kernel.org/pub/software/devel/sparse/dist/)
