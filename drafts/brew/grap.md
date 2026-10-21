---
name: grap
title: grap
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, bell-labs, graphs, language, pic, troff, typesetting]
homepage: https://www.lunabase.org/~faber/Vault/software/grap/
scout_score: 7
status: draft
---

# grap

**TLDR;** A Bell Labs-era language for describing graphs as text and typesetting them inside troff or TeX documents, still being updated in 2025.

Grap is a small language for describing graphs so they can be dropped into typeset documents. It is a preprocessor: grap input is translated into pic, Kernighan's language for drawing diagrams, and whatever system runs pic takes it from there. The homepage says both groff and TeX can use it.

It was specified and first implemented by Brian Kernighan and Jon Bentley at Bell Labs. The free troff, groff, shipped without it. Ted Faber, who maintains this version, says of groff's author: "For some reason, when James J. Clark implemented groff, a free version of troff and associated tools, he didn't implement grap. I finally wanted to use it badly enough that I wrote it."

The idea underneath is the old Unix one: small languages that each do one job and feed the next. A graph is not a picture you draw with a mouse, it is a description that compiles to another description, which compiles to a page. Reading grap is a way into how troff-era documents were built, and why plotting once lived inside the typesetter.

The project is not frozen. Version 1.49 was released on 16 April 2025, with a fix for a mishandled undefined value. The author says it is "probably worth upgrading to".

## Install

```
brew install grap
# grap only emits pic code. To get a finished page you also need a pic-capable system such as groff or TeX.
```

## Try this

```
grap --help
```
Prints the usage summary for the grap executable, a safe first look at what the installed version accepts.

## What's unique

It is a graph language from the original Bell Labs troff toolchain, written as a text-to-text preprocessor for pic rather than as a plotting program with its own output. Its author still maintains it.

## Caveats

It does nothing alone, since it needs pic and a troff or TeX toolchain, and the brief did not cover the input syntax, so expect to read the man pages.

## Links

- [Grap homepage (Ted Faber)](https://www.lunabase.org/~faber/Vault/software/grap/)
