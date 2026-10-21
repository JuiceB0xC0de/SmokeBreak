---
name: colmap
title: COLMAP
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [3d, afternoon, computer-vision, math, photogrammetry, science, visual]
homepage: https://colmap.github.io/
scout_score: 6
status: draft
---

# COLMAP

**TLDR;** Feed it a folder of photos and it works out where each camera stood, then builds a 3D point cloud and mesh of the scene.

COLMAP is a Structure-from-Motion (SfM) and Multi-View Stereo (MVS) pipeline with both a graphical interface and a command line. You give it a collection of images, ordered or not, and it recovers the camera poses and a sparse 3D model of the scene. It then builds dense point clouds and meshes from that.

The idea underneath is that photos taken from different positions contain enough overlap to recover geometry. The sparse stage matches features across images and incrementally solves for where each camera was and where the matched points sit in space. The dense stage uses PatchMatch stereo and stereo fusion to fill in the surfaces. The homepage also lists a GLOMAP global SfM pipeline and a vocabulary-tree image retrieval engine.

It is presented as a research-grade tool, with citations to papers from CVPR, ECCV and ACCV. It is used in academic and industrial 3D reconstruction work. Python bindings (pycolmap) expose most of the pipeline, so you can script it or take it apart stage by stage.

The quick route is the automatic reconstruction: in the project's words, "Use the automatic reconstruction to easily build models with a single click or command." Sample datasets are available, or you can shoot your own set of photos around an object.

## Install

```
brew install colmap
# Other routes: conda install colmap (conda-forge), Docker images at hub.docker.com/r/colmap/colmap, pycolmap from PyPI. Dense reconstruction is compute-heavy; a CUDA GPU helps.
```

## Try this

```
colmap --help
```
Lists the available subcommands of the pipeline.

```
conda install colmap
```
Installs COLMAP from conda-forge, an alternative to Homebrew listed in the README.

## What's unique

It is a complete, research-backed photo-to-mesh pipeline that also ships a GUI, so the whole workflow runs from one click or one command.

## Caveats

Dense reconstruction needs a lot of compute, AMD GPUs are supported only through HIP/ROCm when building from source, and the brief could not confirm the date of the latest release.

## Links

- [Homepage and docs](https://colmap.github.io/)
- [GitHub repository](https://github.com/colmap/colmap)
- [Installation guide](https://colmap.github.io/install.html)
- [Sample datasets](https://demuc.de/colmap/datasets/)
