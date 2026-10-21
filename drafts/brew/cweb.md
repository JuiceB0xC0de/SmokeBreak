---
name: cweb
title: cweb
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, c, knuth, literate-programming, tex]
homepage: https://cs.stanford.edu/~knuth/cweb.html
scout_score: 7
status: draft
---

# cweb

**TLDR;** Knuth and Levy's literate programming system: write one file of prose and C, then get both a compilable program and a typeset, cross-indexed document.

CWEB works from a single source file, `foo.w`, that mixes explanation with code. Two programs read it. `ctangle` pulls the code out and writes `foo.c`, ready for a compiler. `cweave` takes the same file and writes `foo.tex`, a typeset document with cross-references and an index. Since version 3.61 the weaver can also produce PDF with clickable links, through standard TeX with dvipdfm or through pdfTeX.

The idea comes from WEB, which Donald Knuth developed while writing TeX. Silvio Levy adapted it to C in 1987, and it later grew to cover C++ and ANSI C. The stated premise: "The main idea is to regard a program as a communication to human beings rather than as a set of instructions to a computer." You order the program for a reader, not for the compiler, and the tools rearrange it afterwards.

That inversion is the door. Once you write code in the order you would explain it, comments stop being an afterthought and the source becomes a document someone can read start to finish. Much of the later literate programming and notebook tradition descends from this approach.

The tools are old and declared finished. The authors say they do not intend to change CWEB "unless some devastating new bug is discovered." For a developer tool, that is a rare stance. Work on a CWEB 4.0 continues in a separate development project that the homepage links.

## Install

```
brew install cweb
# PDF output also needs TeX, plus dvipdfm or pdfTeX
```

## Try this

```
ctangle --help
```
Shows how ctangle is invoked; it is the half that turns a .w file into compilable C.

```
cweave --help
```
Shows how cweave is invoked; it is the half that turns a .w file into a TeX document.

## What's unique

One file is both the program and its cross-indexed typeset explanation, and the original authors consider the tools complete and frozen.

## Caveats

The homepage is the authors' page for a 1993 book that is out of print, and old .w files may format oddly because newer C++ reserves words like `not` and `xor`; a line like `@s not_eq normal` fixes it.

## Links

- [CWEB homepage (Knuth and Levy)](https://cs.stanford.edu/~knuth/cweb.html)
