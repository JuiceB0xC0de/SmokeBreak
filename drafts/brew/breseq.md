---
name: breseq
title: breseq
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, dna, evolution, genomics, science]
homepage: https://barricklab.org/breseq
scout_score: 6
status: draft
---

# breseq

**TLDR;** A pipeline that compares sequencing reads from an evolved microbe against its ancestor's genome and writes an annotated HTML report of every mutation it finds.

breseq takes a reference genome (GenBank, GFF3 or FASTA) and short-read FASTQ files, maps the reads with Bowtie2, and calls the differences. It reports single-base changes, small insertions and deletions, large deletions, and new junctions supported by reads that straddle two places in the genome. That last category catches things like a mobile element jumping to a new spot. Everything lands in an HTML report you open in a browser.

It was built for a specific job: finding mutations in laboratory-evolved microbes. The docs describe it as a tool "for finding mutations relative to a reference sequence in short-read DNA re-sequencing data for haploid microbial-sized genomes." Its worked examples use clones and populations from the long-term E. coli evolution experiment, so you can see how an evolved strain differs from its ancestor, one mutation at a time.

The idea underneath is resequencing. You do not assemble a genome from scratch. You already know roughly what the answer should look like, so you ask where the new reads disagree with it. Polymorphism mode (`-p`) extends this to mixed populations, where a mutation may be present in only some of the cells. A junction-only reference mode can locate where an engineered cassette landed in a genome. Contig mode (`-c`) maps reads to a de novo assembly.

## Install

```
brew install breseq
# Installs Bowtie2 and R as dependencies. Needs no account. The docs' recommended route is Conda via Bioconda. You also need FASTQ reads and a reference genome; the homepage tutorials supply example data.
```

## Try this

```
breseq --help
```
Prints the options and modes, including polymorphism (-p), contig (-c) and targeted (-t).

```
breseq -l 80 -r REL606.gbk SRR2584524.fastq.gz
```
Homepage example 1a: compares an evolved E. coli clone against the REL606 reference and writes an annotated HTML report.

```
breseq -j 8 -p -r REL606.gbk SRR6173952_1.fastq.gz SRR6173952_2.fastq.gz
```
Homepage example 3: runs a mixed population sample in polymorphism mode on 8 threads.

## What's unique

Unlike general-purpose variant callers, it is tuned for evolved microbes against a reference. It calls new junctions from mosaic reads, which covers mobile element insertions, and its docs walk through real evolution-experiment data.

## Caveats

It targets haploid microbial genomes, not large diploid ones. Results can vary slightly with the Bowtie2 version, and the tutorial data is large (the population sample is 1.4G).

## Links

- [Barrick Lab breseq homepage](https://barricklab.org/breseq)
- [Online breseq documentation (user manual)](https://breseq.barricklab.org/)
- [breseq GitHub repository](https://github.com/barricklab/breseq)
