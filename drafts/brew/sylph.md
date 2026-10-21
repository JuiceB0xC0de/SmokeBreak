---
name: sylph
title: sylph
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, genomics, k-mers, metagenomics, science]
homepage: https://github.com/bluenote-1577/sylph
scout_score: 5
status: draft
---

# sylph

**TLDR;** Sylph tells you which microbial species are in a metagenomic sample by comparing k-mers against genome databases, in seconds rather than hours.

Sylph is a command-line tool for taxonomic profiling of metagenomic shotgun reads. You give it sequencing reads from a sample, such as gut, soil or water, and it reports which species are present and in what proportions. It checks them against reference databases like GTDB, which holds about 200k genomes. It handles short reads and nanopore or PacBio long reads.

The idea underneath is k-mer containment. Instead of classifying every read, or looking only at marker genes, sylph asks how much of a reference genome's k-mer content shows up in the reads. Its stated novelty is a statistical correction for low coverage, so organisms present in small amounts can still be estimated accurately. The README claims it can be more than 50x faster than other methods and produces fewer false positives than Kraken. Those are the authors' benchmark claims, not something checked here.

The same machinery answers a different question. In containment ANI querying, you take one reference genome and search it against your reads. Sylph returns an estimated average nucleotide identity for any matching strain, according to the README down to roughly 0.1x coverage. That is a question about strains, not just which species is present.

The docs also mention a newer database format, syl2db, pre-built databases for prokaryotes, viruses and eukaryotes, and custom databases built from your own assembled genomes.

## Install

```
brew install sylph
# You will need sequencing reads (FASTQ) and a reference database; see sylph-docs.github.io for where to get them.
```

## Try this

```
sylph --help
```
Lists the subcommands and options so you can see how profiling and querying are split up.

## What's unique

Sylph uses k-mer containment with a statistical correction for low coverage, rather than marker genes or exact k-mer classification. The same method gives strain-level ANI estimates for a single genome at very low coverage.

## Caveats

Real use needs sequencing data and a large reference database, the documentation lives on a separate site because the GitHub wiki is out of date, and the speed and accuracy claims are the authors' own.

## Links

- [Project homepage (GitHub)](https://github.com/bluenote-1577/sylph)
- [Documentation](https://sylph-docs.github.io/)
- [Oxford Nanopore benchmark cited in README](https://nanoporetech.com/resource-centre/genomic-and-epigenomic-insights-into-microbial-biology-with-nanopore-metagenomic-and-isolate-sequencing)
