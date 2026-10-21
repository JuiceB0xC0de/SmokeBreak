---
name: malbolge
title: malbolge
source: brew
category: languages-and-oddities
commitment: quick
tags: [ancient, esoteric, language, quick]
homepage: https://esoteric.sange.fi/orphaned/malbolge/README.txt
scout_score: 8
status: draft
---

# malbolge

**TLDR;** An interpreter for Malbolge, an esoteric language built to be nearly impossible to program, shipped with a working cat and a 99 Bottles program.

Malbolge is an esoteric programming language, and this package is the 2004 edition of its release bundle. It contains two interpreters, one in C and one in Perl, plus a handful of sample programs written in the language itself.

The samples are the interesting part. The README lists nop.mal, answer.mal, copy.mal (an implementation of cat) and bb.mal, which outputs an uuencoded gzip of the lyrics to 99 Bottles of Beer. The README is dry about all this: "Quite a long time has passed since Malbolge was released." It adds that the language "turned out to have quite a few helpful features, and some useful (albeit trivial) programs have emerged."

The door here is the idea of a language designed against the programmer. Most languages try to be easy to write. Malbolge's reputation is the opposite, and the bundled programs show that people did eventually get real, if tiny, work out of it. Reading the sample sources next to the interpreter is a quick way to see how strange a working program can look.

The README does not explain the language's rules or the input and output formats, so you will be learning by experiment.

## Install

```
brew install malbolge
```

## Try this

```
malbolge --help
```
Shows whatever usage the installed interpreter offers. The README gives no usage details, so this is the safest first step.

## What's unique

It is a historical release bundle with two interpreters and real sample programs, including cat and a 99 Bottles generator, not just a bare interpreter.

## Caveats

The README has no build or usage instructions, does not say which interpreter the brew executable corresponds to, and shows no sign of recent maintenance.

## Links

- [Malbolge 2004 edition README](https://esoteric.sange.fi/orphaned/malbolge/README.txt)
