---
name: minipro
title: minipro
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, eeprom, firmware, needs-hardware, reverse-engineering, usb]
homepage: https://gitlab.com/DavidGriffith/minipro/
scout_score: 8
status: draft
---

# minipro

**TLDR;** A command-line driver for the cheap TL866 and T48/T56 chip programmers, for reading and writing AVRs, PICs, BIOS chips and EEPROMs from Linux or macOS.

minipro controls XGecu's MiniPRO chip programmers, the small USB boxes with a ZIF socket that you drop a chip into to read or flash it. The README lists the TL866CS, TL866A, TL866II+, T48 and T56, and claims support for more than 13000 target devices, including AVRs, PICs, BIOS chips and EEPROMs.

The project exists because, in the README's words, "XGecu does not provide a program for use on Linux or other flavors of Unix." The maintainers wanted "a simple, free, and open-source program that presents a command-line interface that allows for a GUI front-end if desired." You name the chip with -p and give a file to write with -w or read into with -r.

The idea underneath is that a chip is just a file you have not read yet. Dump an old EEPROM or a microcontroller's flash and you have bytes you can inspect, diff, patch and write back. That makes this a door into firmware archaeology, repairing old hardware, and reverse engineering, with the programmer as the physical bridge.

The T56 adds a wrinkle. It does not keep its FPGA bitstreams in the hardware, so the host software must load them. The project cannot redistribute them, so a build step downloads XGecu's official package and converts the algorithms into one file for minipro.

## Install

```
brew install minipro

Requires a supported XGecu programmer (TL866CS, TL866A, TL866II+, T48 or T56) and libusb. On Linux, the README suggests installing the udev rules (sudo cp udev/*.rules /etc/udev/rules.d/, then sudo udevadm trigger) and adding your user to the plugdev group so you do not need root. T56 users also need to run make algorithm and sudo make install-algorithm from a source checkout.
```

## Try this

```
minipro --help
```
Lists the options for selecting a device and for reading, writing and other operations.

```
minipro -p ATMEGA48 -r atmega48.bin
```
Reads (dumps) the contents of an ATMEGA48 in the programmer's socket into atmega48.bin.

```
minipro -p ATMEGA48 -w atmega48.bin
```
Writes atmega48.bin to the ATMEGA48 in the socket.

## What's unique

It is an open, scriptable command-line replacement for a vendor tool that has no Unix version, covering thousands of chips. Its build also fetches the T56's FPGA bitstreams from the vendor because they cannot be redistributed.

## Caveats

Needs a physical programmer, and writing can overwrite a chip's contents. Tested only on Linux and macOS, and the README does not make the project's recent activity clear.

## Links

- [Project homepage (GitLab)](https://gitlab.com/DavidGriffith/minipro/)
- [XGecu (hardware vendor)](http://www.xgecu.com/en/)
- [FreeBSD ports entry for minipro](https://github.com/freebsd/freebsd-ports/tree/main/sysutils/minipro)
