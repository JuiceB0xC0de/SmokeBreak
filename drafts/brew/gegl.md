---
name: gegl
title: GEGL
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, gimp, image-processing, library, node-graph]
homepage: https://www.gegl.org/
scout_score: 7
status: draft
---

# GEGL

**TLDR;** The node-graph image engine under GIMP, with a command-line tool for chaining pixel operations into pipelines in floating point.

GEGL, the Generic Graphics Library, is a data flow image processing framework. Instead of applying one edit after another to a bitmap, you describe a pipeline: load an image, adjust colour, apply a filter, store the result. The operations are chained into a graph, and the graph is the description of the work.

The homepage says it provides "floating point processing and non-destructive image processing capabilities". Floating point means intermediate results are not squeezed into 8 bits at each step. Non-destructive means the original is untouched and the graph can be changed and re-run. GEGL supplies the operations for loading and storing images, colour adjustments, and GIMP's artistic filters.

It was built as the engine for GIMP, and other projects use it too, including imgflo, GNOME Photos and iconographer. The brief says the command-line syntax matches the one used to build processing flows interactively in GIMP. That makes the terminal a plain way to see what a graph of image operations looks like without a GUI around it.

The brew formula installs two executables, gegl and gegl-imgcmp. The homepage does not say exactly what each does, so start with the help output.

## Install

```
brew install gegl
```

## Try this

```
gegl --help
```
Prints the usage text for the main gegl tool, the starting point for seeing how a pipeline is written on the command line.

```
gegl-imgcmp --help
```
Prints the usage text for the second installed tool, so you can see what it does.

## What's unique

It is the actual graph-based engine behind GIMP, usable outside the GUI with the same syntax for describing pipelines. Most image command-line tools apply one edit at a time; this one treats the pipeline as the thing you build.

## Caveats

The brief found no usage examples and no README, so expect to learn from --help and the project site. Maintenance looks likely but is only weakly evidenced.

## Links

- [GEGL homepage](https://www.gegl.org/)
- [GEGL source on GNOME GitLab](https://gitlab.gnome.org/GNOME/gegl)
