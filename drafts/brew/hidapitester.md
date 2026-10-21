---
name: hidapitester
title: hidapitester
source: brew
category: radio-and-hardware
commitment: quick
tags: [hid, needs-hardware, protocol, quick, reports, usb]
homepage: https://github.com/todbot/hidapitester
scout_score: 7
status: draft
---

# hidapitester

**TLDR;** A command-line tool that finds USB HID devices and sends or reads raw reports as hex, so you can talk to keyboards, LEDs and gadgets from the shell.

hidapitester sits on top of HIDAPI, a cross-platform library for talking to USB Human Interface Devices. You give it arguments that are read left to right and run in order: filters to pick a device (vendor and product ID, usage page, usage, serial), then actions such as opening it, sending Output or Feature reports, reading Input reports, or fetching the report descriptor. Results come back as device listings and hex dumps.

The README says the goal is "to provide a simple, low-dependency command-line tool to test out every API call in hidapi." Default builds are fully static, so nothing else needs to be installed to run it. Report bytes are passed as comma-separated lists, with the first byte as the report ID when the device uses report IDs. Buffer size is set with --length, and reads block for a --timeout in milliseconds or loop forever with the -forever variants.

The idea underneath is that HID is not only keyboards and mice. It is a generic protocol where a device describes its own reports in a descriptor, and the host sends and receives small byte buffers against that description. Lots of hobby hardware, LEDs, and custom gadgets use it because it needs no driver. This tool lets you see and poke that layer directly.

The repo also includes test firmware sketches under test_hardware for RP2040, Teensy and Pro Micro boards. They send and echo raw HID reports, so with a cheap board you can test both ends of the link.

## Install

```
brew install hidapitester
# Needs a USB HID device plugged in to do anything interesting. Building from source needs a C toolchain and hidapi; on Debian/Ubuntu also: sudo apt install libudev1 libudev-dev pkg-config
```

## Try this

```
hidapitester --help
```
Prints the list of filter and action arguments, including the commands for opening, sending and reading reports.

```
hidapitester --vidpid 046D:B378 --nonexclusive --open --read-input
```
The README's macOS example: opens a device in shared mode so a keyboard or mouse keeps working, then reads one Input report.

```
hidapitester --vidpid 0x27b8/0x1ed --open --length 9 --send-feature 1,99,0,255,0  --read-feature 1 --close
```
The README's blink(1) example: sends a Feature report to the LED device and reads one back to get version info.

## What's unique

It is a thin, scriptable window onto HIDAPI itself, covering report descriptors, Feature and Output reports and hex dumps. The bundled firmware sketches let you build the device side as well.

## Caveats

On macOS, devices open exclusively by default, which needs root for keyboards and stops a mouse moving the cursor, so use --nonexclusive; on FreeBSD and NetBSD that flag only prints a warning.

## Links

- [Homepage (GitHub repo)](https://github.com/todbot/hidapitester)
- [Releases and prebuilt binaries](https://github.com/todbot/hidapitester/releases)
- [hidapi library](https://github.com/libusb/hidapi)
