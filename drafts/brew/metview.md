---
name: metview
title: Metview
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, meteorology, python, science, visual, weather]
homepage: https://metview.readthedocs.io/en/latest/
scout_score: 5
status: draft
---

# Metview

**TLDR;** ECMWF's own weather-forecaster workstation, with an icon-driven GUI and a Python API, installable with one brew command.

Metview is a meteorological workstation from ECMWF (the European Centre for Medium-Range Weather Forecasts), developed with INPE, Brazil's space research institute. Its homepage calls it "a complete working environment for both the operational and research meteorologist": one tool for getting weather data, processing it and drawing it.

There are two front ends on one core. The icon-based graphical interface is for interactive work. A Python interface is for batch jobs. The core binaries hold the GUI, most of the data processing code and a Macro programming language, and the Python bindings sit on top of them. Output is processed data and plots, saved as PNG, PDF or SVG, or shown inline in Jupyter notebooks.

The idea underneath is that forecast centres do not work with ad hoc scripts. They work with a shared environment that knows meteorological data formats and how to draw them. Data is reachable through MARS requests, ECMWF's archive query language. Metview opens a door into how professional weather forecasting is actually done, with the same tool the forecasters use.

## Install

```
brew install metview
# Homebrew on macOS is the documented route; Linux via brew is noted as untested.
# Python bindings are a separate install and need the binaries: pip install metview
# Conda alternative: conda install metview metview-python -c conda-forge
```

## Try this

```
metview
```
Starts the graphical workstation with its icon-based interface.

```
metview -slog
```
Starts Metview with logging output, useful if startup misbehaves.

```
python3 -m metview selfcheck
```
After installing the Python bindings, checks that they can find and start the Metview binaries.

## What's unique

One core serves both a GUI workstation and a Python API, built by the weather centre that produces the forecasts. ECMWF maintains the Homebrew and conda packages itself, and there is a no-GUI batch build for notebooks.

## Caveats

It is a large, niche application, and its Python bindings cannot run without the binaries. The docs did not say how big the install is, and real data access may involve MARS, which the brief did not confirm is open to everyone.

## Links

- [Metview documentation](https://metview.readthedocs.io/en/latest/)
- [Installation page](https://metview.readthedocs.io/en/latest/install.html)
- [metview-python on GitHub](https://github.com/ecmwf/metview-python)
