---
name: hmmer
title: HMMER
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, hmm, protein, science, sequence-search]
homepage: http://hmmer.org/
scout_score: 6
status: draft
---

# HMMER

**TLDR;** A toolkit for building statistical profiles of protein or DNA families and searching sequence databases for distant relatives that BLAST-style pairwise search can miss.

HMMER is a suite of about nineteen command-line programs for biosequence analysis built on profile hidden Markov models. You give `hmmbuild` a multiple sequence alignment and it produces a profile, a probabilistic model of what a protein family or DNA element looks like. `hmmsearch` then runs that profile against a sequence database. `hmmscan` does the reverse and checks one sequence against a library of profiles, such as Pfam.

If you have only a sequence and no profile, `phmmer` works like BLAST, and `jackhmmer` iterates, folding each round's hits back into a new profile. `nhmmer` and `nhmmscan` do the same job for DNA. The rest of the suite covers alignment, format conversion, and preparing databases.

The idea underneath is that a family of related sequences carries more information than any single member. A profile records which positions are conserved and which are free to vary, so it can spot a relative that has drifted too far for pairwise comparison to notice. The homepage says HMMER is "designed to detect remote homologs as sensitively as possible." Profile HMMs were once expensive to compute, but it claims that "as of HMMER3, HMMER is essentially as fast as BLAST."

Most of the fun depends on having data. You need your own alignments or a profile database such as Pfam, and the homepage presents Pfam as a common pairing but does not supply it.

## Install

```
brew install hmmer
```

## Try this

```
hmmbuild --help
```
Prints the options for building a profile HMM from a multiple sequence alignment.

```
hmmsearch --help
```
Shows how to search a sequence database with a profile.

```
phmmer --help
```
Shows the BLAST-like mode, which starts from a query sequence instead of a profile.

## What's unique

It brings profile HMM sensitivity to remote homologs at roughly BLAST speed, as a full toolkit for building, searching, scanning, and aligning rather than a single program.

## Caveats

The brief could not confirm exact command syntax or build details because the user guide PDF was unreadable, and you will need your own alignments or a profile database like Pfam to get real results.

## Links

- [HMMER homepage](http://hmmer.org/)
- [HMMER User's Guide (PDF)](http://eddylab.org/software/hmmer/Userguide.pdf)
