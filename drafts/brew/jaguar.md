---
name: jaguar
title: Jaguar
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, embedded, esp32, live-reload, needs-hardware, toit, wifi]
homepage: https://toitlang.org/
scout_score: 5
status: draft
---

# Jaguar

**TLDR;** Jaguar pushes Toit programs to an ESP32 over WiFi and restarts them in under two seconds, with no reflashing or rebooting.

Jaguar is a live-reloading workflow for ESP32 boards programmed in Toit. The host side is a command-line tool, `jag`. The device side is a small Toit application that `jag` flashes onto the board once, over a serial cable. After that, everything happens over WiFi.

You point `jag` at a Toit source file. It compiles the program and sends it to the board. The device runs a small HTTP server that listens for requests, and each request carries a compiled program. Jaguar stops the old version, frees its resources, installs the new one in flash, and starts it again from main. The README claims this takes under two seconds. In its words: "No need to flash over serial, reboot your device, or wait for it to reconnect to your network."

The idea underneath is that the usual embedded loop of edit, flash, reboot, rejoin the network is mostly overhead, and a runtime that can swap programs in place removes it. This makes microcontroller work feel closer to editing a script. Jaguar can also keep named containers installed so they run at boot, which turns a scratch experiment into something that stays on the device.

## Install

```
brew install jaguar
jag setup

Needs an ESP32 board and a serial cable for the first flash (`jag flash`), then WiFi. On Linux you usually need serial port access, e.g. `sudo usermod -aG dialout $USER`, then log out and back in. Packages also exist for Windows (winget), Arch (AUR) and Debian/Ubuntu (.deb).
```

## Try this

```
jag flash
```
Puts the Jaguar application on a serially connected ESP32, prompting for the serial port and WiFi credentials.

```
jag scan
```
Finds ESP32s on the local network that announce themselves over UDP broadcast.

```
jag watch hello.toit
```
Watches the file and its dependencies, and live-reloads the program on the device whenever you save a change.

## What's unique

The device runs a tiny HTTP-served Toit program that accepts new compiled programs and swaps them in place, so there is no reflash in the loop. Per-run options such as `-D jag.wifi=false` let an app take over the WiFi radio itself.

## Caveats

It needs an ESP32 and a serial cable for the first flash, it only runs Toit rather than C or Arduino code, and the brief found no release or commit dates for jag itself.

## Links

- [Toit language homepage](https://toitlang.org/)
- [Jaguar GitHub repository and README](https://github.com/toitlang/jaguar)
- [Two-minute demonstration video](https://youtu.be/cU7zr6_YBbQ)
