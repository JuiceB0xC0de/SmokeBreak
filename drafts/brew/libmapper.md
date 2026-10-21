---
name: libmapper
title: libmapper
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, c, instruments, library, live-performance, networking, osc]
homepage: http://www.libmapper.org
scout_score: 7
status: draft
---

# libmapper

**TLDR;** A C library where instruments and software announce signals on a network, and mappings between them can be rewired at runtime with no central broker.

libmapper lets a program declare data signals, such as a sensor reading or a synth parameter, on a shared network. Anyone can then create a mapping from one or more source signals to a destination signal. Mappings run over shared memory or Open Sound Control (OSC) across a network. The library handles address and datatype translation, and a small expression language can scale, combine, differentiate, integrate, filter or smooth values along the way.

It began as a tool for composers and performers who build their own instruments, such as Arduino-based controllers, and want to connect them to sound synthesizers. It was first written in Max/MSP and later re-implemented in C. The author wanted to change OSC mappings while a piece was running, instead of hard-coding them into patches.

The idea underneath is that the wiring between devices is data you can change, not code. In its own words, the authors "specifically wanted to avoid keeping a 'master' node which is responsible for arbitrating connections or republishing data". Devices announce themselves on a shared multicast UDP port, and a collision-handling protocol gives each one a unique ID. Signal data then flows directly peer-to-peer over UDP or TCP. Nothing sits in the middle holding a device database.

That model has reached hardware: the README's standout examples are the T-Stick instrument and the Maplet Eurorack module. It is also positioned as an open-source alternative to commercial tools like Osculator.

## Install

```
brew install libmapper
# Only liblo is required. Python, Java and C# bindings are optional and need their own toolchains. Also available via PyPI, NuGet and crates.io.
```

## Try this

## What's unique

Mappings are first-class objects that can be rewired at runtime, with a built-in expression language for signal conditioning and no central broker. Most OSC routing tools assume a hub.

## Caveats

The Homebrew formula installs no executables, so this is a library you write code against. Data is limited to numeric vectors, and the README says commercial use requires keeping it dynamically linked.

## Links

- [Homepage](http://www.libmapper.org)
- [GitHub repository and README](https://github.com/libmapper/libmapper)
- [IDMIL software page for libmapper](http://idmil.org/software/libmapper)
