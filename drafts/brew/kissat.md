---
name: kissat
title: Kissat
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, logic, math, sat, science, solver]
homepage: https://github.com/arminbiere/kissat
scout_score: 7
status: draft
---

# Kissat

**TLDR;** A competition-winning SAT solver in plain C that decides whether a Boolean formula can be satisfied, and a door into how modern solvers work.

Kissat takes a Boolean formula, usually in CNF form, and reports whether some assignment of true and false to its variables makes it true. If one exists, it returns it. If none does, it says the formula is unsatisfiable. The README calls it a "keep it simple and clean bare metal SAT solver written in C."

It is a port of CaDiCaL back to C, with new data structures and a different schedule for inprocessing, which is simplifying and rewriting the clause set while the search is running. The release notes name techniques such as clausal congruence closure, bounded variable addition, fast variable elimination, clause vivification, and local search to pick initial phases. The 2024 version, sc2024, won three gold medals in the SAT Competition 2024 main track.

The idea underneath is that a huge class of problems can be written as true/false constraints and handed to one general engine. Scheduling, hardware verification, and puzzles all reduce to SAT. Kissat is a place to see how far that engine has been pushed. The name is a pun: kissat is Finnish for cats.

## Install

```
brew install kissat
```

## Try this

```
kissat --help
```
Prints the command-line options, which is the quickest way to learn the interface since the README gives no usage guide.

## What's unique

It is a deliberate rewrite of CaDiCaL in plain C, aimed at simplicity, and its 2024 competition version took several gold medals.

## Caveats

The README documents only the build step, so input format and options have to be learned from --help, the source, or other docs; you also need your own CNF files to feed it.

## Links

- [Homepage (GitHub repository)](https://github.com/arminbiere/kissat)
- [SAT Competition 2024 system description (paper)](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-SAT-Competition-2024-solvers.pdf)
- [NEWS.md (feature changelog)](https://github.com/arminbiere/kissat/blob/master/NEWS.md)
- [Release history](https://github.com/arminbiere/kissat/releases)
