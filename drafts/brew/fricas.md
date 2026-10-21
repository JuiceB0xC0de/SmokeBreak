---
name: fricas
title: FriCAS
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, axiom, computer-algebra, math, spad, symbolic]
homepage: https://fricas.github.io
scout_score: 6
status: draft
---

# FriCAS

**TLDR;** A free computer algebra system for exact, symbolic mathematics, forked from Axiom, with its algebra library written in a strongly typed language called Spad.

FriCAS is a general-purpose computer algebra system. It is meant for symbolic and exact mathematics rather than floating-point number crunching. The project describes its basic goal as "to create a free advanced world-class CAS." Its README says its algebra library is one of the largest and most advanced among free general-purpose systems.

The idea underneath it is that the mathematics lives in a typed language. The algebra library is written in Spad, a high-level, strongly typed language. The README says this lets mathematical algorithms be expressed naturally and makes the system easier to understand and extend. Most computer algebra tools grow out of an untyped scripting layer. Here the types are part of how the math is described.

FriCAS forked from Axiom in 2007. According to the README, it has since been significantly restructured, made more portable, had several defects fixed, and had large unused parts removed without removing functionality. It is meant as a foundation others can build on. Axiom is a long-running system with deep academic roots, so this is a way into that lineage.

The brief did not cover the input syntax or example sessions. The homepage has Help and Examples sections to start from.

## Install

```
brew install fricas
# installs the fricas and efricas executables; depends on sbcl, gmp and some X11 libraries
```

## Try this

```
fricas --help
```
Prints the command-line options for the FriCAS launcher.

```
efricas --help
```
Shows the options for the second executable, efricas.

## What's unique

It is a long-lived fork of Axiom whose algebra library is written in Spad, a purpose-built, strongly typed language, so the mathematics is expressed in types rather than bolted onto a scripting layer.

## Caveats

The pages read showed no usage examples, and the last-release date is unconfirmed, so expect to learn the syntax from the project's own documentation.

## Links

- [Homepage and documentation](https://fricas.github.io)
- [GitHub repository](https://github.com/fricas/fricas)
- [Project page (SourceForge)](https://fricas.sourceforge.net)
- [Axiom (the project FriCAS forked from)](https://www.nongnu.org/axiom/)
