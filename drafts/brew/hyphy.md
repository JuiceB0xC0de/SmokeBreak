---
name: hyphy
title: HyPhy
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, biology, evolution, phylogenetics, science, statistics]
homepage: https://www.hyphy.org
scout_score: 6
status: draft
---

# HyPhy

**TLDR;** Fits evolutionary models to gene sequences and a tree, then tests where natural selection or recombination left marks. It is the engine behind datamonkey.org.

HyPhy (Hypothesis Testing using Phylogenies) takes a sequence alignment and a phylogenetic tree and fits a statistical model of how the sequences changed over time. Each analysis is a named method that asks a specific question. MEME looks for episodic positive selection at individual sites. FEL, SLAC and FUBAR look for pervasive selection. BUSTED and aBSREL test whole genes and individual branches. RELAX tests whether constraint has relaxed or intensified. GARD looks for recombination breakpoints.

The idea underneath is that a gene's history is written in its mutations, and that you can test hypotheses about that history rather than just eyeball it. If a codon changes more often than chance and neutral drift would predict, something may have been pushing it. HyPhy turns that into likelihood-based tests you can run on your own data.

Results are written as JSON. The companion HyPhy Vision site reads that JSON and draws interactive trees and per-site plots. HyPhy also has its own scripting language, HBL, and a shared library callable from Python and R. The project's own description is "an open-source software package for the analysis of genetic sequences using techniques in phylogenetics, molecular evolution, and machine learning."

The command line is the way in. `hyphy -i` walks you through choosing an analysis and its parameters. Once you know the questions, you can script the same runs with named flags.

## Install

```
brew install hyphy
# Conda alternative: conda install -c bioconda hyphy (you may need to add the bioconda channel first)
# Not available for Windows. You need your own alignment and tree files; the brief mentions no bundled sample data.
```

## Try this

```
hyphy -i
```
Starts the interactive helper, which walks you through picking an analysis and its parameters.

```
hyphy gard --help
```
Prints the options for the GARD recombination analysis, with defaults for type, code, model, rate classes and mode.

```
hyphy meme --alignment data.fas --tree tree.nwk
```
Runs MEME on your alignment and tree to look for episodic positive selection at individual sites.

## What's unique

It covers a wide family of selection and recombination tests in one tool, with machine-readable JSON output. You can also run the same analyses in a browser at v3.datamonkey.org, entirely client-side, with no install.

## Caveats

The 2.5 line is in maintenance mode, with active development moved to HyPhy 3; I could not confirm which line the Homebrew formula tracks. It needs your own sequence data and has no Windows support.

## Links

- [HyPhy homepage](https://www.hyphy.org)
- [GitHub repository (2.5 legacy README)](https://github.com/veg/hyphy)
- [Datamonkey web server](https://www.datamonkey.org)
- [HyPhy 3 repository (active development)](https://github.com/veg/hyphy-3)
