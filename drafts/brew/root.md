---
name: root
title: ROOT
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, cpp, data-analysis, physics, python, science, visual]
homepage: https://root.cern
scout_score: 6
status: draft
---

# ROOT

**TLDR;** CERN's C++ data analysis framework, built for the Large Hadron Collider, with an interactive C++ interpreter and Python bindings for histograms, fits and plots.

ROOT is a framework for storing, processing and analysing very large scientific datasets, from acquisition through to publication-ready plots. It reads event or measurement data, typically held in its own columnar file format, and produces histograms, fits, statistical models and plots. The Homebrew formula also installs a set of command-line tools, such as `root`, `hadd`, `rootls` and `rootcling`.

It was built for the Large Hadron Collider experiments. The homepage says more than 2 exabytes are stored in ROOT files, and that the Higgs discovery used it. The README frames it as a unified package that is reliable, performant and easy to obtain, aiming for the most scientific results per unit of human effort and computing cost.

The interesting part is how you drive it. Cling, a C++-compliant interpreter, lets you prototype in C++ with no compile step. Its type introspection also supports the Python bindings, which use cppyy for on-demand, two-way access between C++ and Python. You can work in either language on the same objects, or run analyses in batch mode.

RDataFrame, the parallel processing framework, can spread an analysis across multiple cores or distributed systems. In the project's words: "Exabytes of scientific data are written in columnar ROOT format." It is a way to see what a working particle-physics analysis toolchain looks like, on your own machine.

## Install

```
brew install root
# Optional since ROOT 6.22. For bash, to set the custom variables the thisroot scripts export:
. $HOMEBREW_PREFIX/bin/thisroot.sh
# No extra hardware or accounts needed. The formula pulls in many dependencies, including gcc and Python.
```

## Try this

```
root --help
```
Lists the command-line options for the main ROOT executable, which starts the interactive Cling session.

```
rootls --help
```
Shows how to list the contents of a ROOT file from the shell.

```
hadd --help
```
Shows how to merge multiple ROOT files into one.

## What's unique

It is real high-energy physics infrastructure, not a toy, and it pairs a C++ interpreter with Python bindings so you can prototype in either language on the same objects.

## Caveats

The install is large, with a long dependency list, and the README's SWAN live demo is only for CERN users.

## Links

- [ROOT homepage](https://root.cern)
- [Installation instructions](https://root.cern/install)
- [Getting started (Learn)](https://root.cern/learn)
- [GitHub repository](https://github.com/root-project/root)
