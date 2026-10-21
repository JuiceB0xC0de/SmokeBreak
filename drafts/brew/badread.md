---
name: badread
title: Badread
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, genomics, python, science, sequencing, simulation]
homepage: https://github.com/rrwick/Badread
scout_score: 8
status: draft
---

# Badread

**TLDR;** A command-line simulator that generates deliberately flawed DNA long reads, with separate dials for chimeras, junk, adapters, glitches and error rates.

Badread takes a reference genome in FASTA format and a quantity such as 50x, then writes simulated long sequencing reads to standard output as FASTQ. The reads are not clean. You choose how many chimeras, junk reads, random reads, adapter leftovers and glitches go in, and how accurate the base calls are.

The author built it to test software that consumes long reads. If you want to know how an assembler or aligner copes when 10% of reads are chimeric, you turn that one dial and watch what breaks. The README says plainly that it "does not try to be best at imitating real reads". The aim is control over read quality, not perfect realism.

For each read it samples a fragment length from a gamma distribution and picks a fragment from the reference, on either strand. It adds adapters, may chain extra fragments as chimeras, and inserts glitches (random sequence added or sequence skipped). Errors are then added using a trained model until the read reaches a target percent identity, and per-base quality scores come from a separate qscore model. Built-in models cover several Nanopore and PacBio chemistries, plus a random one, and you can supply your own.

The idea underneath is that sequencing errors are not uniform noise. They have structure, and a simulator with explicit failure modes lets you study how that structure affects downstream analysis. It is a way into how long-read sequencing goes wrong and why bioinformatics tools need to be robust to it.

## Install

```
brew install badread
# Needs a reference genome in FASTA format; no accounts required. Homebrew pulls in Python, NumPy and SciPy.
```

## Try this

```
badread --help
```
Shows the available subcommands and options, which is a quick way to see the failure-mode dials.

```
badread simulate --reference ref.fasta --quantity 50x | gzip > reads.fastq.gz
```
Runs the default simulation, meant to mimic mediocre ONT R10.4.1 reads, and writes compressed FASTQ.

```
badread simulate --reference ref.fasta --quantity 50x --glitches 1000,100,100 --junk_reads 5 --random_reads 5 --chimeras 10 --identity 80,90,6 --length 4000,2000 | gzip > reads.fastq.gz
```
Produces the README's "very bad reads" preset, with high rates of glitches, junk, random reads and chimeras.

## What's unique

Most simulators try to look like real data. Badread treats each way reads go wrong as an explicit setting you can raise or lower, and it expresses distribution parameters as mean and standard deviation instead of shape and scale.

## Caveats

Accuracy simulation is slow because it periodically realigns reads to hit the target identity, and the README says it runs on macOS and Linux, with WSL suggested on Windows.

## Links

- [GitHub repository](https://github.com/rrwick/Badread)
- [JOSS paper](https://doi.org/10.21105/joss.01316)
- [Zenodo archive](https://doi.org/10.5281/zenodo.2622997)
