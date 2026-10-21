---
name: freesasa
title: FreeSASA
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, biophysics, c-library, pdb, proteins, science]
homepage: https://freesasa.github.io/
scout_score: 6
status: draft
---

# FreeSASA

**TLDR;** Give it a protein structure file and it reports how much of each atom's surface a water molecule could touch, using a rolling-ball algorithm from the 1970s.

FreeSASA calculates solvent accessible surface area (SASA) for biomolecules. Imagine rolling a ball the size of a water molecule over the surface of a protein. The path the ball's center traces out is the accessible surface. Its area says which parts of a molecule sit exposed to the surrounding water and which are buried in the core.

The command-line tool takes a PDB file, the standard format for 3D structures of proteins and nucleic acids, and prints results with no configuration. By default it uses Lee and Richards' algorithm, with Shrake and Rupley's as an alternative. Each atom gets a radius and a polar or apolar label, taken by default from the ProtOr radii (Tsai et al., 1999). Atoms outside standard amino acids and nucleic acids fall back to the element's van der Waals radius.

The project's own pitch is that casual users get answers with sensible defaults, while advanced users can change every parameter, supply their own radii and classification files, and call a C library or Python module on raw coordinate arrays. The share/ directory includes an example using NACCESS parameters.

The idea underneath is that buried versus exposed surface is a quantity you can compute from coordinates alone, and it connects to real questions in structural biology, such as which residues hydrophobic cores hide and where binding might happen. It is a small way into that field's tooling.

## Install

```
brew install freesasa
# The homepage instead lists: brew install brewsci/bio/freesasa
# No account or hardware needed. You will need a PDB file to feed it. The homepage also offers a WebAssembly demo that runs in the browser.
```

## Try this

```
freesasa -h
```
Shows the command-line options, which both the homepage and README point to first.

```
freesasa <pdb-file>
```
Runs a SASA calculation on a PDB file using the default algorithm and radii, and prints the results.

```
man freesasa
```
Opens the man page, if it was installed with the build.

## What's unique

It works on a single PDB file with zero configuration, yet exposes selectable algorithms, custom radii and a documented C API underneath. The browser demo lets you try it before installing anything.

## Caveats

Upkeep status is unclear from the sources, and version 2 broke parts of the 1.x API, so older code written against it may not work.

## Links

- [FreeSASA homepage](https://freesasa.github.io/)
- [Doxygen reference manual (CLI and C API)](http://freesasa.github.io/doxygen/)
- [GitHub repository (mittinatten/freesasa)](https://github.com/mittinatten/freesasa)
