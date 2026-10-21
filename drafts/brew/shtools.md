---
name: shtools
title: SHTOOLS
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, fortran, geophysics, library, math, python, science]
homepage: https://shtools.github.io/SHTOOLS/
scout_score: 6
status: draft
---

# SHTOOLS

**TLDR;** A Fortran 95 library, with a Python interface, for spherical harmonics: transform gravity, magnetic and topography maps of whole planets into frequencies and back.

SHTOOLS works with data on a sphere. Give it a global grid or a set of spherical harmonic coefficients and it transforms between the two, computes power spectra, and produces derived fields. Spherical harmonics are to a globe what Fourier series are to a time signal: they split a map into patterns of increasing spatial detail.

It was built for geophysics and planetary science. The README describes an archive of software for spherical harmonic transforms, multitaper spectral analysis, Slepian expansions, and standard operations on global gravity and magnetic field data. The reference paper is Wieczorek and Meschede (2018) in Geochemistry, Geophysics, Geosystems. The numerical core is Fortran 95, wrapped for Python as pyshtools. It can import gravity, topography and magnetic datasets and draw maps through Cartopy and PyGMT.

The idea underneath is that a field on a sphere can be analysed like a signal. Slepian functions, for example, concentrate that analysis on one region, such as a continent, when you do not have data for the whole globe. You can choose among normalization and phase conventions, convert between real and complex harmonics, and pick a native Fortran or DUCC0 backend for the heavy math.

This is a library, not a command-line tool. The brew formula installs the Fortran library only, and it has no executables. To play with it you almost certainly want the Python package.

## Install

```
pip install pyshtools
# the brew formula installs only the Fortran library, not the Python package:
brew install shtools
# alternative: conda install -c conda-forge pyshtools (Linux and macOS only)
# Building from source needs a Fortran compiler and build tools.
```

## Try this

```
pip install pyshtools
```
Installs the Python package from PyPI, with pre-built binaries for Linux, macOS and Windows.

```
pip install pyshtools --no-binary pyshtools
```
Forces a build from source instead of using the pre-built wheels.

```
make fortran
```
Builds the Fortran 95 library from a cloned repo, run inside the shtools directory.

## What's unique

It pairs a Fortran 95 core with a Python API and includes multitaper and Slepian tools, which are uncommon in general-purpose Python science packages.

## Caveats

The brew and MacPorts packages are the Fortran library, not the Python package, which is easy to mix up; the native backend is accurate to about degree 2800, and beyond that DUCC0 is needed.

## Links

- [Homepage (pyshtools documentation)](https://shtools.github.io/SHTOOLS/)
- [GitHub repository](https://github.com/SHTOOLS/SHTOOLS)
- [Reference paper (Wieczorek and Meschede 2018)](https://doi.org/10.1029/2018GC007529)
- [Gravity and magnetic fields tutorial notebook](https://nbviewer.jupyter.org/github/SHTOOLS/SHTOOLS/blob/master/examples/notebooks/gravity-and-magnetic-fields.ipynb)
