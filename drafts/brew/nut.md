---
name: nut
title: NUT (Network UPS Tools)
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, needs-hardware, network, power, protocol, serial, ups, usb]
homepage: https://networkupstools.org/
scout_score: 5
status: draft
---

# NUT (Network UPS Tools)

**TLDR;** One naming scheme and one network protocol for talking to hundreds of brands of UPS, PDU and solar controller, with drivers for serial and USB.

Network UPS Tools is a suite of programs for monitoring and managing power hardware: uninterruptible power supplies, power distribution units, automatic transfer switches, power supply units and solar controllers. The ninety or so executables Homebrew installs fall into a split: per-device drivers, a network server called `upsd`, and client tools such as `upsc` and `upsmon`.

The drivers do the hard part. Each one talks to a specific family of hardware over serial, USB or another medium and maps what it finds onto NUT's standard variable names. The project describes its aim as providing "a common protocol and set of tools to monitor and manage such devices, and to consistently name equivalent features and data points, across a vast range of vendor-specific protocols and connection media types." `upsd` then serves that data over TCP, and `upsmon` can watch it and trigger a shutdown when the battery runs low. `upssched` handles scheduled actions.

The idea underneath is a translation layer. Every vendor invented its own wire protocol, and NUT squeezes them into one vocabulary. The protocol is registered on port 3493 and was published by the IETF as RFC 9271, the "UPS management protocol", in 2022. It is an informational RFC, not an Internet Standard. Reading how a dozen incompatible protocols get flattened into one is a good way into the practical side of power, serial links and device drivers.

## Install

```
brew install nut
# Real use needs a UPS or other power device, plus the matching driver and cable. The manual has a cable-reference appendix for specific models.
```

## Try this

```
upsc --help
```
Shows how to query a NUT server for the variables a device publishes.

```
upsd --help
```
Shows the options of the network server that publishes device data to clients.

```
upsdrvctl --help
```
Shows the control tool that starts and stops the drivers.

## What's unique

It claims support for at least 201 manufacturers and 1441 device models under one naming scheme, far wider than most UPS tools. Its management protocol has an IETF RFC.

## Caveats

It is only really interesting with power hardware attached, and the homepage notes errata, including a 2025 usbhid-ups bug that could break default shutdown; the Windows port still needs community work.

## Links

- [NUT homepage](https://networkupstools.org/)
- [NUT User Manual (chunked HTML)](https://networkupstools.org/docs/user-manual.chunked/index.html)
- [NUT GitHub repository](https://github.com/networkupstools/nut/)
