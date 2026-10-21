---
name: dynare
title: Dynare
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, economics, math, octave, science, simulation]
homepage: https://www.dynare.org/
scout_score: 5
status: draft
---

# Dynare

**TLDR;** Free software where you write a macroeconomic model nearly as it appears on paper, and it solves, simulates and estimates it for you.

Dynare is a platform for building and running economic models, mainly DSGE (dynamic stochastic general equilibrium) and OLG (overlapping generations) models. These are the mathematical models economists use to ask how a whole economy moves over time when households, firms and shocks interact. The homepage lists solving and estimating a model, computing optimal policy, identification and sensitivity analysis, and perfect-foresight simulation among its tasks.

The pitch is the model language. In the project's words: "Write your model almost as you would on paper and Dynare will take care of the rest!" You describe variables, shocks and equations, and the tool handles the numerical work that would otherwise mean hand-coding solvers. The Homebrew package installs a `dynare-preprocessor` executable. That suggests a step that translates the model file before it runs in the host language, though the brief could not confirm this.

Dynare is not a standalone program. It "runs on top of MATLAB, GNU Octave, and Julia". The Homebrew formula pulls in Octave, so you can stay on the free route. It is free and open-source, mostly GPL v3 or later, in a field where many tools are commercial.

The door here is the idea of a model as an executable object: equations in, an economy's behaviour out. If you have wondered what central bank forecasting models actually look like, this is a way to get your hands on that kind of machinery.

## Install

```
brew install dynare
# Pulls in GNU Octave. Then open Octave and type:
addpath $HOMEBREW_PREFIX/opt/dynare/lib/dynare/matlab
```

## Try this

```
dynare-preprocessor --help
```
Prints the options of the preprocessor executable that the Homebrew package installs.

```
addpath $HOMEBREW_PREFIX/opt/dynare/lib/dynare/matlab
```
Run inside Octave, as Homebrew's caveat instructs, to make Dynare available to the session.

## What's unique

It aims to let a model file read close to the equations on paper, with solving, estimation, policy and sensitivity work in one free tool.

## Caveats

The field is specialised and the useful workflow happens inside Octave, MATLAB or Julia rather than as a standalone command, and the brief could not check the README or documentation.

## Links

- [Dynare homepage](https://www.dynare.org/)
