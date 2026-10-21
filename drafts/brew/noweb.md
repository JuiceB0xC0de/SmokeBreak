---
name: noweb
title: noweb
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, documentation, literate-programming, tex]
homepage: https://www.cs.tufts.edu/~nr/noweb/
scout_score: 6
status: draft
---

# noweb

**TLDR;** A small literate-programming tool: write prose and named code chunks in one file, then weave it into a document or tangle it into compilable source.

noweb belongs to the WEB family of literate-programming tools. You write a single source file that mixes explanation with named code chunks, referenced as <<name>>. Two programs then read that file. The weave side produces a document for people, with back ends for TeX, LaTeX, HTML and troff. The tangle side expands the chunks and pulls out the code in the order a compiler needs.

Norman Ramsey built it to keep literate programming simple and extensible. It is largely language-independent, and the homepage says it works "out of the box" with any programming language. It uses 5 control sequences where WEB uses 27. Ramsey dropped WEB's pretty-printing on purpose. He finds it distracting while editing and too costly to build for every language, so prettyprinting is left to optional filters.

The idea underneath is the one stated on the homepage: "Literate programming is the art of preparing programs for human readers." The source file is arranged for the reader's understanding, not the compiler's, and the tool reorders it for the machine. The design is also small and open. The homepage says a simple back end can be written in about 40 lines of awk and a fuller one in about 250, so you can read how it works and change it without recompiling anything.

The project is old, around thirty-five years by the homepage's count, and it has been used for tens of thousands of lines of code across many languages.

## Install

```
brew install noweb
# LaTeX output may need the TeX support files on your path:
# add $HOMEBREW_CELLAR/noweb/2.13/tex/generic/noweb to TEXINPUTS
# depends on icon (installed by brew); LaTeX output also needs a TeX installation
```

## Try this

```
notangle --help
```
Shows the options for the tangle side, which extracts compilable code from a noweb file.

```
noweave --help
```
Shows the options for the weave side, which produces TeX, LaTeX, HTML or troff documentation.

```
noroots --help
```
Shows how to list the top-level chunks in a noweb file, the ones not referenced by any other chunk.

## What's unique

It is deliberately minimal and language-agnostic, with 5 control sequences, plain-ASCII source, and back ends small enough to write in a few dozen lines of awk.

## Caveats

The author advises using the 2.x line over the Noweb 3 alpha, code is seldom prettyprinted by default, and LaTeX output needs the TEXINPUTS step.

## Links

- [noweb home page (Norman Ramsey, Tufts)](https://www.cs.tufts.edu/~nr/noweb/)
