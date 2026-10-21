---
name: flye
title: Flye
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, assembly, bioinformatics, genomics, graphs, science]
homepage: https://github.com/mikolmogorov/Flye
scout_score: 5
status: draft
---

# Flye

**TLDR;** Flye assembles whole genomes from noisy long sequencing reads using repeat graphs, and a bacterial genome runs on a laptop in a couple of CPU hours.

Flye is a de novo genome assembler for single-molecule reads from PacBio and Oxford Nanopore. You give it raw base-called reads in FASTA or FASTQ, optionally gzipped. It writes a directory containing `assembly.fasta` (the contigs), `assembly_graph.gfa` (the final repeat graph) and `assembly_info.txt` (per-contig length, coverage, circularity and repeat status). The README calls it "a complete pipeline: it takes raw PacBio / ONT reads as input and outputs polished contigs." There is also a `--meta` mode for metagenomes.

The idea underneath is the graph. Many assemblers use de Bruijn graphs, which need exact k-mer matches, and long reads are too error-prone for that. Flye instead builds a repeat graph from approximate matches, which the README says "can tolerate the higher noise of SMS reads." It chains overlapping reads into draft contigs and aligns reads back to them with minimap2. It then collapses repeats and resolves them using the read evidence and the structure of the graph. Each unbranching path becomes an output contig. A final stage realigns all reads and applies a maximum-likelihood correction to each alignment bubble.

The interesting part is looking at what comes out. The graph file shows where the assembler could not decide, and the info file shows which contigs are circular, such as a bacterial chromosome or a plasmid. The project comes from the Pevzner lab and has peer-reviewed papers behind it (Nature Biotechnology 2019, and Nature Methods 2020 for metaFlye).

## Install

```
brew install flye
# alternative: conda install flye (Bioconda)
# Linux and macOS only. No GPU, account or special hardware needed.
```

## Try this

```
wget https://zenodo.org/record/1172816/files/E.coli_PacBio_40x.fasta
```
Downloads a 40x PacBio read set from E. coli, a real sample dataset to assemble.

```
flye --pacbio-raw E.coli_PacBio_40x.fasta --out-dir out_pacbio --threads 4
```
Assembles the reads into out_pacbio, producing assembly.fasta, the repeat graph and assembly_info.txt.

```
flye --nano-raw Loman_E.coli_MAP006-1_2D_50x.fasta --out-dir out_nano --threads 4
```
Assembles the Oxford Nanopore E. coli sample (downloaded separately from the same Zenodo record) so you can compare the two technologies.

## What's unique

It builds a repeat graph from approximate matches instead of a de Bruijn graph, so it works on noisy raw reads without a separate error-correction step. Public sample datasets make a real genome assembly easy to reproduce.

## Caveats

Bacterial genomes are practical at home (the README benchmarks about 2 GB RAM and 2 CPU hours for E. coli), but human-scale runs need hundreds of GB of RAM, and diploid genomes come out as collapsed haploid assemblies.

## Links

- [Flye repository (homepage, README)](https://github.com/mikolmogorov/Flye)
- [Usage manual](https://github.com/mikolmogorov/Flye/blob/flye/docs/USAGE.md)
- [Installation instructions](https://github.com/mikolmogorov/Flye/blob/flye/docs/INSTALL.md)
- [Assembly of Long Error-Prone Reads Using Repeat Graphs, Nature Biotechnology 2019](https://doi.org/10.1038/s41587-019-0072-8)
