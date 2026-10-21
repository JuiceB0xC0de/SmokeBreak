---
name: miniprot
title: miniprot
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, alignment, bioinformatics, genomics, proteins, science]
homepage: https://lh3.github.io/miniprot/
scout_score: 7
status: draft
---

# miniprot

**TLDR;** Aligns a protein sequence to a whole genome, finding the introns and frameshifts in between, which is how new genomes get their genes marked.

miniprot takes a genome FASTA and a protein FASTA and finds where in the genome that protein is encoded. Genes in most animals and plants are chopped into exons separated by long introns, so a protein does not map to DNA as one continuous stretch. miniprot handles that by allowing splice gaps and frameshifts in the alignment. Output is protein-flavoured PAF by default, or GFF3 with `--gff`, where introns and frameshifts show up as CIGAR operators.

Its stated main use is annotating protein-coding genes in a newly sequenced species, using known proteins from other species. It sits in the same space as GeneWise and Exonerate, but maps against whole genomes and is much faster at the residue alignment step.

The design borrows from long-read DNA mapping. The genome is translated in six frames, short ORFs are dropped, amino acids are squashed into 13 classes, and open syncmers of 6 residues are indexed. Seed hits are chained minimap2-style, refined with a second chaining round, and then filled in with striped dynamic programming. Reading the README alongside the output is a good way to see how a gene gets located and spliced in a genome.

There is a bundled test: a human genome region and a mouse protein (DPP3). Running it shows a real cross-species gene alignment in seconds.

## Install

```
brew install miniprot
# Needs an x86_64 or ARM CPU (SSE2 or NEON). Reads gzipped FASTA via zlib.
# Or build from source: git clone https://github.com/lh3/miniprot && cd miniprot && make
```

## Try this

```
miniprot --help
```
Lists the options, including -I for intron size, -t for threads and --gff for output format.

```
./miniprot test/DPP3-hs.gen.fa.gz test/DPP3-mm.pep.fa.gz > aln.paf
```
Aligns a mouse protein to a human genomic region from the repo's test files and writes protein PAF.

```
./miniprot --gff test/DPP3-hs.gen.fa.gz test/DPP3-mm.pep.fa.gz > aln.gff
```
Runs the same alignment but writes GFF3, with the PAF lines embedded, so you can see exons and introns as gene features.

## What's unique

It searches a whole genome for a protein and reports introns and frameshifts directly, using a seed-and-chain approach borrowed from long-read DNA mappers rather than working exon by exon on a small region.

## Caveats

Only runs on x86_64 or ARM CPUs, indexing is slow and memory hungry (the README advises prebuilding the index), and it is not tuned for distant homologs.

## Links

- [Project homepage](https://lh3.github.io/miniprot/)
- [GitHub repository (README)](https://github.com/lh3/miniprot)
- [Manpage](https://lh3.github.io/miniprot/miniprot.html)
- [Paper (Bioinformatics 2023)](https://doi.org/10.1093/bioinformatics/btad014)
