---
name: mummer
title: MUMmer
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, alignment, bioinformatics, fasta, genomics, science]
homepage: https://github.com/mummer4/mummer
scout_score: 5
status: draft
---

# MUMmer

**TLDR;** A suite for aligning whole genomes using suffix trees: feed it two FASTA files, get back coordinates, SNPs, and a classification of rearrangements.

MUMmer finds exact maximal matches between a reference sequence and one or more query sequences, then builds alignments on top of them. The core program, mummer, does the matching with a suffix tree. The README says version 4 finds all 20 bp maximal exact matches between two bacterial genomes of about 5 Mbp each in 20 seconds, using 90 MB of memory.

Most people start with nucmer, which aligns nucleotide sequences all-vs-all and writes a .delta file. By default it keeps only matches that are unique in the reference. A family of show-* tools reads the delta file: show-coords prints alignment coordinates, show-snps lists point differences, show-aligns prints the alignments themselves, and show-diff labels the gaps between them as duplications, relocations, inversions, and translocations. delta-filter prunes the alignments with a longest-increasing-subset calculation, so you keep a consistent 1-to-1 set. dnadiff wraps the whole pipeline and produces a report.

The second idea is promer. It translates both inputs in all six reading frames and aligns the resulting amino acid sequences, so two genomes can still match at the protein level after the DNA has diverged too far for nucmer. The README also says it copes with draft assemblies of hundreds or thousands of contigs.

The tool is from the 2000s and the file formats show it, but the suffix-tree approach is an approachable way into how genome comparison works. You need two FASTA files to try it, and any two related bacterial genomes will do.

## Install

```
brew install mummer
# Runtime needs perl 5.6+, sh, sed and awk on the path. mummerplot needs gnuplot for plots.
```

## Try this

```
nucmer -h
```
Lists nucmer's options, including --mum and --maxmatch, which change which matches it keeps.

```
nucmer -p out ref.fa qry.fa
```
Aligns the query against the reference and writes out.delta.

```
dnadiff ref.fa qry.fa
```
Runs nucmer with defaults and the show-* helpers, then writes a .report summarizing the differences between the two genomes.

## What's unique

It combines a suffix-tree matcher, a delta format shared by a whole family of small show-* tools, and a built-in classifier for rearrangements. Its promer mode aligns six-frame translations, so it can match proteins where DNA has diverged too far.

## Caveats

Upstream supports only GCC, not Clang, and the docs in the repo are described as potentially out of date. Several utilities, such as annotate and nucmer2xfig, are obsolete or headed for removal.

## Links

- [Homepage (GitHub repo, README)](https://github.com/mummer4/mummer)
- [docs/ directory (nucmer, promer, dnadiff READMEs and manual)](https://github.com/mummer4/mummer/tree/master/docs)
- [INSTALL.md (build instructions, containers)](https://github.com/mummer4/mummer/blob/master/INSTALL.md)
