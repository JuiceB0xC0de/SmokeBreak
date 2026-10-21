---
name: modflow6
title: MODFLOW 6
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, fortran, groundwater, hydrology, science, simulation]
homepage: https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model
scout_score: 6
status: draft
---

# MODFLOW 6

**TLDR;** The USGS's groundwater simulator: describe an aquifer, its wells and rivers in text files, and mf6 computes how the water moves through it.

MODFLOW 6 is the sixth core release of the U.S. Geological Survey's modular groundwater model. You describe a model in input files: the grid, the properties of the aquifer, and the stresses on it, such as wells, rivers, recharge and boundary conditions. The `mf6` program solves three-dimensional, transient groundwater flow and writes out simulated heads, flows and budgets. The homepage also lists transport, energy transport and particle tracking models.

The older MODFLOW was built to run one model on a regular layer-row-column grid. Over the years people bolted on features for surface-water interaction, nested and unstructured grids, karst, solute transport and saltwater intrusion, and the variants stopped being compatible. MODFLOW 6 is a rewrite as an object-oriented framework, meant to hold multiple models and multiple types of models in one simulation.

The idea underneath is the package. Each model is split into packages, and each package handles one aspect, such as wells, rivers, lakes or streamflow routing. Models in one simulation can run independently, exchange information, or be solved together in a single matrix. A Water Mover package can send water between packages, for example routing pumped groundwater into a lake.

It is a door into real hydrogeology: the same kind of code used to reason about aquifers, well fields and contamination. The USGS example problems are published online, and Python tools such as FloPy and the ModelMuse GUI are listed as related ways to build inputs.

## Install

```
brew install modflow6
# installs the mf6 executable; gcc is a dependency. Running it needs model input files, which you write by hand or generate with a tool like FloPy.
```

## Try this

```
mf6 --help
```
Prints the command-line options for the solver, a first check that the install works.

## What's unique

One program absorbs the features of MODFLOW-2005, MODFLOW-NWT, MODFLOW-USG, MODFLOW-LGR, SEAWAT buoyancy, MT3D-USGS and MODPATH 7, and it ships converters for older models. It is also public-domain government science software.

## Caveats

The README calls the software preliminary and provisional with no warranty, and the documentation assumes you already know some hydrogeology.

## Links

- [USGS homepage for MODFLOW 6](https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model)
- [GitHub development repository](https://github.com/MODFLOW-USGS/modflow6)
- [Example problems rendered as online descriptions](https://modflow6-examples.readthedocs.io/en/master/examples.html)
