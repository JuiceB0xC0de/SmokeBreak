---
name: primer3
title: primer3
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, biology, dna, pcr, science]
homepage: https://primer3.org/
scout_score: 6
status: draft
---

# primer3

**TLDR;** Primer3 reads a DNA sequence and prints ranked PCR primer pairs, using a plain text-in, text-out format and thermodynamic scoring.

PCR copies a stretch of DNA by starting from two short strands, called primers, that stick to either end of the target. Choosing those two strands is a real design problem. They need the right melting temperature and GC content, they must not stick to each other or fold back on themselves, and they should not amplify the wrong place. Primer3 is the program many labs use to make that choice.

The core binary, `primer3_core`, reads Boulder-IO text records. Each record holds a template sequence, optional target and exclusion regions, and `PRIMER_` settings such as size, melting temperature and product size range. It prints ranked candidate pairs in the same format, or a readable report with `--format_output`. The homepage says it can also design hybridization probes (internal oligos) and sequencing primers.

The interesting part is the scoring. The manual describes some criteria as hard constraints and others as terms in an objective function that defines the optimal pair. From version 2.3, oligo-oligo and hairpin checks use thermodynamic alignment by default. The other installed tools, such as `oligotm` and `ntthal`, look like the same thermodynamic pieces exposed on their own. That makes it a small window into how biology gets turned into numbers you can optimise.

The homepage says development is promoted by "a small group of enthusiastic scientists mainly in their free time."

## Install

```
brew install primer3
# No accounts or hardware needed. Thermodynamic checks need the primer3_config parameter files, either in ./primer3_config/ or /opt/primer3_config/, or pointed to with PRIMER_THERMODYNAMIC_PARAMETERS_PATH.
```

## Try this

```
primer3_core --help
```
Prints the program's usage and options, a first look at what it accepts.

```
primer3_core < example
```
Feeds a Boulder-IO record on stdin, as in the manual, and prints ranked primer pairs in the same format. You need the example file from the source repository.

```
primer3_core --format_output < example
```
Runs the same record but prints a readable report instead of raw Boulder-IO tags.

## What's unique

It is a plain text-in, text-out engine with no GUI or service behind it, and it has been cited in the literature since 2012. The web interfaces Primer3Web and Primer3Plus are separate front ends to the same kind of design logic.

## Caveats

The homepage was last updated in January 2022 and current activity could not be confirmed. Input uses the pre-XML Boulder-IO format, so scripting against it means learning that format.

## Links

- [Primer3 homepage](https://primer3.org/)
- [Source on GitHub (README)](https://github.com/primer3-org/primer3)
- [Primer3 manual](http://primer3.org/manual.html)
