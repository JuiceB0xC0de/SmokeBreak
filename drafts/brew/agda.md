---
name: agda
title: Agda
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, emacs, functional, language, proofs, type-theory]
homepage: https://wiki.portal.chalmers.se/agda/
scout_score: 7
status: draft
---

# Agda

**TLDR;** A programming language where types can depend on values, so a program's type can carry a machine-checked proof about what it does.

Agda is a dependently typed functional language and an interactive proof assistant in one. Types are allowed to mention values. The standard example from the project's own description is the type of vectors of a given length, so a function that appends two vectors can state in its type that the result's length is the sum of the two. The checker verifies that claim before the program runs.

The idea underneath is that a type is a proposition and a program is its proof. The wiki frames Agda as a tool for constructive mathematics, based on Per Martin-Löf's intuitionistic type theory. It sits alongside other dependent-type proof assistants such as Rocq, Epigram, Matita and NuPRL. It supports inductive families, parametrised modules, mixfix operators and Unicode, so the source can look much closer to written mathematics than to typical code.

The usual workflow runs through an Emacs interface, agda-mode. You leave holes in a program and the editor helps you fill them, using the type as guidance. The compiler can also produce executables. The package ships agda2hs as well, which translates Agda code to Haskell, plus als, an executable the brief does not describe.

There is a browser-based Agda Pad if you want a taste before installing anything.

## Install

```
brew install agda
# to use the installed Agda libraries, brew says to run:
mkdir -p $HOME/.config/agda
cp $HOMEBREW_PREFIX/opt/agda/share/agda/example-libraries $HOME/.config/agda/libraries
cp $HOMEBREW_PREFIX/opt/agda/share/agda/example-defaults $HOME/.config/agda/defaults
# redo the copies after upgrading from an earlier version
# the interactive workflow expects Emacs; the Agda Standard Library is a separate download
```

## Try this

```
agda --help
```
Lists the type checker and compiler options.

```
agda-mode --help
```
Shows the helper used to set up the Emacs interface, where the interactive proof workflow lives.

```
agda2hs --help
```
Shows the options for translating Agda code to Haskell.

## What's unique

One language is both the programming language and the proof checker, so a specification lives in the type and is verified by the compiler. The editor-driven, Unicode-heavy workflow makes it feel unlike mainstream languages.

## Caveats

The learning curve is steep, the library setup needs manual copying into ~/.config/agda after install and after upgrades, and the standard library is documented separately on the wiki.

## Links

- [Agda Wiki (homepage)](https://wiki.portal.chalmers.se/agda/)
- [User manual](http://agda.readthedocs.io)
- [Agda source on GitHub](https://github.com/agda/agda)
