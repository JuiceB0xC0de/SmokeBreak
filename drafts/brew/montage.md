---
name: montage
title: Montage
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astronomy, c, fits, image-processing, python, science]
homepage: http://montage.ipac.caltech.edu
scout_score: 5
status: draft
---

# Montage

**TLDR;** Caltech's astronomy toolkit that reprojects, background-matches and stitches FITS sky images into custom mosaics, as about seventy small command-line programs.

Montage takes a pile of FITS images, the standard file format for astronomical data, and builds a single mosaic to your specification. You choose the sky coordinates, projection, spatial sampling and rotation. It reprojects each input, rectifies background emission to a common level, and co-adds the results into a new FITS image. The aim, in the README's framing, is an accurate open-source way to do this while preserving spatial and calibration fidelity.

The design is the interesting part. The homepage describes separate engines for analysing image geometry on the sky, re-projecting, background rectification and co-addition. Each engine is a stand-alone ANSI-C executable whose name starts with m, such as mAdd or mProject, and the `*Exec` variants run a step over a whole directory of images. A mosaic is a pipeline you assemble from these parts, which is also why Montage turns up as an example application in workflow and cloud research. The same code runs on a desktop, a cluster or a grid.

There are also tools for reading and tabulating image metadata, examining images, and visualizing results with three-colour displays and catalogue overlays. Since version 6 the algorithms are available from Python as MontagePy, built from the C code through Cython. The 7.0 README adds HiPS tooling: it builds a large mosaic in a HPX projection, shrinks it repeatedly by factors of two to form a tile hierarchy, and cuts 512x512 tiles.

The door it opens is how sky images get stitched together at all. Pixels from different telescopes sit on different grids, projections and background levels, and the problem is making them agree.

## Install

```
brew install montage
# Homebrew prints a licence caveat pointing to http://montage.ipac.caltech.edu/docs/download.html. Read it before use.
# Alternative: pip install MontagePy (Python 3.x, binary wheels for Linux and Mac)
# You will need your own FITS images to get a mosaic out of it.
```

## Try this

```
mAdd --help
```
Prints usage for the co-addition engine, a quick look at how the m-tools take their arguments.

```
mProject --help
```
Shows usage for the reprojection step that resamples an image onto a new coordinate grid.

```
pip install MontagePy
```
Installs the Python binary-extension version from PyPI, an alternative to the Homebrew executables.

## What's unique

It is a long-standing academic mosaicking toolkit written in portable C, split into small single-purpose programs that scale from a laptop to computational grids. The same algorithms are also available from Python.

## Caveats

The Homebrew caveat says a Caltech/JPL non-commercial licence applies while the homepage and README say BSD 3-clause, so check the download page before commercial use; the on-demand web service has been decommissioned, and the README says regression testing is only partly in place.

## Links

- [Montage homepage](http://montage.ipac.caltech.edu)
- [Montage GitHub repository](https://github.com/Caltech-IPAC/Montage)
- [Montage Python notebooks (MontageMosaics)](https://github.com/Caltech-IPAC/MontageMosaics)
- [Montage download page and licence](http://montage.ipac.caltech.edu/docs/download.html)
