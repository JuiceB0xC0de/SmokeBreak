---
name: iqtree3
title: IQ-TREE 3
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, biology, phylogenetics, science, statistics]
homepage: http://www.iqtree.org
scout_score: 6
status: draft
---

# IQ-TREE 3

**TLDR;** Command-line software that builds evolutionary trees from DNA or protein alignments by maximum likelihood, and can also simulate sequences to test itself against.

IQ-TREE 3 takes a multiple sequence alignment and infers the evolutionary tree that best explains it. It reads common alignment formats: PHYLIP, FASTA, Nexus, Clustal and MSF. It writes a human-readable report with the suffix .iqtree and a Newick tree file ending in .treefile, which viewers such as FigTree, Dendroscope or iTOL can open.

The README says it succeeded IQPNNI and TREE-PUZZLE, and was motivated by the rapid growth of phylogenomic data. That growth called for software that copes with large datasets and richer models of how sequences evolve. It uses a fast stochastic tree search and can run on multicore machines or in distributed parallel setups. It checkpoints automatically, so an interrupted analysis can resume: "IQ-TREE automatically performs checkpointing to resume an interrupted analysis."

The idea underneath is maximum-likelihood phylogenetics. You pick a model of how characters change over time, and the program searches for the tree and branch lengths that make your observed sequences most probable. The choice of model matters, so ModelFinder picks one automatically. Branch support comes from the UFBoot ultrafast bootstrap approximation, with tests such as SH-aLRT, aBayes and AU also bundled.

It also includes AliSim, an alignment simulator that the README says goes beyond Seq-Gen and INDELible. You can generate sequences from a known tree, then see whether the inference recovers it. That makes the tool a way to learn how the method behaves, as well as a tool for analysing real data.

## Install

```
brew install iqtree3
```

## Try this

```
iqtree3 --help
```
Prints the list of options. The README gives no usage examples, so this is the place to start.

## What's unique

The model library is unusually broad: DNA, protein, codon, binary and morphological models, partition and mixture models, polymorphism-aware models, and SNP ascertainment-bias correction. A simulator and several branch-support tests ship in the same tool.

## Caveats

The README has no command examples, so you will need the online documentation for usage, and the homepage did not load when the brief was written (the GitHub README was read instead).

## Links

- [Homepage](http://www.iqtree.org)
- [User documentation](http://www.iqtree.org/doc/)
- [GitHub repository (iqtree3)](https://github.com/iqtree/iqtree3)
