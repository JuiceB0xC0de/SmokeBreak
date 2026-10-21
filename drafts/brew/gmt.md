---
name: gmt
title: GMT (Generic Mapping Tools)
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, geoscience, maps, plotting, science, visual]
homepage: https://www.generic-mapping-tools.org/
scout_score: 6
status: draft
---

# GMT (Generic Mapping Tools)

**TLDR;** About 100 command-line tools that turn tables and grids of data into publication-quality maps, contour plots, 3D views and animations.

GMT is a collection of command-line programs for geographic and Cartesian data. Some filter, fit trends, grid and project data. Others draw the result: x-y plots, contour maps, artificially illuminated surfaces, 3D perspective views and animations. It supports more than 30 map projections, and supplements add roughly 50 more specialised tools.

The homepage calls it "A toolbox for Earth, Ocean, and Planetary Science". It exists so researchers can process data and produce figures in scripts, then rerun the same script when the data changes. The README says it is also used in medical research, engineering, physics, government and hobbyist work.

The underlying idea is that a map is the output of a pipeline. You chain small programs in a shell script: read data, transform it, draw it. Since GMT 6 the same machinery is also an API, and wrappers let you call it from Python (PyGMT), Julia, MATLAB/Octave, C and C++. The project dates back to 1991 and appears in a great many published figures.

The README says GMT needs support data, namely GSHHG coastlines, rivers and political boundaries, plus optional DCW country polygons. That is part of the setup, so expect to look at the install docs before your first map.

## Install

```
brew install gmt
# optional, per the Homebrew caveats:
brew install ghostscript      # needed for psconvert (PostScript to other formats)
brew install ffmpeg           # needed for movie, for MP4/WebM
brew install graphicsmagick   # needed for movie, for animated GIFs
# GMT also needs GSHHG coastline data to draw maps; see the install docs.
```

## Try this

```
gmt --help
```
Prints the top-level usage and the list of available GMT modules, a starting point for finding tools.

```
gmt-config --help
```
Shows the options of the helper that reports how your GMT installation is configured.

```
gmt_update --help
```
Shows usage for the GMT update helper script.

## What's unique

GMT has been used for decades in published geoscience figures and is free and LGPL-licensed. It is now also a callable API, so the same engine works from shell scripts and from Python, Julia or MATLAB/Octave.

## Caveats

Maps need coastline support data (GSHHG) downloaded, and psconvert and movie rely on Ghostscript, FFmpeg and GraphicsMagick that must be installed separately.

## Links

- [GMT homepage](https://www.generic-mapping-tools.org/)
- [GitHub repository](https://github.com/GenericMappingTools/gmt)
- [Install documentation](https://docs.generic-mapping-tools.org/latest/install.html)
- [Citation: Wessel et al. 2019, GMT version 6](https://doi.org/10.1029/2019GC008515)
