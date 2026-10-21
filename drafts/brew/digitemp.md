---
name: digitemp
title: DigiTemp
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [1-wire, afternoon, needs-hardware, protocol, sensors, serial, usb]
homepage: https://www.digitemp.com/
scout_score: 7
status: draft
---

# DigiTemp

**TLDR;** Reads Dallas/Maxim 1-Wire temperature sensors from the command line, a hands-on way into a bus where many sensors share one wire.

DigiTemp is a command-line program for Unix-like systems that reads values from Dallas/Maxim 1-Wire devices attached through a serial or USB adapter. Its main job is temperature: DS18S20, DS1820, DS18B20 and DS1822 sensors. The homepage also lists the DS2438 battery monitor, the DS2422 and DS2423 counters, the DS2409 MicroLAN coupler used in 1-Wire hubs, and the AAG TAI-8540 humidity sensor. It understands hubs with devices on different branches of the network.

The homepage calls it "a simple to use program for reading values from 1-wire devices" and says it has been deployed "from backyard temperature pagodas to government computer clusters."

The idea underneath is the 1-Wire bus itself. Many sensors hang off a single data wire, and each one is addressed individually. The package ships one binary per adapter family: digitemp_DS2490 for USB, digitemp_DS9097 and digitemp_DS9097U for serial. That split shows how much the adapter choice matters on this bus. The author also publishes Eagle CAD and Gerber files, so you can build your own sensor modules.

## Install

```
brew install digitemp
Requires hardware: a 1-Wire adapter (USB or serial) and one or more sensors. The formula depends on libusb-compat. Pick the executable that matches your adapter.
```

## Try this

```
digitemp_DS9097U --help
```
Prints the options for the serial adapter build, a first look at what the tool can do.

```
digitemp_DS2490 --help
```
Prints the options for the USB adapter build.

```
digitemp_DS9097 --help
```
Prints the options for the older passive serial adapter build.

## What's unique

It is a small, direct way into the 1-Wire bus, with a separate binary for each adapter family. The open hardware design files for the sensor modules are also unusual.

## Caveats

Useless without a 1-Wire adapter and sensors, the author no longer sells hardware, and the project looks quiet since roughly 2015 to 2018, with no Windows support planned.

## Links

- [DigiTemp homepage](https://www.digitemp.com/)
