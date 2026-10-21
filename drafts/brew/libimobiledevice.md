---
name: libimobiledevice
title: libimobiledevice
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, c-library, ios, needs-hardware, protocol, usb]
homepage: https://www.libimobiledevice.org/
scout_score: 5
status: draft
---

# libimobiledevice

**TLDR;** A free C library and command-line toolkit that talks to iPhones and iPads over Apple's own protocols, no iTunes needed, so you can read device info, logs and screenshots from a terminal.

libimobiledevice is a cross-platform C library plus a set of small command-line tools for talking to iOS devices. It connects over USB through a daemon called usbmuxd, or over Wi-Fi if Wi-Fi sync is enabled on iOS 11 and later. Through that connection it reaches the services a phone exposes: backup, filesystem access, syslog, diagnostics, provisioning, debugging, screenshots and more. Each service gets its own executable, such as `ideviceinfo`, `idevicesyslog` or `idevicebackup2`.

It started because, in the homepage's words, Linux enthusiasts were not amused by hardware like the iPhone 2G, and iTunes did not exist for Linux. The project, first called libiphone, set out to "bring freedom and 'allow penguins to talk to fruits'". The library reimplements the protocols itself and, per the homepage, does not depend on or bundle any existing libraries from Apple.

The idea underneath is that a phone is a network-style peer with a set of named services behind a handshake. The C API opens a device, performs a lockdown handshake with the lockdown daemon on the phone, then asks for values or starts services. Once you see that shape, the tools read like a map of what the phone offers, and the object-oriented C design is meant to make bindings for other languages easy.

## Install

```
brew install libimobiledevice
# Needs an iPhone or iPad plugged in over USB (or set up for Wi-Fi sync, iOS 11+).
# On Debian/Ubuntu: sudo apt-get install usbmuxd libimobiledevice6 libimobiledevice-utils
```

## Try this

```
ideviceinfo -k ProductVersion
```
Prints a single device key, here the iOS version of the connected device.

```
ideviceinfo -s
```
Dumps the device's details as simple key: value lines, including DeviceName, ProductType, BuildVersion and WiFiAddress.

```
idevicediagnostics restart
```
Restarts the connected device and prints 'Restarting device.'

## What's unique

It is a clean-room reimplementation of Apple's device protocols, so a Linux or other non-Apple machine can reach iOS services that normally need iTunes. Each service is exposed as its own small tool.

## Caveats

You need a physical iOS device; Windows support is partial and needs iTunes' Apple Mobile Device Support, and the homepage's example outputs come from old devices and iOS 12.4.

## Links

- [Homepage](https://www.libimobiledevice.org/)
