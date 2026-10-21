---
name: readsb
title: readsb
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [ads-b, afternoon, aircraft, needs-hardware, network, radio, sdr]
homepage: https://github.com/wiedehopf/readsb
scout_score: 8
status: draft
---

# readsb

**TLDR;** Decodes the radio chatter aircraft broadcast about their position and identity, turning a cheap RTL-SDR dongle into a live table of planes overhead.

readsb is a Mode-S, ADS-B and TIS decoder written in C. It reads radio samples from an SDR, with rtl-sdr as the main path, or takes Beast, SBS or raw messages over the network. It can show a live terminal table of aircraft with `--interactive`, write periodic aircraft.json files, and serve TCP feeds in Beast, SBS, raw, JSON, VRS and ASTERIX formats. An optional HTTP API and recorded traces and heatmaps are also available.

It is a fork of Mictronics readsb, which itself came from dump1090-fa, with a lineage back to antirez's original dump1090. The README says one of its main uses is as the backend of a global aircraft map. It feeds tar1090-style web maps and aggregators, which is where much of the community-run flight tracking you see online comes from.

The idea underneath is that aircraft constantly announce themselves in the clear on 1090 MHz, and anyone with a receiver can decode it. The README mentions an autogain algorithm tuned for ADS-B (`--gain=auto`) and a position-speed check that flags positions as reliable or jumping. It also has a BeastReduce output that forwards fewer messages to save bandwidth for aggregators.

You do not strictly need a dongle. With `--net-only` it can take a feed from another receiver and act as a decoder and relay.

## Install

```
brew install readsb
# Needs an RTL-SDR dongle and a 1090 MHz antenna for live reception. Without one, use --net-only with a --net-connector to another feed. The tar1090 web map is a separate install.
```

## Try this

```
readsb --help
```
Lists the supported device types, network outputs and gain options.

```
./readsb --quiet --net --device-type rtlsdr --gain auto
```
The README's quick-start: reads from an rtl-sdr dongle with automatic gain and networking enabled.

```
readsb --interactive --net --device-type rtlsdr --gain auto
```
Adds a live console table of the planes your receiver is hearing, as the README suggests for a quick test.

## What's unique

It is the decoder behind several public global aircraft maps and aggregators, with a BeastReduce output that cuts bandwidth for aggregators. It also emulates the Kinetic SBS-3 binary protocol, so BaseStation-style software can connect to it directly.

## Caveats

The README says it is continually under development and to "expect bugs, segfaults and all the good stuff"; the --help text may be out of date, the trace format is subject to change, and the macOS install script for the web map does not work.

## Links

- [readsb GitHub repository](https://github.com/wiedehopf/readsb)
- [tar1090 web interface](https://github.com/wiedehopf/tar1090)
- [Automatic installation for readsb (adsb-scripts wiki)](https://github.com/wiedehopf/adsb-scripts/wiki/Automatic-installation-for-readsb)
- [Homebrew formula for readsb](https://formulae.brew.sh/formula/readsb)
