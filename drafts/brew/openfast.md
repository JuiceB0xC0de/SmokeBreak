---
name: openfast
title: OpenFAST
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [days-off, engineering, fortran, science, simulation, wind-energy]
homepage: https://openfast.readthedocs.io
scout_score: 7
status: draft
---

# OpenFAST

**TLDR;** A research-grade wind turbine simulator that couples aerodynamics, waves, controls and structural flex into one time-domain model of a whole turbine.

OpenFAST simulates how a wind turbine behaves as one connected system. You describe the turbine in input files (rotor, tower, substructure, controller) and set the wind and wave conditions. It then runs nonlinear, coupled aero-hydro-servo-elastic simulations in the time domain. The docs also describe linearizing about an operating point to get natural frequencies, damping and mode shapes.

It is built as a glue code that connects separate modules for aerodynamics, hydrodynamics (for offshore structures), control and electrical dynamics, and structural dynamics. The coupler advances them together in time through a modular interface. The glue code and most modules are Fortran 2003, and modules can also be written in C or C++. A FAST.Farm extension runs one OpenFAST model per turbine to study wake effects across a wind farm.

The docs describe it as a community model for research labs, academia and industry, and the successor to FAST v8. The stated aim is software that is "well tested, well documented, and self-sustaining". The idea underneath is that a turbine is a feedback loop between wind, flexing steel, water and a controller, and you can swap any one of those parts out and watch how the whole thing responds.

There is no GUI described in the pages read. It is a command-line simulator driven by input files.

## Install

```
brew install openfast
# Installs the `openfast` executable. Pulls in gcc and openblas as dependencies. You will need a turbine input file to run a simulation; the docs also offer Docker, binaries, a Python wrapper (openfast_io) and source builds.
```

## Try this

```
openfast --help
```
Prints the command-line usage so you can see how the simulator expects to be pointed at a turbine input file.

## What's unique

Rather than one monolithic simulator, it is a coupler that lets you swap aero, hydro, control and structural modules and run them together. It covers fixed-bottom and floating offshore turbines, and whole farms through FAST.Farm.

## Caveats

You need turbine input files to do anything real, and the brief did not cover the input format or example cases, so expect to read the docs before your first run.

## Links

- [Documentation homepage](https://openfast.readthedocs.io)
- [GitHub repository](https://github.com/OpenFAST/openfast)
- [Installation docs](https://openfast.readthedocs.io/en/latest/source/install/index.html)
- [Releases and Windows executables](https://github.com/OpenFAST/openfast/releases)
