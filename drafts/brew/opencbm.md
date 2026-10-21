---
name: opencbm
title: OpenCBM
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, commodore, floppy, iec-bus, needs-hardware, retro, usb]
homepage: https://spiro.trikaliotis.net/opencbm
scout_score: 7
status: draft
---

# OpenCBM

**TLDR;** Command-line tools and a driver that let a modern PC talk to real Commodore 1541 floppy drives over the IEC serial bus.

OpenCBM is a driver, a development library and a set of command-line tools for controlling Commodore 8-bit disk drives such as the VIC-1541. The PC connects through a homemade or bought cable, either on a parallel port (XM1541 or XA1541) or over USB (XU1541 or XUM1541, also sold as ZoomFloppy). Tools such as cbmctrl, cbmcopy, d64copy and cbmformat then read and write files, D64 disk images and drive status. It also includes imgcopy, a fast disk copier, and supports the VIC-1530/1531 tape units through ZoomTape.

The author's reason for it: the Commodore serial bus protocol is proprietary and not natively supported by modern hardware or software. In the project's words, "OpenCBM provides an interface to this so-called IEC bus at the level of simple TALK and LISTEN commands, similar to the one provided by the Commodore kernel routines." Lower-level bus control is available too, so the PC can act as a controller for the drive.

The idea underneath is that a 1980s disk drive is a small computer on a shared serial bus, and your PC can join that bus and talk to it. The homepage FAQ goes into how this works. Parallel-port cables need the drive's DATA line to raise a parallel-port interrupt, so the driver can answer CLK without busy-waiting the whole CPU. That is why the XM1541 cable swaps the RESET and DATA lines relative to the XE1541 design. It is a good case study in bit-banging a slow protocol with tight timing.

OpenCBM is the Windows port (cbm4win) and successor to cbm4linux. Each cable is driven by a plugin chosen in opencbm.conf or with the -@ adapter option.

## Install

```
brew install opencbm
# Requires real hardware: a Commodore drive (e.g. a 1541) and a supported cable (parallel XM1541/XA1541, or a USB XUM1541/ZoomFloppy). Adapters are selected via /etc/opencbm.conf or the -@ option.
```

## Try this

```
cbmctrl --help
```
Lists the parameters and subcommands for cbmctrl, the low-level tool for sending commands to the drive.

```
d64copy --help
```
Shows the options for copying a disk to or from a D64 image.

```
cbmcopy --help
```
Shows the options for copying individual files to and from a drive.

## What's unique

It talks to real 1541-era drives and exposes the IEC bus at the level of TALK and LISTEN commands, rather than just emulating a disk. It has moved from parallel cables to USB adapters over the years.

## Caveats

Nothing happens without a real drive and a supported cable, the last release the brief shows is an RC from January 2022, and building from source on Linux can be fiddly.

## Links

- [Homepage (Spiro Trikaliotis, OpenCBM section)](https://spiro.trikaliotis.net/opencbm)
- [GitHub repository (README)](https://github.com/OpenCBM/OpenCBM)
- [Online manual and installation instructions](http://opencbm.trikaliotis.net/)
- [Bug tracker](https://github.com/OpenCBM/OpenCBM/issues)
