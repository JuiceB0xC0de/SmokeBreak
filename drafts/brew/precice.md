---
name: precice
title: preCICE
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, cfd, library, multi-physics, science, simulation]
homepage: https://precice.org/
scout_score: 6
status: draft
---

# preCICE

**TLDR;** A coupling library that connects separate physics solvers, such as fluid and structure codes, so they exchange data mid-run without being rewritten.

preCICE does not solve any physics itself. It sits between existing solver programs, each simulating one part of a coupled problem, and lets them swap data at every time step. It handles communication, time interpolation, and mapping data between the solvers' different meshes. Solvers either call its API (C++, C, Fortran, Python, Matlab and others) or use an adapter for a ready-made code such as OpenFOAM, CalculiX, FEniCS, deal.II, or Nutils.

The idea underneath is partitioned coupling. Instead of building one giant multi-physics code, you take a fluid solver and a structure solver that already exist and make them talk. The homepage puts it this way: "Partitioned means that preCICE couples existing programs/solvers capable of simulating a subpart of the complete physics involved in a simulation." A classic example is fluid-structure interaction, where air or water pushes on a body and the body deforms in response.

The design is peer to peer, so solvers talk directly rather than through a central server. The library provides quasi-Newton acceleration for strong coupling and radial-basis-function mapping between non-matching meshes. The coupling scheme, for example serial-explicit, is set in an XML configuration file. It is an academic project from TU Munich and the University of Stuttgart, and the name stands for Precise Code Interaction Coupling Environment.

The Homebrew package gives you the core library and a handful of command-line tools. The real fun starts when you pair it with a solver adapter and a tutorial case from the docs.

## Install

```
brew install precice
# Bindings for Python, Fortran, Matlab, Julia and Rust are installed separately.
# Solvers and their adapters (OpenFOAM, CalculiX, etc.) are also separate installs.
```

## Try this

```
precice-version
```
Prints the installed preCICE version, which is the docs' suggested check that the install worked.

```
precice-tools --help
```
Lists the built-in tools and their subcommands.

```
precice-config-validate --help
```
Shows how to check a preCICE XML configuration file for errors.

## What's unique

It couples programs that already exist, including unmodified solvers through adapters, rather than asking you to adopt a new monolithic multi-physics code. Around the library sits a fuller ecosystem of adapters, language bindings, and a version-pinned distribution.

## Caveats

The library alone does little; you need solvers and adapters to see a coupled simulation, and the README points to external docs rather than showing command-line usage beyond precice-version.

## Links

- [Homepage](https://precice.org/)
- [GitHub repository](https://github.com/precice/precice)
- [Installation docs](https://precice.org/docs/installation/overview/)
