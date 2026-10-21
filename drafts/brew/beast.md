---
name: beast
title: BEAST
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [bayesian, biology, days-off, java, mcmc, phylogenetics, science]
homepage: https://beast.community/
scout_score: 6
status: draft
---

# BEAST

**TLDR;** A Bayesian sampler that infers time-measured evolutionary trees from DNA or RNA sequences, used for real research in viral spread and phylogenetics.

BEAST (Bayesian Evolutionary Analysis Sampling Trees) is a Java program that takes molecular sequences, with optional sampling dates and trait data, and produces posterior samples of rooted, time-measured phylogenies and their parameters. It uses MCMC, a random walk through the space of possible trees and model settings.

The idea underneath is that a single best tree is the wrong thing to ask for. The homepage describes BEAST as a framework for testing evolutionary hypotheses without conditioning on one tree topology. In its words: "BEAST uses MCMC to average over tree space, so that each tree is weighted proportional to its posterior probability." Uncertainty stays in the answer instead of being hidden.

The workflow is a pipeline. BEAUti, a graphical tool, writes the model setup as an XML file. The beast program runs the sampler on that file. Then loganalyser, logcombiner, treeannotator and treestat help you summarise the logs and trees. BEAST also uses the separate BEAGLE library to speed up its likelihood calculations.

It is entirely oriented towards rooted trees under strict or relaxed molecular clock models. Around it sits an ecosystem of tutorials covering phylodynamics, phylogeography and model selection, plus companion programs such as Tracer, TempEst and FigTree. It is a way into Bayesian inference as practised in real science.

## Install

```
brew install beast
Requires Java (the formula pulls in openjdk@25) and the BEAGLE library, both installed as dependencies. You will need sequence data in order to do anything useful; the site's tutorials are the place to find examples.
```

## Try this

```
beast --help
```
Lists the command-line options for running the sampler on an XML file.

```
beauti
```
Opens the graphical tool where you import sequences and set up a model, then save it as the XML file that beast runs.

```
treeannotator --help
```
Shows the options for summarising the sampled trees into a single annotated tree.

## What's unique

It is the reference tool for time-calibrated Bayesian phylogenetics, with a full set of companion programs and tutorials. It is a separate project from BEAST2.

## Caveats

The installing page calls the latest build a beta, suitable for general use but possibly still buggy, and it only handles rooted, time-measured trees under clock models.

## Links

- [Homepage and documentation](https://beast.community/)
- [Installing BEAST](https://beast.community/installing)
- [Releases on GitHub (beast-dev/beast-mcmc)](https://github.com/beast-dev/beast-mcmc/releases/)
