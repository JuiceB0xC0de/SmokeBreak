---
name: openhmd
title: OpenHMD
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, c-library, needs-hardware, reverse-engineering, usb-hid, vr]
homepage: http://openhmd.net
scout_score: 5
status: draft
---

# OpenHMD

**TLDR;** An open C library with reverse-engineered drivers that reads head tracking from many competing VR headsets through one API. Unmaintained, but a clear look at USB HID hardware.

OpenHMD is a C library that lets an application ask for head tracking and related data from VR headsets and some controllers. It covers devices such as the Oculus Rift, HTC Vive, PlayStation VR and Windows Mixed Reality. Raw USB HID reports come in from the hardware, and a single cross-platform API goes out: enumerate devices, open one, read from it.

The project exists because each vendor shipped its own SDK. The homepage states the aim as "a Free and Open Source API and drivers for immersive technology", supporting as many devices as possible in a portable package. Each device driver is the product of reverse engineering, hacking and testing, and the project's blog describes support arriving through hackathons. Drivers talk over HIDAPI (hidraw on Linux), and you pick which ones to compile in at build time.

The idea underneath is that a headset is mostly a stream of sensor packets. Once someone works out the report format, you can turn those bytes into orientation. There is also an External Sensor driver, so you can feed in your own sensor data and still use OpenHMD's sensor fusion. It is licensed under the Boost Software License so it can be linked into both free and proprietary software.

The project is old and marked unmaintained, with driver work having largely moved to Monado. The code is still a readable example of how a device family gets pulled out of vendor lock-in.

## Install

```
brew install openhmd
# Needs a supported VR headset or controller to show real data.
# On Linux, add a udev rule so USB devices open without root, then replug the device. The README links a wiki list of rules.
```

## Try this

```
simple --help
```
Runs the bundled example executable's help, a starting point for reading from a connected device.

```
meson configure ./build -Ddrivers=...
```
When building from source, selects which drivers to compile, using a comma-separated list such as rift, vive, psvr, wmr, external.

## What's unique

It is one open C API shared by reverse-engineered drivers for many rival headsets, rather than one vendor's SDK. The permissive Boost license lets proprietary software link it.

## Caveats

The README says it is not actively maintained, the last release (v0.3.0) is from July 2019, and you need compatible hardware to see anything.

## Links

- [Homepage](http://openhmd.net)
- [GitHub repository](https://github.com/OpenHMD/OpenHMD)
- [Supported devices (GitHub wiki)](https://github.com/OpenHMD/OpenHMD/wiki/Support-List)
- [API reference (Doxygen)](http://openhmd.net/doxygen/0.1.0/openhmd_8h.html)
- [Monado (successor project)](https://monado.freedesktop.org/)
