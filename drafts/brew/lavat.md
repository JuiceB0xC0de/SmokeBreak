---
name: lavat
title: lavat
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [generative, metaballs, quick, simulation, tui, visual]
homepage: https://github.com/AngelJumbo/lavat
scout_score: 6
status: draft
---

# lavat

**TLDR;** A terminal lava lamp: metaball blobs drift, merge and split on screen, and you reshape them with single keystrokes while it runs.

lavat is a small C program that draws a lava lamp in the terminal. A set of blobs moves around, and when they get close they fuse into one shape and then pull apart again. Flags set the colour, speed, ball count, ball radius, rim, and the characters used to draw them. Most of these can also be changed with single keys while it is running.

The README calls it a "little program that simulates a lava lamp in the terminal", and that is the whole pitch. It is a toy to leave running in a spare pane. The credits point to a JavaScript lava lamp tutorial as the inspiration, and the terminal drawing is done with Termbox2.

The idea underneath is metaballs. Each blob is not a hard circle but a field that fades with distance. Where fields overlap they add up, and anything above a threshold is drawn. That is why two blobs bulge toward each other and join instead of just overlapping. The README does not describe the internals, but the options imply this approach. The `-F` flag swaps the glyphs for your own character set, and multi-character sets give a faux-3D shading.

The `-G` mode adds a bit of physics: per the README, balls heat up at the bottom, rise, cool at the top, then fall. The gradient and gravity features were added after the original, with gravity landing in January 2026.

## Install

```
brew install lavat
# Needs a Unix-like system. Zoom your terminal out before running for finer resolution. The README's own route is: git clone https://github.com/AngelJumbo/lavat, then sudo make install (needs a C compiler and make).
```

## Try this

```
lavat -c green -k red
```
Runs the default lamp with named colours, green blobs and a red rim colour.

```
lavat -g -b 8 -r 10 -R 3 -G
```
Gradient colours with gravity and buoyancy: 8 balls of radius 10 with a rim of 3, rising and falling.

```
lavat -c blue -R2 -F @@:::::: -r10
```
Draws the blobs with custom characters, giving a shaded, almost 3D look.

## What's unique

You can reshape the lamp live from the keyboard, and the custom glyph option turns the blobs into shaded ASCII art. The gravity mode makes them behave like heated wax rather than drifting at random.

## Caveats

Unix-like systems only; wide or unicode characters can render badly with -F, and the -R rim will not show with the default colour unless you also set -k.

## Links

- [Homepage / repository](https://github.com/AngelJumbo/lavat)
- [Demo GIFs repo](https://github.com/AngelJumbo/demos/tree/main/lavat)
- [Termbox2 (library credit)](https://github.com/termbox/termbox2)
