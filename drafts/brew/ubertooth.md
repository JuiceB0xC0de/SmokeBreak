---
name: ubertooth
title: Ubertooth
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [2.4ghz, afternoon, ble, bluetooth, needs-hardware, radio, sniffer, wireshark]
homepage: https://greatscottgadgets.com/ubertoothone/
scout_score: 8
status: draft
---

# Ubertooth

**TLDR;** Host tools for the Ubertooth One, an open 2.4 GHz board that sniffs Bluetooth LE traffic and feeds it into Wireshark.

Project Ubertooth is an open source wireless development platform aimed at Bluetooth experimentation. The hardware is the Ubertooth One, a small board with a 2.4 GHz dipole antenna on an RP-SMA connector. The Homebrew formula installs the computer-side tools that talk to it, including ubertooth-btle, ubertooth-btbr, ubertooth-rx and ubertooth-specan.

Its main job is as a BLE (Bluetooth Smart) sniffer. The README also says it can capture some data from Basic Rate Bluetooth Classic connections, and it is plain that the Classic support is partial. The docs mention capturing traffic into Wireshark, so you can read what nearby devices say to each other with a familiar packet viewer.

The idea underneath is that Bluetooth is not magic. It is a protocol hopping across 2.4 GHz channels, and with an open board and open tools you can watch it happen. The tool list also includes a spectrum analyzer (ubertooth-specan) and a firmware updater (ubertooth-dfu). Together they show the air around you, not just the packets. The brief does not cover what each tool outputs, so the tool docs are the place to learn that.

## Install

```
brew install ubertooth
# Needs a physical Ubertooth One board. Firmware must be flashed (see the readthedocs firmware page).
# The README says libbtbb must be built from its 2020-12-R1 release, paired with the 2020-12-R1 Ubertooth release. See the readthedocs build_guide page.
```

## Try this

```
ubertooth-btle --help
```
Lists the options for the BLE sniffer, the tool most people start with.

```
ubertooth-util --help
```
Shows the utility commands for talking to the board itself.

```
ubertooth-specan --help
```
Shows the options for the spectrum analyzer tool.

## What's unique

It is a cheap, open 2.4 GHz board that turns a desk into a BLE sniffing station with Wireshark output, with source for both the hardware and the host tools.

## Caveats

The Ubertooth One is retired and Great Scott Gadgets has no plan to make more, so you need a used board. Classic Bluetooth capture is partial, the latest release is 2020-12-R1, and setup depends on building and flashing from separate docs pages.

## Links

- [Homepage (Ubertooth One product page)](https://greatscottgadgets.com/ubertoothone/)
- [GitHub repository (README)](https://github.com/greatscottgadgets/ubertooth)
- [Documentation on Read the Docs](https://ubertooth.readthedocs.io/en/latest/)
