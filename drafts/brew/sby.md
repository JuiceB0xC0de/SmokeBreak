---
name: sby
title: SymbiYosys (sby)
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, formal-verification, hardware, proofs, verilog, yosys]
homepage: https://symbiyosys.readthedocs.io/en/latest/
scout_score: 5
status: draft
---

# SymbiYosys (sby)

**TLDR;** A driver for formal hardware verification: describe a circuit's properties in one file and sby either proves them or hands back a waveform showing how they break.

SymbiYosys, run as `sby`, is a front-end for Yosys-based formal verification flows. You write a `.sby` file with sections for tasks, options, engines, script and files. sby runs the Yosys steps in the script section (for example `read -formal`, `hierarchy -check`, `prep`) and passes the result to a solver engine such as smtbmc with boolector. Each task ends in PASS or FAIL.

The idea underneath is that testing and proving are different things. A simulation shows that a circuit behaved on the inputs you tried. Formal verification asks a solver whether any input sequence can violate an assertion. sby supports bounded and unbounded checks of safety properties, liveness properties, and cover statements, which ask the solver to find a way to reach a state you care about and generate a test bench from it.

When a check fails, the output is concrete. The engine writes a counterexample trace as a VCD waveform, a standalone Verilog testbench, and a constraints file. The docs teach this with a worked FIFO example that includes a deliberately broken variant, so you see a failure and read the trace as part of the lesson.

A single `.sby` file can hold several named tasks, such as a bounded check, a check meant to fail, and a cover run, each with its own engine and script steps.

## Install

```
brew install sby
# The README recommends the OSS CAD Suite binary bundle instead, since it includes all supported solvers: https://github.com/YosysHQ/oss-cad-suite-build
# The tutorial also assumes boolector is installed, and suggests GTKWave to view waveforms. No hardware or account is needed.
```

## Try this

```
sby fifo.sby
```
Runs the default tasks (basic and cover) on the tutorial FIFO design. Both should pass; if not, the docs suspect the installation or a solver.

```
sby -f fifo.sby nofullskip
```
Runs the task that is meant to fail, overwriting the previous output directory, and writes a counterexample trace.

```
gtkwave fifo_nofullskip/engine_0/trace.vcd noskip.gtkw
```
Opens the failing trace in GTKWave with the tutorial's save file so you can see how the property broke.

## What's unique

One declarative file drives bounded checks, deliberately failing checks, and cover runs, and every failure comes back as a waveform and a testbench. The documentation teaches through a broken design on purpose.

## Caveats

Full SystemVerilog Assertion support and the industry-grade SystemVerilog and VHDL parsers need the commercial Tabby CAD Suite evaluation license, and the homepage given is the older docs domain, with the current guide at yosyshq.readthedocs.io.

## Links

- [Documentation homepage](https://symbiyosys.readthedocs.io/en/latest/)
- [Getting started tutorial (FIFO example)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html)
- [GitHub repository](https://github.com/YosysHQ/sby)
- [OSS CAD Suite build](https://github.com/YosysHQ/oss-cad-suite-build)
