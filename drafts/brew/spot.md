---
name: spot
title: Spot
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, automata, cli, formal-methods, library, logic, math, model-checking]
homepage: https://spot.lre.epita.fr
scout_score: 7
status: draft
---

# Spot

**TLDR;** A toolkit of Unix-style filters for temporal logic formulas and omega-automata: simplify an LTL formula, turn it into an automaton, test translators against each other.

Spot is a C++20 library for working with LTL (linear temporal logic) and omega-automata, which are automata that run on infinite sequences. LTL lets you write properties like "every request is eventually answered". Omega-automata are the machines that can check such properties over a system that never stops. Spot reads LTL in several syntaxes plus a subset of the linear fragment of PSL. It reads automata in five formats: HOA, never claims, LBTT, DSTAR and PGsolver.

Most of the algorithms are also exposed as command-line tools, and as Python bindings. The brew package installs 16 executables. Formulas and automata go in, and simplified formulas, translated or transformed automata, test results, benchmark results and synthesis outputs come out. The tools are described as filters that can be piped together, so ltlfilt works on formulas and autfilt works on automata.

The idea underneath is that a logical property and a machine can be the same thing in two forms. Translating a formula into an automaton is the core step in model checking and in reactive synthesis, where a controller is generated from a specification. Spot covers this ground, including safety and parity games and Emerson-Lei acceptance conditions, which is less common than tools limited to Büchi or parity acceptance.

The homepage describes ltlcross as "a rewrite of LBTT, but with support for PSL and automata with arbitrary acceptance conditions". It checks LTL-to-automata translators against each other, which is a good way to see how the field tests its own tools. The homepage also mentions an online translator and a Jupyter notebook called spot-sandbox, but these were not verified.

## Install

```
brew install spot
```

## Try this

```
ltl2tgba --help
```
Lists the options of the tool that translates an LTL formula into an automaton.

```
ltlfilt --help
```
Shows how to simplify, check and transform LTL formulas read from files or pipes.

```
autfilt --help
```
Shows the operations available on automata, such as reduction and determinization.

## What's unique

It handles both LTL and omega-automata with arbitrary Emerson-Lei acceptance conditions, through filter-style tools that pipe together. ltlcross and autcross give a generic way to test or benchmark other translators.

## Caveats

It is GPL v3, so anything linking with the library must be GPL-compatible, and the brief did not cover command examples or build details, so expect to read the documentation.

## Links

- [Spot homepage](https://spot.lre.epita.fr)
