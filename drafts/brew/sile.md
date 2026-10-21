---
name: sile
title: SILE
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, fonts, lua, pdf, tex, typesetting]
homepage: https://sile-typesetter.org
scout_score: 6
status: draft
---

# SILE

**TLDR;** A typesetting system in the spirit of TeX, scriptable in Lua, that turns plain-text source or XML into a printed-quality PDF.

SILE takes a source document, such as a `.sil` file, and lays it out as a PDF. It is conceptually close to TeX and borrows some of its concepts and algorithms, but it is not a TeX derivative. The README calls it "a new typesetting and layout engine written from the ground up using modern technologies and borrowing some ideas from graphical systems such as InDesign."

Underneath, the command line is a Rust binary with a Lua VM built in (since v0.15.0), and a pure-Lua command line remains as `sile-lua`. Documents and extensions are scripted in Lua: "SILE is completely programmable using the Lua programming language." Text shaping goes through HarfBuzz and fontconfig, ICU handles Unicode, and PDF output uses libtexpdf, a PDF library extracted from TeX. Third-party packages come in through LuaRocks.

The door it opens is how a page actually gets made: line breaking, frames, text set on a grid. The README says it can also take XML straight to PDF without XSL stylesheets. If you have ever wondered what TeX does and whether you could change it with a scripting language you already know, SILE is a readable place to look.

## Install

```
brew install sile
# Homebrew does not install the default fonts. Without them the examples will not work unless modified:
brew install --cask font-gentium-plus
brew install --cask font-libertinus
brew install --cask font-hack
```

## Try this

```
sile --help
```
Lists the command line options of the Rust-based CLI.

```
sile test.sil
```
Renders a one-line test document to test.pdf, which also checks that the install and fonts work.

```
sile-lua --help
```
Shows the options of the pure-Lua command line that predates the Rust binary.

## What's unique

It is a TeX-inspired typesetter written in Lua rather than a TeX derivative, so both documents and extensions are plain Lua scripts. It also offers frame-based page layout and grid typesetting.

## Caveats

There is no Windows support (the README expects it to be broken, and points to WSL), and the default font is in flux: Homebrew's caveat names Gentium Plus while the README says v0.15.14 switches to Gentium Book.

## Links

- [Homepage](https://sile-typesetter.org)
- [GitHub repository](https://github.com/sile-typesetter/sile)
- [Full manual (PDF)](http://sile-typesetter.org/manual/sile-latest.pdf)
- [Examples gallery](http://www.sile-typesetter.org/examples/)
