---
name: lastz
title: lastz
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, alignment, bioinformatics, dna, genomics, science]
homepage: https://lastz.github.io/lastz/
scout_score: 5
status: draft
---

# lastz

**TLDR;** A DNA pairwise aligner from Penn State's Miller Lab that lines up whole chromosomes, short reads, or a sequence against itself, and still takes BLASTZ's old command-line syntax.

LASTZ takes two sequence files, a target and a query, and writes out where they resemble each other. Input can be FASTA, Nib or 2Bit. Output goes to stdout in formats such as MAF, LAV, AXT, SAM, PAF, a BLASTN-style report, or a general tab-delimited layout where you pick the columns. It is written in C and was built by Bob Harris of the Miller Lab at Penn State as a backward-compatible successor to BLASTZ.

Under the hood it runs a staged pipeline. It indexes seed words from the target, finds short near-matches in the query, and extends them without gaps into high-scoring segment pairs. Those are chained into syntenic anchors, extended with gapped alignment, filtered by score or user criteria, and then re-searched at higher sensitivity in the gaps between them. The query's reverse complement is handled too. Most of the options (`--step`, `--seed`, `--notransition`, `--nogapped`, `--chain`) trade speed for sensitivity at one of these stages.

The idea underneath is comparative genomics. Aligning human chromosome 4 against chicken chromosome 4 shows which stretches of sequence survived hundreds of millions of years of divergence. The docs use exactly that example. A quick, low-sensitivity pass takes minutes, and the full default run takes hours, so you can feel the sensitivity-versus-time tradeoff directly.

The same tool also maps short reads onto a chromosome, using strict filters on coverage and identity, and aligns a sequence to itself to expose repeats and duplications. The docs include a worked example of each.

## Install

```
brew install lastz
# Installs the lastz and lastz_D executables. You need your own FASTA, Nib or 2Bit sequence files; no account or GPU is required.
```

## Try this

```
lastz --help
```
Lists every option; running lastz with no arguments prints the common-options help.

```
lastz hg18.chr4.fa galGal3.chr4.fa --notransition --step=20 --nogapped --format=maf > hg18_4_vs_galGal3_4.maf
```
Runs the docs' quick, low-sensitivity alignment of human chromosome 4 against chicken chromosome 4 and writes MAF. The docs report about 2.5 minutes and 400 MB of RAM on a 2 GHz machine.

```
lastz target --self --nomirror
```
Aligns a sequence against itself, computes only one copy of each mirror-image pair, and omits the trivial main-diagonal block.

## What's unique

It is a drop-in BLASTZ replacement with a very deep option set, including coverage and identity filters, dynamic target masking, and explicit control over the seeding, HSP and chaining stages. The same tool covers whole chromosomes, short reads and self-alignment.

## Caveats

Full-genome runs are slow (the docs give 4.5 hours for human vs chicken chromosome 4 at default settings), the author says the working branch may be less stable than tagged releases, and genomes over 2 Gb need a special build (lastz_32).

## Links

- [Homepage and documentation](https://lastz.github.io/lastz/)
- [Source repository](https://github.com/lastz/lastz)
- [Releases](https://github.com/lastz/lastz/releases)
- [KegAlign (GPU version)](https://github.com/galaxyproject/KegAlign)
