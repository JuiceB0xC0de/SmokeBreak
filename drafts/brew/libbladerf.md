---
name: libbladerf
title: libbladeRF
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, fpga, library, needs-hardware, radio, sdr, usb]
homepage: https://nuand.com/
scout_score: 7
status: draft
---

# libbladeRF

**TLDR;** Host driver and command-line tools for the bladeRF USB 3.0 software defined radio, which turns a computer into a transceiver from 47 MHz to 6 GHz.

libbladeRF is the C library that lets a computer talk to a bladeRF, a USB 3.0 SuperSpeed software defined radio board from Nuand. Through it, software receives raw RF sample streams or sends samples out to be transmitted. The board covers roughly 47 MHz to 6 GHz, with 2x2 MIMO channels and sampling up to 61.44 MHz.

The Homebrew package installs the library plus four tools: bladeRF-cli for loading the FPGA, querying the device and driving it from a prompt, bladeRF-fsk, bladeRF-power and bladeRF-update. The wider repository also holds the firmware for the Cypress FX3 USB controller and the HDL for the Cyclone IV FPGA, so the whole stack from gateware to host code is open to read.

The project's stated aim is that by providing source code, thorough documentation, easy to grasp tutorials and a place for open discussion, modern radio systems will be demystified. The idea underneath is that a radio is mostly a stream of numbers. Once the antenna and converters hand you samples, modulation, demodulation and measurement become software problems you can inspect and rewrite.

Nothing here runs without the physical board. The library has nothing to talk to otherwise, so this is a door for people who own a bladeRF or are considering buying one.

## Install

```
brew install libbladerf
Requires a physical bladeRF board from Nuand. The FPGA image and FX3 firmware are separate downloads from nuand.com, and a firmware update may be needed on first use. The README points to the wiki for those steps.
```

## Try this

```
bladeRF-cli -p
```
Lists attached bladeRF devices so you can confirm the board is visible over USB.

```
bladeRF-cli -e info -e version
```
Prints device information and version details once the board is detected.

```
bladeRF-fsk --help
```
Shows the options for the CPFSK modem utility that links two bladeRFs for text chat or file transfer.

## What's unique

bladeRF-fsk is a host-software modem that turns two bladeRFs into a text chat or file transfer link at a raw 250 kbps. On a gain calibrated bladeRF 2.0 micro, bladeRF-power makes the radio work as a power meter.

## Caveats

It needs a bladeRF board that costs several hundred dollars, and unplugging the device mid firmware upgrade can leave it in the FX3 bootloader, which needs the recovery command in bladeRF-cli.

## Links

- [Nuand homepage](https://nuand.com/)
- [bladeRF source repository (GitHub)](https://github.com/Nuand/bladeRF)
- [bladeRF wiki](https://github.com/nuand/bladeRF/wiki)
