---
name: prjtrellis
title: Project Trellis
source: brew
category: take-things-apart
commitment: days-off
tags: [bitstream, days-off, fpga, needs-hardware, reverse-engineering, yosys]
homepage: https://github.com/YosysHQ/prjtrellis
scout_score: 7
status: draft
---

# Project Trellis

**TLDR;** Open documentation and tools for the bitstream format of Lattice ECP5 FPGAs, reverse-engineered by correlating thousands of vendor-generated designs.

Project Trellis documents how a Lattice ECP5 FPGA is configured: which bits in the bitstream turn on which routing, logic and tile features. It ships a device database, a C++ library called libtrellis (with Python bindings via pybind11) that reads and writes bitstreams and tiles, and a handful of command-line tools. In an open flow it sits between Yosys, which synthesises Verilog, and nextpnr, which does place and route.

The interesting part is how the format was learned. The README describes a black-box process: Lattice's proprietary Diamond tool is asked to generate a large number of small designs, and the resulting bitstreams are cross-correlated to work out what each bit does. The scripts that drive this are called fuzzers, borrowing the name from software testing. The finished database can be downloaded precompiled (prjtrellis-db), or rebuilt from scratch, which the README says takes several hours.

The idea underneath is that a closed chip can be documented from the outside, by changing one thing at a time and watching what changes in the output. It follows Project X-Ray, which does the same for Xilinx Series 7 devices, and the README credits the TinyFPGA project for the original inspiration.

The brew formula installs five executables: ecpbram, ecpmulti, ecppack, ecppll and ecpunpack. The README does not describe them individually, so check each one's `--help` to see what it does.

## Install

```
brew install prjtrellis
# Pulls in boost, boost-python3 and python. To go beyond reading the tools' help you need Yosys and nextpnr (with the ECP5 architecture enabled), and an ECP5 board plus OpenOCD to program one.
```

## Try this

```
ecppack --help
```
Prints the options of ecppack, one of the five installed tools.

```
ecpunpack --help
```
Shows the usage of ecpunpack, another tool in the set.

```
ecppll --help
```
Lists the options of ecppll, a further tool from the install.

## What's unique

It documents a closed chip's configuration purely from the outside, by fuzzing the vendor tool and correlating bitstreams. It is a sibling of Project X-Ray, which does this for Xilinx parts.

## Caveats

The README looks dated (it mentions Ubuntu 16.04 and 17.10), current maintenance is unconfirmed, and regenerating the database needs proprietary Lattice Diamond and several hours.

## Links

- [Project Trellis homepage (GitHub)](https://github.com/YosysHQ/prjtrellis)
- [prjtrellis-db (compiled device database)](https://github.com/YosysHQ/prjtrellis-db)
- [Project Trellis ReadTheDocs documentation](http://prjtrellis.readthedocs.io/en/latest/)
