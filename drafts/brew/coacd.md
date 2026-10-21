---
name: coacd
title: CoACD
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [3d, afternoon, geometry, math, mesh, physics]
homepage: https://github.com/SarahWeiii/CoACD
scout_score: 5
status: draft
---

# CoACD

**TLDR;** Splits a 3D triangle mesh into a small set of convex pieces, chosen so collisions behave like the original shape.

CoACD takes a triangle mesh and cuts it into convex parts. Each part is a convex hull, and together they approximate the original shape closely enough to serve as collision geometry in a physics or game engine. Output is written as .obj and .wrl files, and the Python API returns a list of convex hulls.

The reason to do this is that many geometry algorithms, collision detection among them, only work on convex shapes. A mug, a chair or a robot gripper is not convex. Break it into a handful of convex pieces and those algorithms work on it again. The README says the method keeps the collision behaviour of the input with fewer components.

The interesting part is how the cuts are chosen. The paper title describes a collision-aware concavity measure and a Monte Carlo tree search over cutting strategies, instead of splitting greedily and hoping. Cutting is treated as a search problem: try a cut, look ahead at what it leads to, and keep the sequence that scores best. Because the search is stochastic, `--seed` exists to reproduce a result.

In most cases only one knob matters. The README says: "you only need to adjust the `threshold` (0.01~1) to balance the level of detail and the number of decomposed components." Lower values give more pieces and a tighter fit, and you can see the trade-off on your own models.

## Install

```
brew install coacd
# Alternative: pip install coacd (Python package; Linux x86_64, Windows amd64, macOS x86_64 and Apple silicon)
# Building from source needs git and cmake >= 3.24 plus a recent compiler. No account or GPU is needed.
```

## Try this

```
pip install coacd
```
Installs the Python package from PyPI, which gives you the bundled example script and the API that returns convex hulls.

```
./main -i PATH_OF_YOUR_MESH -o PATH_OF_OUTPUT
```
Decomposes a triangle .obj mesh with default parameters and writes the convex parts to the output path. This is the binary built from source.

```
./main -i PATH_OF_YOUR_MESH -o PATH_OF_OUTPUT -t 0.05 -mi 200 -md 4 -mn 25
```
Runs the same decomposition with a lower concavity threshold and different search iteration, depth and node settings, so you can compare piece count and fit.

## What's unique

The cuts are chosen to preserve collision behaviour, not just to minimise geometric error, using a tree search instead of greedy splitting. A `--split` option writes each part to its own file so engines like MuJoCo or Bullet don't merge them back into one convex shape.

## Caveats

Input must be a triangle mesh, non-manifold meshes are preprocessed in ways that can change the geometry, and the default settings are the fast ones, so better results cost runtime. The brew formula lists no executables, so the command-line examples come from the source build.

## Links

- [GitHub repository](https://github.com/SarahWeiii/CoACD)
- [Project page](https://colin97.github.io/CoACD/)
- [Paper (arXiv)](https://arxiv.org/pdf/2205.02961.pdf)
- [Video](https://www.youtube.com/watch?v=r12O0z0723s)
