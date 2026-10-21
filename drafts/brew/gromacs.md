---
name: gromacs
title: GROMACS
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [biophysics, days-off, molecular-dynamics, science, simulation]
homepage: https://www.gromacs.org/
scout_score: 7
status: draft
---

# GROMACS

**TLDR;** A molecular dynamics engine that simulates proteins, lipids and other particles moving under Newtonian physics, driven entirely by the command-line gmx tool.

GROMACS simulates the Newtonian equations of motion for systems from hundreds to millions of particles. It is built mainly for biomolecules such as proteins, lipids and nucleic acids, though its homepage says many groups also use it for polymers and fluid dynamics. You give it clear-text topology and parameter files plus run settings. It gives back trajectories and energies that its analysis tools can read.

Everything lives under one program, `gmx`, with subcommands such as `gmx grompp` (prepare a run) and `gmx mdrun` (execute it). The docs say no scripting is required: each tool takes command-line options for input and output files.

The project stresses speed. The nonbonded interactions that usually dominate a simulation are calculated extremely fast, using SIMD kernels on CPUs and CUDA, OpenCL or SYCL on GPUs. CPU and GPU work can run at once with load balancing, and parallelism uses either MPI or a built-in thread-MPI for a single workstation.

The idea underneath is that you can watch matter behave from first principles: define atoms, forces and a timestep, then see what a molecule does. The brief does not go into the integration algorithms, so for that you need the manual. It is a community-driven project, and as the About page says: "GROMACS is a proper name. It is not an acronym for anything."

## Install

```
brew install gromacs
source $HOMEBREW_PREFIX/share/gromacs/GMXRC
# Homebrew installs GMXRC there; source it before using gmx. GPU backends are a separate matter and depend on how the build is configured.
```

## Try this

```
gmx --help
```
Lists the available gmx subcommands, which is a quick tour of the whole suite.

```
source $HOMEBREW_PREFIX/share/gromacs/GMXRC
```
Sets up the environment so the gmx tools are on your path, as the Homebrew caveat describes.

## What's unique

It combines hand-tuned SIMD and GPU kernels with a plain command-line workflow and clear-text input files. It also has an automated topology builder for proteins, including multimeric structures.

## Caveats

You need real molecular dynamics background (topologies, force fields, input structures) to get far, and the brief shows no ready-made starter run.

## Links

- [GROMACS homepage](https://www.gromacs.org/)
- [About GROMACS](https://www.gromacs.org/about.html)
- [Installation guide (2026.4)](https://manual.gromacs.org/documentation/current/install-guide/index.html)
