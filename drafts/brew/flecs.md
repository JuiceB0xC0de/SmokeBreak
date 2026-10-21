---
name: flecs
title: Flecs
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c, cpp, ecs, games, generative, library, simulation]
homepage: https://www.flecs.dev
scout_score: 5
status: draft
---

# Flecs

**TLDR;** A small C and C++ library that organizes simulations as plain data plus functions, handling millions of entities per frame, with a browser explorer for inspecting the running program.

Flecs is an Entity Component System (ECS) library. Instead of building objects with methods and inheritance, you split a world into three things: entities, which are just identifiers; components, which are plain data types attached to entities; and systems, which are functions that run over every entity matching a query, such as everything that has both a position and a velocity.

The README presents this as a way of organizing code and data "that lets you build games that are larger, more complex and are easier to extend." Underneath is a storage idea. Entities with the same set of components are grouped together in cache-friendly archetype tables, laid out as structure-of-arrays. The README says this lets it process millions of entities every frame. It also mentions a lockless scheduler for spreading work across CPU cores. Systems run in a pipeline, and the simulation advances each time your program calls `ecs_progress`.

The pattern is the door here. Once you think of a program as a queryable database of data with functions running over it, game loops, particle systems, agent simulations and generative toys start to look alike. Flecs also bundles a reflection framework with a JSON serializer, a statistics addon, and a web-based Flecs Explorer for watching and controlling a live app. The same library runs in the browser through emscripten, with a demo at flecs.dev/city.

This is a library you compile into your own program, not a tool with a command line. The brief covers the C99 and C++17 APIs; bindings for C#, Rust, Zig, Lua and Clojure are community-maintained.

## Install

```
brew install flecs
# This installs the library and headers only. There is no executable. You need a C or C++ compiler and your own program to link it against.
```

## Try this

## What's unique

The README claims it is the first open source ECS with full support for entity relationships. It also ships a live browser-based explorer and a reflection system in the same small library, which is unusual for an ECS.

## Caveats

It is a programming library with nothing to run from a shell, and the brief found no install or build commands, so you will be reading the docs to get started.

## Links

- [Homepage](https://www.flecs.dev)
- [Documentation](https://www.flecs.dev/flecs/Docs.html)
- [GitHub repository](https://github.com/SanderMertens/flecs)
- [Flecs Explorer (web UI)](https://flecs.dev/explorer)
