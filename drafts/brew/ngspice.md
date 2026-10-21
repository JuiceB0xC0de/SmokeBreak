---
name: ngspice
title: ngspice
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, circuits, electronics, simulation, spice]
homepage: https://ngspice.sourceforge.io/
scout_score: 7
status: draft
---

# ngspice

**TLDR;** An open source SPICE simulator: describe an analog or digital circuit as a text netlist, run it, and plot the voltages and currents.

ngspice simulates electronic circuits from a written description. You list the parts (resistors, capacitors, inductors, diodes, transistors, transmission lines, logic gates) and how they connect, and it solves the circuit and gives back graphs of voltages, currents and other quantities, or a data file. It handles analog, digital, and mixed analog/digital circuits.

The input is a netlist, either a text file or typed at the command line. In the project's words, "ngspice does not provide schematic entry. Its input is command line or file based." Third-party front ends exist if you want to draw circuits instead. Under the hood it reads the netlist, preprocesses it (subcircuits, parameters, compatibility handling), builds the circuit structure, sets up the matrix and solves it.

The idea underneath is SPICE itself: a circuit is a set of equations, and a program can solve them to show what a real board would do before you solder anything. Device models describe how real parts behave, and ngspice can read model parameters and netlists from PSPICE and LTSPICE, and HSPICE libraries from semiconductor foundry PDKs. That means circuits written for commercial tools can often run here too.

It is a long-running project. The homepage cites FOSDEM talks through 2025 and a current user manual (version 47), so it appears to be actively maintained.

## Install

```
brew install ngspice
# For graphical plotting on macOS, also install X11:
brew install --cask xquartz
```

## Try this

```
ngspice --help
```
Prints the command-line options, a starting point for running netlist files in batch or interactive mode.

## What's unique

It accepts PSPICE, LTSPICE and HSPICE model files, including foundry PDK libraries, and has built-in event-driven digital and mixed-signal simulation, which is less common in free SPICE tools.

## Caveats

There is no schematic entry, so you write netlists by hand or use a third-party front end, and plotting needs X11 (XQuartz on macOS); the manual is also described as a work in progress.

## Links

- [ngspice homepage](https://ngspice.sourceforge.io/)
- [ngspice documentation page (manual, internals)](https://ngspice.sourceforge.io/docs.html)
