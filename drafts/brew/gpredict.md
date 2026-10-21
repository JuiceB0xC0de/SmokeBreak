---
name: gpredict
title: gpredict
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, gui, orbits, satellites, science, simulation]
homepage: https://oz9aec.dk/gpredict/
scout_score: 6
status: draft
---

# gpredict

**TLDR;** A desktop app that tracks satellites in real time, draws their orbits on maps and radar plots, and predicts when they will pass over you.

Gpredict is a free, GPL-licensed satellite tracking and orbit prediction application. It follows a large number of satellites and shows their positions and other data in lists, tables, maps, and polar plots, the radar-style view of where something is in your sky. It can also predict future passes and give detailed information about each one.

The idea that sets it apart, according to its homepage, is the module. You group satellites into visualisation modules, and each module is configured on its own, so you control the look and feel of each. A single instance can also track satellites relative to several observer locations at once, so you can compare what is overhead at home with what is overhead somewhere else.

Underneath is a question worth chewing on: how do you know where a thing in orbit is, right now, from a spot on the ground? The homepage does not explain the prediction mechanism, so that part is yours to dig into. It is a good door into orbital mechanics, and into the amateur radio world where people listen for passes.

The project's own words: "Gpredict is a real-time satellite tracking and orbit prediction application." It installs hamlib as a dependency, which hints at radio-related use, but the homepage text does not say what that covers.

## Install

```
brew install gpredict
# GTK desktop app: needs a graphical session, no account or hardware required to start
```

## Try this

```
gpredict
```
Opens the GUI, where you can set up a module, pick an observer location, and watch satellites on the map and polar plot.

```
gpredict --help
```
Lists the command-line options the program accepts.

## What's unique

Satellites are grouped into independently configured modules, and one instance can track passes for several observer locations at once.

## Caveats

It is a GUI app, and the homepage I read gave no install steps, platform list, or release date, so how actively it is maintained is unconfirmed.

## Links

- [Gpredict homepage (OZ9AEC)](https://oz9aec.dk/gpredict/)
