---
name: clingo
title: clingo
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, asp, declarative, logic, math, solver]
homepage: https://potassco.org/clingo/
scout_score: 7
status: draft
---

# clingo

**TLDR;** A solver for answer set programming: describe a puzzle or combinatorial problem as logic rules, and clingo computes every solution that satisfies them.

Clingo is a grounder and solver for answer set programming (ASP), a declarative style of logic programming. You do not write steps. You write a logic program that says what a valid solution looks like, and clingo computes *answer sets*, each one representing a solution to the problem.

The README puts it this way: "ASP offers a simple and powerful modeling language to describe combinatorial problems as *logic programs*." The system "then takes such a logic program and computes *answer sets* representing solutions to the given problem." Two stages are at work. Grounding turns a program with variables into a variable-free one, and solving searches that for models. The INSTALL file says clingo builds on libpotassco and clasp, and builds the gringo, clingo, and reify applications.

The idea underneath is a different way of thinking about problems like scheduling, configuration, and puzzles. Instead of designing a search algorithm, you state constraints and let a general-purpose solver do the search. That makes it a door into declarative logic, constraint solving, and knowledge representation.

The brief could not reach the usage guide, so the examples here come from elsewhere. The README links an online version of clingo, which is the quickest way to try writing a program without installing anything.

## Install

```
brew install clingo
# the formula also pulls in Python, Lua and cffi for scripting support
```

## Try this

```
clingo --help
```
Prints the solver's options, a first look at what the system can be asked to do.

```
gringo --help
```
Shows the options for the grounder on its own, the stage that expands your rules before solving.

```
reify --help
```
Shows the help for reify, one of the three applications named in the INSTALL file.

## What's unique

Clingo bundles both the grounder and the solver in one toolchain, and the README links an online version so you can try it without installing anything.

## Caveats

The brief could not reach the homepage text or the Getting Started page, so there are no verified usage examples here, and the README is short and points to separate documentation.

## Links

- [Potassco clingo homepage](https://potassco.org/clingo/)
- [GitHub repository and README](https://github.com/potassco/clingo)
- [Online version of clingo](https://potassco.org/clingo/run/)
- [Releases (source and binary downloads)](https://github.com/potassco/clingo/releases)
