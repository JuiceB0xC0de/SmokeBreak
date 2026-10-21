---
name: fastga
title: FastGA
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, alignment, bioinformatics, genomics, science]
homepage: https://github.com/thegenemyers/FASTGA
scout_score: 6
status: draft
---

# FastGA

**TLDR;** A whole-genome aligner that compares two genome assemblies directly through their indexes and finds all local alignments, for example two 2 Gbp bat genomes in about five minutes on 8 cores.

FastGA, from Gene Myers and Chenxi Zhou, takes two genome assemblies as FASTA (plain or gzipped) or ONEcode sequence files and finds every local DNA alignment between them. The README targets alignments over 100bp at 70% or more similarity, between high-quality, nearly complete genomes. By default it streams PAF to stdout. It can also write PSL or its own compact binary `.1aln` format.

Under the hood, each FASTA becomes a genome database (`.1gdb` plus a hidden 2-bit sequence file) and a truncated suffix-array-like index (`.gix`). The tool compares the two indexes directly instead of querying one genome's index with the other's sequences. It finds 'adaptamer' seeds, an idea credited to Martin Frith, chains them within diagonal bands, and runs the wave-based local aligner from daligner on each chain.

The results are stored as trace points, so a `.1aln` file stays small. The README's example holds 635,000+ local alignments in 44.5 MB. You expand it to PAF or PSL only when you need to. The package ships a set of small tools around that: plotting, chaining, converting, and inspecting alignments, plus tools for annotation intervals and for managing the databases and indexes.

The door it opens is comparative genomics: how two genomes differ, where they share ancestry, and how repeats show up. Running FastGA on a single genome compares it against itself and skips self-matches, which is useful for repeat detection or for finding homologous regions between haplotypes.

## Install

```
brew install fastga
# Bioconda alternatives: conda install fastga, or pixi global install fastga
# You need two genome assemblies as FASTA and plenty of disk: GIX indexes take about 13-14 GB per gigabase.
```

## Try this

```
FastGA --help
```
Prints the usage summary and the options of the main aligner.

```
FastGA A B
```
Compares two genome assemblies and streams the alignments to stdout as PAF, using 8 threads by default.

```
FAtoGDB A.fa
```
Converts a FASTA into a genome database, A.1gdb, which the README recommends keeping in place of the FASTA.

## What's unique

It aligns by comparing two genome indexes directly and stores results as compact trace points that expand to PAF or PSL later. That keeps whole-genome results small.

## Caveats

Indexes are large, about 14 GB per gigabase. Results are asymmetric unless you use -S. It is built for near-complete, high-quality assemblies, and the authors say sensitivity on distant genomes and satellite repeats still needs work.

## Links

- [GitHub repository and README](https://github.com/thegenemyers/FASTGA)
- [Bioconda recipe page (install and versions)](https://bioconda.github.io/recipes/fastga/README.html)
- [ONEcode data encoding framework (underlying file format)](https://github.com/thegenemyers/ONEcode)
- [DALIGNER (the aligner whose wave-based local alignment FastGA builds on)](https://github.com/thegenemyers/DALIGNER)
