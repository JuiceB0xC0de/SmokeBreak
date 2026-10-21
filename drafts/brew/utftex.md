---
name: utftex
title: utftex
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [math, quick, tex, tui, unicode, visual]
homepage: https://github.com/bartp5/libtexprintf
scout_score: 6
status: draft
---

# utftex

**TLDR;** Turns TeX-style math into multi-line Unicode text for monospace terminals, so fractions, matrices and Greek letters print in plain output.

utftex takes a LaTeX-like math string as an argument and prints a multi-line rendering using Unicode symbols and box-drawing characters. A fraction becomes a stacked numerator and denominator with a rule between them. Arrays become ruled tables. Operators and Greek letters come from large tables that map LaTeX commands to Unicode code points.

It is built on libtexprintf, a C library with a printf-style API. The author wants the math capabilities of Unicode to be usable in monospace text applications. The project was inspired by asciiTeX and its fork, and it supports much more TeX syntax. A Node.js binding is available through npm.

The idea underneath is a notation-to-text layout engine. Math is two-dimensional, a terminal is a grid of cells, and the program has to decide where each glyph goes. Unicode supplies the vocabulary: mathematical italic and script letters, and combining marks such as the arrow for \vec.

The companion utfstringinfo works the other way. Give it a string and it lists each character's UTF-8 bytes, its Unicode code point, and the utftex command that produces it, if there is one. It is a small way into how Unicode text is put together.

## Install

```
brew install utftex
# Needs a monospace font with good Unicode coverage. The README recommends JuliaMono.
```

## Try this

```
utftex '\frac{\alpha}{\beta+x}'
```
Draws a fraction with alpha over beta+x as a three-line box.

```
utftex -F mathnormal '\frac{1}{a+x}'
```
Renders the variables as Unicode mathematical italic letters.

```
utftex '\vec x'
```
Prints an x with a combining arrow above it. This is a good test of whether your font handles combining marks.

## What's unique

It supports much more TeX syntax than the asciiTeX tools that inspired it, and it ships Unicode tables mapping LaTeX commands to symbols. The utfstringinfo companion also tells you which utftex command produces a given character.

## Caveats

Output depends heavily on your font: non-monospace fonts or missing glyphs misalign the drawing, and combining marks often fail. The brief could not confirm whether the project is currently maintained.

## Links

- [Project homepage (GitHub README)](https://github.com/bartp5/libtexprintf)
- [JuliaMono, the font the README recommends](https://juliamono.netlify.app/)
- [monospacifier, a tool to make a monospace font from a variable-width one](https://github.com/cpitclaudel/monospacifier)
