---
name: minisat
title: MiniSat
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, constraint-solving, math, sat]
homepage: https://github.com/stp/minisat
scout_score: 5
status: draft
---

# MiniSat

**TLDR;** A small, readable SAT solver that decides whether a Boolean formula can be satisfied, and a classic door into constraint solving.

MiniSat takes a Boolean satisfiability problem, usually a CNF file named on the command line, and reports whether some assignment of true and false makes the whole formula true. If one exists, it prints a model.

It was written to help researchers and developers get started on SAT. The project page calls it "a minimalistic, open-source SAT solver" and says it is meant to be easy to modify and to serve as a backend for other tools. It also supports incremental SAT and a way to add non-clausal constraints. It is famous for winning all the industrial categories at the SAT 2005 competition while staying small and well documented.

The idea underneath is that a surprising number of hard problems can be written as one giant true-or-false formula and handed to a solver: scheduling, hardware verification, puzzles, package dependencies. Learn to encode a problem as CNF and you can use a whole family of tools. The source is split into mtl/ (a small template library), utils/, core/ (the core solver) and simp/ (an extended solver with simplification), so it is practical to read as well as run.

## Install

```
brew install minisat
```

## Try this

```
minisat --help
```
Lists the solver's options, including the heuristics and restart settings you can tune.

```
minisat <cnf-file>
```
Runs the solver on a CNF file and reports whether it is satisfiable, with a model if so.

```
minisat <cnf-file> -no-luby -rinc=1.5 -phase-saving=0 -rnd-freq=0.02
```
Runs with flags that, per the README, reproduce the heuristics of version 2.0.

## What's unique

It is a compact, readable solver that still won industrial categories at SAT 2005, which made it a standard base for teaching and for building other tools on top of.

## Caveats

The README has unfinished TODO sections, shows no release dates, and does not explain the solving algorithm, so you will need a CNF file of your own and outside reading.

## Links

- [GitHub repository](https://github.com/stp/minisat)
- [MiniSat project page](http://minisat.se)
