---
name: hy
title: Hy
source: brew
category: languages-and-oddities
commitment: quick
tags: [language, lisp, macros, python, quick, repl]
homepage: https://github.com/hylang/hy
scout_score: 5
status: draft
---

# Hy

**TLDR;** A Lisp that compiles to Python's own syntax tree, so you can write parentheses and still call any Python library.

Hy reads Lisp source, typed at a REPL or saved in .hy files, and turns it into Python abstract syntax tree objects. Python then runs those objects like any other Python code. Because there is no separate runtime in between, Python modules and functions are usable directly from Lisp forms.

The README states the motivation plainly: "Lisp and Python should love each other. Let's make it happen." The pitch is that you keep "the whole beautiful world of Python at your fingertips, in Lisp form."

The idea underneath is that a language can be a different front end onto an existing runtime. Python's AST is a data structure, and Hy shows what happens when you generate it from s-expressions instead of from Python's usual syntax. It is a cheap way to see how a Lisp feels when it has pip's whole ecosystem behind it.

Homebrew also installs two other executables, hy2py and hyc. The README does not say what they do, so try their --help output before assuming anything.

## Install

```
brew install hy
# Homebrew pulls in its own Python as a dependency. The README's own route is: pip3 install --user hy
```

## Try this

```
hy
```
Starts an interactive REPL where you can type Lisp forms and call Python from them.

```
hy myprogram.hy
```
Runs a Hy program from a .hy file you have written.

```
hy2py --help
```
Shows the options for hy2py, one of the extra executables the README leaves undescribed.

## What's unique

Hy compiles straight to Python AST rather than to a separate runtime, so Lisp code gets Python's libraries without a bridge layer. There is also a web console at hylang.org/try-hy if you want to try it before installing.

## Caveats

It is not a standalone Lisp: it runs on Python and inherits its runtime, and the README says nothing about performance or which Python features differ.

## Links

- [Hy on GitHub (homepage)](https://github.com/hylang/hy)
- [The Hy homepage](http://hylang.org)
- [Documentation](http://hylang.org/hy/doc)
- [Try Hy with a web console](http://hylang.org/try-hy)
