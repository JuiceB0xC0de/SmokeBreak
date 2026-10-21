---
name: thrax
title: Thrax
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, fst, grammar, linguistics, nlp, openfst]
homepage: https://www.openfst.org/twiki/bin/view/GRM/Thrax
scout_score: 5
status: draft
---

# Thrax

**TLDR;** Write grammars as short readable scripts and compile them into finite-state transducers that tokenise text, spell out numbers, or model word morphology.

Thrax is a set of command-line tools from the OpenGrm project. You write `.grm` source files that combine regular expressions with context-dependent rewrite rules. The compiler turns each file into an FST archive (`.far`), a weighted finite-state transducer that maps input strings to output strings. The README's example grammar tokenises English, turning "Well, I can't eat muffins" into "Well , I ca n't eat muffins", and it also spells out numbers, so it doubles as a text normaliser.

A grammar file has an Imports section and a Body of functions and statements. Other grammars can import a compiled archive by alias. The language has operators for concatenation, union, composition, rewrite and `CDRewrite` for context-dependent rules, plus Feature, Category and Paradigm tools for morphology. It builds on the OpenFst library.

The idea underneath is that a lot of language processing, such as text normalisation, tokenising and inflecting words, can be written as rules and compiled into one machine that is composable and fast. Plain finite-state rewriting cannot handle nesting or copying, so Thrax adds pushdown (PDT) and multi-pushdown (MPDT) extensions. The MPDT example handles reduplication, turning "kidongo" into "kididongo".

The name comes from Dionysius Thrax, "the reputed first Greek grammarian".

## Install

```
brew install thrax
# Pulls in openfst as a dependency. The homepage also lists: conda install -c conda-forge thrax (Linux x86 and Mac OS X, for people who already use conda).
```

## Try this

```
thraxmakedep example.grm
```
Generates a Makefile for the sample grammar, which the Quick Tour has you copy to a writable directory first.

```
make
```
Builds example.far from the grammar, using the Makefile that thraxmakedep created.

```
thraxrewrite-tester --far=example.far --rules=TOKENIZER
```
Starts an interactive session where each line you type is run through the TOKENIZER rule and the rewritten text is shown.

## What's unique

The grammar language is short and readable for FST work, with named functions, imports and string literals. The pushdown extensions let the same toolkit express nesting and reduplication, which plain finite-state rewriting cannot.

## Caveats

Documentation is on an older TWiki, with the Quick Tour last edited in 2019, and thraxrewrite-tester only works with grammars compiled to standard (tropical) arcs.

## Links

- [Thrax homepage (OpenFst TWiki)](https://www.openfst.org/twiki/bin/view/GRM/Thrax)
- [Thrax Quick Tour](https://www.openfst.org/twiki/bin/view/GRM/ThraxQuickTour)
