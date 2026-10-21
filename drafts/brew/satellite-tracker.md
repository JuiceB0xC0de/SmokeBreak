---
name: satellite-tracker
title: satellite-tracker
source: brew
category: deeper-rabbit-holes
commitment: quick
tags: [astrodynamics, quick, rust, satellites, science, sgp4, tui]
homepage: https://github.com/ShenMian/tracker
scout_score: 6
status: draft
---

# satellite-tracker

**TLDR;** A terminal app that tracks satellites in real time on a scrolling world map, using live orbital data and the SGP4 model to predict where they go next.

The binary is called `tracker`. It pulls orbital element data (OMM, sourced automatically from CelesTrak) and runs each object through SGP4, the standard model for turning those numbers into a position at a given moment. The results are drawn on a world map that scrolls horizontally with no edge, with the night side of the Earth shaded from the subsolar point.

Besides the map, there is a polar sky view that converts positions into azimuth and elevation for an observer, and a timeline for pass times. A time-shift control moves the calculation into the past or future, so you can see where an object was or will be. You can also follow a single object.

The idea underneath is that a satellite's orbit is not a stored track. It is a handful of numbers (an element set) plus a propagation model, and the position falls out of the math at whatever time you ask. Element sets go stale as drag and manoeuvres change orbits, which is why the app keeps refreshing them. Watching the map and the sky view side by side is a good way to see how a ground track relates to what you would see looking up.

The README gives no separate rationale beyond describing it as a terminal-based real-time satellite tracking and orbit prediction application. Configuration and keymap are documented in separate files in the repository.

## Install

```
brew install satellite-tracker
# the executable is named `tracker`
# other routes: paru -S tracker (Arch AUR), scoop bucket add extra && scoop install tracker (Windows), cargo install --git https://github.com/ShenMian/tracker (needs a Rust toolchain)
# needs network access for the CelesTrak data updates
```

## Try this

```
tracker --help
```
Lists the command-line options for the binary.

```
tracker
```
Opens the terminal UI with the scrolling world map, day/night shading, and satellite positions fetched from CelesTrak.

## What's unique

It combines SGP4 propagation on live CelesTrak data, a sky view, time travel, and object following in one terminal UI, with day/night shading driven from the subsolar point.

## Caveats

Auto-updates need network access to CelesTrak, and the README names no Rust version or supported terminals; the Homebrew formula (satellite-tracker) and executable (tracker) have different names.

## Links

- [Project homepage (GitHub)](https://github.com/ShenMian/tracker)
- [Configuration docs](https://github.com/ShenMian/tracker/blob/main/docs/configuration.md)
- [Keymap docs](https://github.com/ShenMian/tracker/blob/main/docs/keymap.md)
