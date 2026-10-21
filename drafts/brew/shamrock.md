---
name: shamrock
title: Shamrock
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astrophysics, gpu, hpc, science, simulation, sycl]
homepage: https://shamrock-code.github.io
scout_score: 6
status: draft
---

# Shamrock

**TLDR;** An open-source astrophysical fluid simulation code written in SYCL, so one codebase runs on NVIDIA, AMD, Intel GPUs or plain CPUs.

Shamrock simulates astrophysical fluids: gas and matter flowing under gravity and pressure. The brief says it covers particle-based SPH and grid-based methods, and the homepage lists SPH, AMR and others. It runs on a laptop CPU, a single GPU, or many GPUs across a cluster using MPI.

The authors describe it as "a general purpose HPC hydrodynamics simulation code focused on astrophysical contexts" and say it "aims to be Modern, Modular, Fast, Portable." Its accelerated parts are written in SYCL, a C++ programming model that compiles to CUDA, ROCm, OpenMP, OpenCL and other backends. The brew formula pulls in AdaptiveCpp for that role, plus Open MPI and Python.

The idea underneath is performance portability. Simulation codes are often tied to one vendor's GPU toolchain and have to be rewritten when the supercomputer changes. Writing the kernels once in SYCL is a bet that the same source can follow the hardware. The homepage says Python can be used as a package, in a notebook, or as an interpreter, which suggests a scripted way in. The brief did not confirm input and output formats, so the Sphinx quickstart is the place to learn how a run is set up.

The code is described in a 2025 MNRAS paper (arXiv 2503.09713), so you can read how the methods work before running anything.

## Install

```
brew install shamrock
# pulls in adaptivecpp, open-mpi, python and libomp
# the README also lists building from source, Spack, or a third-party Docker image (linux/amd64)
```

## Try this

```
shamrock --help
```
Prints the options of the installed executable, a first look at how a run is driven.

```
docker run -it --platform=linux/amd64 ghcr.io/shamrock-code/shamrock:latest-oneapi
```
Starts an interactive container with the third-party oneAPI build of Shamrock, if you prefer not to build locally.

```
git clone --recurse-submodules https://github.com/Shamrock-code/Shamrock.git
```
Fetches the source with its submodules, so you can follow the quickstart guide and read the code.

## What's unique

Single-source SYCL lets one astrophysics code target NVIDIA, AMD, Intel and CPU backends, which is unusual in this field. The homepage claims scaling from laptops to exascale machines.

## Caveats

The README gives no build steps beyond clone and Docker, maintenance status is unclear from the brief, and the performance figures on the homepage are unverified.

## Links

- [Homepage](https://shamrock-code.github.io)
- [Main documentation (Sphinx)](https://shamrock-code.github.io/Shamrock/sphinx/index.html)
- [Quickstart guide](https://shamrock-code.github.io/Shamrock/sphinx/user_guide/quickstart.html)
- [arXiv paper 2503.09713](https://arxiv.org/abs/2503.09713)
