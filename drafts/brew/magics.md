---
name: magics
title: Magics
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, library, python, science, visual, weather]
homepage: https://confluence.ecmwf.int/display/MAGP/Magics
scout_score: 5
status: draft
---

# Magics

**TLDR;** ECMWF's own weather-map plotting library: feed it GRIB, BUFR or NetCDF data and it draws contours, wind fields and graphs as PNG, PDF or SVG.

Magics is the plotting software from ECMWF, the European Centre for Medium-Range Weather Forecasts. It draws weather and climate maps and graphs: contours, wind fields, observations, satellite images, symbols, text, axes, and graphs including boxplots. It is a library, reached through Python or Fortran interfaces, or through ECMWF's Metview environment.

It reads the formats that meteorology actually uses. GRIB 1 and 2 come in through ECMWF's ecCodes library. It also reads gaussian, regular and fitted grids, BUFR, NetCDF, and ODB databases. Output goes to PostScript, EPS, PDF, GIF, PNG or SVG. A script assembles a plot from these pieces and writes it to a file.

The idea underneath is that forecast data is a stack of gridded numbers in specialised formats, and a map is just a careful rendering of them. Magics is the plotting engine under Metview, so it is the same code that draws maps at a working forecasting centre. The homepage also says it uses the Terralib library in cooperation with Brazil's INPE.

The brew formula installs several executables (magics, metgram, magml, magjson and others). The pages read for this entry did not explain them, so check each with its help output before relying on it.

## Install

```
brew install magics

This pulls in several libraries (cairo, eccodes, netcdf, pango, proj, qtbase). The README also lists PyPI (package Magics), conda-forge (package magics), a Docker image (ecmwf/magics), and a Binder notebook gallery that needs no install. You will need your own GRIB or NetCDF data to plot.
```

## Try this

```
magics --help
```
Prints the usage text for the main executable, a safe way to see what it expects.

```
metgram --help
```
Shows the options for metgram, one of the other executables the formula installs.

## What's unique

It is the plotting engine ECMWF itself uses under Metview, and it reads GRIB, BUFR, NetCDF and ODB natively. A Binder gallery lets you try it before installing.

## Caveats

The documentation is thin on usage examples, the README points to a separate installation guide, and it is a compiled library with many dependencies aimed at meteorologists.

## Links

- [Homepage (Confluence)](https://confluence.ecmwf.int/display/MAGP/Magics)
- [Installation guide](https://software.ecmwf.int/magics/Installation+Guide)
- [GitHub repository](https://github.com/ecmwf/magics)
- [Docker image](https://hub.docker.com/r/ecmwf/magics)
