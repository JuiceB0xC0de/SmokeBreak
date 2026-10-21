---
name: icestorm
title: IceStorm
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, bitstream, fpga, needs-hardware, reverse-engineering]
homepage: https://prjicestorm.readthedocs.io
scout_score: 8
status: draft
---

# IceStorm

**TLDR;** Open-source tools and documentation for the Lattice iCE40 FPGA bitstream format, letting you pack, unpack and inspect the file that configures the chip.

An FPGA is a chip whose wiring is set by a file called a bitstream. Normally that format is secret and you must use the vendor's closed toolchain. Project IceStorm documents the bitstream format of the Lattice iCE40 family and provides small command-line tools for analyzing and creating those files. In its own words, it "aims at documenting the bitstream format of Lattice iCE40 FPGAs and providing simple tools for analyzing and creating bitstream files."

The docs describe the chip tile by tile: logic tiles, IO tiles, RAM tiles, and on the UltraPlus parts the DSP tiles, SPRAM and RGB LED driver. They also cover the bitstream file layout, how configuration RAM and block RAM are organized, and the CRC checks. The tools are built on that reverse-engineered knowledge. Some convert between text and binary forms (icepack, iceunpack), some report on timing or PLL settings (icetime, icepll), and iceprog uploads a binary to a board over USB.

The larger idea is that a chip's configuration can be read as an ordinary file format. Together with Yosys and nextpnr, IceStorm forms a fully open-source flow from hardware description to a running FPGA. That makes it a good door into how FPGAs work inside, with no vendor software involved.

## Install

```
brew install icestorm
You need an iCE40 board with an FTDI USB interface to program a chip with iceprog. The docs have separate pages on installing the FTDI library and on macOS notes. Yosys and nextpnr are separate tools for the rest of the flow.
```

## Try this

```
icepack --help
```
Prints usage for the tool that converts between the text and binary bitstream forms.

```
icetime --help
```
Shows the options for the timing analysis tool.

```
iceprog example.bin
```
Programs a binary file to a connected iCE40 board over USB. This needs hardware and fails if no FTDI device is found.

## What's unique

The iCE40 bitstream format was documented by reading the chip, and these tools are the working result. It is a key piece of a fully open-source FPGA flow.

## Caveats

Most useful with an iCE40 board; the brief could not confirm maintenance status, and the docs list FTDI driver and build errors as common troubles.

## Links

- [Project IceStorm documentation](https://prjicestorm.readthedocs.io)
- [GitHub repository (YosysHQ/icestorm)](https://github.com/YosysHQ/icestorm)
