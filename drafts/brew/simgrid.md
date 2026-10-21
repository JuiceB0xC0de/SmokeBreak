---
name: simgrid
title: SimGrid
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [days-off, distributed-systems, library, mpi, science, simulation]
homepage: https://simgrid.org/
scout_score: 7
status: draft
---

# SimGrid

**TLDR;** A research library for simulating distributed systems, so you can predict how clusters, networks and data centers behave without building them.

SimGrid is a framework for building simulators of distributed computer systems. You write a program in C++, C, Python, or Java that describes a platform (clusters, LANs, WANs, DSL peers, data centers) and the applications running on it. The simulator then predicts performance, including time and energy. It can also be used to debug and profile real MPI applications.

The homepage says it exists to "prototype, evaluate and compare relevant platform configurations, system designs, and algorithmic approaches" for distributed applications. A research community, initially in France and the U.S.A., has developed it for about 20 years. Ready-made models for common platform types are described as fast, scalable, and experimentally validated, so you build on them instead of writing your own network model.

The idea underneath is that you can study a system too big, too costly, or too awkward to run for real by simulating it. You change a topology or an algorithm and compare results, repeatably, on one laptop. SimGrid also includes what the docs call a prototypical model checker, for formally checking simple algorithms and applications.

The docs are blunt: "Technically speaking, SimGrid is a library. It is neither a graphical interface nor a command-line simulator running user scripts." The brew package also installs companion tools such as smpicc, smpicxx, smpirun, tesh, and simgrid-mc. The pages the brief covers did not show how they are used.

## Install

```
brew install simgrid
# Needs a C++ toolchain, and you write your own program against the API in C, C++, Python, or Java. On Windows, support is via WSL only.
```

## Try this

```
smpirun --help
```
Shows the options for running an MPI program on a simulated platform.

```
smpicc --help
```
Shows the compiler wrapper used to build MPI programs against SimGrid.

```
tesh --help
```
Shows the options of tesh, a tool installed alongside the library.

## What's unique

It is an embeddable simulation library with its own validated platform models, not a ready-made simulator. It can also run real MPI applications on a simulated platform.

## Caveats

Not a point-and-run tool: you must write a program against the API, the model checker is described as prototypical, and the brief found no example commands.

## Links

- [Homepage](https://simgrid.org/)
- [Documentation](https://simgrid.org/doc/latest/)
