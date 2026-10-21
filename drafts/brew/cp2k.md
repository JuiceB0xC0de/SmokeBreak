---
name: cp2k
title: CP2K
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [chemistry, days-off, fortran, mpi, physics, science, simulation]
homepage: https://www.cp2k.org/
scout_score: 5
status: draft
---

# CP2K

**TLDR;** A Fortran package that simulates atoms and electrons from an input file, covering DFT, tight-binding and classical force fields in one code, free under the GPL.

CP2K is a quantum chemistry and solid state physics package for atomistic simulation. In the project's words, it "can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems." Its main method is density functional theory using mixed Gaussian and plane waves approaches (GPW and GAPW). It also supports MP2, RPA, GW, tight-binding (xTB, DFTB), semi-empirical methods (AM1, PM3, PM6, RM1, MNDO) and classical force fields (AMBER, CHARMM).

You do not click anything. You write an input file describing the system and the calculation, then run the binary on it. The calculation can be molecular dynamics, metadynamics, Monte Carlo, Ehrenfest dynamics, vibrational analysis, core level spectroscopy, energy minimization, or a NEB or dimer search for transition states. The README does not spell out the output format beyond a REFERENCES section listing the papers to cite.

The idea underneath is that one framework can cover many levels of theory, from full electronic structure down to cheap classical models, so you can move between accuracy and cost without changing tools. The code is Fortran 2008 and runs in parallel with threads, MPI and GPU acceleration (CUDA, HIP/ROCm, OpenCL). The README names Quickstep, FIST and QM/MM as key parts, and the source tree includes the basis sets and pseudopotentials in a data directory.

The stated aim is that it is free and open so people can try it and modify it. The homepage says it comes without warranty or direct support.

## Install

```
brew install cp2k
# Installs MPI and OpenMP-hybrid builds (cp2k.psmp, cp2k.popt) plus unit-test and miniapp binaries. Pulls in gcc, open-mpi, openblas, fftw, libxc and others, so expect a large download.
```

## Try this

```
cp2k.psmp --help
```
Prints the command-line usage of the MPI and OpenMP-hybrid build.

```
cp2k.popt --help
```
Prints usage for the MPI-only build, so you can compare the two.

```
git clone https://github.com/cp2k/cp2k.git cp2k
```
Fetches the development source, including the data directory of basis sets and pseudopotentials, and the tests directory to read for example inputs.

## What's unique

One input-driven code spans DFT, wavefunction methods, semi-empirical methods and classical force fields. It is developed in the open, with a public test dashboard across architectures.

## Caveats

It comes with no warranty or direct support, assumes you know the underlying theory, has no graphical interface, and most real systems need serious compute rather than a laptop.

## Links

- [CP2K homepage](https://www.cp2k.org/)
- [GitHub repository (README)](https://github.com/cp2k/cp2k)
- [CP2K manual (keyword reference and install guides)](https://manual.cp2k.org/)
- [CP2K test dashboard](https://dashboard.cp2k.org)
