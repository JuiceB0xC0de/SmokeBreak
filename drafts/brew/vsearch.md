---
name: vsearch
title: vsearch
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, microbiome, science, sequences]
homepage: https://github.com/torognes/vsearch
scout_score: 5
status: draft
---

# vsearch

**TLDR;** An open-source command-line tool that clusters, searches and de-chimeras DNA sequence files, a free alternative to USEARCH for microbiome amplicon work.

VSEARCH reads FASTA or FASTQ files, plain or gzip/bzip2 compressed, and does the bulk sequence work of amplicon-based microbiome studies. It can cluster sequences, dereplicate them, detect chimeras (de novo or against a reference), classify taxonomy with SINTAX, merge paired-end reads, filter and convert FASTQ, and search queries against a database. Results come out as alignment text, user-defined tables, BLAST-style tables, UC files, or OTU tables in biom, classic, or mothur formats.

It exists because of USEARCH, a tool by Robert C. Edgar from 2010. The README states the aim as creating an alternative that is open source, free of charge, 64-bit for very large databases, and as accurate and as fast as USEARCH. Most nucleotide commands and option names follow USEARCH version 7, so it works as a near drop-in replacement.

The name stands for 'vectorized search'. It uses SIMD vectorization and multiple threads for speed. Its aligner is a full dynamic-programming global aligner (Needleman-Wunsch), where USEARCH defaults to a heuristic seed-and-extend approach. The README says the full aligner usually gives more accurate alignments and better recall, especially around gaps.

The door it opens is how a microbiome survey is reduced to a handful of countable groups: millions of short reads get compared, merged into clusters, and stripped of chimeric artefacts. You can watch that happen on your own files, and the man pages describe each step.

## Install

```
brew install vsearch
# No account or hardware needed. You need your own FASTA/FASTQ files to do anything useful.
```

## Try this

```
vsearch --help
```
Lists the commands and options the binary supports.

```
man vsearch
```
Opens the hub manual page listing every command, if the man pages are on your MANPATH.

```
vsearch --usearch_global queries.fsa --db database.fsa --id 0.9 --alnout alnout.txt
```
The README's example: finds database sequences at least 90% identical to each query and writes the alignments to alnout.txt.

## What's unique

It is a freely licensed, USEARCH-style tool that runs a full Needleman-Wunsch global aligner instead of a heuristic one. The README says it runs on five Linux CPU architectures, plus macOS and Windows.

## Caveats

It is built for short sequences and the README warns it will be slow beyond about 5,000 bp; it has no amino acid or local alignment support, and not every USEARCH 8 feature.

## Links

- [Homepage / GitHub repository](https://github.com/torognes/vsearch)
- [Online documentation](https://torognes.github.io/vsearch/)
- [Latest release binaries](https://github.com/torognes/vsearch/releases/latest)
- [Citation paper: Rognes et al. 2016, PeerJ](https://doi.org/10.7717/peerj.2584)
