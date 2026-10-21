---
name: liquidctl
title: liquidctl
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, hid, needs-hardware, pc-hardware, python, rgb, usb]
homepage: https://github.com/liquidctl/liquidctl
scout_score: 7
status: draft
---

# liquidctl

**TLDR;** One command-line tool and Python library that reads and controls PC liquid coolers, fan hubs, RGB lighting and memory from many vendors, without their own software.

liquidctl talks to PC hardware that normally ships with a vendor's own control app. Point it at a supported device and it reads status (fan and pump speed, liquid temperature, noise level, DIMM temperature) or sets fan curves, pump speed, LED colours and lighting modes. Output is plain text, or JSON with `--json` for the list, initialize and status commands.

Each supported device has a driver module. Drivers reach hardware over USB HID (via hidapi), raw USB (via PyUSB and libusb), or SMBus on Linux for some memory and motherboard RGB parts. The README's support table covers coolers, fan and LED controllers, PSUs, GPUs and DDR4 memory from Corsair, NZXT, ASUS, Aquacomputer, Gigabyte, Lian Li, MSI and others.

The idea underneath is that a lot of consumer hardware is just a USB device speaking a small protocol, and a driver can replace the vendor app. That makes it a way into how HID and USB devices work, and how a cross-platform driver is organised. The driver APIs can also be used from Python: "The liquidctl driver APIs can be used to build Python programs that monitor or control the devices, and offer features beyond the ones provided by the CLI."

Most devices need an initialize step after each boot. The README says so explicitly, and covers autostart with systemd units, Windows Task Scheduler and macOS launchctl.

## Install

```
brew install liquidctl
# Needs a supported device plugged in to do anything useful. Also available via: python -m pip install liquidctl
# On Linux, devices are not accessible to normal users by default: use sudo or install extra/linux/71-liquidctl.rules from the repo.
```

## Try this

```
liquidctl --help
```
Shows the available commands and options, which works even with no supported device attached.

```
liquidctl list
```
Lists every recognised supported device with an index, for example 'Device #0: Corsair Vengeance RGB DIMM2'.

```
liquidctl status
```
Prints current readings for all devices, such as fan rpm, voltage, current, noise level, liquid temperature and pump speed.

## What's unique

One CLI and one Python API cover coolers, fan hubs, PSUs, RAM, GPUs and motherboard RGB from many vendors. The README's support table is candid about partial support, broken devices and devices that need unsafe flags.

## Caveats

It does nothing without a supported device, Linux needs root or udev rules, and on Windows some devices need a Zadig driver swap that can make them unusable if it was not needed.

## Links

- [liquidctl on GitHub](https://github.com/liquidctl/liquidctl)
- [Per-device docs](https://github.com/liquidctl/liquidctl/tree/main/docs)
- [liquidtux, sibling Linux hwmon drivers](https://github.com/liquidctl/liquidtux)
