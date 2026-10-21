---
name: cuttlefish
title: cuttlefish
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, genomics, graphs, rust, science]
homepage: https://combine-lab.github.io/cuttlefish/
scout_score: 5
status: draft
---

# cuttlefish

**TLDR;** Builds compacted de Bruijn graphs from genome FASTA or sequencing reads, using disk-backed memory so it scales to collections of 150,000 bacterial genomes.

Cuttlefish takes DNA sequences, either reference FASTA files or sequencing reads in FASTQ (gzipped is fine), and builds a compacted de Bruijn graph. Chop every sequence into overlapping substrings of length k, treat each as an edge, and merge every unbranching path into one node. Each node is a maximal unitig, a stretch of sequence with no ambiguity about what comes next. The output is those unitigs as a FASTA file.

It can also build a colored graph over a collection of genomes. Each input file is a color, and the output records which sources cover which stretch of each unitig. That turns a pile of genomes into one shared structure where common sequence is stored once and differences show up as branches.

The design point is memory. Partition buckets, blocked edge matrices and collation buckets live on disk, so peak RAM tracks the number of worker threads rather than the size of the graph. The README claims it has built the colored graph of 150,000 bacterial genomes on a single machine. You choose the thread budget with `-t` and the scratch directory with `-w`.

The de Bruijn graph is the idea underneath, and it is a door into genome assembly, read indexing and pangenomics. Many tools in those fields start from a graph like this one. This is the third generation of the project. Versions 1 and 2 were C++ and are kept on separate branches with their own papers.

## Install

```
brew install cuttlefish
# alternatives: conda install -c bioconda cuttlefish, or cargo install cuttlefish-rs-cli (needs Rust 1.91+)
```

## Try this

```
cuttlefish --help
```
Lists the subcommands, including build and the commands for comparing graphs, querying colors, cleaning up and probing.

```
cuttlefish build --ref --seq genome.fa -k 31 -t 16 -w work/ -o graph
```
Builds an uncolored compacted graph from one reference FASTA with k=31 on 16 threads, keeping intermediate files in work/ and writing output under the prefix graph.

```
cuttlefish build --ref --list genomes.list -k 31 -t 32 -w work/ -o graph --color
```
Builds a colored graph over a collection, where each path listed in genomes.list is one source color.

## What's unique

Its external-memory design ties RAM use to worker count instead of graph size, and it builds colored graphs over very large genome collections on one machine.

## Caveats

Aimed at bioinformaticians, and the docs assume you already know de Bruijn graphs and unitigs; you also need your own FASTA or FASTQ data to run it.

## Links

- [Cuttlefish documentation site](https://combine-lab.github.io/cuttlefish/)
- [GitHub repository](https://github.com/COMBINE-lab/cuttlefish)
- [RECOMB 2026 paper preprint (DOI)](https://doi.org/10.1101/2025.02.02.636161)
