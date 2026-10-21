---
name: tfel
title: TFEL/MFront
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, code-generation, mechanics, science]
homepage: https://thelfer.github.io/tfel/web/index.html
scout_score: 5
status: draft
---

# TFEL/MFront

**TLDR;** A code generator from CEA and EDF that turns short material-law descriptions into C++ for many finite element solvers, with a local tester.

TFEL/MFront is a code generator for material knowledge in numerical mechanics. You write a short file in one of MFront's domain-specific languages, and MFront translates it into plain C++ built on the TFEL library. The languages cover material properties (Young's modulus, thermal conductivity), mechanical behaviours (constitutive laws for finite element and FFT solvers), and simple point-wise models such as fuel swelling.

The idea underneath is to write a material behaviour once, in a readable form, and not rewrite it for every solver. The homepage lists interfaces for Cast3M, Code-Aster, Abaqus Standard and Explicit, CalculiX, ANSYS APDL, ZeBuLoN, ElmerFEM, and the AMITEX_FFTP and TMFFT FFT solvers. The README says the generated code is competitive with the solvers' native implementations.

The bundled MTest tool tests a material's local behaviour by imposing constraints on strain or stress components, with no mesh and no full simulation. In the project's words, it "has been much faster (from ten to several hundred times depending on the test case) than using a full-fledged finite element solver."

The project is a collaboration of CEA and EDF. A 2015 paper in Computers & Mathematics with Applications introduces it as part of the PLEIADES fuel element modelling platform. It is a door into how constitutive laws, the equations saying how a material responds to load, actually become running code inside simulation software.

## Install

```
brew install tfel
# Homebrew pulls in python@3.15. The README says the current version is built on C++-20, so a modern C++ compiler is expected if you build from source or compile generated code.
```

## Try this

```
mfront --help
```
Lists the code generator's options, including the choice of DSL and solver interface.

```
mtest --help
```
Shows how to run a local material test under imposed strain or stress.

```
tfel-config --help
```
Shows the helper that reports the compiler and linker settings for the installed TFEL library.

## What's unique

One source file targets many commercial and research finite element solvers. MTest lets you check a behaviour in isolation before committing to a full simulation.

## Caveats

The domain is specialised and assumes some computational mechanics background, the homepage calls it a work in progress, and I did not verify build details or usage for every tool.

## Links

- [Homepage](https://thelfer.github.io/tfel/web/index.html)
- [GitHub repository](https://github.com/thelfer/tfel)
- [Introducing paper (DOI)](https://doi.org/10.1016/j.camwa.2015.06.027)
