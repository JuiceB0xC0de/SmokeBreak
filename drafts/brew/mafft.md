---
name: mafft
title: MAFFT
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, fft, math, science, sequences]
homepage: https://mafft.cbrc.jp/alignment/software/
scout_score: 5
status: draft
---

# MAFFT

**TLDR;** A multiple sequence alignment program that lines up many protein or DNA sequences at once, with speed and accuracy settings you pick between.

MAFFT takes a FASTA file of amino acid or nucleotide sequences and writes an alignment to standard output. It works out for itself whether the input is protein or nucleotide. Multiple sequence alignment means stacking related sequences so that matching positions line up in columns, which is the starting point for comparing how genes and proteins are related.

The program offers several strategies that trade accuracy against speed. The homepage lists L-INS-i as accurate, for up to about 200 sequences, and FFT-NS-2 as fast, for up to about 30,000 sequences. If you are unsure which to use, the --auto option lets MAFFT choose. A PartTree algorithm is also mentioned for building an approximate tree from a large number of unaligned sequences.

The idea underneath is in the title of the 2002 paper the homepage cites: 'MAFFT: a novel method for rapid multiple sequence alignment based on fast Fourier transform'. The Fourier transform, a signal-processing tool, is used here on biological sequences. The homepage does not explain the mechanism in detail, so the paper is the place to go for how it works. That makes MAFFT a door into bioinformatics, and into the question of why aligning many sequences is hard enough to need shortcuts.

## Install

```
brew install mafft
```

## Try this

```
mafft --auto input > output
```
Reads a FASTA file, lets MAFFT pick a strategy, and writes the alignment to the output file.

```
mafft-linsi input > output
```
Runs the accurate L-INS-i option, meant for up to about 200 sequences.

```
mafft input > output
```
Runs the fast FFT-NS-2 option, intended for larger sets of sequences.

## What's unique

One program covers a range of accuracy and speed trade-offs, with an --auto mode that chooses for you. It also detects protein versus nucleotide input without being told.

## Caveats

You need your own FASTA file to get anything out of it, and versions 7.463 to 7.486 have a memory bug in the FFT-NS-i option and in --auto, so use 7.487 or later.

## Links

- [MAFFT homepage](https://mafft.cbrc.jp/alignment/software/)
