---
name: uhubctl
title: uhubctl
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, libusb, needs-hardware, power-control, raspberry-pi, usb]
homepage: https://github.com/mvp/uhubctl
scout_score: 7
status: draft
---

# uhubctl

**TLDR;** A command-line tool that cuts and restores power to individual ports on USB hubs, so you can reboot a stuck device from software.

uhubctl switches power on single ports of USB hubs that support per-port power switching. It has four actions: off, on, cycle, and toggle. Run with no arguments, it lists the supported hubs it finds and their locations. You then name a hub by location, such as `-l 1-1`, and a port or list of ports with `-p`. It is written in C on top of libusb.

The idea comes from hub-ctrl.c by Niibe Yutaka, a tool for AC power control through USB hubs. The aim is practical: a phone, light, fan, or stuck modem plugged into a hub port can be turned off or reset without anyone walking over and pulling the cable.

Underneath is something most people never see. Hubs advertise in their USB descriptors whether they can switch power per port, and the README suggests checking with `lsusb -v`. On Linux 6.0 and later, uhubctl uses the kernel's standard interface to toggle port power. Otherwise it sends the control requests directly through libusb. As the README puts it, "not many USB hubs correctly support per-port power switching", but "quite a few modern motherboards have built-in root hubs that do support this feature", so you may not need to buy anything.

The README also documents Raspberry Pi wiring in detail. Each board has a different hub topology, and the Pi 5's four hubs turn out to be ganged together.

## Install

```
brew install uhubctl
# Needs libusb (installed as a Homebrew dependency).
# On Linux, use sudo or add a udev rule, e.g. the ready-made udev/rules.d/52-usb.rules from the repo, then run: sudo udevadm trigger --attr-match=subsystem=usb
# Needs a USB hub or root hub with per-port power switching.
```

## Try this

```
uhubctl
```
Lists every supported hub it finds, with the locations you need for -l.

```
uhubctl -a off -p 2
```
Turns off power on port 2 of the default smart hub. Be careful which port you pick.

```
uhubctl -l 2 -a 0
```
The README's Raspberry Pi 4B example: turns off the USB3 hub at location 2, whose four ports are ganged together.

## What's unique

It does one narrow thing: real per-port power switching over USB. The README also keeps a hands-on hardware compatibility table and per-board Raspberry Pi wiring notes.

## Caveats

Only hubs with real per-port power switching work, and the README says its compatibility list is incomplete. Some hubs cut data but not power, Windows cannot switch power, and turning off the wrong built-in port can cut off your keyboard or mouse.

## Links

- [Project homepage and README (GitHub)](https://github.com/mvp/uhubctl)
- [Releases](https://github.com/mvp/uhubctl/releases)
- [Ready-made udev rule file](https://github.com/mvp/uhubctl/blob/master/udev/rules.d/52-usb.rules)
