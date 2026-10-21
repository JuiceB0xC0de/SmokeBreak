---
name: cahute
title: Cahute
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, calculators, library, needs-hardware, reverse-engineering, serial, usb]
homepage: https://cahute.org/
scout_score: 7
status: draft
---

# Cahute

**TLDR;** A C library and command-line tools for talking to Casio calculators over serial and USB, covering about three decades of hardware and wire protocols.

Cahute is a library plus a small set of utilities for talking to CASIO calculators from the 1990s to today. The tools move files to and from calculator storage (`p7`), capture and stream the calculator screen to the host (`p7screen`), and flash the ROM on fx-9860G and compatible models (`p7os`). The package also installs `xfer9860`. The library can convert the calculators' text encoding and read and write their file formats.

The interesting part is the range. The homepage documents the link protocols by calculator generation: CASIOLINK, CAS40, CAS50, CAS100, CAS300, and Protocol 7.00 for models after the fx-9860G. It also covers a USB Mass Storage transport. The project's own line is that it can "extract programs from all CASIO calculators since 1991, over USB and serial links."

It builds on earlier reverse-engineering work, and the homepage credits CaS, Caspro, Casetta, fxReverse, xfer9860, UsbConnector and the Cemetech Prizm Wiki. The docs site is a full documentation set, with a Windows USB drivers page and a guide to capturing USB traffic in Wireshark. That makes it a way into how small devices speak to a host, and how people recover those protocols from the outside.

## Install

```
brew install cahute
# Needs a supported CASIO calculator and a serial or USB link to do anything useful. Dependencies libusb and sdl2-compat are pulled in by brew.
```

## Try this

```
p7 --help
```
Lists the options for transferring files to and from an fx-9860G compatible calculator.

```
p7screen --help
```
Shows how to capture or stream the calculator screen to your computer.

```
p7os --help
```
Shows the options for the ROM flashing tool. Read them before pointing it at a real device.

## What's unique

It is an open reimplementation that spans CAS40 through Protocol 7.00, and it documents the wire protocols in detail. Most similar tools cover only one protocol generation.

## Caveats

Without a Casio calculator and a cable you can only read the docs; officially supported platforms are Arch Linux and macOS, with Debian, Windows and others still in progress.

## Links

- [Cahute homepage and documentation](https://cahute.org/)
