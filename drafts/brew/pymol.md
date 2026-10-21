---
name: pymol
title: PyMOL
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, gui, molecules, python, science, visual]
homepage: https://pymol.org/
scout_score: 5
status: draft
---

# PyMOL

**TLDR;** A molecular viewer for spinning proteins and other biomolecules in 3D, built on open-source code that commercial licenses pay for.

PyMOL renders and inspects 3D molecular structures such as proteins and other biomolecules. The homepage describes it as a user-sponsored system on an open-source foundation, maintained and distributed by Schrodinger. The brief does not spell out inputs and outputs, so the usual picture applies: you load a structure, rotate it, and change how it is drawn.

The odd part is how it is funded. The open-source repository holds most of the source under a BSD-like license, while the full commercial product, called 'Incentive PyMOL' in the repo README, adds maintenance and support. License purchases pay for development. The homepage credits the original author, Warren L. DeLano, with that vision, and puts it this way: "Open source enables open science."

The door it opens is structural biology. Proteins are shapes, and much of what they do follows from those shapes. A viewer like this lets you look at one and see why a drug fits a pocket or why a fold holds together. The name hints at Python, and the install pulls in python and numpy, but the brief does not describe the scripting side, so look there yourself.

## Install

```
brew install pymol
# To generate movies, also run: brew install ffmpeg
# Needs OpenGL and a desktop session; the formula pulls in PyQt for the GUI.
```

## Try this

```
pymol
```
Launches PyMOL, opening its viewer window.

```
pymol --help
```
Prints the command-line options the launcher accepts.

## What's unique

It is a commercial product whose source is mostly published under a permissive license, with license sales funding the open code. That is an unusual model for scientific visualization software.

## Caveats

Current commercial versions need a paid license, the open-source build is separate, and the brew formula's own licensing and version may differ from the homepage bundles.

## Links

- [PyMOL homepage](https://pymol.org/)
- [Open-source PyMOL repository (GitHub)](https://github.com/schrodinger/pymol-open-source)
- [INSTALL file](https://github.com/schrodinger/pymol-open-source/blob/master/INSTALL)
- [PyMOL wiki: Linux install](http://pymolwiki.org/index.php/Linux_Install)
