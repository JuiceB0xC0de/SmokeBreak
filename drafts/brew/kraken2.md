---
name: kraken2
title: Kraken 2
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, genomics, k-mer, metagenomics, needs-big-disk, science]
homepage: https://github.com/DerrickWood/kraken2
scout_score: 5
status: draft
---

# Kraken 2

**TLDR;** Kraken 2 labels DNA sequencing reads with the organisms they came from by matching k-mer minimizers against a reference database.

Kraken 2 is a taxonomic sequence classifier written in C++, with Perl and shell scripts around it and a newer Python wrapper called `k2`. It reads DNA sequences (or amino acids, with a protein database) in FASTA or FASTQ form, optionally compressed with gzip, bzip2 or xz. For each sequence it writes a taxonomic label, and it can also write a sample-level report counting reads per taxon.

The idea underneath is the k-mer. Every short stretch of a genome is a fingerprint of where it came from. Kraken 2 keeps only minimizers of those k-mers, in a compact probabilistic hash table that maps each minimizer to the lowest common ancestor of all the genomes containing it. A read is reduced to minimizers, each is looked up, and the tree of life settles the answer. The manual says this trades a small false-positive rate (under 1% of queries) for speed and lower memory, and confidence thresholds can compensate.

It exists because the first Kraken needed a lot of memory for its k-mer list. The README calls this "the second version of the Kraken taxonomic sequence classification system" and notes it is a rewrite that is not backwards compatible. The `k2` wrapper adds classification across several databases at once, merging results by lowest common ancestor, and downloads from NCBI over HTTP.

The tool is a door into metagenomics: working out what is living in a soil sample, a gut, or a water supply from a pile of sequenced fragments. The manual also covers building custom databases and shrinking them for small machines.

## Install

```
brew install kraken2
# Needs a reference database before it can classify anything. A standard build takes roughly 100 GB of disk, and about 29 GB of RAM to run (manual's figures), unless --memory-mapping is used.
```

## Try this

```
k2 classify --help
```
Lists classification options such as --db, --confidence, --report, --paired and --memory-mapping.

```
k2 build --help
```
Shows how to build a database, including --standard, --special with greengenes, rdp, silva or gtdb, --kmer-len, --minimizer-len and --max-db-size.

```
k2 classify --db archaea,viral,univec --output output.txt --threads 9 --report report.txt reads.fna
```
Classifies reads against three NCBI databases at once, writing per-read labels to output.txt and a per-taxon count report to report.txt.

## What's unique

Instead of storing every k-mer, it stores only minimizers and accepts a small false-positive rate for speed and lower memory. The manual describes ways to shrink a database further for low-memory machines.

## Caveats

The developers say macOS and other non-Linux systems are not explicitly supported, and on macOS the default GCC lacks OpenMP, which limits runs to a single thread. The standard database needs about 100 GB of disk and tens of GB of RAM.

## Links

- [GitHub repository (homepage)](https://github.com/DerrickWood/kraken2)
- [Operating Manual (docs/MANUAL.html)](https://github.com/DerrickWood/kraken2/blob/master/docs/MANUAL.html)
- [Kraken 2 paper (Genome Biology 2019)](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1891-0)
- [Project site (ccb.jhu.edu)](https://ccb.jhu.edu/software/kraken2/)
