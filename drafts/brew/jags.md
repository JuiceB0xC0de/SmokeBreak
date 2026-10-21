---
name: jags
title: JAGS
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, bayesian, math, mcmc, simulation, statistics]
homepage: https://mcmc-jags.sourceforge.io
scout_score: 7
status: draft
---

# JAGS

**TLDR;** A command-line Gibbs sampler that runs Bayesian models written in the BUGS language, so you can do MCMC simulation at home.

JAGS, short for Just Another Gibbs Sampler, is a program for analysing Bayesian hierarchical models using Markov Chain Monte Carlo simulation. Its homepage describes it as "not wholly unlike BUGS". You describe a statistical model in the BUGS language, and JAGS runs the sampling engine on it. The `jags` executable is the command-line entry point.

The homepage lists three aims: a cross-platform engine for the BUGS language, extensibility so users can write their own functions, distributions and samplers, and a platform for experimenting with ideas in Bayesian modelling. So it is meant to be a workbench as well as a fixed tool.

The idea underneath is that you declare what you believe about the data and the unknowns, and the machine draws samples from the resulting posterior distribution instead of solving it in closed form. The BUGS-style model language is declarative: you write relationships between quantities, not an algorithm. That makes it a way into Bayesian statistics and MCMC.

The homepage has no usage examples, so the model syntax and output format are not covered here. The project documentation is the place to start.

## Install

```
brew install jags
```

## Try this

```
jags --help
```
Prints the command-line options of the JAGS engine, a starting point before you write a first model file.

## What's unique

It is a long-running open-source descendant of the BUGS tradition, and it is designed to be extended with your own samplers and distributions, not just run as a fixed engine.

## Caveats

The homepage offers no tutorial or examples, so expect to learn the BUGS model language from the documentation; the latest release found is 4.3.2 from March 2023.

## Links

- [JAGS homepage](https://mcmc-jags.sourceforge.io)
- [JAGS project files and source on SourceForge](https://sourceforge.net/projects/mcmc-jags)
