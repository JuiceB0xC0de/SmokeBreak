---
name: nest
title: NEST
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, neuroscience, python, science, simulation]
homepage: https://www.nest-simulator.org/
scout_score: 8
status: draft
---

# NEST

**TLDR;** A simulator for networks of spiking neurons, running since 1994 and scaling from a laptop to supercomputers, driven from Python.

NEST simulates spiking neural networks. It cares about the dynamics, size and structure of a whole network, not the physical shape of individual neurons. You describe the network in Python through PyNEST, or use the stand-alone nest application, and a C++ kernel runs the simulation. It ships with over 50 neuron models and over 10 synapse models, including Tsodyks-Markram short-term plasticity and several STDP variants.

The homepage says a NEST simulation "tries to follow the logic of an electrophysiological experiment that takes place inside a computer". You set up the instruments much as a lab would: neurons and synapses, plus devices that stimulate or record. Then you run it. You can inspect and change the state of each neuron and connection while the run is in progress, and devices write their data to memory or to file.

Connectivity is stored as an adjacency list, not a single weight matrix. Two neurons can therefore have several connections with different properties between them. That is a small design choice with large consequences for what you can model.

The idea underneath is that you can build a model of cortex-like activity, balanced random networks, or learning and plasticity, and watch what the network does. The project says it has existed since 1994 under the name SYNOD, so this is long-running research software, not a toy.

## Install

```
brew install nest
# PyNEST lives with the Homebrew Python: add $HOMEBREW_PREFIX/opt/python@3.15/bin to your PATH to use it.
# Alternative, per the README: brew install libomp (macOS only, for multithreading), then pip install nest-simulator
```

## Try this

```
pip install nest-simulator
```
Installs NEST from PyPI, the README's quick install, so you can import it from Python.

```
nest-config --help
```
Shows the options of the helper that reports how your NEST was built and configured.

```
nest-server --help
```
Shows the options for the NEST server executable that Homebrew installs.

## What's unique

Connectivity is an adjacency list, so the same pair of neurons can have several differently parameterised connections. It is also research software with a history back to 1994 that scales from a laptop to supercomputers.

## Caveats

It models network-level dynamics, not detailed single-neuron morphology, it is GPL v2 or later, and on macOS multithreading needs libomp.

## Links

- [Homepage](https://www.nest-simulator.org/)
- [Documentation](https://nest-simulator.org/documentation)
- [pip install guide](https://nest-simulator.org/documentation/installation/pip_install.html)
- [GitHub repository](https://github.com/nest/nest-simulator)
