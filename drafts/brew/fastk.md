---
name: fastk
title: FastK
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, c, dna, genomics, science]
homepage: https://github.com/thegenemyers/FASTK
scout_score: 5
status: draft
---

# FastK

**TLDR;** A k-mer counter by Gene Myers that turns DNA reads into frequency histograms, tables and per-read profiles, with set-logic tools for combining the results.

FastK reads DNA sequencing data (fastq, fasta, BAM, SAM, CRAM, gzipped files, or Dazzler databases) and counts every k-mer, meaning every substring of length k. The default k is 40. It always writes a histogram of how often each k-mer occurs. With options it also writes a sorted table of k-mers with counts, or a profile of counts along each read.

A k-mer and its reverse complement are treated as the same thing. FastK stores the lexicographically smaller of the two as the canonical form and counts by sorting. The README says profiles can be recorded during that sort, which it calls much more efficient than building a hash afterwards, as other counters do. It is aimed at high-quality assembly data such as Illumina reads or PacBio HiFi, and is designed to handle arbitrarily large inputs on modest memory.

The real draw is the companion toolkit. Histex shows histograms, Tabex lists table entries by prefix range, and Profex shows read profiles. Logex combines whole k-mer tables with set expressions, and Symmex makes tables symmetric so they can be streamed. Fastmerge and Fastcat splice partial runs together for cluster jobs. This makes it a way into how genome assemblers and quality tools reason about sequence without aligning anything: a k-mer spectrum alone says a lot about coverage, error and heterozygosity.

## Install

```
brew install fastk
```

## Try this

```
FastK -k40 -t part1.fasta
```
Counts 40-mers in the file, writing a histogram and a sorted k-mer table.

```
Logex 'AnB = A &. B' Tab1 Tab2
```
Writes AnB.ktab holding the k-mers common to both tables, keeping the left count.

```
Histex --help
```
Prints usage for viewing a .hist histogram, including the GeneScope variant.

## What's unique

Per-read profiles come out of the same sort that does the counting, and Logex lets you do set logic on whole k-mer tables in one command.

## Caveats

It does not work above 128GB of memory or for k beyond roughly 128, all inputs must be the same type, and Haplex, Homex and Vennex are deprecated; you also need real sequencing data to see anything interesting.

## Links

- [FastK repository (README)](https://github.com/thegenemyers/FASTK)
- [Dazzler DB (input format)](https://github.com/thegenemyers/DAZZ_DB)
- [merfin (relative profile use case)](https://github.com/arangrhie/merfin)
