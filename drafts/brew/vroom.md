---
name: vroom
title: VROOM
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, math, operations-research, optimization, routing]
homepage: http://vroom-project.org/
scout_score: 5
status: draft
---

# VROOM

**TLDR;** An open-source engine that takes vehicles, pickups and deliveries with time windows and capacities, and returns optimized routes in milliseconds.

VROOM solves vehicle routing problems. You describe a fleet of vehicles and a set of jobs (single-location pickups or deliveries) and shipments (a pickup paired with a delivery that must ride on the same route). Constraints can include capacities on several metrics, skills, time windows, service durations, priorities, working hours and driver breaks. It returns a set of routes. It is written in C++20 and handles several well-known variants at once: TSP, CVRP, VRPTW, MDHVRPTW and PDPTW.

It does not ship its own road network. Travel times come from an external routing engine (OSRM, Openrouteservice or Valhalla), or from a custom cost matrix you build yourself. That split is the useful part: the optimizer only has to reason about a table of costs between places, and the map data lives elsewhere. The homepage says the free version relies on OpenStreetMap data.

The idea underneath is combinatorial optimization. Deciding which vehicle serves which stop, and in what order, blows up quickly as stops are added, so a good-enough answer found fast often beats a perfect answer found never. The project's own line is "Good solutions, fast." The README does not describe the search algorithm, so that is the thing to go and read about.

The README also frames it as a tool for people, not a replacement: "Vroom doesn't replace domain expertise." It is maintained by Verso, which also sells a premium API built on it. VROOM can also be used as a C++ library (libvroom).

## Install

```
brew install vroom
# You also need a routing backend (OSRM, Openrouteservice or Valhalla) or your own cost matrix.
# The README points to building from source (wiki) or vroom-docker, which bundles the vroom-express HTTP wrapper.
```

## Try this

```
vroom --help
```
Lists the command-line options, a quick way to see how problems and routing backends are passed in.

## What's unique

One engine handles several classic routing variants together, including pickup-and-delivery with time windows, and plugs into open routing engines rather than bundling its own map data.

## Caveats

Route quality depends on the routing engine or cost matrix you supply, and the README gives no install command or platform list, so setup details live in the wiki.

## Links

- [Homepage (Vroom by Verso)](http://vroom-project.org/)
- [GitHub repository](https://github.com/VROOM-Project/vroom)
- [Demo frontend](http://map.vroom-project.org/)
- [Usage wiki](https://github.com/Vroom-Project/vroom/wiki/Usage)
- [vroom-docker](https://github.com/Vroom-Project/vroom-docker)
