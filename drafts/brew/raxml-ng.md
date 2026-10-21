---
name: raxml-ng
title: RAxML-NG
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, maximum-likelihood, phylogenetics, science]
homepage: https://cme.h-its.org/exelixis/web/software/raxml/
scout_score: 5
status: draft
---

# RAxML-NG

**TLDR;** Infers evolutionary trees from aligned DNA or protein sequences by maximum likelihood, the real method biologists use to work out who descends from whom.

RAxML-NG takes a multiple sequence alignment and a substitution model, then searches for the tree that makes the observed sequences most probable. It can also run bootstrap replicates, map support values onto a tree, or score a fixed topology. The output is tree files and run logs.

The search works by hill climbing. It starts from a tree, applies Subtree Pruning and Regrafting (SPR) moves, which cut a branch off and reattach it elsewhere, and keeps whatever improves the likelihood. The number of possible trees explodes as you add species, so the search is a heuristic and not a proof. Likelihood calculation is handled by a separate optimized library, coraxlib.

It is the successor to RAxML (Stamatakis 2014). The README describes it as faster, more flexible and more user-friendly, and says it carries over checkpointing and load balancing for partitioned alignments from ExaML. Version 2.0 adds adaptive search heuristics, automatic model selection (MOOSE) and fast branch support metrics.

The door it opens is phylogenetics itself: how substitution models, rate variation and bootstrap support turn a pile of sequences into a defensible family tree. You need an alignment to begin, and the project's wiki has a hands-on tutorial.

## Install

```
brew install raxml-ng
```

## Try this

```
raxml-ng -h
```
Prints the built-in help listing the run modes and options.

```
raxml-ng --fast --msa testDNA.fa --model DNA
```
Runs a quick single tree inference on a DNA alignment, with automatic model selection and early stopping. You supply your own alignment file.

```
raxml-ng --all --msa testAA.fa --model LG+G8+F --tree pars{10} --bs-trees 200
```
Searches from 10 parsimony starting trees and runs 200 bootstrap replicates on a protein alignment, giving a best tree with support values.

## What's unique

It is a maintained successor to a well-known phylogenetics program, with adaptive search, automatic model selection and fast support metrics. It also keeps a compatibility mode for the older v1.1.0 behaviour.

## Caveats

It is a specialist bioinformatics tool that needs an alignment and some model knowledge, the brew homepage points to the legacy RAxML 8 page, development lives on Codeberg, and the code is AGPL-3.0.

## Links

- [Legacy RAxML homepage (from brew metadata)](https://cme.h-its.org/exelixis/web/software/raxml/)
- [Primary repository on Codeberg](https://codeberg.org/amkozlov/raxml-ng)
- [Documentation wiki and hands-on tutorial](https://codeberg.org/amkozlov/raxml-ng/wiki)
- [RAxML-NG paper (Bioinformatics 2019)](https://doi.org/10.1093/bioinformatics/btz305)
