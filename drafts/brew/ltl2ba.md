---
name: ltl2ba
title: ltl2ba
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, automata, formal-methods, logic, math, model-checking]
homepage: https://lsv.ens-paris-saclay.fr/~gastin/ltl2ba/
scout_score: 6
status: draft
---

# ltl2ba

**TLDR;** Turns a linear temporal logic formula, such as 'always, if request then eventually grant', into a Büchi automaton you can feed to the Spin model checker.

ltl2ba takes a formula in linear temporal logic (LTL) and produces a Büchi automaton: a small state machine that accepts exactly the infinite behaviours the formula describes. Its stated use is to print a Spin "never claim", which the Spin model checker can use to verify properties of a system. The homepage also runs it as a web form that draws the automaton for you.

The input uses propositional symbols, boolean operators (!, ->, <->, &&, ||) and temporal operators (G, F, U, R, X). There is no operator priority, so parentheses are required. The options include several simplification passes and a choice between drawing the generalised Büchi automaton or the Büchi automaton, rendered through dot from Graphviz.

The idea underneath is that a statement about time, like "this never happens" or "this keeps happening", can be compiled into a machine that reads a run of a system and checks it. That is the core trick behind a large family of model checkers. The tool is based on the paper "Fast LTL to Büchi Automata Translation" from CAV '01, and it is a small, old, academic program, so it is a good way to watch that translation happen.

## Install

```
brew install ltl2ba
# Drawing automata relies on dot from Graphviz: brew install graphviz
```

## Try this

```
ltl2ba --help
```
Prints the usage text for the command-line translator, so you can see which options your build supports.

## What's unique

It is a long-lived academic translator that reads Spin's formula syntax and emits Spin never claims, so it plugs straight into a well-known model checker.

## Caveats

The brief could not verify command-line usage, platform details or release dates, and the web form's server returns a 403 on some formulas containing '!' (the page says to write NOT instead).

## Links

- [Homepage (LTL2BA web form)](https://lsv.ens-paris-saclay.fr/~gastin/ltl2ba/)
- [Denis Oddoux's thesis (French)](https://lsv.ens-paris-saclay.fr/~gastin/ltl2ba/)
- [JLtl2Ba Java interface](https://lsv.ens-paris-saclay.fr/~gastin/ltl2ba/)
