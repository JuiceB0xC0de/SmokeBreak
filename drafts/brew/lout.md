---
name: lout
title: Lout
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, functional, language, postscript, typesetting]
homepage: https://savannah.nongnu.org/projects/lout
scout_score: 6
status: draft
---

# Lout

**TLDR;** A document formatter in the LaTeX family, built on a purely functional language, that turns plain-text descriptions into PostScript.

Lout is a document formatting system written by Jeffrey Kingston at the Basser Department of Computer Science, University of Sydney. It reads a high-level plain-text description of a document, similar in style to LaTeX, and produces PostScript for laser printers and graphic displays. A plain-text output mode exists too, and so does a PDF mode the project calls highly experimental.

The interesting part is what sits underneath. Most typesetting and layout in Lout is implemented in the Lout language itself, which is purely functional. In the project's words, this "simplifies reasoning about the operations performed." Layout becomes a matter of functions applied to content rather than a pile of macros rewriting each other.

Lout also treats multilingual support as a core design feature rather than an add-on. The project says it is "inherently multilingual" and lists 16 supported languages. It is a way to see how a typesetting system might look if designed as a language from the start, as a contrast to TeX.

The brief could not reach the README or the author's documentation, so the details of the markup syntax are not covered here. The Homebrew formula also installs a second executable, prg2lout, whose purpose is not described in the brief.

## Install

```
brew install lout
```

## Try this

```
lout --help
```
Prints the usage summary and the list of command-line options, a first look at what the formatter accepts.

```
prg2lout --help
```
Shows the usage for the second installed tool, which the formula ships alongside lout.

## What's unique

A TeX-style formatter whose layout language is purely functional and multilingual by design, from a single university author rather than the TeX lineage.

## Caveats

The built-in PDF output is described as highly experimental, so the project suggests generating PostScript and converting it with GhostScript; recent activity is unknown.

## Links

- [Savannah project page](https://savannah.nongnu.org/projects/lout)
