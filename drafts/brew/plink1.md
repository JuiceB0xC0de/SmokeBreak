---
name: plink1
title: PLINK 1.9
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, genetics, genomics, science, statistics]
homepage: https://www.cog-genomics.org/plink/1.9/
scout_score: 5
status: draft
---

# PLINK 1.9

**TLDR;** A single-binary genetics toolkit that filters, converts and tests genotype data for disease associations, the standard workhorse of genome-wide studies, now openly labelled legacy.

PLINK 1.9 is a command-line toolset for whole-genome association analysis. It reads genotype data in PLINK's own binary (.bed/.bim/.fam) and text (.ped/.map) formats, plus VCF/BCF, Oxford .gen/.bgen, 23andMe text and GCTA matrices. It writes new filesets, summary statistics such as allele frequencies, missingness, Hardy-Weinberg and linkage disequilibrium, and association results.

Everything runs through one `plink` executable driven by flags. A typical session is a pipeline: filter samples and variants, convert or merge filesets, compute statistics, run a test such as `--assoc`, `--linear` or `--logistic`, then post-process the report with something like `--clump`. The homepage index also covers identity-by-descent, runs of homozygosity, epistasis, and population structure via `--pca`.

The idea underneath is that genome-wide association is mostly careful bookkeeping on a huge table of people by variants, and the hard parts are efficiency and quality control. PLINK 1.9 is a comprehensive update of Shaun Purcell's original PLINK, written by Christopher Chang. The homepage describes it as "designed to perform a range of basic, large-scale analyses in a computationally efficient manner."

It is a door into statistical genetics: population stratification, LD pruning, and why a plain case/control test can mislead you.

## Install

```
brew install plink1
# No runtime or account needed. Linux 64-bit binaries may report 'Kernel too old' on very old kernels; see the caveats.
```

## Try this

```
plink --help
```
Prints the flag reference, a quick view of the data management, statistics and association options.

```
plink --make-bed
```
Writes a binary fileset from your input data; run it with an input fileset such as --file or --bfile to convert formats.

```
plink --assoc
```
Runs basic case/control or quantitative-trait association tests on a supplied fileset and writes a results report.

## What's unique

It is the long-standing standard file format and toolkit for genome-wide association work, and its homepage is unusually candid about what it dropped and what it does badly.

## Caveats

It is maintained but legacy: the homepage says "We recommend migrating away from PLINK 1" toward PLINK 2.0, several 1.07 flags are unsupported, and its phasing and imputation code is obsolete.

## Links

- [PLINK 1.9 homepage](https://www.cog-genomics.org/plink/1.9/)
- [PLINK 1.07 binary mirror and download page](https://zzz.nyspi.org/plink/download.shtml)
