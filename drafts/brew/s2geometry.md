---
name: s2geometry
title: S2 Geometry
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, cpp, geometry, geospatial, library, math]
homepage: https://github.com/google/s2geometry
scout_score: 6
status: draft
---

# S2 Geometry

**TLDR;** A C++ library for geometry on a sphere instead of a flat map, built with geographic data in mind.

S2 Geometry is a C++ library for working with shapes drawn on the surface of a sphere. Most geometry libraries assume a flat plane, and geographic work then leans on a projection that bends distances and shapes. S2 starts from the sphere. In the README's words: "Unlike many geometry libraries, S2 is primarily designed to work with spherical geometry, i.e., shapes drawn on a sphere rather than on a planar 2D map."

The README says this makes it especially suitable for geographic data. It does not go into the inputs, outputs, or internals, so the details are in the docs at s2geometry.io, which the brief did not cover. The overview and C++ quick start pages there are the place to start.

The idea underneath is that the planar shortcuts break down on a globe. Lines that look straight on a map are not shortest paths, and shapes near the poles or the date line behave oddly. Working natively on the sphere removes that class of problem. It is a real door into how mapping and location systems think about the Earth.

There is no command-line tool here. It is a library you build and link against. A Python interface exists as an optional SWIG build, and the README lists Go and Java implementations made by others.

## Install

```
brew install s2geometry
# Library only, no executables. Needs a C++ toolchain to use. Depends on abseil, which brew pulls in.
# Building from source: Bazel 8+ or CMake 3.22+ with a C++17 compiler. The Python interface needs a separate SWIG build.
```

## Try this

```
bazel build //:s2
```
From s2geometry/src in a source checkout, builds the library without running tests.

```
bazel test "//:*"
```
Builds and runs the full test suite, which needs Bazel 8 or newer.

```
cmake -DBUILD_TESTS=yes -DCMAKE_PREFIX_PATH=/path/to/absl/install -DCMAKE_CXX_STANDARD=17 ..
```
Configures the CMake build from a build directory, pointed at your Abseil install.

## What's unique

It is built for the sphere from the start, not as a flat geometry library adapted to the globe.

## Caveats

All releases are 0.x with no API or ABI stability guarantees, the Python API is described as particularly unstable, and the README says the s2loop_measures_test fails on Apple M1.

## Links

- [GitHub repository](https://github.com/google/s2geometry)
- [S2 documentation site](http://s2geometry.io)
- [S2 overview](http://s2geometry.io/about/overview)
- [C++ quick start](http://s2geometry.io/devguide/cpp/quickstart)
