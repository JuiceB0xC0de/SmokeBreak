---
name: veryfasttree
title: VeryFastTree
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bioinformatics, parallel, phylogenetics, science, simd]
homepage: https://github.com/citiususc/veryfasttree
scout_score: 5
status: draft
---

# VeryFastTree

**TLDR;** A multithreaded, vectorized fork of FastTree-2 that builds phylogenetic trees from alignments with up to millions of sequences, using the same flags.

VeryFastTree reads a multiple sequence alignment (NEXUS, Fasta, Fastq or interleaved Phylip, optionally zlib- or bzip2-compressed) and writes a phylogenetic tree: a guess at how the sequences are related by descent. This is the basic data structure of evolutionary biology, and it gets expensive fast. Its author reports a one-million-taxa tree in 36 hours on a two-socket 32-core Xeon server.

It is a tuned fork of FastTree-2. The inference phases, methods and heuristics are left as they were. What changes is how the work runs: a tree-partitioning method lets subtrees be processed in parallel, and the likelihood arithmetic is vectorized with SSE3, AVX, AVX2 or AVX512 intrinsics. There is also an experimental CUDA path. The authors claim it is more than 3x faster than FastTree-2 with the same topological accuracy.

The idea underneath is that a good scientific heuristic can be kept and the engineering around it rebuilt. Command-line arguments match FastTree-2's, so an existing pipeline can swap the binary name. In its default mode it is also deterministic, which the README contrasts with the parallel version of FastTree-2. The project's own words: "VeryFastTree keeps exactly the same command line arguments than FastTree-2."

The extra options (-threads, -threads-level, -threads-mode, -ext, -fastexp, -disk-computing) control the parallel and memory strategies. If -threads is not given, the thread count comes from OMP_NUM_THREADS.

## Install

```
brew install veryfasttree
# Installs the VeryFastTree executable. Needs libomp (pulled in by brew). You also need a multiple sequence alignment file to do anything useful.
```

## Try this

```
VeryFastTree --help
```
Prints the usage and options, including the FastTree-2-compatible flags and the extra threading and memory options.

```
cmake -LH
```
Run from a source checkout, lists the build options (USE_NATIVE, USE_AVX2, USE_AVX512, USE_CUDA and others) with descriptions, a quick look at the vectorization choices.

## What's unique

It is a drop-in replacement for FastTree-2 with identical flags, and it is deterministic by default while still running in parallel.

## Caveats

The speed figures are the authors' own benchmark on one server, not independent measurements, and the project looks maintained but quiet, with v4.0 from July 2023 as the latest release the README mentions.

## Links

- [GitHub repository and README](https://github.com/citiususc/veryfasttree)
- [GigaScience 2024 paper (DOI)](https://doi.org/10.1093/gigascience/giae055)
- [Bioconda package](https://anaconda.org/bioconda/veryfasttree)
- [Python bindings on PyPI](https://pypi.org/project/veryfasttree/)
