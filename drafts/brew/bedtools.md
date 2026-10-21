---
name: bedtools
title: bedtools
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, genomics, science, sets, unix-pipes]
homepage: https://github.com/arq5x/bedtools2
scout_score: 6
status: draft
---

# bedtools

**TLDR;** A suite of small Unix tools that treat stretches of a genome as sets, so you can intersect, merge and subtract them in a pipe.

bedtools does arithmetic on genomic intervals: a start and end position on a chromosome, such as a gene, a sequencing peak or a read alignment. Its tools take files in common formats (BAM, BED, GFF/GTF, VCF) and apply set operations to them: intersect, merge, subtract, complement, count, shuffle and compare.

Each tool does one fairly simple job. The docs say that "quite sophisticated analyses can be conducted by combining multiple bedtools operations on the UNIX command line." The README calls it "the swiss army knife for genome arithmetic" and says it was "First created through urgency and adrenaline" by Aaron Quinlan in Spring 2009.

The idea underneath is that many biological questions are set-theory questions. Which peaks do two experiments share? Which gene is nearest to each peak? How many alignments land on each exon? Once you see genomic features as intervals on a line, these become overlaps and distances, and the same few operations answer a lot of them.

There is also an algorithm story. If the input is pre-sorted by chromosome and start position, the sorted path scales much better than the unsorted path, which uses an R-tree. The docs publish a speed comparison against bedops' bedmap, with the commands, so you can check the claim yourself.

## Install

```
brew install bedtools
You need your own interval data (BED, BAM, GFF/GTF or VCF) to get anything interesting out of it. For CRAM input, set the CRAM_REFERENCE environment variable to the reference genome.
```

## Try this

```
bedtools --help
```
Lists the subcommands, so you can see the whole set-operation toolbox at once.

```
bedtools intersect -a exp1.bed -b exp2.bed -f 0.50 -r > both.bed
```
Keeps the peaks shared by two experiments, requiring 50% reciprocal overlap.

```
bedtools closest -a both.bed -b genes.bed -io > both.nearest.genes.txt
```
Finds the closest gene for each shared peak, ignoring overlapping intervals.

## What's unique

It is a set of small composable Unix tools rather than one large program, and the author publishes a reproducible sorted-input speed comparison against a similar tool.

## Caveats

Except for BAM, input must be tab-delimited with Unix line endings, and chromosome names must match across files (chr1 is not 1).

## Links

- [Homepage (GitHub)](https://github.com/arq5x/bedtools2)
- [Documentation (readthedocs)](http://bedtools.readthedocs.org)
- [Stable releases (GitHub)](https://github.com/arq5x/bedtools2/releases)
- [Cheat-sheet from Ilya Levantis (gist)](https://gist.github.com/ilevantis/6d6ecf8718a5803acff736c2dffc933e)
