---
name: mmseqs2
title: MMseqs2
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, clustering, proteins, science, search]
homepage: https://mmseqs.com/
scout_score: 6
status: draft
---

# MMseqs2

**TLDR;** A fast search and clustering suite for protein and nucleotide sequences, built as a much quicker alternative to BLAST for huge datasets.

MMseqs2 takes FASTA or FASTQ files, or its own database format, and returns alignment hits, sequence clusters, or taxonomic labels. It runs on multiple cores, can spread across servers, and has a GPU search path. Prebuilt workflows download public reference databases such as UniProt/Swiss-Prot, UniRef, NR, NT and Pfam.

It exists because classic tools like BLAST and PSI-BLAST become too slow once a collection reaches millions or billions of sequences. The README's claim: "MMseqs2 can run 10000 times faster than BLAST. At 100 times its speed it achieves almost the same sensitivity." Those are the authors' numbers, not independently checked here.

The idea underneath is that sequence comparison is a scaling problem as much as a biology problem. Clustering a protein set means grouping sequences by similarity, which is a way of asking which proteins are relatives. `easy-cluster` uses a cascaded algorithm, while `easy-linclust` has runtime that scales linearly with input size and is recommended for very large data. Search modes include iterative profile searches, translated searches, and taxonomy assignment by lowest common ancestor of hits.

Memory is the main constraint: about 1 byte per residue for clustering, and per target residue for search. The software splits the target database into parts that fit in available RAM.

## Install

```
brew install mmseqs2
# Also available via conda (conda install -c conda-forge -c bioconda mmseqs2), Docker (ghcr.io/soedinglab/mmseqs2), or a static binary from mmseqs.com/latest. GPU search needs a supported NVIDIA GPU; it is optional.
```

## Try this

```
mmseqs easy-cluster examples/DB.fasta clusterRes tmp --min-seq-id 0.5 -c 0.8 --cov-mode 1
```
Clusters the sequences in a FASTA file at 50% minimum identity and 80% coverage, using the example data from the source repository.

```
mmseqs easy-search examples/QUERY.fasta examples/DB.fasta alnRes.m8 tmp
```
Searches query sequences against a FASTA target in one step and writes tab-separated hits to alnRes.m8.

```
mmseqs databases UniProtKB/Swiss-Prot swissprot tmp
```
Downloads and sets up the Swiss-Prot reference protein database so you can search against real annotated proteins.

## What's unique

It pairs BLAST-style sensitivity goals with linear-time clustering, a one-command downloader for public reference databases, and optional GPU and multi-server search, all in one binary.

## Caveats

The speed claims are the authors' own; large databases need a lot of RAM, and the example files come from the GitHub repository rather than the brew install.

## Links

- [Homepage](https://mmseqs.com/)
- [GitHub repository](https://github.com/soedinglab/MMseqs2)
- [Nature Biotechnology 2017 paper (MMseqs2 search)](https://doi.org/10.1038/nbt.3988)
