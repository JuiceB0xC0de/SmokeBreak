---
name: damask-grid
title: DAMASK grid solver
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [crystal-plasticity, days-off, materials, mpi, science, simulation]
homepage: https://damask-multiphysics.org
scout_score: 6
status: draft
---

# DAMASK grid solver

**TLDR;** A spectral FFT solver that simulates how polycrystalline metal deforms, grain by grain, from a voxel microstructure and a load case.

DAMASK, the Düsseldorf Advanced Material Simulation Kit, is a crystal plasticity package. This formula installs its grid solver. You give it three files: a .vti geometry describing a grain structure on a regular grid, a load case in YAML, and a material YAML that defines the constitutive models and homogenization. It runs a spectral solve using FFTs with mixed periodic boundary conditions and writes an HDF5-based result file, called DADF5.

The project's argument is that "treating mechanics in isolation is no longer sufficient to study emergent advanced high-strength materials." Deformation can interact with phase transformation, heating and damage. DAMASK takes a modular approach: further field equations are solved fully coupled, using a staggered scheme, alongside the crystal plasticity.

The solver runs in parallel with OpenMP threads, MPI, or both. MPI splits the domain along the z-axis into layers of roughly equal height. The wider project also has a Python library for pre- and post-processing (texture generation, Voronoi polycrystals, load case generation, IPF plots), plus ParaView integration for looking at results. The formula installs only the solver, not those parts.

The door here is micromechanics: how a metal's bulk behaviour emerges from many small crystals, each with its own orientation and slip systems. The solver is the small part. The material models are the larger subject.

## Install

```
brew install damask-grid

Needs no special hardware, but the dependency list is long (PETSc, HDF5 with MPI, Open MPI, gcc), so expect a sizeable install. You also need your own geometry, load case and material files. The project offers curated example setups as grid.tar.xz and config.tar.xz downloads.
```

## Try this

```
damask_grid --help
```
Prints the solver version and usage instructions.

```
damask_grid --load {load}.yaml --geom {grid}.vti --material {material}.yaml
```
Runs a simulation. All three flags are mandatory, and the curly brackets are placeholders for your file names. Results land in a DADF5 file named after the inputs.

```
mpiexec -n {n_proc} damask_grid --load {load}.yaml --geom {grid}.vti --material {material}.yaml
```
Runs the same solve across n_proc MPI processes, splitting the domain along the z-axis.

## What's unique

It is a documented, citable (DOI) spectral crystal plasticity code that installs with one formula, with a Python toolchain around it. That is unusual for research-grade materials simulation.

## Caveats

You must supply or download input files before anything runs. Development happens on a private GitLab instance, GitHub is a read-only mirror, and the brief found no release or last-commit date.

## Links

- [DAMASK homepage](https://damask-multiphysics.org)
- [Usage and grid solver docs](https://damask-multiphysics.org/documentation/usage.html)
- [GitHub read-only mirror](https://github.com/damask-multiphysics/DAMASK)
- [Citation DOI](https://doi.org/10.1016/j.commatsci.2018.04.030)
