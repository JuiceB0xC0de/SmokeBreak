---
name: halide
title: Halide
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, gpu, image-processing, language]
homepage: https://halide-lang.org
scout_score: 5
status: draft
---

# Halide

**TLDR;** A language embedded in C++ and Python that splits what an image computation does from how it runs, so you can retune performance without touching the math.

Halide is for writing fast image and array processing code. You describe the algorithm as functions over x and y, such as a 3x3 box filter. Then you write a separate schedule: how to tile, vectorize and parallelize the loops, and where intermediate results are stored or recomputed.

The pipeline is built through the C++ API as an in-memory representation, not parsed from a separate source file. Scheduling calls like `tile`, `vectorize`, `parallel` and `compute_at` are applied to the same `Func` objects that hold the algorithm. Changing the schedule changes execution order and locality, and the algorithm stays the same. Halide can then compile the result to an object file for ahead-of-time use, or JIT-compile and run it in the same process.

The idea underneath is that most of the work in fast numeric code is not the math but the loop structure around it, and the two can be pulled apart. The same computation can be reorganized for different CPUs or GPU APIs (CUDA, OpenCL, Metal, Vulkan) without rewriting what it computes. The README puts it this way: "Rather than being a standalone programming language, Halide is embedded in C++."

The Homebrew formula also installs some tools named after 2019 and 2021 autoscheduler papers, such as cost-model retraining utilities. The README does not describe them, so their purpose here is unverified.

## Install

```
brew install halide
# or, for the Python binding and a binary build: pip install halide
# Building from source needs CMake 3.28+, C++17 and LLVM 21, 22 or 23.
```

## Try this

```
pip install halide
```
Installs the latest full release from PyPI, which the README calls the easiest way to get a binary build, even for C++ users.

```
get_host_target --help
```
Runs one of the executables Homebrew installs; its purpose is not described in the README, so the help output is the place to start.

```
gengen --help
```
Shows the options of another installed executable, which the README does not explain.

## What's unique

The algorithm-versus-schedule split is the hook: the homepage's box filter is written once, and tiling, vectorizing and parallelizing are separate lines you can change freely. It is embedded in C++ and Python rather than being a standalone language.

## Caveats

It is a compiler toolchain with real build requirements (LLVM, CMake), the Makefile build is unsupported, Vulkan and WebGPU are marked beta, and the homepage and README disagree on some target details.

## Links

- [Homepage](https://halide-lang.org)
- [Tutorials](https://halide-lang.org/tutorials)
- [API docs](https://halide-lang.org/docs)
- [GitHub repository](https://github.com/halide/Halide)
