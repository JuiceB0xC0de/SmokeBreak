---
name: paml
title: PAML
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, biology, phylogenetics, science, statistics]
homepage: https://github.com/abacus-gene/paml
scout_score: 6
status: draft
---

# PAML

**TLDR;** Nine command-line programs that fit evolutionary models to DNA and protein alignments by maximum likelihood, then test hypotheses about selection and divergence times.

PAML (Phylogenetic Analysis by Maximum Likelihood) is a package maintained by Ziheng Yang. You give it a sequence alignment, a tree, and a plain-text control file. It gives back text: parameter estimates, likelihood values, and the results of hypothesis tests. The package has nine executables, including baseml for nucleotides, codeml for codons and proteins, mcmctree for Bayesian divergence dating, evolver for simulation, and yn00 for pairwise estimates.

It does not build trees. The README says so directly: "PAML is not good for tree making, although it may be used to estimate parameters and test hypotheses to study the evolutionary process once you have reconstructed trees using other programs". You bring a tree from something like IQ-TREE, RAxML-NG, PhyML, or PHYLIP, and PAML asks questions of it. Did selection act on this gene? How fast did these lineages diverge? When did they split?

The idea underneath is that an evolutionary model is a probability model. You can compute how likely your observed sequences are under it. Compare the likelihoods of two competing models and you can test a biological hypothesis with statistics. That idea is a door into molecular evolution, codon models, and molecular clock dating.

The package is decades old and still gets releases. The README says most user problems come from badly formatted sequence or tree files and control files, so expect to spend your first session reading the Wiki's data formatting section.

## Install

```
brew install paml
```

## Try this

```
baseml
```
Starts the nucleotide model program, the release notes' suggested check that the install works. It looks for a control file in the current directory.

```
codeml
```
Starts the codon and protein model program. It reads a control file to set up the analysis.

```
mcmctree --combine <directory_name>
```
Merges MCMC sample files from independent MCMCtree runs saved in one directory into mcmc_combined.txt.

## What's unique

It is a long-lived, widely cited package for codon selection analyses and Bayesian divergence dating, and the author still maintains it. It does the statistics on a tree you already have rather than building one.

## Caveats

It needs correctly formatted alignments, trees, and control files to do anything; the Wiki is still under construction and the PDF manuals are being migrated.

## Links

- [GitHub repository (homepage)](https://github.com/abacus-gene/paml)
- [PAML Wiki](https://github.com/abacus-gene/paml/wiki/)
- [Releases](https://github.com/abacus-gene/paml/releases)
- [PAML FAQs (PDF)](https://github.com/abacus-gene/paml/blob/master/doc/pamlFAQs.pdf)
