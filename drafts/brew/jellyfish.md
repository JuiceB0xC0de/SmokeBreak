---
name: jellyfish
title: Jellyfish
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, dna, genomics, k-mers, science]
homepage: https://github.com/gmarcais/Jellyfish
scout_score: 6
status: draft
---

# Jellyfish

**TLDR;** Jellyfish counts every substring of length k in DNA sequence files, quickly and with little memory, a basic step in many genome analyses.

Jellyfish reads FASTA and multi-FASTA files of DNA and counts k-mers: all the substrings of length k that appear in the sequence. It writes the counts in a binary format. `jellyfish dump` turns that into readable text, and `jellyfish query` looks up the count for specific k-mers.

The README describes k-mer counting as a central step in many DNA sequence analyses. Jellyfish exists to make that step cheap. It claims to use "an order of magnitude less memory and an order of magnitude faster than other k-mer counting packages". Those are the authors' claims, backed by a 2011 paper in Bioinformatics.

The technique underneath is the interesting part. The README says it uses an efficient encoding of a hash table and the compare-and-swap CPU instruction to increase parallelism. In other words, many threads update one shared table without taking locks. The brief does not go into more detail than that, but the paper is linked below.

The larger idea is that a genome becomes a frequency table of short words. Counting those words is a way to look at sequence data without aligning it to anything. The brief does not cover the command-line options beyond dump and query, so the project's doc directory is the place to learn the counting step.

## Install

```
brew install jellyfish
```

## Try this

```
jellyfish --help
```
Lists the subcommands, including the dump and query commands for reading the binary count files.

## What's unique

It counts k-mers with a lock-free hash table built on compare-and-swap, which is how it keeps memory use and run time low. It is established, citable bioinformatics software with a peer-reviewed paper behind it.

## Caveats

The brief could not confirm recent activity, and it has no flag-level usage detail, so you will need the doc directory and your own FASTA data to do anything real.

## Links

- [Homepage / GitHub repository](https://github.com/gmarcais/Jellyfish)
- [Documentation (doc directory)](https://github.com/gmarcais/Jellyfish/tree/master/doc)
- [Citation paper (Bioinformatics 2011)](http://bioinformatics.oxfordjournals.org/cgi/content/abstract/27/6/764)
- [Release downloads](https://github.com/gmarcais/Jellyfish/releases)
