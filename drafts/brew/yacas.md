---
name: yacas
title: Yacas
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, cas, language, math, symbolic]
homepage: https://www.yacas.org/
scout_score: 6
status: draft
---

# Yacas

**TLDR;** Yacas is a small computer algebra system with its own scripting language, where you write the rules that transform mathematical expressions.

Yacas, short for Yet Another Computer Algebra System, manipulates mathematical expressions symbolically. You type expressions in ordinary infix notation, and it works on them as symbols rather than just numbers. The core engine also does arbitrary-precision arithmetic.

The README describes it as "small and highly flexible" and says it "serves as a free alternative to commercial CAS software." It ships with a modest library of mathematical functions, but the project says that is not the main draw: "its real strength is in the language in which you can easily write your own symbolic manipulation algorithms."

That is the idea underneath it. A parser reads expressions, and the engine applies rules to them. Since the rules are user-defined, the built-in library is a set of examples more than a ceiling. Symbolic algebra is a rewriting system you can open up and extend, and Yacas lets you see that from the inside. The docs list a Reference Manual, a Programming in Yacas guide, and a Book of Algorithms, which look like the natural next steps.

There is also a browser demo, Yacas Online, linked from the homepage, if you want to try the language before installing anything.

## Install

```
brew install yacas
```

## Try this

```
yacas --help
```
Prints the command-line options, a safe first look at how the executable is invoked.

## What's unique

It is a self-contained CAS with its own rule-writing language, not a wrapper around another system, and its stated strength is writing your own symbolic algorithms.

## Caveats

The brief could not confirm how recently the project has been updated; the homepage lists release 1.9.1 but no dates, and the docs were only seen as a table of contents.

## Links

- [Homepage](https://www.yacas.org/)
- [GitHub repository (README)](https://github.com/grzegorzmazur/yacas)
- [Documentation](https://yacas.readthedocs.io/en/latest/)
- [Getting started guide](https://yacas.readthedocs.io/en/latest/getting_started/index.html)
