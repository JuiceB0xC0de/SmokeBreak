---
name: projectm
title: projectM
source: brew
category: quick-weird-payoffs
commitment: afternoon
tags: [afternoon, audio, generative, milkdrop, opengl, presets, visual]
homepage: https://github.com/projectM-visualizer/projectm
scout_score: 6
status: draft
---

# projectM

**TLDR;** An open-source reimplementation of Winamp's Milkdrop visualizer that turns live audio into evolving OpenGL imagery driven by community-made preset files.

projectM is a library, libprojectM, that takes in raw audio samples and renders visuals with OpenGL. It runs beat detection and an FFT over the audio, then feeds those features into a preset. Each preset is a Milkdrop-style file made of pixel shaders plus equations and parameters, so a whole visualization is a small piece of math that reacts to sound.

It exists as a modern, cross-platform, reusable take on Milkdrop, the Winamp visualizer written by Geiss. The README puts the goal this way: "Experience psychedelic and mesmerizing visuals by transforming music into equations that render into a limitless array of user-contributed visualizations."

The interesting design choice is the split. The repository holds only the rendering library. Frontends, plug-ins and tools live in separate repositories, and the Milkdrop preset format is the shared language between them. The README names projectMSDL as the canonical frontend, and it uses SDL2 to capture audio input. The library ships with no presets at all. Community packs fill that gap, ranging from about 4K and 10K presets up to a 130K+ MegaPack that weighs 4.08GB zipped.

That makes it a door into generative graphics. Presets are readable equations and shaders, so you can open one, change a number, and watch what the music does to it.

## Install

```
brew install projectm
# Presets are not included. Download a pack separately, e.g. the Cream of the Crop pack (about 10K presets) from the projectM GitHub organisation, plus the base Milkdrop texture pack.
# Needs an audio source for the visuals to react to.
```

## Try this

```
projectMSDL --help
```
Lists the options of the SDL frontend, which is the way to see visuals from this install.

## What's unique

It keeps the Milkdrop preset format alive outside Winamp, so decades of community-made visualizations still run, on a library other programs can embed.

## Caveats

The Homebrew formula is the old 3.1.12 release, the README calls the frontends development previews that are not feature-complete, and no presets come with it.

## Links

- [projectM GitHub homepage](https://github.com/projectM-visualizer/projectm)
- [projectMSDL frontend releases](https://github.com/projectM-visualizer/frontend-sdl-cpp/releases)
- [Cream of the Crop preset pack (about 10K presets)](https://github.com/projectM-visualizer/presets-cream-of-the-crop)
- [Demo video playlist (4k render)](https://www.youtube.com/watch?v=jJmLQGhYWys&list=PLFLkbObX4o6TK1jGL6pm1wMwvq2FXnpYJ)
