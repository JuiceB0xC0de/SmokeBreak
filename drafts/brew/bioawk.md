---
name: bioawk
title: bioawk
source: brew
category: languages-and-oddities
commitment: quick
tags: [awk, bioinformatics, genomics, language, quick, text-processing]
homepage: https://github.com/lh3/bioawk
scout_score: 6
status: draft
---

# bioawk

**TLDR;** Brian Kernighan's awk taught to read FASTA, FASTQ, SAM, VCF, BED and GFF, so genome files can be queried by column name in one-liners.

Bioawk is a modified copy of the original BWK awk. Add `-c` and name a format, and it gives each field a name, so you write `$POS` or `$name` instead of counting columns. It also reads gzipped input directly and adds a few built-in functions, such as `revcomp` and `and`. The README says that when none of the new features are used, it should behave exactly like the original awk.

It exists because bioinformatics files are mostly line-oriented text, which is what awk was built for, but the column layouts are easy to forget. SAM has a flag field packed with bits, FASTQ spreads one record over four lines, and VCF has a header you have to skip. Bioawk puts that knowledge inside the language, so the one-liner stays a one-liner.

Under the hood, `-c` swaps awk's line reader for one that parses FASTA and FASTQ and reads gzip through zlib. Field names come from a built-in format (sam, vcf, bed, gff, fastx) or from the first line of the input with `-c hdr`. The idea behind it is that a classic tool can be extended for a domain by changing how it reads records, while the language stays the same. If you know awk, you already know most of it.

## Install

```
brew install bioawk
```

## Try this

```
bioawk -c help
```
Lists the supported formats and the variable names each one gives you.

```
bioawk -c fastx '{print ">"$name;print revcomp($seq)}' seq.fa.gz
```
Reverse-complements every sequence in a gzipped FASTA file, using the name and seq fields.

```
bioawk -c sam 'and($flag,4)' aln.sam.gz
```
Pulls the unmapped reads out of a gzipped SAM file by testing a bit in the flag field.

## What's unique

It remains a drop-in awk apart from the opt-in `-c` mode, and it can take column names from a header line. Built-ins like `revcomp` replace small scripts for sequence work.

## Caveats

The last release, v1.0, dates from 2013. The README warns the replacement line reader may fail in corner cases, and gzip input only works with `-c`. You also need your own FASTA, SAM or VCF files to try it on.

## Links

- [Bioawk on GitHub (homepage and README)](https://github.com/lh3/bioawk)
- [Releases page](https://github.com/lh3/bioawk/releases)
- [Original BWK awk source mirror cited by the README](http://www.cs.princeton.edu/~bwk/btl.mirror/)
