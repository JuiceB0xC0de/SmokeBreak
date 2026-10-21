---
name: voro++
title: Voro++
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, geometry, library, math, science]
homepage: https://math.lbl.gov/voro++
scout_score: 5
status: draft
---

# Voro++

**TLDR;** A C++ library that computes a 3D Voronoi cell around each particle one at a time, returning volume, centroid, and face count per cell.

Voro++ takes a set of particle positions in three dimensions and works out the Voronoi cell for each one: the region of space closer to that particle than to any other. For each cell it can report properties such as volume, centroid, and number of faces. It is built as a static library of C++ classes, and a command-line utility is included that exposes most of its features.

The unusual part is how it gets there. Most tools build the whole tessellation at once. Voro++ builds each particle's cell directly, on its own. In the project's words: "A distinguishing feature of the Voro++ library is that it carries out cell-based calculations, computing the Voronoi cell for each particle individually." The homepage says this makes it well suited to special boundary conditions and walls, and that its algorithms tolerate numerical precision errors.

The author built it for cell-based statistics on particle systems, where the shape and size of each cell says something about how the particles are packed. It also includes a radical tessellation, contributed by a collaborator, for packings of particles of different sizes. Behind it sits a broader idea: partitioning space by nearest neighbour turns up in physics, materials science, and graphics, and the per-cell numbers are a way to measure a structure rather than just draw it.

It comes from Lawrence Berkeley National Laboratory and is maintained by Chris Rycroft. Gnuplot and POV-Ray are optional helpers for looking at the output.

## Install

```
brew install voro++
# Builds from source otherwise: review config.mk, then run make and sudo make install (defaults to /usr/local). No external dependencies. Gnuplot and POV-Ray are optional for viewing output.
```

## Try this

## What's unique

It builds each Voronoi cell directly rather than computing a global tessellation, which suits per-particle statistics and walls or unusual boundaries. It also offers a radical tessellation for polydisperse packings.

## Caveats

The last listed release is 0.4.6 from October 2013, and the brief did not check the repository for newer activity; the brew formula lists no executables, so the command-line utility may not be installed by it.

## Links

- [Voro++ homepage](https://math.lbl.gov/voro++)
- [Download page (install instructions, references)](https://math.lbl.gov/voro++/download/)
