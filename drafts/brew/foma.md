---
name: foma
title: foma
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, automata, language, library, linguistics]
homepage: https://github.com/mhulden/foma
scout_score: 7
status: draft
---

# foma

**TLDR;** A finite-state compiler for building transducers, the machines computational linguists use to turn words into their parts and back again.

foma compiles regular expressions into finite-state transducers, which are automata that read one string and write another. In computational morphology, that lets a single machine map a surface word like "running" to an analysis, and run the same machine in reverse to generate words. The README is one line: "Finite-state transducer technology." Everything below that line comes from the package listing and the scout's notes.

The Homebrew package installs three executables: `foma`, `flookup`, and `cgflookup`. The README does not say what they do. Going by the names, `foma` is the interactive compiler and the other two look up words in compiled machines, but that is inference, not documentation. The project is also a C library, so the same machinery can be embedded in other programs.

The idea underneath is that a lot of language structure, such as inflection, stems, and sound changes, can be written as regular expressions and compiled into automata. It is a different way to think about language than parsing or statistical models, and it is a door into a long tradition of rule-based linguistics tooling. The repository says its wiki was exported from code.google.com/p/foma, so the project is old enough to have started on Google Code.

## Install

```
brew install foma
```

## Try this

```
foma --help
```
Prints the options for the main compiler and interactive shell.

```
flookup --help
```
Shows how the lookup tool is invoked.

```
cgflookup --help
```
Shows the options for the third executable, which the README does not explain.

## What's unique

It is a working finite-state toolkit that is also an embeddable C library. It can be built to WebAssembly, with a demo page for testing regular expressions in a browser.

## Caveats

The README is very thin and does not explain the regular expression syntax or what the three executables do, and the wiki was not reachable from the brief, so expect to find documentation elsewhere.

## Links

- [GitHub homepage and README](https://github.com/mhulden/foma)
