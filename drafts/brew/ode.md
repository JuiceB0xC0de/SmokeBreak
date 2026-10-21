---
name: ode
title: ODE (Open Dynamics Engine)
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c, library, physics, rigid-body, simulation]
homepage: https://www.ode.org/
scout_score: 6
status: draft
---

# ODE (Open Dynamics Engine)

**TLDR;** A C/C++ physics library that simulates rigid bodies, joints and contacts, the kind of engine that moves vehicles and walking creatures in games.

ODE is a library for simulating articulated rigid body dynamics. You describe bodies, joints and forces through a C/C++ API, then call a step function and it advances the physics. It has joint types, collision detection with friction built in, and optional triangle-mesh collision through OPCODE or GIMPACT.

The homepage frames it as a physics SDK: something a game or simulation embeds so it does not have to write its own solver. It says ODE is "currently used in many computer games, 3D authoring tools and simulation tools." The examples it gives are ground vehicles, legged creatures and moving objects in VR.

The idea underneath is that a lot of simulated motion is a set of rigid bodies connected by constraints, with contacts resolved each step. Once you see that, you can build a car, a ragdoll or a walking robot out of the same few pieces, then change a force, a joint or a collision and watch what happens. The source ships demos drawn with an OpenGL-based DrawStuff library, so there is something to look at without writing a renderer.

The Homebrew formula installs one executable, `ode-config`. The README does not mention it, so it is presumably a helper that reports build flags for programs linking against the library. This is a library you build things with, not a program you run.

## Install

```
brew install ode
# Library only. To build the demos you need CMake 3.10+, a C/C++ compiler, and OpenGL/GLU (demos are on by default); see the README.
```

## Try this

```
ode-config --help
```
Shows the options of the helper the Homebrew formula installs; presumably it reports compile and link flags for projects using ODE.

```
cmake -B build -DCMAKE_BUILD_TYPE=Release
```
From a clone of the GitHub repo, configures a Release build that includes the demos by default.

```
cmake --build build --parallel
```
Compiles the library and demos so you can run the DrawStuff demos and start changing forces and joints.

## What's unique

It is a mature physics engine you can build from source and perturb, with demos that make the rigid-body behaviour visible. Most physics libraries are just a dependency.

## Caveats

It is a library with a C/C++ API, not a standalone tool, so the fun starts with building the source demos or writing code; the homepage is dated and GIMPACT mesh collision is marked experimental.

## Links

- [ODE homepage](https://www.ode.org/)
- [GitHub repository (odedevs/ode)](https://github.com/odedevs/ode)
- [ODE manual (wiki)](https://ode.org/wiki/index.php?title=Manual)
- [API documentation](http://opende.sf.net/docs/index.html)
