---
name: skani
title: skani
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, dna, genomics, rust, science]
homepage: https://github.com/bluenote-1577/skani
scout_score: 6
status: draft
---

# skani

**TLDR;** Compares two DNA genomes and prints how similar they are and how much of each lines up, fast enough to search tens of thousands of genomes in seconds.

skani calculates average nucleotide identity (ANI) and aligned fraction (AF) between genomes, metagenome-assembled genomes (MAGs) and contigs. You hand it FASTA files and it prints a tab-separated table: the ANI, and how much of each genome the comparison actually covered. It works for sequences above roughly 80% ANI.

It has three main modes. `dist` compares genomes pairwise or all-vs-all. `search` looks up query genomes in a prebuilt sketch database. `triangle` takes a folder of genomes and writes a similarity matrix or an edge list. Sketches are built once with `skani sketch` and reused.

The idea underneath is a trade between exact alignment and cheap sketching. Pure k-mer sketching tools such as Mash are fast but, per the README, "may underestimate ANI for incomplete MAGs". skani uses approximate mapping with no base-level alignment, plus a k-mer sketch filter to skip hopeless pairs. The cited Nature Methods paper describes the method as sparse chaining. Reporting aligned fraction next to ANI tells you whether a high identity rests on the whole genome or only a small piece.

That makes it a way into microbial genomics: how species are drawn by sequence similarity, why incomplete assemblies complicate that, and how comparison scales to databases of tens of thousands of genomes.

## Install

```
brew install skani
# Needs your own FASTA genome files. Alternatives: conda install -c bioconda skani, or build from source with Rust.
```

## Try this

```
skani --help
```
Lists the subcommands (dist, sketch, search, triangle) and their options.

```
skani dist genome1.fa genome2.fa
```
Prints ANI and aligned fraction for the two genomes. Argument order does not change the ANI.

```
skani triangle genome_folder/* > skani_ani_matrix.txt
```
Compares every genome in the folder against every other and writes an all-vs-all ANI matrix.

## What's unique

It reports aligned fraction alongside ANI, so you can see how much of each genome the number is based on. The README claims it is about 40-50x faster than FastANI and close to Mash's speed on very diverse datasets.

## Caveats

With default parameters only results above roughly 82% ANI are reliably reported, and v0.4 changed the sketch format in a breaking way, so older sketches are not readable by v0.3.x and earlier.

## Links

- [GitHub repository (homepage)](https://github.com/bluenote-1577/skani)
- [Basic usage guide (wiki)](https://github.com/bluenote-1577/skani/wiki/skani-basic-usage-guide)
- [Nature Methods paper (Shaw and Yu, 2023)](https://doi.org/10.1038/s41592-023-02018-3)
- [Pre-sketched databases (wiki)](https://github.com/bluenote-1577/skani/wiki/Pre%E2%80%90sketched-databases)
