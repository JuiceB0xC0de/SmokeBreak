---
name: aspcud
title: aspcud
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, asp, cudf, logic-programming, packaging, solvers]
homepage: https://potassco.org/aspcud/
scout_score: 6
status: draft
---

# aspcud

**TLDR;** A package dependency solver that hands the install-or-conflict puzzle to an answer set programming engine, so the logic is declared rather than coded.

aspcud reads a CUDF problem file, a standard description of packages, versions, dependencies and conflicts, and writes a CUDF solution file saying which packages to install. Optimisation criteria go on the command line, so you can say what kind of solution you prefer. The CUDF format and benchmark instances come from the Mancoosi project.

The work is split into small pieces. The preprocessor `cudf2lp` turns the CUDF specification into a set of logic facts. Those facts, plus an encoding file, go to the clingo grounder and the clasp solver. A small C program, `aspcud`, calls these tools in order and prints the answer back as CUDF.

The idea underneath is answer set programming. You do not write a search algorithm. You write rules describing what a valid installation looks like, and a solver finds models that satisfy them. Dependency resolution is a good fit, because it is a pile of constraints with a preference for the best answer.

Two encodings ship with it, selectable with `-e`: `misc2012.lp` and `specification.lp`. Reading them is a compact way to see a real, practical problem written declaratively.

## Install

```
brew install aspcud
The README says clasp and gringo must be installed separately (see the potassco clingo repository); brew pulls in clingo as a dependency. It also points to an INSTALL.md and an examples folder. No hardware or account needed.
```

## Try this

```
aspcud --help
```
Prints the usage text, including the options such as the encoding selector.

```
aspcud problem.cudf solution.cudf <criteria>
```
Reads a CUDF problem, solves it with ASP, and writes a CUDF solution optimised against your criteria. Use a file from the repo's examples folder.

```
cudf2lp --help
```
Shows the converter that turns a CUDF problem into logic facts, so you can see what the solver actually receives.

## What's unique

It applies answer set programming to a practical packaging problem, with the logic in swappable encodings and the solver doing the search. The split into converter, small driver and encodings is easy to read and modify.

## Caveats

The README gives no release dates or platform list, so maintenance status is unclear, and the homepage returned an empty page when fetched.

## Links

- [aspcud homepage (empty when fetched)](https://potassco.org/aspcud/)
- [aspcud GitHub repository and README](https://github.com/potassco/aspcud)
- [clingo (grounder)](https://github.com/potassco/clingo)
