---
name: fastani
title: FastANI
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, genomics, minhash, science]
homepage: https://github.com/ParBLiSS/FastANI
scout_score: 5
status: draft
---

# FastANI

**TLDR;** Estimates how similar two bacterial genomes are in seconds, using MinHash mapping instead of alignment, and shows where species boundaries fall.

FastANI takes whole-genome assemblies in FASTA format (gzip is fine) and reports their Average Nucleotide Identity. You can compare one genome to one, one to a list, or a list to a list. Each result is a tab-delimited row: query, reference, ANI value, the number of bidirectional fragment mappings, and the total number of query fragments. An optional `--matrix` flag also writes a PHYLIP-style lower-triangular matrix.

ANI is a standard yardstick for asking whether two microbes belong to the same species. The classic method, following Goris et al. 2007, aligns fragments of one genome against another with BLAST, which is slow when you have thousands of genomes. FastANI follows the same workflow but swaps the alignment step for Mashmap, a MinHash-based mapping engine. It finds orthologous mappings, estimates identity from them, and averages over the fragments that map in both directions. The README reports accuracy on par with the BLAST-based solver and a two to three orders of magnitude speedup.

The underlying idea is that sketching, which means keeping a small hashed summary of a sequence, can stand in for exhaustive comparison. That is why a paper could run this over 90,000 prokaryotic genomes and look for clear species boundaries. The README's bundled example compares a Shigella flexneri genome to E. coli K-12 and reports an ANI of 97.7507, with 1303 of 1608 fragments mapped.

## Install

```
brew install fastani
# Input: genome assemblies in FASTA format. The optional --visualize step needs R with the genoPlotR package.
```

## Try this

```
fastANI -h
```
Prints the help page with usage and all command-line options, including thread count.

```
fastANI -q data/Shigella_flexneri_2a_01.fna -r data/Escherichia_coli_str_K12_MG1655.fna -o fastani.out
```
Compares the two bundled test genomes from the repo and writes one result row. The README's sample output is an ANI of 97.7507 with 1303 of 1608 fragments mapped.

```
fastANI --ql [QUERY_LIST] --rl [REFERENCE_LIST] -o [OUTPUT_FILE]
```
Runs many-to-many comparison, where each list file holds one genome path per line.

## What's unique

It swaps BLAST-style alignment for a Mashmap MinHash mapping step and claims comparable accuracy at far higher speed. It also documents its own asymmetry: A-to-B and B-to-A can differ slightly, and `--matrix` averages the two.

## Caveats

Pairs with ANI much below 80% produce no output (the README suggests amino-acid comparison instead), and the README asks for inputs with an N50 of at least 10 Kbp.

## Links

- [GitHub repository (homepage)](https://github.com/ParBLiSS/FastANI)
- [Latest releases (binaries)](https://github.com/ParBLiSS/FastANI/releases)
- [Paper: High Throughput ANI Analysis of 90K Prokaryotic Genomes Reveals Clear Species Boundaries](https://doi.org/10.1038/s41467-018-07641-9)
