---
name: verilator
title: Verilator
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, c++, hardware-design, hdl, simulation, systemverilog, verilog]
homepage: https://www.veripool.org/wiki/verilator
scout_score: 6
status: draft
---

# Verilator

**TLDR;** Verilator compiles Verilog and SystemVerilog hardware designs into C++ models, so you can simulate a circuit you wrote as a fast native program.

Verilator reads hardware description language (Verilog or SystemVerilog), lints it, and compiles the design into optimized C++ or SystemC model files. You can wrap that model in your own testbench, or pass --binary and let Verilator build a standalone simulator executable. It can also insert assertion and coverage points, and it emits JSON if you want to build your own tools on top of it.

Most simulators interpret the design. Verilator does not translate HDL line by line into C++ either. It builds an optimized model that can be partitioned for multithreading, and then wraps that model in a C++ or SystemC module. Once the design is ordinary compiled code, you can link it into other programs, or into other simulators.

The homepage pitches it as "the fastest Verilog/SystemVerilog simulator" and frames open tooling as spending on compute instead of licenses. It claims roughly 100x the speed of Icarus Verilog on one thread, and 200 to 1000x with multithreading. Those are the project's own figures and the brief did not verify them.

The larger idea is that a chip design is a program you can compile, test and measure like any other. It is a way into digital logic, CPU design and hardware verification without buying a commercial tool.

## Install

```
brew install verilator
You also need a C++ compiler on your machine, since Verilator generates C++ that gets built. The brief did not show install steps, so check the project's installation page for details.
```

## Try this

```
verilator --help
```
Prints the command-line options, which are modelled on GCC and Synopsys VCS.

## What's unique

It compiles hardware designs to C++ instead of interpreting them, and it is backed by the CHIPS Alliance and Linux Foundation. Arm and RISC-V vendor IP supports it out of the box.

## Caveats

The homepage says it may not suit you if you need a full replacement for a closed-source simulator, SDF annotation, or mixed-signal simulation, and x/z handling is limited in some contexts.

## Links

- [Verilator homepage (Veripool)](https://www.veripool.org/wiki/verilator)
