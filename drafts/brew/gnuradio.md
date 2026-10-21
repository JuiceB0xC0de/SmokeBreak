---
name: gnuradio
title: GNU Radio
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, gui, needs-hardware, python, radio, sdr, signal-processing]
homepage: https://www.gnuradio.org/
scout_score: 5
status: draft
---

# GNU Radio

**TLDR;** A toolkit for building software radios by wiring signal-processing blocks into flowgraphs, drawn in a GUI or written in Python or C++.

GNU Radio is a free and open-source signal processing runtime and development toolkit. You build a signal chain out of blocks. Each block takes in sampled data, from SDR hardware or from a file, and passes processed data on to the next block, a sink, or a plot. You can assemble the chain in Python or C++, or draw it in GNU Radio Companion and run it from there.

The README says it was originally developed for software-defined radios and for simulating wireless communications. It lists uses in digital communications, radio astronomy, and nuclear and particle physics, across hobbyist, academic, and commercial settings.

The idea underneath is that a radio is a pipeline of mathematical operations on samples: filter, mix, demodulate, decode. Once you see it that way, the hardware is just a source of numbers, and a recorded file works as well as an antenna. That makes it a door into signal processing and radio without needing a bench of equipment.

The Homebrew package installs helper tools alongside the main application, including gnuradio-companion, grcc, gr_modtool, gr_plot, and several uhd_ utilities for Ettus radios.

## Install

```
brew install gnuradio
# Homebrew flags this formula as deprecated. On Debian or Ubuntu the README suggests: sudo apt install gnuradio
# Live radio work needs SDR hardware. Flowgraphs that use files or simulated signals do not.
```

## Try this

```
gnuradio-companion --qt
```
Opens GNU Radio Companion in its Qt interface, where you drag blocks onto a canvas and connect them into a flowgraph.

```
gnuradio-companion --help
```
Lists the options for the flowgraph editor.

```
gr_plot --help
```
Shows how to plot recorded sample data from a file.

## What's unique

It is a runtime and development toolkit, not just an application. The same blocks can be drawn visually or scripted in Python or C++.

## Caveats

The Homebrew formula is marked deprecated, and the README says GNU Radio 4.0 is developing in a separate repo, so the brew package may lag the 4.x line.

## Links

- [GNU Radio homepage](https://www.gnuradio.org/)
- [GNU Radio wiki](https://wiki.gnuradio.org/)
- [Doxygen API docs](https://www.gnuradio.org/doc/doxygen/)
