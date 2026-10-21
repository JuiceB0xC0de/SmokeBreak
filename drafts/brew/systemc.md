---
name: systemc
title: SystemC
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, c++, hardware-modelling, language, library, simulation]
homepage: https://systemc.org/overview/systemc/
scout_score: 5
status: draft
---

# SystemC

**TLDR;** A C++ class library that lets you model and simulate hardware in ordinary C++, standardised as IEEE 1666, so software can run before the chip exists.

SystemC is a library, not an application. You write a C++ program against its classes, compile it against the SystemC libraries, and the resulting binary is the simulation. There is no new syntax and no separate hardware description language. The Homebrew package is the core library plus its examples folder.

The idea behind it, as the project describes it, is that designing a system-on-chip needs one language spanning hardware and software. Architects can then weigh partitioning, performance and power, and embedded software can start before RTL or silicon exists. The README lists system-level modelling, architectural exploration, performance modelling, software development, functional verification and high-level synthesis as uses.

Under the hood, INSTALL.md says the build uses QuickThreads where it supports the processor, and otherwise falls back to POSIX threads on Unix or Fibers on Windows to run simulation processes. The README does not describe the scheduler or event model. For that, it points to the standard: "The main documentation of SystemC is the IEEE Std. 1666-2023 Standard SystemC Language Reference Manual."

The door it opens is hardware modelling from the software side. Concurrent processes, simulated time and modules wired together are the concepts hardware designers work in, and you can explore them with a C++ compiler instead of a chip toolchain.

## Install

```
brew install systemc
Needs a C++17 compiler to build your own models. To build from source instead, INSTALL.md describes CMake 3.16+ with GCC 9.3+, Clang 13+ or MSVC 2019+. The default install prefix is /opt/systemc.
```

## Try this

```
mkdir build
```
First step of the INSTALL.md source build, creating a build directory inside the SystemC source tree.

```
ccmake ..
```
From inside build/, opens the interactive configurator. Examples are built by default (ENABLE_EXAMPLES is ON).

```
make check
```
After make, runs the test suite, including the bundled examples.

## What's unique

Hardware modelling is delivered as a plain C++ class library standardised by the IEEE, rather than as a separate hardware description language.

## Caveats

This is a library with no executables, and the documentation is mostly the IEEE standard; INSTALL.md says only some platform and compiler combinations are well tested and the CMake scripts need more testing.

## Links

- [Homepage (SystemC overview)](https://systemc.org/overview/systemc/)
- [GitHub reference implementation (accellera-official/systemc)](https://github.com/accellera-official/systemc)
- [INSTALL.md (build and install notes)](https://github.com/accellera-official/systemc/blob/master/INSTALL.md)
- [IEEE Std 1666-2023 (standard)](https://ieeexplore.ieee.org/document/10246125)
