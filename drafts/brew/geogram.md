---
name: geogram
title: geogram
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, delaunay, geometry, library, mesh, visual, voronoi]
homepage: https://github.com/BrunoLevy/geogram/wiki
scout_score: 6
status: draft
---

# geogram

**TLDR;** A C++ geometry library from Inria research code, with Delaunay, Voronoi, remeshing and boolean ops, plus a mesh viewer and demo programs to poke at.

Geogram is a C++ library of geometric algorithms for people building geometry tools. Its README lists surface reconstruction, remeshing, parameterization and texturing, intersections and boolean operations, and constructive solid geometry. Below those sit the lower-level pieces: exact predicates, 2D and 3D Delaunay triangulations, a mesh data structure, geometric search structures, spectral mesh processing, and a linear solver for CPU and GPU.

It began as Bruno Levy's post-doc work around Y2K and carries forward the main results of the former ALICE Inria project (2004-2018). The wiki describes that as more than 30 research articles whose results are maintained and reproducible, some used in industrial products. The library is meant as a lasting home for research code that would otherwise rot in a paper's supplementary folder. It won the Symposium on Geometry Processing Software Award in 2023.

The brew formula installs more than the library. It also puts a handful of executables on your path, including `vorpaview`, which the wiki identifies as a mesh viewer, and several `geogram_demo_*` programs named for Delaunay triangulation, CSG, raytracing and picking. There is also GLUP, which the project calls "3D Graphics without the headache", a small graphics layer used by the demos. The same code is compiled to WebAssembly through Emscripten for in-browser demos. The brief did not cover what each executable does, so `--help` is the place to start.

## Install

```
brew install geogram
# pulls in glfw; the demos open graphical windows, so run them on a desktop session
```

## Try this

```
vorpaview --help
```
Prints the options for the mesh viewer, the quickest way into the installed tools.

```
geogram_demo_Delaunay2d --help
```
Shows the options for the 2D Delaunay triangulation demo.

```
vorpalite --help
```
Lists what the vorpalite command-line tool accepts.

## What's unique

It packages research code from more than 30 geometry-processing papers as a maintained, reproducible library, and ships viewers and demos alongside it. It also runs in the browser through Emscripten.

## Caveats

It is primarily a programming library, so real use means writing C++; the brief did not confirm what most of the installed executables do, and the wiki is large.

## Links

- [Wiki home (brew homepage)](https://github.com/BrunoLevy/geogram/wiki)
- [GitHub repository and README](https://github.com/BrunoLevy/geogram)
- [Programmer's reference manual](https://brunolevy.github.io/geogram/)
- [In-browser demos (Emscripten)](https://github.com/BrunoLevy/geogram/wiki/compiling_Emscripten#examples)
- [Linux compile guide](https://github.com/BrunoLevy/geogram/wiki/compiling_Linux)
