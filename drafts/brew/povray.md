---
name: povray
title: POV-Ray
source: brew
category: quick-weird-payoffs
commitment: afternoon
tags: [afternoon, generative, graphics, old-school, raytracing, visual]
homepage: https://www.povray.org/
scout_score: 5
status: draft
---

# POV-Ray

**TLDR;** A ray tracer from 1991 where you write a text description of a scene and the program renders it as a three-dimensional image.

POV-Ray, the Persistence Of Vision RAYtracer, is a free ray tracer for making three-dimensional graphics. You describe a scene in a text file, and the program works out how light would travel through it and writes out an image. The homepage calls it "a high-quality, Free Software tool for creating stunning three-dimensional graphics." The brief did not cover the scene-file syntax, so look at the documentation for the details.

Its lineage is documented. The site says POV-Ray "would not exist if it were not for David's kind contribution of the DKBTrace source code," a raytracer by David K. Buck. The first beta is dated July 29, 1991, which makes this one of the older graphics tools still around.

The idea underneath is that an image can be a program's output rather than something you draw. You write down geometry, materials and lights, and the renderer does the rest. That is a way into ray tracing, procedural scenes and how rendering works. The source is published, and the site notes it is "available for those wanting to do their own ports."

## Install

```
brew install povray
```

## Try this

```
povray --help
```
Prints the command-line options, a first look at what the renderer accepts.

## What's unique

It is a long-lived free ray tracer with a documented lineage back to DKBTrace and a first beta in 1991. You build images by writing a scene description rather than using a modelling GUI.

## Caveats

Development is quiet: 3.8 is still in beta after a long break, the docs list 3.7 as current, and the project says official Windows releases are stuck on an expired code-signing key.

## Links

- [POV-Ray homepage](https://www.povray.org/)
- [POV-Ray documentation index](https://www.povray.org/documentation/)
