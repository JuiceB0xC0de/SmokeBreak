---
name: gemmi
title: gemmi
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, cif, cli, crystallography, library, proteins, science]
homepage: https://project-gemmi.github.io/
scout_score: 5
status: draft
---

# gemmi

**TLDR;** A command-line toolkit for reading, searching and converting protein structure files, with a CIF-aware grep that can sweep the whole Protein Data Bank archive.

GEMMI is a C++ library for macromolecular crystallography, and it ships with a command-line program, also called gemmi, that bundles many small subcommands. It reads and writes coordinate files (PDB, mmCIF, mmJSON), CIF/STAR files, reflection data (MTZ, SF-mmCIF, XDS_ASCII), CCP4/MRC density maps, and restraint CIF files. Output is usually a converted file, a text report, or a histogram in the terminal.

The subcommand that makes the best first stop is grep. CIF is the format behind the Protein Data Bank's structure files, and its data lives in both name-value pairs and loops, which plain Unix grep handles badly. In the docs' words, "Gemmi-grep parses the CIF syntax and prints values from both name-value pairs and loops." The output pipes into sort, awk and uniq, so a question like "which experimental methods appear across the archive" becomes a one-line shell pipeline.

The docs claim that searching the whole compressed mmCIF archive from the PDB (35GB of gzipped files) takes between 10 and 30 minutes on an average computer. That is the door into the larger idea: the structures of proteins and other biomolecules are public, stored as plain text, and you can interrogate them like any other dataset. Other subcommands go further into crystallography proper, such as map, mask and sfcalc, for density maps, bulk-solvent masks and structure factors.

GEMMI is an open-source project of CCP4 and Global Phasing Ltd, two major providers of crystallography software. It also has Python bindings, partial WebAssembly bindings, and an online viewer, so the same code can be reached from a script or a browser.

## Install

```
brew install gemmi
# Some features read $CLIBD_MON and $PDB_DIR; set them only if you use those. You need a CIF or mmCIF file to try most commands, for example one downloaded from the Protein Data Bank.
```

## Try this

```
gemmi -h
```
Prints the top-level usage and the list of subcommands, such as align, blobs, cif2json, convert, grep and validate.

```
gemmi grep _refine.ls_R_factor_R_free 5fyi.cif.gz
```
Prints one tag's value from a structure file, as a line with the block name and value, e.g. 5FYI:0.2358.

```
gemmi map -h
```
Shows usage for the map subcommand, which summarizes a CCP4 density map, plots a histogram, and can write masks or re-gridded maps.

## What's unique

It treats CIF syntax as the core, so its tools work on archive-scale data where plain grep fails on looped tags. One project covers a C++ library, a CLI, Python bindings and browser builds.

## Caveats

The brief could not confirm a last-commit date, though the docs are at 0.7.6-dev and the README's copyright runs through 2025; the docs call one command gemmi diff while the usage text lists cifdiff, so check gemmi -h for exact names.

## Links

- [Project homepage (redirects to GitHub)](https://project-gemmi.github.io/)
- [Documentation: gemmi program page](https://gemmi.readthedocs.io/en/latest/program.html)
- [GitHub repository and README](https://github.com/project-gemmi/gemmi)
- [JOSS paper (citation)](https://doi.org/10.21105/joss.04200)
