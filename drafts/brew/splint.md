---
name: splint
title: Splint
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, history, lint, security, static-analysis]
homepage: https://splint.org/
scout_score: 5
status: draft
---

# Splint

**TLDR;** A C static checker from the 2000s that works as a better lint, and checks harder if you annotate your source with extra specifications.

Splint reads C source files and reports likely security holes and coding mistakes without running the program. Its name is short for Secure Programming Lint. The homepage also calls it SPecifications Lint and "First Aid for Programmers".

The idea underneath it is annotation-assisted checking. With no extra work, the homepage says, "Splint can be used as a better lint." If you invest more effort and add annotations to your code, it "can perform stronger checking than can be done by any standard lint." The annotations are a way of telling the checker what you intended, so it can compare that against what the code does.

The papers linked from the homepage cover buffer overflow detection and dynamic memory error detection, which gives a sense of the era and the problems it was built for. The homepage does not describe the analysis in more detail or the output format, so expect to learn that by running it.

It is old. The last release, 3.1.2, was announced in July 2007. That makes it a useful historical artifact: a look at how people tried to make C safer through specifications before newer analyzers and sanitizers became common.

## Install

```
brew install splint
```

## Try this

```
splint --help
```
Prints the list of options and flags, a first look at what the checker can be told to do.

## What's unique

It is an early annotation-driven checker for C. You start with plain lint-style checking and add annotations for stronger checks, a different trade-off from lint tools that work without annotations.

## Caveats

The project is quiet: the last release was 3.1.2 in 2007, and the homepage says nothing about modern C standards or compilers.

## Links

- [Splint homepage](https://splint.org/)
- [Source code (GitHub)](https://github.com/splintchecker/splint)
- [Windows installer by Mao Yu (third party)](https://github.com/maoserr/splint_win32/downloads)
