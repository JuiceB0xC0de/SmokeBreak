---
name: spglib
title: spglib
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, crystallography, library, math, science, symmetry]
homepage: https://spglib.readthedocs.io/en/latest/
scout_score: 6
status: draft
---

# spglib

**TLDR;** A C library that takes a crystal's atom positions and tells you its space group, with a tolerance setting so slightly distorted real structures still count.

Spglib finds the symmetries of a crystal. You give it lattice vectors, atom positions, atom types, and a tolerance called symprec. It returns symmetry information: the space group number, the symmetry operations, Wyckoff positions, a primitive cell, a refined structure, and irreducible k-points. The main call, `spg_get_dataset`, returns a `SpglibDataset` struct that you free with `spg_free_dataset`.

The tolerance is the interesting part. Real structures from experiments or simulations are never perfectly symmetric, because atoms sit slightly off their ideal places. The README puts it this way: "To tolerate tiny distortion of crystal structure, it has to be specified when calling symmetry search function." Change the tolerance and the same structure can land in a different space group, which shows how fuzzy the line between symmetric and not really is.

The underlying idea is that a crystal is a pattern repeated in space, and the possible patterns fall into a finite, well-studied catalogue of space groups. Spglib is a way to run that classification on your own data. It also handles magnetic space-group search. Python, Fortran, Rust, and Ruby interfaces sit alongside the C API, and the authors cite a 2024 paper, 'Spglib: a software library for crystal symmetry search'.

There is no command-line tool here. This is a library, so the first poke is a few lines of Python or C of your own.

## Install

```
brew install spglib
# The README says only conda and pip are officially supported; the brew formula was not checked against it.
# Python route: pip install spglib
# Needs C11 or later to build the C library. No accounts or hardware needed.
```

## Try this

```
pip install spglib
```
Installs the Python package from PyPI, the officially supported route, so you can call the symmetry search from a script.

```
conda install -c conda-forge spglib
```
Installs the conda package, which bundles the C and Fortran libraries.

```
ctest --test-dir ./build
```
After a CMake build from source, runs the C library's test suite, which is enabled by default.

## What's unique

It is the reference symmetry-finding library behind many crystallography tools. It handles magnetic space groups as well as ordinary ones, and its tolerance-based search copes with slightly distorted real structures.

## Caveats

It ships no executables, so you need to write code against it, and the README's only worked example is a short C snippet. Official packaging covers only conda and pip, and other platforms need a manual CMake build.

## Links

- [Documentation (homepage)](https://spglib.readthedocs.io/en/latest/)
- [GitHub repository](https://github.com/spglib/spglib)
- [Citation paper (Sci. Technol. Adv. Mater., Meth. 2024)](https://www.tandfonline.com/doi/full/10.1080/27660400.2024.2384822)
