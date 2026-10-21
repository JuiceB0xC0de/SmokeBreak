---
name: librtlsdr
title: librtlsdr
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, needs-hardware, radio, sdr, usb]
homepage: https://osmocom.org/projects/rtl-sdr/wiki
scout_score: 8
status: draft
---

# librtlsdr

**TLDR;** Turns a cheap Realtek RTL2832 TV-tuner USB dongle into a software-defined radio receiver, with a set of small command-line tools.

librtlsdr is the rtl-sdr project's library and toolset for Realtek RTL2832-based DVB-T USB dongles. These dongles were built to receive digital TV. The software lets them be used as general radio receivers, with the raw signal handed to your computer instead of a TV picture. The README is one line: it "turns your Realtek RTL2832 based DVB dongle into a SDR receiver."

The Homebrew formula installs eight command-line programs: rtl_adsb, rtl_biast, rtl_eeprom, rtl_fm, rtl_power, rtl_sdr, rtl_tcp and rtl_test. From the names alone, they cover things like capturing samples, FM demodulation, power scanning, serving a dongle over TCP, ADS-B, and device configuration. I could not read the project wiki, so this is inference from the names, not documentation.

The idea underneath is software-defined radio. Instead of fixed circuits for each kind of signal, hardware digitizes a slice of spectrum and software does the rest. That makes the radio world around you something you can inspect, record and decode with code, and a cheap dongle is a low-cost way to start.

## Install

```
brew install librtlsdr

Needs a Realtek RTL2832-based USB dongle plugged in to do anything useful. Depends on libusb, which Homebrew pulls in.
```

## Try this

```
rtl_test --help
```
Prints the options for the dongle test tool, a sensible first check that the tools installed.

```
rtl_fm --help
```
Shows the options for the FM receiver tool.

```
rtl_power --help
```
Shows the options for the spectrum power scanner.

## What's unique

The hardware is a cheap TV-tuner dongle repurposed as a general radio receiver. The install is a bundle of small single-purpose command-line tools, not one big program.

## Caveats

You need the dongle hardware to get anything real out of it, and the official wiki was blocked behind a JavaScript challenge when the brief was written, so the docs are unread here.

## Links

- [Project wiki](https://osmocom.org/projects/rtl-sdr/wiki)
- [GitHub repository](https://github.com/osmocom/rtl-sdr)
