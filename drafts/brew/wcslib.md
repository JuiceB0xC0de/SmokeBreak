---
name: wcslib
title: wcslib
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astronomy, fits, library, math, projections, science]
homepage: https://www.atnf.csiro.au/computing/software/wcs/
scout_score: 6
status: draft
---

# wcslib

**TLDR;** The reference C library for FITS World Coordinate System transforms, which map pixels in astronomical images to positions on the sky, plus a few small utilities.

A FITS image is just an array of numbers. The header holds keywords that say where on the sky each pixel points, and in what spectral or time terms. WCSLIB reads those keywords and does the maths that turns pixel positions into sky coordinates and back again. The homepage describes it as a C implementation of the transformations defined in the FITS WCS papers, with FORTRAN wrapper functions.

The interesting part is the standard underneath. Mapping a sphere onto a flat image can be done in many ways, and the papers define the projections, spectral representations and time handling that astronomers have agreed to use. The HEALPix (HPX) projection comes from Paper V and the XPH butterfly projection from Paper VI. Each projection is a different compromise about what to distort.

The package also installs a few command-line tools. HPXcvt converts 1D HEALPix pixelization data in FITS, in ring or nested order inside a binary table extension, into a 2D primary image array with HPX or XPH coordinates. The homepage does not describe the other installed tools (fitshdr, sundazel, tofits, wcsware) beyond their names.

The homepage offers test data too: example FITS files for each projection in Paper II and for the spectral representations in Paper III. It also offers a 13MiB WMAP 3-year ILC map for trying HPXcvt. That makes it possible to check transforms against known files and see how a whole-sky map gets flattened.

## Install

```
brew install wcslib
# installs the cfitsio dependency; test FITS files are downloaded separately from the homepage
```

## Try this

```
HPXcvt --help
```
Shows the options for converting HEALPix data in FITS into a 2D HPX or XPH image.

```
fitshdr --help
```
Shows usage for the FITS header utility.

```
wcsware --help
```
Shows usage for the WCS utility that works with header keywords.

## What's unique

It is the reference implementation of the FITS WCS standard, and the homepage says it won the 2025 ADASS software prize. It also comes with example data for every projection in the standard.

## Caveats

This is mainly a library for people writing code, and the homepage is a literature and download page that does not document the utilities, so expect to read the source or the doxygen manual.

## Links

- [FITS World Coordinate Systems (FITSWCS) homepage](https://www.atnf.csiro.au/computing/software/wcs/)
