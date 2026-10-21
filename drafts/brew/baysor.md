---
name: baysor
title: Baysor
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bayesian, bioinformatics, science, segmentation, spatial-transcriptomics]
homepage: https://github.com/kharchenkolab/Baysor
scout_score: 5
status: draft
---

# Baysor

**TLDR;** Baysor assigns each detected RNA molecule in a spatial transcriptomics image to a cell, using positions and gene identity, with or without a prior segmentation.

Imaging-based spatial transcriptomics tells you where individual RNA molecules sit in a tissue and which gene each one belongs to. What it does not hand you is cells. Baysor takes a table of molecules with x, y and gene columns (z is optional, for 3D) and decides which molecules belong together as a cell. In the README's words: "Baysor finds cells from molecule positions and gene composition, with or without a prior segmentation."

The method is a Bayesian segmentation model over molecule positions and gene identities. You give it a rough cell radius (-s) and a minimum number of molecules per cell (-m). If you already have a segmentation, say from a stained-nucleus image, you can pass it as a second input and set how much to trust it with --prior-segmentation-confidence (default 0.2). The README does not go deeper into the model, so the paper is the place for that.

The idea underneath is that the molecules carry information about cell boundaries. Where molecules of the same expression profile cluster, a cell is likely there, even if the image did not show an edge. That makes it a way into computational biology: segmentation choices change every downstream result in a spatial dataset.

The current release is a native C++ rewrite (cpp-0.9.0). The older Julia version is archived, and the README warns against installing it unpinned.

## Install

```
brew install baysor

You also need your own data: a molecule table (CSV) with x, y and gene columns. No account or licence key is mentioned. Release binaries and a Docker image (Linux x86-64) also exist.
```

## Try this

```
baysor --help
```
Lists the available commands and options.

```
baysor run -m 30 -s 8 molecules.csv
```
Segments the molecules in molecules.csv into cells and writes results to the 'segmentation' directory. The README calls 30 and 8 examples, not defaults, so set them for your protocol.

## What's unique

It can refine an existing segmentation or work from molecules alone, and you set how much weight a prior segmentation gets. It also ships 'segfree' and 'preview' commands, though the README does not explain them.

## Caveats

It needs real imaging-based spatial transcriptomics data to be worth running, and the parameters must be tuned to your protocol.

## Links

- [Baysor on GitHub](https://github.com/kharchenkolab/Baysor)
- [Cell segmentation docs (parameters, priors, inspecting results)](https://kharchenkolab.github.io/Baysor/latest/run/)
- [Xenium workflow](https://kharchenkolab.github.io/Baysor/latest/xenium/)
- [Citation: Petukhov et al., Nat Biotechnol 2021](https://doi.org/10.1038/s41587-021-01044-w)
