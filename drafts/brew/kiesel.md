---
name: kiesel
title: Kiesel
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, engine, javascript, language, zig]
homepage: https://kiesel.dev/
scout_score: 6
status: draft
---

# Kiesel

**TLDR;** A JavaScript engine written from scratch in Zig, installable as a single kiesel executable, for seeing how an ECMAScript engine works without V8 underneath.

Kiesel is described as a JavaScript engine written in Zig. It is not a wrapper around V8 or JavaScriptCore. The Homebrew formula installs one executable, `kiesel`, which presumably runs JavaScript source, though the brief could not confirm inputs, outputs or features.

The idea underneath it is that a JavaScript engine is a program like any other. It has a parser, a representation of the language's semantics, objects, a runtime and a pile of built-in functions, all defined by the ECMAScript specification. Reading or running an engine small enough to follow is a way into how those parts fit together.

The homepage at kiesel.dev renders only a title, "Kiesel JavaScript Engine", to a non-JavaScript fetch, so there is little in the way of stated goals from the author. Treat it as an open door rather than a guided tour: install it, poke at it, and see what it does.

## Install

```
brew install kiesel
```

## Try this

```
kiesel --help
```
Prints the usage text, which is the quickest way to find out what modes and options the executable actually offers.

## What's unique

It is a complete ECMAScript engine built from scratch in Zig rather than a binding to an existing engine, which makes it a possible case study in engine design.

## Caveats

The brief rests on the Homebrew description and scout notes; project status, spec conformance, performance and docs are all unverified.

## Links

- [Homepage](https://kiesel.dev/)
