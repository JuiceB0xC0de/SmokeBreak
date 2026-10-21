---
name: hackrf
title: HackRF
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, needs-hardware, open-hardware, radio, sdr, usb]
homepage: https://greatscottgadgets.com/hackrf/
scout_score: 8
status: draft
---

# HackRF

**TLDR;** Command-line tools for HackRF, an open-source software-defined radio board that lets your computer transmit and receive across a wide slice of the radio spectrum.

HackRF is a low-cost, open-source software-defined radio (SDR) platform. The board connects to a computer over USB, and the signal processing happens in software on the host rather than in fixed radio circuitry. The Homebrew formula installs the host-side tools, which come as nine small single-purpose programs instead of one big application.

The names hint at the split. `hackrf_info` is the obvious first call for identifying a connected board. `hackrf_sweep` and `hackrf_transfer` suggest scanning across frequencies and moving raw samples to or from the radio. Others, such as `hackrf_spiflash`, `hackrf_cpldjtag`, `hackrf_clock`, `hackrf_biast` and `hackrf_operacake`, point at firmware, the board's programmable logic, clocking, antenna power and an add-on switch board. The README does not describe what each tool takes in or puts out, so check each one's `--help`.

The idea underneath is that a radio becomes a program. Once a receiver is a stream of samples on your computer, tuning, demodulating and decoding are code you can read and change. The project describes itself as "a low cost, open source Software Defined Radio platform," and the hardware designs, firmware, host software and docs all live in one GPL-2.0 repository, so you can follow the signal from the antenna down to the schematics.

## Install

```
brew install hackrf
# Needs the physical board (HackRF One or HackRF Pro, sold via the Great Scott Gadgets site). The software installs without it, but does nothing useful.
```

## Try this

```
hackrf_info
```
Queries a connected HackRF board and reports on it. The brief does not show its output, so treat this as the first check that the board is found.

```
hackrf_sweep --help
```
Lists the options for the sweeping tool, which scans across frequency ranges.

```
hackrf_transfer --help
```
Lists the options for the tool that moves raw samples to and from the radio.

## What's unique

Hardware designs, firmware, host code and docs all sit in one open repository, and the board is sold as an inexpensive product. The software is split into small single-purpose tools.

## Caveats

Needs purchased hardware to do anything useful, and support is limited: only issues labelled "technical support" carry a stated two-week response target.

## Links

- [Homepage (Great Scott Gadgets HackRF product page)](https://greatscottgadgets.com/hackrf/)
- [GitHub repository (README, source, hardware designs)](https://github.com/greatscottgadgets/hackrf)
