---
name: dump1090-fa
title: dump1090-fa
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [adsb, afternoon, aircraft, needs-hardware, radio, sdr]
homepage: https://github.com/flightaware/dump1090
scout_score: 8
status: draft
---

# dump1090-fa

**TLDR;** Decodes the transponder messages airplanes broadcast overhead, turning a cheap SDR dongle into a live aircraft display in a terminal or browser map.

dump1090-fa is an ADS-B, Mode S, and Mode 3A/3C demodulator and decoder from FlightAware. It takes raw radio samples from a software defined radio plugged into your machine, or aircraft data arriving over a network connection, and decodes the transponder messages. The result is a list of nearby aircraft in a terminal, or a map in a browser.

The idea underneath is that aircraft announce who they are and where they are, unencrypted, on a known frequency, and anyone with an antenna can listen. Nothing is hacked here. The tool is a door into how radio samples become bits, how bits become position reports, and how a pile of hobbyist receivers can add up to a global tracking network.

It is the FlightAware ground station component and the successor to dump1090-mutability. Paired with PiAware, it can also send what your antenna hears to FlightAware as crowd-sourced data. You can use it purely locally, too.

There is a neat trick inside. It uses starch to build several versions of the DSP code and picks the fastest one your hardware supports at runtime. Priority lists called wisdom files control the choice, with defaults compiled in for x86, ARM 32-bit, and ARM 64-bit. You can also generate your own with a benchmark run.

## Install

```
brew install dump1090-fa
# Needs an SDR (RTL-SDR, bladeRF, HackRF, LimeSDR, or a SoapySDR device) and an antenna, or a network feed of aircraft data.
```

## Try this

```
dump1090-fa --version
```
Shows which DSP implementations were chosen for your hardware.

```
dump1090 --help
```
Lists the available options for receiving and displaying aircraft.

```
view1090 --help
```
Lists the options for the terminal viewer, which shows aircraft from a network feed.

## What's unique

It benchmarks its own DSP code and selects the fastest implementation for the hardware via wisdom files. It also covers both ends of the hobby: a local display and optional upload to a crowd-sourced network through PiAware.

## Caveats

You need SDR hardware or a network feed to see anything, packaging is aimed at Debian and Raspbian, and the README gives no usage examples for the viewer or map.

## Links

- [GitHub repository (homepage)](https://github.com/flightaware/dump1090)
- [PiAware (crowd-sourced feeding)](http://flightaware.com/adsb/piaware)
- [starch (DSP implementation selector)](https://github.com/flightaware/starch)
