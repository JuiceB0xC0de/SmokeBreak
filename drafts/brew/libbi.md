---
name: libbi
title: LibBi
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [bayesian, days-off, gpu, math, science, simulation, statistics]
homepage: https://libbi.org/
scout_score: 6
status: draft
---

# LibBi

**TLDR;** A modelling language and compiler for Bayesian state-space models, built around particle filters that can run on multi-core CPUs, GPUs and clusters.

LibBi is a toolkit for state-space modelling and Bayesian inference. You describe a system that changes over time, with hidden state you cannot observe directly and noisy measurements you can. LibBi then estimates the hidden state and the model's parameters from the data.

Models are written in LibBi's own domain-specific language. A parser and compiler written in Perl turn that description into code built on a C++ template library. In the project's words, "LibBi consists of a C++ template library, as well as a parser and compiler, written in Perl, for its own modelling language."

The staple methods are sequential Monte Carlo, also called particle filtering, including particle MCMC and SMC^2. An extended Kalman filter and some parameter optimisation routines are also on offer. The homepage says it targets "multi-core CPUs, many-core GPUs (graphics processing units) and distributed-memory clusters".

The idea underneath is that particle filters keep many guesses about the hidden state alive at once and reweight them as data arrives. That makes them a natural fit for parallel hardware. It is a door into probabilistic inference, tracking and time-series modelling from the angle of generated, parallel code. An R interface, RBi, is mentioned in the project news.

## Install

```
brew install libbi
# Homebrew pulls in autoconf, automake, boost, gsl, netcdf and qrupdate. The README points to an INSTALL.md for build details; GPU or cluster use likely needs extra setup that the sources do not describe.
```

## Try this

```
libbi --help
```
Prints the usage text for the main libbi command, the place to start since the online getting-started page is missing.

```
bi --help
```
Shows the help for the bi executable, the second command the formula installs.

## What's unique

It pairs a small modelling language with a compiler that generates C++ template code, aimed at particle-filter methods on GPUs and clusters rather than a single CPU.

## Caveats

The project has been quiet since the 1.4.5 release in July 2019, and the getting-started and documentation pages returned 404 when checked, so learning it means digging through the repository.

## Links

- [LibBi homepage](https://libbi.org/)
- [LibBi GitHub repository (README)](https://github.com/libbi/LibBi)
