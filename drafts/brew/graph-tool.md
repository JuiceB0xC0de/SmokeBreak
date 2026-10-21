---
name: graph-tool
title: graph-tool
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, graphs, library, math, network-science, python, statistics]
homepage: https://graph-tool.skewed.de/
scout_score: 5
status: draft
---

# graph-tool

**TLDR;** A Python network analysis library with a C++ Boost core, known for fast graph algorithms and statistical community detection that tries to avoid overfitting.

graph-tool is a Python module for building, manipulating and statistically analysing graphs. You load or construct a network, then run centrality, structural, layout and community detection routines on it. It reads and writes formats such as GraphML, GML and dot, and has its own binary network format.

The Python API is a front end. In the project's words: "Contrary to most other Python modules with similar functionality, the core data structures and algorithms are implemented in C++, making extensive use of template metaprogramming, based heavily on the Boost Graph Library." Many algorithms are parallelised with OpenMP, which is why the formula pulls in libomp.

The idea underneath is inferential community detection. Instead of running a heuristic and hoping the groups it finds are real, you fit a statistical model of how the network was generated. The author argues this avoids the overfitting of off-the-shelf methods. That opens onto stochastic block models, Bayesian inference on networks, and reconstructing networks from dynamics.

Filtered graphs are a smaller, useful trick. You can temporarily mask vertices and edges, and every function accepts the filtered view. The homepage says this costs nothing when filtering is unused.

## Install

```
brew install graph-tool
# Drawing needs extra formulae:
brew install gtk+3 py3cairo pygobject3 python-matplotlib
# For zstd decompression, point Python at the bundled package:
export PYTHONPATH="$HOMEBREW_PREFIX/opt/graph-tool/libexec/lib/python3.15/site-packages"
# Needs Python 3. The formula installs a Python module, not a command-line tool.
```

## Try this

```
brew install graph-tool
```
Installs the Python module and its C++ dependencies. It has no executables, so you import it from Python afterwards.

```
docker pull tiagopeixoto/graph-tool
```
Pulls the published image if you would rather skip a local build. The homepage also offers a Colab notebook for a trial without installing.

## What's unique

It puts a Boost-based C++ core under a Python API and ships statistically principled inferential community detection. Filtered graph views work with every function.

## Caveats

It is a library with no command-line tool, graph drawing and zstd support need extra setup, and the brief could not confirm a recent release date.

## Links

- [graph-tool homepage](https://graph-tool.skewed.de/)
