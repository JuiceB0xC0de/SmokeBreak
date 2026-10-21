---
name: gpsd
title: gpsd
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, daemon, gps, needs-hardware, network, protocol, serial]
homepage: https://gpsd.gitlab.io/gpsd/
scout_score: 6
status: draft
---

# gpsd

**TLDR;** A daemon that reads GPS receivers on serial or USB and serves position, course and velocity as JSON on TCP port 2947, so many programs can share one sensor.

gpsd sits between a GPS (or AIS) receiver and the programs that want its data. It reads the raw output from receivers attached over serial or USB and makes location, course and velocity available to query on TCP port 2947. Clients exchange JSON with it, described in the gpsd_json(5) man page. The project says this is much easier to parse than the NMEA 0183 sentences most receivers emit.

The reason it exists is sharing. With gpsd, several location-aware applications can use one sensor without contention or lost data, and none of them has to write its own NMEA parser. gpsd works out the baud rate and whether the device is GPS or AIS by inspecting the data stream. The project also carries a long-running critique of GPS standards and vendors, and argues for a simpler protocol.

The idea underneath is that a satellite receiver is just a chatty serial device, and a small daemon turns it into a network service. The package ships diagnostic tools such as cgps, gpsmon, gpspipe and gpsdecode, which let you watch the stream at different levels. It also includes a C library, a C++ wrapper and a Python module. The homepage says it underlies the Android map location service and appears in drones, marine navigation and driverless-car stacks.

## Install

```
brew install gpsd
# Homebrew caveat: gpsd does not auto-detect devices. Once started, add your receiver manually:
GPSD_SOCKET="$HOMEBREW_PREFIX/var/gpsd.sock" $HOMEBREW_CELLAR/gpsd/3.27.5/sbin/gpsdctl add /dev/tty.usbserial-XYZ
# Needs a GPS or AIS receiver on serial or USB to produce any data. On Debian/Ubuntu: sudo apt-get install gpsd
```

## Try this

```
gpsd --help
```
Lists the daemon's options, including how to point it at a device.

```
gpsmon --help
```
Shows the options for the monitor that displays raw receiver data.

```
gpspipe --help
```
Shows how to stream gpsd's data to standard output, for example as JSON.

## What's unique

It turns any attached GPS receiver into a shared network service with a JSON protocol, and under Linux it runs with zero configuration. It is also very widely deployed.

## Caveats

You need a GPS or AIS receiver to see any data, macOS support is limited, and the README says flatly that Windows is not supported.

## Links

- [Project homepage](https://gpsd.gitlab.io/gpsd/)
- [GitLab repository](https://gitlab.com/gpsd/gpsd)
