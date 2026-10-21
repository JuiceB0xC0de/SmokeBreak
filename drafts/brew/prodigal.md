---
name: prodigal
title: Prodigal
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [bacteria, bioinformatics, dna, genomics, quick, science]
homepage: https://github.com/hyattpd/Prodigal
scout_score: 6
status: draft
---

# Prodigal

**TLDR;** Prodigal reads bacterial DNA in FASTA format and predicts where the protein-coding genes are, with no training data, in about ten seconds for E. coli.

Prodigal is a command-line gene finder for prokaryotic genomes, written by Doug Hyatt. You give it a FASTA file of DNA (a finished genome, a draft assembly, or a metagenome) and it predicts the protein-coding genes. Coordinates can be written as GFF3, GenBank, or Sequin table, and the predicted protein translations can go to a separate FASTA file.

The idea underneath it is that a genome can be used to interpret itself. The README calls Prodigal "an unsupervised machine learning algorithm" that "does not need to be provided with any training data, and instead automatically learns the properties of the genome from the sequence itself, including RBS motif usage, start codon usage, and coding statistics." Bacterial genes are dense and statistically distinctive, so the program can bootstrap a model from the raw sequence, then use it to call genes and pick likely translation start sites.

That makes it a way into real bioinformatics without needing a reference database or an account. Feed it a genome, look at the proteins it finds, and you are looking at the first step of how newly sequenced microbes get annotated. The README also says it can report confidence scores and RBS details for every candidate start site, which is where you can start to see how uncertain the problem is.

## Install

```
brew install prodigal
# You also need a DNA sequence file in FASTA format. No accounts or runtimes are required.
```

## Try this

```
prodigal -h
```
Prints the full list of options, including output formats and modes.

```
prodigal -i my.genome.fna -o my.genes -a my.proteins.faa
```
Reads a genome FASTA, writes gene coordinates to my.genes and predicted protein sequences to my.proteins.faa.

```
prodigal -i my.metagenome.fna -o my.genes -a my.proteins.faa -p meta
```
Runs the same prediction in metagenome mode, for mixed or fragmentary input.

## What's unique

It is unsupervised, so it needs no reference database or training set because it learns from each input genome. It also handles draft genomes and metagenomes, not just finished ones.

## Caveats

The README's latest entry is version 2.6.3 from February 2016, so the project looks quiet, and it only handles prokaryotes, not eukaryotic genomes.

## Links

- [GitHub repository (homepage)](https://github.com/hyattpd/Prodigal)
- [Wiki documentation](https://github.com/hyattpd/prodigal/wiki)
- [Options cheat sheet](https://github.com/hyattpd/prodigal/wiki#cheat-sheet)
- [Project website](http://prodigal.ornl.gov/)
