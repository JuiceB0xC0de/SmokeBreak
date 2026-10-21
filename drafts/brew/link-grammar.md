---
name: link-grammar
title: link-grammar
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, language, library, linguistics, nlp, parser]
homepage: https://github.com/opencog/link-grammar
scout_score: 7
status: draft
---

# link-grammar

**TLDR;** A parser that draws English sentences as ASCII diagrams of typed links between words, from a 1991 theory of grammar that still runs.

Link Grammar Parser takes a plain sentence and returns a graph of typed links between its words, drawn as an ASCII diagram in the terminal. Each link joins two words and carries a label for the kind of relationship, such as subject to verb or verb to object. It ships dictionaries for English, Thai, Russian, Arabic, Persian and limited subsets of several other languages.

The idea underneath is the connector. Each word's dictionary entry lists the connectors it can offer, and a parse is a set of links pairing compatible connectors, with the links forming a planar graph. The connector set a word actually uses in a parse is its disjunct. The README's example: `S- O+` marks a transitive verb, one that takes both a subject and an object. The README calls the disjunct a very fine-grained part of speech, and costs on disjuncts roughly reflect how likely each usage is.

Most parsers hand back one tree. This one gives a ranked set of linkages for the same sentence, so ambiguity is something you see. The theory was first published in 1991 by Temperley, Lafferty and Sleator at Carnegie Mellon. This is the reference implementation, now maintained under the OpenCog project. The README says HPSG-style constituent or dependency trees can be derived from the output by conversion rules.

The package also installs `link-generator`, an experimental tool that fills words into wildcard slots while keeping the sentence grammatical. Bindings exist for C, Python, Java, Node.js and others, so the parser can be pulled into your own code once you have played with it.

## Install

```
brew install link-grammar
# no accounts or hardware needed; dictionaries are found by two-letter language directory, e.g. `link-parser ru`
```

## Try this

```
link-parser
```
Opens the linkparser> prompt. Type a sentence and it prints the linkages, their costs and the ASCII diagram. The README says !var lists settings and !help lists more commands.

```
link-parser ru -verbosity=4
```
Runs the parser on the Russian dictionary with verbose output, which the README suggests for debugging dictionary lookups.

```
man link-generator
```
Opens the man page for the experimental generator that fills wildcard slots in sentences with words that keep them grammatical.

## What's unique

Instead of one tree, it gives ranked linkages and shows each word's disjunct. It comes straight from the original 1991 theory, with dictionaries for many languages that can be updated while parsing continues.

## Caveats

The README's own test corpora report known errors (about 88 for en/corpus-basic.batch), some English link-crossing cases are handled only by a workaround, and the README did not show a recent release date.

## Links

- [Project homepage (GitHub)](https://github.com/opencog/link-grammar)
- [Main project web page](https://opencog.github.io/link-grammar-website/)
- [English link type documentation](https://opencog.github.io/link-grammar-website/dict/index.html)
- [Link Grammar on Wikipedia](https://en.wikipedia.org/wiki/Link_grammar)
