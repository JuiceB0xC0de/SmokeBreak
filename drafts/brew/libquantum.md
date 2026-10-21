---
name: libquantum
title: libquantum
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c, library, quantum, science, simulation]
homepage: http://www.libquantum.de/
scout_score: 6
status: draft
---

# libquantum

**TLDR;** A C library that simulates quantum registers, gates and measurements on an ordinary computer, with Shor's and Grover's algorithms included.

libquantum is a C library for simulating quantum mechanics, with a special focus on quantum computing. It gives you a quantum register, basic gates such as Hadamard and Controlled-NOT, and measurement of a single qubit or the whole register. Beyond gate-model computing, it can compute the time evolution of arbitrary Hamiltonians, including time-dependent ones, by numerical integration of the Schrödinger equation or by exact diagonalization.

According to its homepage, it began as a pure quantum computer simulator, and general quantum simulation was added later. The stated aim is to run quantum algorithms and quantum mechanics simulations on ordinary classical hardware with high performance and low memory use. The homepage also lists decoherence support, a quantum error correction interface, and the density operator formalism.

The idea underneath is that a quantum computer can be modelled classically, at a cost that grows quickly with the number of qubits. Implementations of Shor's factoring algorithm and Grover's search algorithm are included, so you can read how those famous algorithms look as gates acting on a register. It was also used as an official SPEC CPU2006 benchmark.

This is a library, not a command-line tool. You write C against it. The project is old and quiet, so treat it as a readable, working reference rather than a modern framework.

## Install

```
brew install libquantum
# Library only, no executables. Needs a C compiler with complex number support to build programs against it.
```

## Try this

## What's unique

One long-running C codebase covers both gate-model quantum computing and general Hamiltonian and open-system simulation. Shor's and Grover's algorithms ship with it.

## Caveats

It installs no commands, so you must write C to use it, and the homepage gives no usage example or build steps; the latest news there is from 2013.

## Links

- [Homepage](http://www.libquantum.de/)
