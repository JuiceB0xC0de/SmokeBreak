---
name: healpix
title: HEALPix
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astronomy, cosmology, fits, math, science, sphere]
homepage: https://healpix.sourceforge.io
scout_score: 6
status: draft
---

# HEALPix

**TLDR;** A way of cutting a sphere into equal-area pixels, built for mapping the cosmic microwave background, with command-line tools for analysing full-sky maps.

HEALPix stands for Hierarchical Equal Area isoLatitude Pixelization. It is a scheme for dividing the surface of a sphere into pixels that all cover the same area, plus a software package built around that grid. The package ships in C, C++, Fortran 90, IDL, Java and Python. It handles spherical harmonic transforms, filtering, pixel queries, median filtering, mask handling and map rotation. FITS is the usual file format. Outputs include maps, harmonic coefficients and images, among them Google Earth/Sky and DomeMaster planetarium images.

It was built for cosmic microwave background satellite data, from WMAP and then Planck. Those missions needed full-sky maps at arcminute resolution and fast, accurate statistics. The homepage says its use has since spread well beyond the CMB field.

The idea underneath is the grid. The sphere is split into 12 base curvilinear quadrilaterals, and each pixel divides into four at the next resolution level. Pixels sit on lines of constant latitude, which, according to the homepage, makes spherical harmonic integrals scale as about N^1/2 rather than N. The transforms come from a shared optimised library called libsharp. The stated finest resolution reaches 0.4 milli-arcseconds.

The Homebrew formula installs a set of command-line programs, such as `anafast_cxx`, `smoothing_cxx`, `udgrade_cxx` and `map2tga`. The pages I read describe the package's features but not these programs' usage, so the executable names are the main hint at what each does.

## Install

```
brew install healpix
# Depends on cfitsio. Python users usually want healpy instead: pip install healpy
# Fortran codes on Apple ARM chips need CFITSIO 4.1.0 or higher.
```

## Try this

```
anafast_cxx --help
```
Prints usage for the C++ tool whose name suggests it analyses a map into harmonic coefficients.

```
smoothing_cxx --help
```
Prints usage for the smoothing tool, a good first look at how these programs take FITS maps.

```
udgrade_cxx --help
```
Prints usage for the tool that appears to change a map's resolution, which shows the hierarchical pixel idea in practice.

## What's unique

The equal-area, iso-latitude grid is what makes harmonic analysis fast, and the homepage says so directly rather than just claiming equal pixels. The base-12 recursive quartering gives a clean hierarchy of resolutions.

## Caveats

The pages I read give no command-line usage, so expect to work from --help and the source package docs; releases are infrequent, with 3.83 from November 2022 the latest listed.

## Links

- [HEALPix homepage](https://healpix.sourceforge.io)
- [Getting HEALPix (downloads page)](https://healpix.sourceforge.io/downloads.php)
