---
name: packmol
title: Packmol
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, chemistry, molecular-dynamics, science, simulation]
homepage: https://www.ime.unicamp.br/~martinez/packmol/
scout_score: 5
status: draft
---

# Packmol

**TLDR;** Packmol packs hundreds or thousands of molecules into boxes, spheres, or membranes without overlaps, building the starting point for molecular dynamics simulations from a short text file.

Packmol is a command-line program that builds starting coordinates for molecular dynamics. You give it a coordinate file for one molecule of each type (PDB, TINKER, or XYZ), say how many copies you want, and describe where they should go. It writes out a single file with everything placed. The user guide's example packs 2000 water molecules into a 40 Å cube from a short input file.

It exists because a simulation that starts with atoms sitting on top of each other blows up. In the homepage's words, Packmol "creates an initial point for molecular dynamics simulations by packing molecules in defined regions of space", so that short-range repulsive interactions do not wreck the run. Under the hood it optimizes the positions and rotations of each molecule until a minimum atom-atom distance (the `tolerance`, typically 2.0 Å for all-atom systems) and the region constraints are met.

The interesting part is the constraint language. Regions are geometric: inside or outside a box, sphere, ellipsoid, or cylinder, above or below a plane, and even per-atom selections. A few lines can describe a lipid layer, a vesicle, or a tube, and the project says this makes ordered systems like lamellar, spherical, or tubular lipid layers easy to build. A restart file lets very large systems be assembled in stages.

The guide is clear that this is a first-pass generator, not a simulator. The output still needs energy minimization and equilibration in a real MD engine. Still, it is a good way to see what the setup side of computational chemistry looks like.

## Install

```
brew install packmol
# Homebrew builds it with gcc (Fortran). You also need your own molecule coordinate files (PDB, TINKER, or XYZ) and an input file. The guide also points to a Julia wrapper, Packmol.jl, that needs no compilation.
```

## Try this

```
packmol < packmol.inp
```
Reads a Packmol input file on stdin, packs the listed molecules into the regions you described, and writes the output coordinate file.

```
packmol -i packmol.inp -o output.pdb
```
Same run with command-line arguments (from v21.1.0 on); -o optionally overrides the output filename set in the input file.

## What's unique

Systems are described as geometric regions rather than coordinates, so a membrane interface or a vesicle takes a few lines of input. Restart files let very large systems be built in stages.

## Caveats

It is only a preprocessing step, so the output needs minimization and equilibration elsewhere; packing can also fail to converge and need tuning of settings like discale or maxit.

## Links

- [Packmol homepage (UNICAMP)](https://www.ime.unicamp.br/~martinez/packmol/)
- [Packmol site with downloads, input examples, and version history](https://m3g.github.io/packmol/)
- [Packmol user guide](https://m3g.github.io/packmol/userguide.shtml)
