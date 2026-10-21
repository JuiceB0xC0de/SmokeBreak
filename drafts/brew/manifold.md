---
name: manifold
title: Manifold
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, cad, geometry, library, math, mesh]
homepage: https://github.com/elalish/manifold
scout_score: 5
status: draft
---

# Manifold

**TLDR;** A C++ geometry library whose mesh Boolean operations are meant to always return a valid closed solid, with a web playground to try it.

Manifold is a library for building and combining triangle meshes that describe closed solid objects. You can make shapes with OpenSCAD-style constructors or from signed-distance functions, then union, subtract and intersect them, smooth and refine the result, and write it out. It has bindings for C, JS/TS via WASM, Python and several other languages.

The reason it exists is reliability. The README puts it this way: "Our primary goal is reliability: guaranteed manifold output without caveats or edge cases." It calls a robust mesh Boolean "an open problem for many years" and says this may be the first guaranteed-manifold one. Speed through parallelism, using TBB, is the second goal.

The idea underneath is what "manifold" means for a mesh: every edge joins exactly two faces and the surface encloses a volume, so the object could exist as a solid. Most mesh Boolean code can produce holes, stray edges or self-intersections on awkward input, and everything downstream then breaks. Manifold treats a valid solid as an invariant and tracks vertex properties and IDs so you can tell which input object each surface came from. The README links to a wiki for the algorithm details, which is the place to go deeper.

The project has opinions. It discourages STL export because STL loses topology, and points to 3MF or glTF with the EXT_mesh_manifold extension. Its user list includes OpenSCAD, Blender, Godot and BRL-CAD.

## Install

```
brew install manifold
This installs the C++ library and its dependencies (clipper2, tbb), with no executables. For quicker experiments, the README lists PyPI (manifold3d) and npm (manifold-3d) packages, or the ManifoldCAD web app, which needs no install.
```

## Try this

```
help(manifold3d)
```
Inside a Python interpreter after importing manifold3d, prints the binding documentation so you can see what shapes and operations exist.

```
python3 run_all.py -e
```
From a source checkout's Python examples, runs the samples and exports models. The README says to install trimesh and pytest first.

```
git clone --recurse-submodules https://github.com/elalish/manifold.git
```
Fetches the source with submodules, the first step toward building it and running make test.

## What's unique

Few mesh Boolean tools promise valid solid output, and this one says it is probably the first to do so. It also refuses to write STL files by design.

## Caveats

Non-manifold input is rejected with an error and Merge only repairs slightly broken meshes, the WASM build is serial-only, and I could not confirm recent maintenance activity.

## Links

- [Homepage / GitHub](https://github.com/elalish/manifold)
- [ManifoldCAD web app](https://manifoldcad.org)
- [Algorithm documentation (wiki)](https://github.com/elalish/manifold/wiki/Manifold-Library)
- [C++ documentation](https://manifoldcad.org/docs/html/classmanifold_1_1_manifold.html)
