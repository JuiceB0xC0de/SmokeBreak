---
name: nextpnr-ice40
title: nextpnr-ice40
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, fpga, needs-hardware, open-source-toolchain, place-and-route, verilog]
homepage: https://github.com/YosysHQ/nextpnr
scout_score: 6
status: draft
---

# nextpnr-ice40

**TLDR;** An open-source place and route tool that turns a synthesized netlist into a configuration for Lattice iCE40 FPGAs, with a GUI that shows the layout forming.

nextpnr-ice40 is the iCE40 target of nextpnr, a place and route tool for FPGAs. Synthesis turns your hardware description into a netlist of generic logic. Place and route then decides which physical cell on the chip hosts each piece of logic and which wires connect them. This tool takes a Yosys JSON netlist, a PCF file mapping signals to physical pins, and a device flag such as `--hx1k`. It writes an ASCII `.asc` configuration file.

The rest of the open flow is handled by other tools. IceStorm's `icepack` converts the `.asc` file to a binary bitstream, and `iceprog` uploads it to a board. Internally, nextpnr runs packing, placement and routing against the iCE40 chip database from Project IceStorm. The README says it aims to be "a vendor neutral, timing driven, FOSS FPGA place and route tool", meant to stand in for vendor-specific flows.

The idea underneath is that an FPGA design is a physical layout problem, not only code. The optional GUI makes this visible: you can pack, place and route from toolbar buttons or a Python console and watch the design settle onto the chip. A recording feature saves frames that ffmpeg can stitch into a movie of the process.

iCE40 is one of several architectures sharing the same placer and router, so what you learn here carries over to other back ends.

## Install

```
brew install nextpnr-ice40
# Pulls in icestorm, boost, eigen and python as dependencies. Yosys is needed separately to synthesize designs: brew install yosys
# Running the blinky example on real hardware requires an iCEstick board. The GUI is off by default and needs a GUI build.
```

## Try this

```
nextpnr-ice40 --help
```
Lists the supported iCE40 devices and the options for input, constraints, output and the GUI.

```
yosys -p 'synth_ice40 -top blinky -json blinky.json' blinky.v
```
Synthesizes the blinky example Verilog into the JSON netlist that nextpnr reads.

```
nextpnr-ice40 --hx1k --json blinky.json --pcf blinky.pcf --asc blinky.asc
```
Places and routes the design for an HX1K chip and writes blinky.asc.

## What's unique

It is one iCE40 back end of a shared, vendor-neutral, timing-driven placer and router. It has a GUI with a Python console and a frame-capture feature for making movies of place and route.

## Caveats

Real use needs an iCE40 board such as the iCEstick plus Yosys, and the GUI is not built by default, so the visual part may need a source build.

## Links

- [nextpnr homepage (GitHub repo)](https://github.com/YosysHQ/nextpnr)
- [arXiv paper on the Yosys+nextpnr flow](https://arxiv.org/abs/1903.10407)
- [Project IceStorm (iCE40 bitstream tools)](https://github.com/YosysHQ/icestorm)
- [Yosys](https://yosyshq.net/yosys/)
