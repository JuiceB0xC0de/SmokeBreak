---
name: supermodel
title: Supermodel
source: brew
category: games
commitment: afternoon
tags: [afternoon, arcade, emulator, games, reverse-engineering, sega]
homepage: https://github.com/trzy/Supermodel
scout_score: 8
status: draft
---

# Supermodel

**TLDR;** An emulator for Sega's Model 3 arcade boards, rebuilt entirely from reverse engineering because Sega never published documentation for the hardware.

Supermodel emulates the Model 3, Sega's 3D arcade platform from 1996 to 1999. It uses OpenGL and SDL2 and runs on Windows, Linux, and macOS. The README says it lets you "relive state-of-the-art 3D arcade gaming as it existed from 1996 through 1999."

The interesting part is how it got built. No public documentation for the Model 3 exists, so, in the README's words, what is known "has been painstakingly reverse engineered from scratch." The original hardware had an on-board scene graph and geometry processor that could transform, light, and rasterize tens of thousands of polygons per frame at 57.524 fps. Reproducing that behaviour from the outside, with no spec to check against, is the project's whole story.

The stated aim is "to develop an emulator that is both accurate and playable." Those two goals pull against each other, and watching a project balance them is a good way into emulation, hardware preservation, and what it takes to learn a machine nobody documented. It also supports network play over low-latency connections, which is unusual for an arcade emulator.

The formula also installs a second executable, ppcd. The README does not mention it, so this entry does not describe it.

## Install

```
brew install supermodel
# The README does not say which game ROMs are needed or how to get them. You supply those yourself.
```

## Try this

```
supermodel --help
```
Prints the command-line options, a good first look at what the emulator can configure.

```
ppcd --help
```
Shows usage for the second executable the formula installs. The README does not cover it, so treat it as something to explore.

## What's unique

It is a preservation project built from reverse engineering alone, since Sega never documented the Model 3. Network play is also an unusual feature for an arcade emulator.

## Caveats

The README does not say which game ROMs you need or how to obtain them, and the project lost its web hosting and forum, so Discord is now the main place for questions.

## Links

- [Homepage and README (GitHub)](https://github.com/trzy/Supermodel)
- [Releases](https://github.com/trzy/Supermodel/releases)
- [Discord community](https://discord.gg/XDd7TMMUMz)
