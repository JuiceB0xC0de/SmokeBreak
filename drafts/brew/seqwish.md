---
name: seqwish
title: seqwish
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, genomics, graphs, pangenome, rust]
homepage: https://github.com/pangenome/seqwish
scout_score: 5
status: draft
---

# seqwish

**TLDR;** Turns a pile of pairwise sequence alignments into a variation graph, so many genomes collapse into one shared structure.

seqwish takes sequences (FASTA or FASTQ, plain or gzipped) and alignments between them in PAF format, then writes a variation graph as GFA1. The alignments are usually all-versus-all, made by an aligner such as wfmash or minimap2. Each alignment must carry a cg:z: CIGAR tag. The graph goes to the file given with -g, or to standard output if -g is left out.

The idea underneath is that a reference genome is a single line, while a graph can hold many genomes at once, with shared stretches merged and differences shown as branches. seqwish builds that graph from the alignments alone. Per the README, it concatenates the sequences into one coordinate space, then for each base collapses the transitive closure of aligned bases into a single graph base. Links between graph bases come from the rewritten input sequences. Runs of unbranching bases are then compressed into single nodes.

It is designed for very large inputs with many noisy sequences, with memory kept bounded through disk-backed sorts and succinct rank/select structures. The author describes the conversion as lossless, and the project's own line is "These sequences wish they were squished into a graph." It is both a command-line tool and a Rust library, and it is described in the paper "Unbiased pangenome graphs" (Bioinformatics, 2023).

## Install

```
brew install seqwish
# No account or special hardware needed. Input needs PAF alignments with cg:z: CIGAR tags from an aligner such as wfmash or minimap2, which are installed separately.
# Temp files go in the current directory by default; use -b to move them.
```

## Try this

```
seqwish --help
```
Lists the options, including the sequence, alignment, graph output, thread and match-length flags.

```
minimap2 x.fa x.fa -c -X > x.paf
```
Aligns a FASTA against itself, with -c so the PAF includes the CIGAR strings seqwish requires.

```
seqwish -s x.fa -p x.paf -g x.gfa
```
Builds a variation graph in GFA format from the sequences and their alignments.

## What's unique

It induces the graph directly from alignments, with bounded memory on large noisy inputs. The README claims the Rust version gives byte-for-byte identical output to the older C++ one.

## Caveats

It is a pipeline piece: you need an aligner to feed it, and downstream tools like vg, GCSA2 and GBWT for most analyses. Recency of development could not be confirmed from the README.

## Links

- [GitHub repository](https://github.com/pangenome/seqwish)
- [Paper: Unbiased pangenome graphs, Bioinformatics 2023](https://doi.org/10.1093/bioinformatics/btac743)
- [API documentation on docs.rs](https://docs.rs/seqwish)
- [Bioconda recipe](https://bioconda.github.io/recipes/seqwish/README.html)
