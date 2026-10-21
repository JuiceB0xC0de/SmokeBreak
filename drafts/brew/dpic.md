---
name: dpic
title: dpic
source: brew
category: languages-and-oddities
commitment: quick
tags: [ancient, diagrams, language, latex, quick, svg]
homepage: https://ece.uwaterloo.ca/~aplevich/dpic/
scout_score: 5
status: draft
---

# dpic

**TLDR;** dpic compiles pic, a small text language for describing diagrams, into SVG, PDF, PostScript, LaTeX or xfig drawings.

dpic is an implementation of pic, a "little language" for drawing diagrams from a text description. You write the diagram as source, and dpic compiles it into a drawing. The homepage lists output for LaTeX, PDF, SVG, PostScript and xfig 3.2, so one source file can feed several toolchains.

Pic comes from the 1980s Unix typesetting world, where documents were built from small tools that each did one job in a pipe. The idea is that a diagram is a program: you describe the shapes and how they relate, and the layout follows. That makes diagrams diffable, scriptable and easy to keep in version control.

The pages available for this entry did not show the input syntax or a worked example, so this entry does not describe the language itself. The manual linked from the homepage is the place to start. The project is still distributed: the homepage offers version 2025.08.01 with a changelog.

## Install

```
brew install dpic
```

## Try this

```
dpic --help
```
Prints the usage text and the list of options, including how to choose an output format.

## What's unique

It is a still-distributed implementation of a long-lived text-diagram language, with several output back ends from the same source.

## Caveats

The README and manual could not be read when this entry was researched, so the input syntax and exact workflow are unverified here.

## Links

- [dpic homepage](https://ece.uwaterloo.ca/~aplevich/dpic/)
- [dpic GitLab repository](https://gitlab.com/aplevich/dpic)
