---
name: ditaa
title: ditaa
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [ascii-art, diagrams, images, java, quick]
homepage: https://ditaa.sourceforge.net/
scout_score: 7
status: draft
---

# ditaa

**TLDR;** Draw boxes and arrows with plain characters in a text file, run ditaa, and get a clean bitmap diagram back.

ditaa is a small command-line utility written in Java. It reads a text file containing a diagram made of characters like `|`, `-`, `+`, `/` and `\`, and writes out an image, PNG by default. It can also process HTML files, replacing the contents of `pre class='textdiagram'` blocks with generated `<img>` tags.

The author, Stathis Sideris, lists several reasons for building it. One was plain curiosity: "Simply for hack value. I wanted to know if/how it could be done and how easily." Others were modernising old ASCII diagrams in legacy FAQs and embedding diagrams in text formats like HTML, DocBook, LaTeX and code comments.

The idea underneath is that the drawing is the source. ditaa reads the ASCII as a set of open and closed shapes and renders them as graphics. There is no separate diagram language to learn first. A little extra markup goes a long way: colour codes such as `cRED` or a hex `cXXX`, tags like `{d}`, `{s}` and `{io}` for special symbols, dashed lines when a line contains `=` or `:`, and rounded corners where `/` and `\` meet. The homepage calls it "a diagram markup language, with very loose syntax."

Because the diagram stays editable text, it can be diffed, kept in a comment, and re-rendered later by a newer version with no edits.

## Install

```
brew install ditaa
# depends on openjdk; ditaa runs on a Java runtime
```

## Try this

```
ditaa --help
```
Prints the option help. The homepage says running the jar with no arguments does the same.

```
java -jar ditaaXXX.jar
```
Runs ditaa directly from a downloaded jar (XXX is the version) and prints its options if given no arguments.

## What's unique

There is no separate diagram language to learn. The ASCII drawing is the source, and loose rules let colour, dashes and rounded corners come from a few extra characters.

## Caveats

The homepage is undated and partly out of date, pointing at SourceForge, Subversion and versions 0.6b and 0.8, and some features are marked experimental or unfinished.

## Links

- [ditaa homepage](https://ditaa.sourceforge.net/)
