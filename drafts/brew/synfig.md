---
name: synfig
title: Synfig
source: brew
category: quick-weird-payoffs
commitment: afternoon
tags: [afternoon, animation, rendering, vector, visual]
homepage: https://www.synfig.org/
scout_score: 5
status: draft
---

# Synfig

**TLDR;** A free, open-source 2D animation system where you set key poses and the software calculates the frames between, with a command-line renderer installed by brew.

Synfig Studio is a 2D animation application built around vector and bitmap artwork. It offers vector tweening, more than 50 layer types, a bone system for cutout animation, and parameters that can be linked directly or through mathematical expressions. The Homebrew formula describes itself as a command-line renderer and installs two executables, `synfig` and `synfig-config`. The pages read for this entry do not document those commands, so what follows about them is limited to the brew description.

The project's stated aim is to remove frame-by-frame drawing. In its own words, it "eliminates the need to create animation frame-by-frame, allowing you to produce 2D animation of a higher quality with fewer people and resources." You set key positions and the inbetween frames are computed.

The idea underneath is that an animation is a described scene rather than a stack of images. Layers, parameters and expressions describe the scene, and a renderer evaluates it at each moment in time. That is why a headless renderer makes sense: the project file is the source and the frames are build output. The homepage showcases independent productions such as the Morevna Project as examples of what the system can make.

The formula pulls in a large set of dependencies, including ffmpeg, ImageMagick, cairo, pango and mlt, which fits a tool that composes layers, text and video output.

## Install

```
brew install synfig
# The brew formula installs the synfig and synfig-config executables. The GUI app is documented separately at https://synfig.readthedocs.io/en/latest/installation.html
```

## Try this

```
synfig --help
```
Prints the command-line options of the renderer, which is the quickest way to see what the tool accepts.

```
synfig-config --help
```
Shows what the companion config tool offers; its purpose is not documented in the sources read for this entry.

## What's unique

It is a serious open-source alternative for 2D animation that uses bones and expression-linked parameters to build puppets from bitmap or vector art, rather than redrawing every frame.

## Caveats

The brew description says command-line renderer, but the homepage and README only describe a GUI editor and document no CLI usage, so expect to explore with --help.

## Links

- [Synfig homepage](https://www.synfig.org/)
- [GitHub repository](https://github.com/synfig/synfig)
- [Installation docs](https://synfig.readthedocs.io/en/latest/installation.html)
- [Building from source docs](https://synfig-docs-dev.readthedocs.io/en/latest/building/Building%20Synfig.html)
