---
name: bas55
title: bas55
source: brew
category: languages-and-oddities
commitment: quick
tags: [basic, ecma-55, interpreter, language, quick, retro]
homepage: https://jorgicor.niobe.org/bas55/
scout_score: 7
status: draft
---

# bas55

**TLDR;** A small interpreter for ECMA-55 Minimal BASIC, the 1978 standard, tested against the US National Bureau of Standards conformance programs.

bas55 implements Minimal BASIC as defined by the ECMA-55 standard. It provides an interpreter and an editor with line renumbering. The homepage calls it a complete system, and a Windows build is offered as a zip of the same tools.

Minimal BASIC is the stripped-down core of the language: numbered lines, a handful of statements, no frills. ECMA-55 pins that core down in a short formal document, which makes it a rare case of BASIC having a real specification. Most BASICs that people remember are vendor dialects, each different. This one follows the written standard.

The author says the interpreter was tested against the National Bureau of Standards Minimal BASIC test programs, so conformance seems to be a real goal rather than a nostalgia gesture. That makes it a way to see what BASIC looked like before dialects diverged, and a small example of how a language standard gets checked against an implementation.

The README is thin and gives no motivation or usage walkthrough, so the online manual is the place to learn how to run programs.

## Install

```
brew install bas55
```

## Try this

```
bas55 --help
```
Prints the interpreter's usage and options, the quickest way to learn how to run a program file.

## What's unique

Few modern tools implement Minimal BASIC as the ECMA-55 standard defines it. This one checks itself against the NBS conformance test suite and bundles a renumbering editor.

## Caveats

The README has no usage steps, so you will need the online manual, and the project appears maintained but not very actively developed.

## Links

- [Homepage](https://jorgicor.niobe.org/bas55/)
- [Source repository (GitHub)](https://github.com/jorgicor/bas55)
- [ECMA-55 standard](https://www.ecma-international.org/publications-and-standards/standards/ecma-55/)
