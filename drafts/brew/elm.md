---
name: elm
title: Elm
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, functional, javascript, language, web]
homepage: https://elm-lang.org
scout_score: 6
status: draft
---

# Elm

**TLDR;** A small functional language that compiles to JavaScript, built around one architecture and a promise of no runtime errors in practice.

Elm is a functional language for websites and web apps. You write Elm source files and the compiler outputs JavaScript that runs in the browser. The official guide describes it as "a functional language that compiles to JavaScript. It helps you make websites and web apps."

Every Elm program follows The Elm Architecture. There is a model, an `init` value, an `update` function that takes a message and the current model and returns a new model, and a `view` function that renders the model to HTML. The guide's sample is a counter: a `Msg` type with `Increment` and `Decrement`, wired together with `Browser.sandbox`.

The guide says Elm's guarantees come from the language design, not from stacking JavaScript libraries. It lists them: no runtime errors in practice, friendly error messages, reliable refactoring, and enforced semantic versioning for packages. That last one means the compiler checks that a version bump matches the API change.

The larger idea is that state, change and display can be separated this cleanly, and that a compiler can enforce it. The guide claims these ideas carry over to JavaScript, and that a real Elm project will leave you "writing better JavaScript code." That is the project's own claim, not something checked here.

## Install

```
brew install elm
```

## Try this

```
elm --help
```
Lists the compiler's subcommands, a first look at what the tool can do.

## What's unique

The language promises no runtime errors in practice, and its package manager has the compiler enforce semantic versioning against actual API changes.

## Caveats

The brief found no release dates or commit history, so whether Elm is actively maintained is unknown, and the guarantees quoted are the project's own claims.

## Links

- [Elm homepage](https://elm-lang.org)
- [An Introduction to Elm (guide)](https://guide.elm-lang.org)
- [Elm docs](https://elm-lang.org/docs)
