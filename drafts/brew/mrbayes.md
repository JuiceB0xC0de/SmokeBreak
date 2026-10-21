---
name: mrbayes
title: MrBayes
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bayesian, math, mcmc, phylogenetics, science]
homepage: https://nbisweden.github.io/MrBayes/
scout_score: 6
status: draft
---

# MrBayes

**TLDR;** A command-line program that estimates evolutionary trees from DNA, protein or trait data using Bayesian MCMC, the standard way to ask how species are related.

MrBayes reads sequence or character data (nucleotides, amino acids, restriction sites, morphological traits, even mixed in one analysis) and estimates which evolutionary trees and model parameters best explain it. Instead of returning one answer, it samples from a posterior distribution using Markov chain Monte Carlo. The output is a set of sampled trees and parameters, plus majority-rule consensus trees in FigTree format with branch and node summaries.

The idea underneath is that a phylogeny is a hypothesis with uncertainty, not a fact. A chain wanders through the space of possible trees and models, spending more time where the data fit better. Convergence monitoring during the run and diagnostics afterward tell you whether the wandering has settled. Checkpointing lets a run be extended or recovered after a crash. It also supports model choice through Bayes factors using the stepping-stone method.

The homepage describes a general-purpose tool with one command-line interface across Macintosh, Windows and UNIX. It can link parameters across partitions and handles positive selection and multi-species coalescent (BEST) models. Optional MPI spreads jobs across a cluster, and optional BEAGLE support speeds up codon and amino acid models on compatible NVIDIA GPUs.

The interface is an interactive prompt rather than a GUI. Learning it means learning how phylogenetic models are specified, which is the real door into the field.

## Install

```
brew install mrbayes
# installs the `mb` executable; pulls in beagle and open-mpi as dependencies
# from source instead: git clone --depth=1 https://github.com/NBISweden/MrBayes.git && cd MrBayes && ./configure && make && sudo make install
```

## Try this

```
mb --help
```
Prints the program's command-line usage, a first look at how it is driven.

## What's unique

It mixes data types in one analysis, links parameters across partitions, and covers positive selection and multi-species coalescent models, all from a plain terminal.

## Caveats

It has been in maintenance mode since release 3.2.6 in November 2015, so expect bug fixes rather than new features, and you need your own sequence data and the manual to get far.

## Links

- [Homepage](https://nbisweden.github.io/MrBayes/)
- [GitHub repository (README, build instructions, examples)](https://github.com/NBISweden/MrBayes)
- [MrBayes project site](http://mrbayes.net/)
