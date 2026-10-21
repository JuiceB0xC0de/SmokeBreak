---
name: vrpn
title: VRPN
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, library, needs-hardware, peripherals, protocol, vr]
homepage: https://github.com/vrpn/vrpn/wiki
scout_score: 5
status: draft
---

# VRPN

**TLDR;** A network layer that makes VR trackers, buttons and dials look identical to applications, wherever the hardware is plugged in.

VRPN, the Virtual Reality Peripheral Network, is a library plus a set of servers that put VR hardware on a network. A host PC at each VR station reads the physical devices. The application talks to them through client classes and never needs to know where the hardware sits.

The idea underneath is a class-of-service abstraction. Devices fall into a few base types: Analog, Button, Dial, ForceDevice, Imager, Sound, Text and Tracker. Every device of one type produces the same kind of report. In the project's words, "all tracking devices look like they are of the type vrpn_Tracker." Swap one tracker model for another and the application code stays the same.

When a device has special features, an application can derive a specialised class, for example to set a tracker's update rate. Other trackers simply ignore commands they do not understand. It was developed at the UNC CISMM NIH National Research Resource and has since been maintained by Sensics and then ReliaSolve. It predates most modern VR middleware, so it shows how this problem was solved before the current tooling existed.

The Homebrew formula installs a `vrpn_server` executable, the server side that reads devices and serves their reports. It is plumbing, so most of the interest is in reading how the device classes fit together.

## Install

```
brew install vrpn
# Real use needs a supported VR device (tracker, button box, etc.) and a client application or the VRPN client library.
```

## Try this

```
vrpn_server --help
```
Prints the server's usage and options, a first look at how it is configured to serve devices.

## What's unique

It predates most modern VR middleware, and its core idea is one common device class per kind of peripheral, so a single tracker class covers many different tracker models.

## Caveats

Needs VR hardware to do anything interesting, and the wiki was last edited in 2019 and admits some platforms and the debian branch are not actively maintained.

## Links

- [Project wiki (homepage)](https://github.com/vrpn/vrpn/wiki)
- [Source repository](https://github.com/vrpn/vrpn)
- [Source downloads and releases](https://github.com/vrpn/vrpn/releases)
- [Supported hardware devices](https://github.com/vrpn/vrpn/wiki/Available-hardware-devices)
