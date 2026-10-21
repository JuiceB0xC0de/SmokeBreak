---
name: abnfgen
title: abnfgen
source: brew
category: languages-and-oddities
commitment: quick
tags: [abnf, fuzzing, grammar, parsers, quick, testing]
homepage: https://www.quut.com/abnfgen/
scout_score: 6
status: draft
---

# abnfgen

**TLDR;** Feed it a grammar written in ABNF and it prints random documents that match, a quick way to see a grammar run backwards and to fuzz parsers.

abnfgen is a small C tool that reads a grammar in Augmented Backus-Naur Form, the notation used in RFC 4234 and in many internet protocol specs, and expands its rules at random. The output is text on stdout, or with `-d` and `-n`, a directory of numbered files. The page's example grammar, `ring = 1*12("ding" SP) "dong" CRLF`, produces output like `DInG DiNg doNg`.

Its author, Jutta Degener, uses it to stress-test parsers she has written. In her words, it usually turns up "about a week's worth of painful crashes and bugs to find for about a day of work getting the grammar just right." It also works as a rough check that a grammar is syntactically valid, and as a way to illustrate a grammar with examples you would not have thought of.

The idea underneath is that a grammar is a generator as well as a recognizer. Parsing walks a document back to its rules; generation walks the rules out to documents. Once you have both directions, you can aim random inputs at anything that consumes that format. The author's advice is to weight rules toward short output, reuse familiar identifier names, and add occasional noise rules.

It departs from standard ABNF in three ways. Single quotes give case-sensitive literals. A number in curly braces before an alternative, such as `{2}`, sets how likely that branch is. Numeric codes like `%d13` are emitted as UTF-8. The `-l` flag turns these extensions off.

## Install

```
brew install abnfgen
# needs only a Unix-like system; the project's own page describes building from source with a C compiler (./configure, make)
```

## Try this

```
abnfgen -h
```
Prints the quick-reference usage summary.

```
./abnfgen GRAMMAR
```
Generates a random document from the grammar file GRAMMAR; the page's ding-dong example prints something like 'DInG DiNg doNg'.

```
./abnfgen -d demo -n 100 section-4.txt
```
Writes 100 random grammars into demo/0001.tst through demo/0100.tst, generated from the ABNF-definition-of-ABNF section of RFC 4234.

## What's unique

It is a grammar-driven generator aimed at breaking parsers rather than producing text for people. Its tutorial has it generate random grammars from the grammar of ABNF itself, then feed those back into itself to see if it crashes.

## Caveats

The page calls it alpha, says recursion-depth handling and chance annotations don't quite work everywhere, and licenses it as 'copyrighted, free for any use' rather than under a formal open-source license.

## Links

- [abnfgen homepage](https://www.quut.com/abnfgen/)
- [RFC 4234 (ABNF definition, plain text)](http://www.ietf.org/rfc/rfc4234.txt)
