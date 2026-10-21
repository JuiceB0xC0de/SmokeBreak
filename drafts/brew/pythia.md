---
name: pythia
title: PYTHIA
source: brew
category: deeper-rabbit-holes
commitment: days-off
tags: [c++, days-off, monte-carlo, physics, science, simulation]
homepage: https://pythia.org
scout_score: 6
status: draft
---

# PYTHIA

**TLDR;** A research-grade Monte Carlo generator that simulates high-energy particle collisions, the same kind of tool collider physicists use, and you can build it at home.

PYTHIA generates simulated collision events for electrons, protons, photons and heavy nuclei. It bundles the physics models needed to go from a hard collision to the particles that come out: hard and soft interactions, parton distributions, initial- and final-state parton showers, multiparton interactions, fragmentation and decay.

The homepage describes it as "largely based on original research, but also borrows many formulae and other knowledge from the literature." It is categorized as "a general-purpose Monte Carlo event generator." In plain terms, it plays out a collision many times with random sampling, so you can see what a detector might record. The homepage describes the models it contains rather than how events are sampled internally, so the manual is where that story lives.

The upstream distribution is a source tarball (currently 8.318) that you unpack and build with make. It ships with example programs in an examples directory, which you build one at a time and run. The only executable the brew formula lists is pythia8-config, a helper for building your own programs against the library. The real work happens in the C++ library and the examples.

The door here is Monte Carlo simulation as a way of doing physics. Quarks and gluons are never seen directly, so theory is tested by generating fake events and comparing them to real data. PYTHIA is also used for validation through MCplots and Rivet, and a worksheet for summer schools and self-study is available.

## Install

```
brew install pythia
# Upstream route: download pythia8318.tgz from pythia.org, then tar xvfz pythia8318.tgz, cd pythia8318, read the README, and run make. Requires a C++ toolchain. I did not verify what the brew formula puts on disk beyond pythia8-config.
```

## Try this

```
pythia8-config --help
```
Shows the options of the config helper used to get compile and link flags for programs built against PYTHIA.

```
make mainNNN
```
From the examples directory of the source tree, builds one example program; NNN is the three-digit example number.

```
./mainNNN > mainNNN.log
```
Runs the built example and writes its output to a log file you can read.

## What's unique

It is a real collider event generator with a peer-reviewed manual, used in actual physics research, that one person can build and run on a laptop. It also comes with a worksheet for learning.

## Caveats

The manual is the main reference rather than a quick-start and assumes a physics background; the homepage gives instructions only for Linux and Mac, and I did not verify how the brew formula lays out the examples.

## Links

- [PYTHIA homepage](https://pythia.org)
- [PYTHIA 8.3 manual (arXiv:2203.11601)](https://arxiv.org/abs/2203.11601)
- [PYTHIA releases on GitLab](https://gitlab.com/Pythia8/releases)
