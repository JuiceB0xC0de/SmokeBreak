---
name: fastme
title: FastME
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, biology, math, phylogenetics, science]
homepage: http://www.atgc-montpellier.fr/fastme/
scout_score: 5
status: draft
---

# FastME

**TLDR;** Builds evolutionary trees from distance matrices or sequence alignments, using Balanced Minimum Evolution to beat Neighbor Joining at similar speed.

FastME infers phylogenetic trees, the branching diagrams that show how species or genes are related. It reads a square PHYLIP distance matrix, or a DNA, protein, or PHYLIP alignment from which it estimates the distances itself, and writes out a tree.

The idea underneath is Balanced Minimum Evolution (BME). Of all possible trees, pick the one with the smallest total estimated evolutionary distance among the taxa. Neighbor Joining is a fast greedy way to get a decent tree. FastME starts from an NJ-like tree and then improves it with rearrangements: Nearest Neighbor Interchange (NNI) and Subtree Pruning and Regrafting (SPR). The goal is a better topology without paying the full cost of a likelihood search.

The homepage says FastME is aimed at large datasets, where likelihood-based methods "may be computationally demanding". It also lists several distance estimation methods, bootstrap support, and parallel computation. The tool comes from the 2015 FastME 2.0 paper by Lefort, Desper, and Gascuel, and the same group hosts a web form that runs it online.

It is a door into how trees get inferred at all: distances, tree search, and the tradeoff between speed and statistical rigor.

## Install

```
brew install fastme
```

## Try this

```
fastme --help
```
Prints the available options for input data, distance methods, tree refinement, and bootstrapping.

```
FastME -m I -w N
```
The flags the web form's BioNJ pipeline uses: BioNJ mode with no refinement. You supply your own input file and any other options.

## What's unique

It starts from a Neighbor-Joining-like tree and then searches for a better BME tree with SPR moves. The aim is accuracy closer to likelihood methods at distance-method speed.

## Caveats

The brief found no release date or version on the homepage, and you need your own PHYLIP matrix or alignment to do anything real.

## Links

- [FastME homepage (ATGC platform)](http://www.atgc-montpellier.fr/fastme/)
- [FastME 2.0 paper, Molecular Biology and Evolution](https://doi.org/10.1093/molbev/msv150)
