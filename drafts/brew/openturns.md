---
name: openturns
title: OpenTURNS
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, math, python, science, simulation, statistics, uncertainty]
homepage: https://github.com/openturns/openturns
scout_score: 5
status: draft
---

# OpenTURNS

**TLDR;** A C++ and Python library for uncertainty quantification: give it distributions and a model, get back sensitivities, reliability estimates and output distributions.

OpenTURNS is a scientific library for treating uncertainty. You describe inputs as probability distributions and random variables, wrap a model of your system, and the library returns statistical results: distributions of outputs, sensitivity measures, and reliability estimates. It has a C++ core and Python bindings. It installs no command-line executables, so you use it from Python.

The stated reason it exists is practical. In the project's words, "Targeted users are all engineers who want to introduce the probabilistic dimension in their so far deterministic studies." Many engineering calculations return one number from one set of inputs. Real inputs are never exact, so the question becomes how much the answer moves when they wobble, and how likely failure is.

That shift, from a single answer to a distribution of answers, is the door into a large field: uncertainty propagation, sensitivity analysis, and reliability analysis. The library is aimed at industrial use rather than statisticians. The README is short and does not list specific algorithms, so the documentation is where to find out what it covers.

The project is free software under LGPL-3.0-or-later. The README warns that backwards compatibility is not always kept, and that breaks are marked in the ChangeLog.

## Install

```
brew install openturns
# Python is required for the Python module. Other routes from the install page: pip3 install openturns, or conda install -y openturns (conda-forge via Miniforge, not Anaconda's default channel). No hardware or account needed. The Homebrew install was not checked in the brief.
```

## Try this

```
pip3 install openturns
```
Installs the Python binary package from PyPI, a quick way to get the Python module if you want to skip Homebrew.

```
nix-shell -p openturns
```
Opens a Nix shell that provides OpenTURNS without touching your main environment.

## What's unique

It covers a wide range of uncertainty and risk methods in one library, with a C++ core and Python bindings, aimed at engineers rather than statisticians.

## Caveats

The README is short and lists no features, and backwards compatibility is not always kept between versions, so check the docs for the version you install.

## Links

- [Project homepage (GitHub)](https://github.com/openturns/openturns)
- [Documentation (latest release)](http://openturns.github.io/openturns/latest/contents.html)
- [Installation guide](http://openturns.github.io/openturns/latest/install.html)
- [Project website](http://www.openturns.org)
