---
name: libdivecomputer
title: libdivecomputer
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bluetooth, library, needs-hardware, protocol, reverse-engineering, usb]
homepage: https://www.libdivecomputer.org/
scout_score: 7
status: draft
---

# libdivecomputer

**TLDR;** An open source C library that talks to dive computers from Shearwater, Suunto, Scubapro and many other makers over serial, USB and Bluetooth.

Libdivecomputer is a cross-platform C library for communicating with dive computers. The homepage lists vendors including Shearwater, Suunto, Scubapro, Oceanic, Mares and Uwatec. It also lists transports: serial, USB, USB HID, IrDA, Bluetooth Classic and Bluetooth Low Energy. Supported platforms include Windows, Linux, Mac, BSD, Android and iOS.

The README gives only the general purpose: a library for communication with dive computers from various manufacturers. It does not spell out a longer problem statement. A dive computer is a small, sealed device that logs depth, time and decompression data, and each maker has its own way of talking to it. A library that hides those differences behind one interface is what other diving software can build on.

That is the door it opens. Each vendor's protocol is a separate small puzzle, and a single library now speaks dozens of them across very different physical links, from old infrared to modern Bluetooth LE. The Homebrew formula also installs an executable called `dctool`. The fetched pages do not describe it, so `--help` is the place to start.

It is released under the LGPL. Bug reports and questions go to a mailing list.

## Install

```
brew install libdivecomputer
# Actually talking to a dive computer needs the device and its connection (serial, USB or Bluetooth). Without one you can still read the help output.
```

## Try this

```
dctool --help
```
Prints the usage and available subcommands of the command-line tool that ships with the library.

## What's unique

It is a rare open door into proprietary dive computer protocols, covering dozens of vendors across several transports, including Bluetooth LE, in one library.

## Caveats

Most of the fun needs a real dive computer, and the fetched pages give no release dates and no per-model support list, so how complete support is for any given device is unclear.

## Links

- [Homepage](https://www.libdivecomputer.org/)
- [GitHub repository (README)](https://github.com/libdivecomputer/libdivecomputer)
- [SourceForge project page](http://sourceforge.net/projects/libdivecomputer/)
