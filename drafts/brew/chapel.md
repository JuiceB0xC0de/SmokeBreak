---
name: chapel
title: Chapel
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, gpu, hpc, language, parallel]
homepage: https://chapel-lang.org/
scout_score: 6
status: draft
---

# Chapel

**TLDR;** A compiled parallel programming language where threads, multiple machines and GPUs are all written with the same few language constructs, and it runs on a laptop.

Chapel is a compiled, open-source language for parallel computing. You write one program using constructs such as `coforall` (a task per core), `forall` (iterations in parallel) and `on loc` (move work to another compute node, called a locale). The compiler, `chpl`, turns that into machine code. The homepage shows small examples: Hello World, a distributed Hello World, parallel file IO, a 1D heat diffusion solver and a GPU kernel.

The project's own line is "Productive parallel computing at every scale." It was built for high-end supercomputers, and the README says it is also meant for the CPUs and GPUs of laptops, desktops, commodity clusters and the cloud.

The idea underneath is a global-view style. Most languages bolt parallelism on through a library or a separate GPU API. Chapel instead has you write over whole arrays and domains, and `on` clauses decide where the work lands. The homepage says GPU programming uses the same language features as distributed execution, with no separate API. The distributed array example uses `blockDist`, and the GPU example uses `here.gpus` with `on gpu`.

The brew install also provides `mason` (a package manager), `chpldoc`, `chplcheck` (a linter), a language server and `c2chapel`. Those make it feel like a complete toolchain rather than a research toy.

## Install

```
brew install chapel
# Programs compile single-locale by default. For local multi-locale runs or simulated GPUs, use the extra flags in the first two try_this commands below.
```

## Try this

```
chpl --comm=gasnet --comm-substrate=udp
```
Compiles a Chapel program for multi-locale execution, so you can simulate several nodes on your own machine. Add your source file name.

```
chplrun-udp ./your_program_name
```
Runs the program you compiled with the gasnet/udp settings across local locales.

```
chpl --locale-model=gpu --gpu=cpu
```
Compiles a program with GPU kernels but simulates the GPU on the CPU, so no graphics card is needed.

## What's unique

Distributed multi-node execution and GPU kernels use the same language constructs, with no separate API, and you can try both on a laptop.

## Caveats

Compiled programs are single-locale by default, multi-locale and simulated GPU runs need extra compile flags, and the bundled libfabric multi-locale setup is experimental.

## Links

- [Project homepage](https://chapel-lang.org/)
- [Chapel documentation](https://chapel-lang.org/docs/)
- [Sample computations / examples](https://chapel-lang.org/docs/examples/)
- [Try Chapel online](https://chapel-lang.org/tryit/)
