---
name: octomap
title: OctoMap
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [3d, afternoon, c++, library, mapping, octree, robotics]
homepage: https://octomap.github.io/
scout_score: 6
status: draft
---

# OctoMap

**TLDR;** A C++ library that turns robot sensor readings into a 3D map of occupied, free and unknown space, stored as an octree.

OctoMap builds 3D occupancy maps from sensor data such as laser scans. Space is divided into an octree, and each node holds a probability that the region is occupied. New readings update those probabilities, which is how the map copes with noise and with things that move.

The design choice that makes it interesting is that unknown space is part of the model. Regions nobody has observed are simply absent from the tree, so the map records what is free, what is occupied, and what has not been looked at yet. For a robot exploring on its own, that third category matters most, because it says where to go next. The tree grows as needed and can be saved in a compact form.

It is also multi-resolution. A coarse view of the same map can serve a high-level planner while a fine view serves a local one. The project comes out of the University of Freiburg and is cited as Hornung et al., Autonomous Robots, 2013. Its own description: "The OctoMap library implements a 3D occupancy grid mapping approach, providing data structures and mapping algorithms in C++ particularly suited for robotics."

The repository has two parts: octomap, the library, and octovis, a visualisation library and tools. Homebrew installs eight command-line executables, including converters and comparison tools for octree files. The README I read does not describe them, so start with their help output.

## Install

```
brew install octomap
```

## Try this

```
convert_octree --help
```
Prints usage for the octree conversion tool, a good first look at what file formats it handles.

```
compare_octrees --help
```
Shows how to compare two octree maps.

```
bt2vrml --help
```
Shows usage for the tool that appears to export a binary tree map to VRML for viewing.

## What's unique

Unknown space is a first-class part of the map, not an afterthought, and one map serves both coarse planning and fine detail through multi-resolution octrees.

## Caveats

Octomap is BSD-licensed but octovis is GPL, the eight executables are undocumented in the README I read, and recent maintenance activity is unconfirmed.

## Links

- [Homepage](https://octomap.github.io/)
- [GitHub repository](https://github.com/OctoMap/octomap)
- [Online API documentation (doxygen)](https://octomap.github.io/octomap/doc/)
