---
name: augustus
title: Augustus
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, gene-prediction, genomics, science]
homepage: https://bioinf.uni-greifswald.de/augustus/
scout_score: 6
status: draft
---

# Augustus

**TLDR;** A gene finder that reads raw eukaryotic genome sequence and predicts where genes, exons, introns and alternative transcripts sit, and can be retrained for a new species.

AUGUSTUS takes a genome sequence and reports predicted gene models: where each gene starts and ends, how its exons and introns are laid out, and in some cases alternative transcripts with probabilities attached. The README describes it as a program "to find genes and their structures in one or more genomes."

It can work ab initio, from the DNA sequence alone. It can also fold in extrinsic evidence such as EST or mRNA alignments, protein alignments and RNA-Seq reads. That evidence is what lets it predict UTRs and alternative transcripts. The homepage says it is often the most accurate ab initio program for species it has been trained on.

The idea underneath is that a genome is a long string with no labels, and gene structure has to be inferred statistically. The model is trained from a set of known genes. AUGUSTUS ships with parameter sets for many animals, plants, fungi and some protists and bacteria. It also includes a training program, etraining, and an optimization script that tunes meta parameters such as splice window sizes. So you can teach it a new species rather than only running what it came with.

The extra executables in the formula (bam2hints, bam2wig, filterBam, joingenes and others) are the plumbing for turning evidence files into hints and merging predictions. Most of the learning is in how the pieces fit together, and the brief does not cover that detail.

## Install

```
brew install augustus

The homebrew formula pulls in bamtools, boost and htslib. Set AUGUSTUS_CONFIG_PATH to the directory holding the config and species parameter files if the programs cannot find it. The programs check that variable first, then fall back to ../config relative to the executable. You also need a genome sequence file to run it on. The web server needs no install.
```

## Try this

```
augustus --help
```
Prints the usage message, including the options for choosing a species parameter set and supplying extrinsic hints.

```
etraining --help
```
Shows the training program's options, which estimate model parameters from a set of known genes.

```
export AUGUSTUS_CONFIG_PATH=/my_path_to_AUGUSTUS/augustus/config/
```
Points augustus and etraining at the directory with the species parameter files, which they need before they can predict anything.

## What's unique

It is retrainable, with a training program included, and it has a flexible way to mix in cDNA, EST, RNA-Seq and protein evidence. It is a long-used research gene finder you can run on your own machine, not only a web service.

## Caveats

The homepage news items are dated 2009 and 2012, though the GitHub repo has CI and Debian and Ubuntu packages; UTR prediction is trained only for a short list of species, and you need real genome data to see anything useful.

## Links

- [Homepage (Greifswald bioinformatics group)](https://bioinf.uni-greifswald.de/augustus/)
- [GitHub repository and README](https://github.com/Gaius-Augustus/Augustus)
- [Running AUGUSTUS guide (docs/RUNNING-AUGUSTUS.md)](https://github.com/Gaius-Augustus/Augustus/blob/master/docs/RUNNING-AUGUSTUS.md)
- [Web server (WebAUGUSTUS)](http://bioinf.uni-greifswald.de/webaugustus/)
