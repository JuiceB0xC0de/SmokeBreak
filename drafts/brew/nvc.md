---
name: nvc
title: nvc
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, fpga, hardware-description, llvm, simulation, vhdl]
homepage: https://www.nickg.me.uk/nvc/
scout_score: 7
status: draft
---

# nvc

**TLDR;** A free VHDL compiler and simulator that compiles hardware descriptions to native code via LLVM, so you can run digital circuits from the terminal.

VHDL is a language for describing digital hardware: gates, registers, clocks, and how signals change over time. NVC takes VHDL source files and a testbench, then simulates the circuit on your machine. It implements almost all of VHDL-2008 (IEEE 1076-2008).

It works the way a software toolchain does. You analyse the source files (`-a`), elaborate the design (`-e`), and run it (`-r`). The README compares these steps to compiling, linking and executing a program. Under the hood, NVC uses LLVM to turn the design into native machine code. The README says simulation performance is a particular emphasis, and that it has been used on several real-world designs.

The idea underneath is that hardware is concurrent: everything in a circuit happens at once, and a simulator has to fake that on a sequential CPU. Writing a small testbench and watching signals change on a clock edge is a quick way into that way of thinking. Waveforms can be opened in GTKWave or Surfer.

It is a simulator only. It does not produce anything you could program into an FPGA or ASIC. Verification libraries such as OSVVM and UVVM, and vendor libraries such as Vivado and Quartus, can be compiled in with `nvc --install`.

## Install

```
brew install nvc
# You supply your own VHDL source files and a testbench. GTKWave or Surfer is needed only to view waveforms.
```

## Try this

```
nvc --help
```
Lists the analyse, elaborate and run commands and the other options.

```
nvc -a my_design.vhd my_tb.vhd -e my_tb -r
```
Analyses your files, elaborates my_tb as the top-level testbench, and runs the simulation in one command.

```
nvc --install osvvm
```
Compiles the OSVVM verification framework libraries into ~/.nvc/lib so your testbenches can use them.

## What's unique

It is an open-source VHDL simulator that focuses on speed by compiling to native code through LLVM. It also documents support for verification frameworks (OSVVM, UVVM, VUnit, cocotb) and FPGA vendor libraries, which is unusual for a free tool.

## Caveats

It is not a synthesizer and does not support PSL; the author describes it as a spare-time project with no warranty and no expectation of support.

## Links

- [Homepage](https://www.nickg.me.uk/nvc/)
- [GitHub repository](https://github.com/nickg/nvc)
- [Online manual](https://www.nickg.me.uk/nvc/manual.html)
- [Features page (VHDL-2008 and VHDL-2019 status)](https://www.nickg.me.uk/nvc/features.html)
