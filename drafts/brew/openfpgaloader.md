---
name: openfpgaloader
title: openFPGALoader
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bitstream, fpga, jtag, needs-hardware, usb]
homepage: https://trabucayre.github.io/openFPGALoader/
scout_score: 6
status: draft
---

# openFPGALoader

**TLDR;** One command-line tool that loads bitstreams onto FPGAs from many vendors, replacing a drawer of vendor-specific programmers.

An FPGA is a chip whose logic is rewired by a file called a bitstream. Loading that file normally means installing a different vendor tool for each chip family and each programming cable. openFPGALoader is a single utility that does the loading for FPGAs from Xilinx, Altera/Intel, Lattice, Gowin, Efinix, Anlogic and Cologne Chip, over many boards and USB cables.

The grammar is small. You give it a bitstream and either a board name with -b or a JTAG cable model with -c. By default the design goes into the FPGA's SRAM, so it vanishes at power-off. With -f it is written to the attached flash instead and survives power cycles.

The interesting trick is spiOverJtag. On some boards the flash chip is only reachable through the FPGA itself. The tool first loads a small helper bitstream that bridges JTAG to the SPI flash, and then writes the flash through that bridge. The FPGA temporarily becomes the programmer for its own memory.

Under the hood it picks a driver for the cable (FTDI MPSSE, CMSIS-DAP, USB-Blaster, Xilinx cables and others) and a parser for the bitstream format. The README says it runs on Linux, Windows, macOS and OpenBSD.

## Install

```
brew install openfpgaloader
Needs an FPGA board or a JTAG cable to do anything real. On Linux, USB access may need the udev rules file (70-openfpgaloader.rules) and plugdev/dialout group membership, according to the release notes.
```

## Try this

```
openFPGALoader --help
```
Prints the full list of options, including the supported cables and board selection flags.

```
openFPGALoader -b arty arty_bitstream.bit
```
Loads the bitstream into the SRAM of an Arty board. The design runs until power is removed.

```
openFPGALoader -b arty -f arty_bitstream.bit
```
Writes the same bitstream into the board's flash so it persists across power cycles.

## What's unique

One command-line grammar covers many vendors, boards and cables. The spiOverJtag helper bitstream lets it reach flash chips that have no direct programming path.

## Caveats

It is only useful with real hardware, and support depends on your exact board, cable and FPGA, so check the compatibility list before buying anything.

## Links

- [Documentation homepage](https://trabucayre.github.io/openFPGALoader/)
- [GitHub repository](https://github.com/trabucayre/openFPGALoader)
- [Board compatibility list](https://trabucayre.github.io/openFPGALoader/compatibility/board.html)
- [First steps guide](https://trabucayre.github.io/openFPGALoader/guide/first-steps.html)
- [Releases](https://github.com/trabucayre/openFPGALoader/releases)
