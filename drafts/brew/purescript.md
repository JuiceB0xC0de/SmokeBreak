---
name: purescript
title: PureScript
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, functional, haskell-like, javascript, language, types]
homepage: https://www.purescript.org/
scout_score: 5
status: draft
---

# PureScript

**TLDR;** A small, strongly typed, Haskell-inspired language that compiles to readable JavaScript, giving you a serious type system in the browser and Node.

PureScript is a functional language whose compiler, `purs`, takes PureScript source and emits JavaScript. The output is meant to be readable, and it can call existing JavaScript code, so it can run in a browser or under Node alongside whatever you already have.

The type system is the main draw. It has algebraic data types, type classes with functional dependencies, higher-kinded types, higher-rank polymorphism, and row polymorphism, which is how it types extensible records. The project describes itself as "a small strongly typed programming language with expressive types that compiles to JavaScript, written in and inspired by Haskell." The compiler itself is written in Haskell.

It is a useful door into typed functional programming if you have heard of Haskell but would rather see the ideas applied to a JavaScript target. It is Haskell-inspired, not Haskell, so expect differences. The brief did not cover compiler internals, so the best way to see what the language does is the PureScript By Example book or the in-browser editor.

## Install

```
brew install purescript
# Spago, the recommended build tool, installs separately: npm install -g spago
# Needs Node and npm to run the generated JavaScript and manage JS dependencies.
```

## Try this

```
purs --help
```
Lists the compiler's subcommands, so you can see what the compiler offers.

```
npm install -g spago
```
Installs Spago, which the homepage calls the recommended build tool for PureScript projects.

## What's unique

It brings a Haskell-style type system, including row polymorphism and extensible records, to the JavaScript ecosystem while keeping the output readable and interoperable with existing JS.

## Caveats

The homepage's npm instructions cite a Node 8 minimum that is probably out of date, and I could not confirm recent release activity from the pages read.

## Links

- [PureScript homepage](https://www.purescript.org/)
- [GitHub repository and releases](https://github.com/purescript/purescript)
- [PureScript By Example book](https://book.purescript.org/)
- [Try PureScript in the browser](http://try.purescript.org)
- [Pursuit package index](http://pursuit.purescript.org/)
