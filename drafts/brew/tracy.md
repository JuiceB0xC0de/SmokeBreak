---
name: tracy
title: Tracy
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, gamedev, gpu, gui, performance, profiler, telemetry]
homepage: https://tracy.nereid.pl/
scout_score: 6
status: draft
---

# Tracy

**TLDR;** A nanosecond-resolution profiler that streams timing data from a running program into a live viewer, covering CPU, GPU, memory, locks and context switches.

Tracy is a profiler for games and other real-time applications. You add Tracy's client integration to your program, and while the program runs, timing data streams to a separate viewer window. The README calls it "a real time, nanosecond resolution, remote telemetry, hybrid frame and sampling profiler for games and other applications."

The README lists what it can see: CPU work (direct support for C, C++, Lua, Python and Fortran, plus third-party bindings for languages such as Rust, Zig, C#, OCaml and Odin), GPU work across OpenGL, Vulkan, Direct3D 11/12, Metal, OpenCL, CUDA and WebGPU, memory allocations, locks, and context switches. It can also attach screenshots to captured frames, so a slow frame can be matched with what was on screen.

The idea underneath is to look at timing as it happens rather than reading a summary afterward. Because the viewer is separate from the program and connected over the network, the profiled program can be on another machine. The brew install also ships a set of command-line helpers, including tracy-capture, tracy-csvexport, tracy-import-chrome and tracy-merge. The README does not describe them, so their exact roles are best checked with their --help output.

The full explanation of how it works lives in the PDF manual, which is the place to go next.

## Install

```
brew install tracy
# Profiling your own program means adding Tracy's client code to it; the manual (tracy.pdf) covers build instructions.
```

## Try this

```
tracy-profiler --help
```
Prints the options for the profiler viewer, the window that receives and displays live timing data.

```
tracy-capture --help
```
Shows the options for the command-line capture tool, which records a session to a file without opening the viewer.

```
tracy-csvexport --help
```
Shows how to export captured data as CSV.

## What's unique

It combines frame profiling and sampling in one tool, with live remote telemetry, GPU coverage across many graphics and compute APIs, and screenshots tied to captured frames.

## Caveats

The main documentation is a PDF, you need a program instrumented with the Tracy client to see anything interesting, and non-C/C++/Lua/Python/Fortran languages rely on third-party bindings of unknown quality.

## Links

- [Homepage (interactive demo)](https://tracy.nereid.pl/)
- [Documentation (tracy.pdf, latest release)](https://github.com/wolfpld/tracy/releases/latest/download/tracy.pdf)
- [Releases (binaries and changelog assets)](https://github.com/wolfpld/tracy/releases)
- [CppCon 2023 introduction by Marcos Slomp](https://youtu.be/ghXk3Bk5F2U?t=37)
