---
name: openvdb
title: OpenVDB
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, gpu, library, simulation, vfx, volumetrics]
homepage: https://www.openvdb.org/
scout_score: 5
status: draft
---

# OpenVDB

**TLDR;** A C++ library from DreamWorks for storing sparse 3D volumes like smoke, clouds and fire, and the data structure behind much film VFX.

OpenVDB is an open-source C++ library for storing and manipulating sparse volumetric data on three-dimensional grids. Think of a voxel grid for a cloud or a puff of smoke: most of the space is empty, and a dense array wastes memory on nothing. OpenVDB is built around a hierarchical data structure, the VDB tree, that only spends storage where something actually exists, along with a large suite of tools that work on that structure.

DreamWorks Animation developed it for the volumetric work typical of feature film production. The project's homepage says it won an Academy Award, and it is now maintained by the Academy Software Foundation. Its own description calls it "a novel hierarchical data structure and a large suite of tools for the efficient storage and manipulation of sparse volumetric data discretized on three-dimensional grids."

The idea underneath is that sparsity is a data-structure problem. Once you have a tree that can represent huge, mostly empty 3D space cheaply, fluid simulation, level sets and smoke rendering become tractable. The project has also grown NanoVDB, a GPU-oriented variant, and OpenVDB AX, both optional builds.

The brew formula installs three small executables, vdb_print, nanovdb_print and nanovdb_validate. The sources the brief drew on do not say what they do, so treat them as something to discover with --help. The real entry point is the library and its documentation.

## Install

```
brew install openvdb
# Pulls in boost, c-blosc, jemalloc, openexr and tbb. Building from source with CMake is the documented developer route; NanoVDB and AX need extra configure flags.
```

## Try this

```
vdb_print --help
```
Shows the usage text for the vdb_print executable that the formula installs.

```
nanovdb_print --help
```
Shows the usage text for the NanoVDB print tool.

```
nanovdb_validate --help
```
Shows the usage text for the NanoVDB validation tool.

## What's unique

It is an Academy Award-winning library from a major studio's production tooling, now stewarded by the Academy Software Foundation. Its hierarchical sparse grid is the core idea, and NanoVDB extends it toward the GPU.

## Caveats

It is a C++ library rather than a ready-to-play program, so you will need to write code or have VDB files to get much out of it; the GitHub trunk is also less stable than the production releases.

## Links

- [Homepage](https://www.openvdb.org/)
- [Documentation (Doxygen)](https://www.openvdb.org/documentation/doxygen)
- [GitHub repository](https://github.com/AcademySoftwareFoundation/openvdb)
- [Releases](https://github.com/AcademySoftwareFoundation/openvdb/releases)
