---
name: lammps
title: LAMMPS
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, materials, molecular-dynamics, mpi, science, simulation]
homepage: https://docs.lammps.org/
scout_score: 7
status: draft
---

# LAMMPS

**TLDR;** A molecular dynamics simulator from Sandia National Laboratories: write a script describing atoms and forces, and it steps the physics forward for you.

LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) is a classical molecular dynamics code focused on materials modeling. You do not click through a GUI. You write an input script: commands that define the simulation box, place atoms, choose interaction potentials, and say how long to run. LAMMPS reads it, prints progress to the screen, and writes a logfile called log.lammps, plus any other output files the script asks for.

The docs say it was designed to run efficiently on parallel computers and to be easy to extend and modify. It was originally developed at Sandia National Laboratories, with most funding from the US Department of Energy, and now includes contributions from many groups. Extra force fields and behaviours are added through its own styles and a plugin mechanism.

The idea underneath is that a lot of materials science is Newton's laws applied to many atoms at once. You pick a model for how atoms push and pull on each other, then step forward in tiny increments of time and watch what emerges: melting, diffusion, fracture, flow. The same script can run on a laptop in serial or be spread across many processors with MPI. Small experiments make sense at home, and the manual is thorough enough to teach the vocabulary as you go.

## Install

```
brew install lammps
# installs lmp_serial and lmp_mpi. Parallel runs need an MPI launcher (open-mpi is pulled in as a dependency).
```

## Try this

```
lmp_serial -help
```
Lists the compilation options, packages and styles included in this binary, so you know what your build can do.

```
lmp_serial -in in.file
```
Runs the input script in.file from the current directory on a single processor, printing progress and writing log.lammps.

```
mpirun -np 4 lmp_mpi -in in.file
```
Runs the same script spread across 4 MPI tasks.

## What's unique

It is a long-running, DOE-backed materials MD code that you extend with your own styles and plugins. Its documentation is unusually thorough, with a full command reference and benchmarks.

## Caveats

You need to write or find an input script before anything happens, and some examples need optional packages that may not be compiled into the brew build.

## Links

- [LAMMPS documentation (homepage)](https://docs.lammps.org/)
- [Stable branch manual](https://docs.lammps.org/stable/)
- [Download an executable for Linux](https://docs.lammps.org/Install_linux.html)
- [Pre-built static Linux executables](https://download.lammps.org/static/)
