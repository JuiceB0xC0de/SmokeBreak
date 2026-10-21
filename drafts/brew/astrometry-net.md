---
name: astrometry-net
title: Astrometry.net
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, astronomy, fits, math, science, visual]
homepage: https://github.com/dstndstn/astrometry.net
scout_score: 8
status: draft
---

# Astrometry.net

**TLDR;** Give it a photo of the night sky with no location info and it works out where in the sky the camera was pointing.

Astrometry.net takes an astronomical image whose sky coordinates are unknown or untrusted and solves it blind. The output is a standards-compliant WCS solution, the metadata that maps every pixel to a position on the sky, plus lists of known catalogue objects inside the field of view. The main command is `solve-field`. The package installs about fifty executables around it, including `build-astrometry-index` for making index files and a pile of FITS and table utilities.

The authors state the goal plainly: "to create correct, standards-compliant, astrometric meta-data for every useful astronomical image ever taken, past and future, in any state of archival disarray." Old plates, phone snapshots and telescope frames with missing headers all count. If every image knows where it points, the world's astronomical images can be organised, annotated and searched.

The matching works from index files that hold star patterns taken from a catalogue. The solver looks for patterns in your image that match patterns in the index, with no prior pointing hint. The README cites the 2010 Lang et al. paper, "Astrometry.net: Blind astrometric calibration of arbitrary astronomical images", for the method and does not explain the algorithm itself. The idea underneath is turning a picture of stars into geometry you can look up.

There is also a public web service at nova.astrometry.net, so you can see what the output looks like before building anything.

## Install

```
brew install astrometry-net
# Solving real images needs index files, which are separate. The docs cover them under 'Building Index Files for Astrometry.net'. The README's own route is Docker: astrometrynet/solver:0.98 ships with some index files and the demo images.
```

## Try this

```
solve-field --help
```
Lists the options of the main solver.

```
docker run --volume "$(pwd):$(pwd)" -w "$(pwd)" astrometrynet/solver:0.98 solve-field image.jpg
```
Runs the solver from the official Docker image on your own image.jpg, with the current directory mounted into the container.

```
(cd /tmp; docker run --volume "$(pwd):$(pwd)" -w "$(pwd)" astrometrynet/solver:0.98 solve-field --dir . /src/astrometry/demo/apod5.jpg)
```
Solves a bundled demo image and writes the results to /tmp as apod5* files.

## What's unique

It solves blind, with no hint about where the camera pointed, and returns real WCS metadata rather than just a label. It is aimed at calibrating archival images as well as new ones.

## Caveats

Nothing solves until you have index files, the README does not describe the build or list platforms, and the whole work is GPL v3 or later because it links GPL libraries.

## Links

- [GitHub homepage and README](https://github.com/dstndstn/astrometry.net)
- [Documentation (Read the Docs)](https://astrometrynet.readthedocs.io/en/latest/)
- [Lang et al. 2010 paper on arXiv](http://arxiv.org/abs/0910.2233)
- [Public web service (nova.astrometry.net)](http://nova.astrometry.net)
