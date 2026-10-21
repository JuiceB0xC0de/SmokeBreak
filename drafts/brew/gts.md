---
name: gts
title: GTS: the GNU Triangulated Surface Library
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c, geometry, library, math, mesh]
homepage: https://gts.sourceforge.net/
scout_score: 5
status: draft
---

# GTS: the GNU Triangulated Surface Library

**TLDR;** A C library and small toolset for 3D triangle meshes, with robust boolean operations, Delaunay triangulation and STL conversion, hiding behind many other programs.

GTS is a C library for surfaces made of interconnected triangles. It covers 2D Delaunay and constrained Delaunay triangulation, union, intersection and difference of surfaces, refinement and coarsening, isosurface extraction, and measurements such as area, volume and curvature. The brew formula also installs a handful of command-line tools built on it: stl2gts, gts2stl, gts2dxf, gts2oogl, gtscheck, gtscompare, delaunay, happrox and transform.

The homepage says it began as "a simple and efficient library to scientists dealing with 3D computational surface meshes". It is written in C with a GTK-style object hierarchy: points, vertices, segments, edges, triangles, faces and surfaces, with inheritance and virtual functions. Bounding-box trees and Kd-trees handle point location and intersection tests.

The interesting idea is how geometry code survives degenerate cases. Boolean operations and point-in-surface tests use Simulation of Simplicity, a technique that treats ties and coincident points as if the input were perturbed slightly, so the code does not need a pile of special cases. The floating-point predicates use fast adaptive arithmetic adapted from Jonathan Shewchuk's work. The isosurface code uses marching tetrahedra, added in 2002 to avoid the topological defects of marching cubes.

Most people meet GTS as a dependency of something else. Installing it directly gives you the converters and checkers, and a way into the robustness problems of computational geometry.

## Install

```
brew install gts
# Needs glib, netpbm and gettext, which brew pulls in. To write your own code against it, gts-config supplies compile flags, in the style of glib.
```

## Try this

```
gtscheck --help
```
Shows the options of the surface checker, which tests a GTS surface for problems such as degenerate or intersecting faces.

```
stl2gts --help
```
Shows how to convert an STL mesh into GTS's own text format.

```
delaunay --help
```
Shows how to build a Delaunay triangulation from a set of points.

## What's unique

It is a small, old, exact-predicate geometry kernel with Simulation of Simplicity boolean operations, and its source is readable enough to learn from.

## Caveats

The latest release on the homepage is 0.7.6 from March 2006, the site looks dated, and the release notes say boolean operations can fail on some nested closed loops or degenerate faces.

## Links

- [GTS homepage](https://gts.sourceforge.net/)
