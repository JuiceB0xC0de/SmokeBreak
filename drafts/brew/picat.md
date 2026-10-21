---
name: picat
title: Picat
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, constraints, language, logic-programming, prolog, tabling]
homepage: https://picat-lang.org/
scout_score: 7
status: draft
---

# Picat

**TLDR;** A logic programming language that mixes Prolog-style search and unification with loops, assignments, tabling, and constraint solvers, so planning problems become short rule sets.

Picat is a general-purpose language built on pattern-matching rules. Predicates, functions, and actors are all defined with rules, and programs run on the language's own virtual machine. It can be used for scripting, symbolic computation, and modeling tasks.

It is a cousin of Prolog, and it keeps the declarative features: explicit non-determinism, unification, list comprehensions, constraints. It also adds assignments and loops, so ordinary programming does not require twisting a problem into logic. The homepage says pattern matching lets the implementation index rules and run faster than Prolog.

The idea underneath is tabling, which memoizes calls and answers. With a mode declaration such as `max` on an argument, a tabled search keeps only the best answer. The homepage's Euler #67 example uses this to solve a 100-row triangle in 0.01 seconds. The same mechanism drives planning: its Farmer's problem example tables state transitions and uses `best_plan` instead of a separate planner.

Picat also offers constraint modeling through several solver modules (cp, sat, mip, smt) behind a common interface. That makes it a place to try out the same puzzle on different solving engines without changing languages.

## Install

```
brew install picat
```

## Try this

```
picat --help
```
Prints the command-line options for running Picat programs and starting the interpreter.

## What's unique

Tabling with aggregate modes, explicit non-determinism, and a shared interface to the cp, sat, mip, and smt solvers sit in one language that also reads like a scripting language.

## Caveats

The speed and brevity claims relative to Prolog are the authors' own, not independent benchmarks, and this entry is based on the homepage rather than the documentation.

## Links

- [Picat homepage](https://picat-lang.org/)
- [Picat news group](https://groups.google.com/g/picat-lang)
