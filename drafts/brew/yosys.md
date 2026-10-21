---
name: yosys
title: Yosys
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, formal-methods, fpga, hardware, synthesis, verilog]
homepage: https://yosyshq.net/yosys/
scout_score: 7
status: draft
---

# Yosys

**TLDR;** Yosys turns Verilog hardware descriptions into gate-level netlists through a chain of scriptable passes, so you can watch a circuit get synthesized step by step.

Yosys is a framework for Verilog RTL synthesis. You give it a hardware description written in Verilog-2005 (the README also mentions an informally defined synthesizable subset of SystemVerilog) and it works down to a netlist of logic gates and flip-flops. It can target ASIC standard cell libraries in Liberty format, or Xilinx 7-Series, Lattice iCE40 and ECP5 FPGAs. It can also write BLIF, EDIF, BTOR, SMT-LIB or plain RTL Verilog.

You drive it from an interactive shell or from a synthesis script, chaining named passes. A typical flow reads the Verilog, picks a top module with hierarchy, uses proc and opt to turn always blocks into netlist elements, maps to an internal cell library with techmap, then hands flip-flops and combinational logic to dfflibmap and abc before writing the result back out. The synth command bundles a sensible default script that you can build on.

The idea underneath is that synthesis is not a black box. It is a pipeline of small, inspectable transformations, and you can stop after any pass to see what the design looks like. The homepage says Yosys "can be adapted to perform any synthesis job by combining the existing passes (algorithms) using synthesis scripts and adding additional passes as needed by extending the Yosys C++ code base."

It also has built-in formal methods for property and equivalence checking, and it serves as the synthesis backend for other formal tools such as sby and mcy. That makes it a door into both digital design and formal verification.

## Install

```
brew install yosys
```

## Try this

```
yosys --help
```
Lists the command-line options of the binary.

```
read_verilog mydesign.v
```
Typed inside the yosys shell, this loads your Verilog source into the design.

```
synth -top mytop
```
Runs the default generic synthesis script with mytop as the top module; help synth explains each step.

## What's unique

It is a scriptable pipeline of named passes rather than a fixed tool, extensible in C++, with formal checking built in. It also underpins other open-source formal tools.

## Caveats

read_verilog does no syntax checking (the README suggests linting with Verilator first), and SystemVerilog support covers only a synthesizable subset.

## Links

- [Yosys homepage](https://yosyshq.net/yosys/)
- [Yosys GitHub repository](https://github.com/YosysHQ/yosys)
- [Yosys documentation (Read the Docs)](https://yosyshq.readthedocs.io/projects/yosys)
