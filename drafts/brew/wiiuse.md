---
name: wiiuse
title: wiiuse
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bluetooth, c, library, needs-hardware, wii]
homepage: https://github.com/wiiuse/wiiuse
scout_score: 6
status: draft
---

# wiiuse

**TLDR;** A small C library that pairs Nintendo Wii Remotes over Bluetooth and hands their motion, IR, and expansion data to your own program.

Wiiuse connects to Wii Remotes through each operating system's Bluetooth stack: BlueZ on Linux, the Microsoft stack on Windows, and the native one on Mac. Your program includes `wiiuse.h`, calls `wiiuse_poll` or `wiiuse_update` in a loop, and reads controller state back through the API. It is single-threaded and nonblocking. In the README's words, that "makes a light weight and clean API."

It covers motion sensing, IR tracking, the Nunchuk, the Classic Controller, the Balance Board, and the Guitar Hero 3 controller. Expansions are initialized and calibrated over a few seconds after connection, which is why the README asks you to keep polling for 10 to 15 seconds before enabling Motion Plus.

The current project is a community fork. The original upstream stopped being maintained, and the fork was made to replace scattered ad-hoc forks with one project that has real infrastructure. The protocol knowledge comes from the wiibrew.org reverse-engineering community, so the library is also a worked example of how a consumer gadget's wireless protocol gets figured out and turned into a clean API.

The README says the library sees little change "not because it is dead, but because it is effectively complete." Old and quiet is fine here, since the controller's protocol is not going to change.

## Install

```
brew install wiiuse
# Needs a Bluetooth adapter and a real Wii Remote. Linux builds need BlueZ dev files (libbluetooth-dev on Debian/Ubuntu) and CMake. The formula installs a library only, with no executables. The example programs come from building the source yourself.
```

## Try this

```
mkdir build && cd build
```
Creates the out-of-tree build directory used for building from source on Linux and Mac.

```
cmake .. -DBUILD_EXAMPLE_SDL=NO
```
Generates the makefile and skips the optional SDL example, which needs SDL 1.2 and OpenGL.

```
make wiiuseexample
```
Builds the example program that connects to Wii Remotes and prints their state, so you can see the API in use.

## What's unique

It is a small, nonblocking C library that still covers the Balance Board and the Guitar Hero 3 controller, which many newer Wii tools skip.

## Caveats

It needs real Wii Remote hardware and a Bluetooth adapter. Third-party controllers may not work, Windows may lag with more than about two remotes, and the maintainer describes themselves as mostly absentee.

## Links

- [GitHub repository (homepage)](https://github.com/wiiuse/wiiuse)
- [Issue tracker](https://github.com/wiiuse/wiiuse/issues)
- [Changelog](https://github.com/wiiuse/wiiuse/blob/master/CHANGELOG.mkd)
- [xwiimote (alternative using the Linux kernel Wiimote support)](https://github.com/dvdhrm/xwiimote)
