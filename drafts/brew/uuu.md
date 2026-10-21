---
name: uuu
title: uuu
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bootloader, embedded, needs-hardware, nxp, protocol, usb]
homepage: https://github.com/nxp-imx/mfgtools
scout_score: 5
status: draft
---

# uuu

**TLDR;** A command-line tool that talks to the i.MX boot ROM over USB and pushes bootloaders or whole disk images onto a bare NXP board.

uuu, the Universal Update Utility from NXP's mfgtools 3.0, flashes NXP i.MX application processors over USB. You point it at a boot image such as u-boot.imx, a .uu script file, or an interactive shell, and it sends the contents to a board sitting in USB recovery mode. It can also write whole images, such as a .wic.zst, into eMMC. While it works, it prints a progress display listing devices, succeeded and failed counts, and the SDP command in flight.

The interesting part is where it connects. A board with no working software still has a boot ROM, and that ROM speaks a small USB protocol. uuu sends commands like SDP: boot and SDP: jump to it, which gets code running before any operating system exists. Watching that exchange with -v is a view into the earliest stage of how an embedded chip comes to life.

Daemon mode makes the loop tangible. Run it with -d and it waits for a known device to appear, then downloads to it. The README notes that u-boot.imx can be replaced and the new file will be sent the next time the board resets, which makes it handy for iterating on a bootloader.

There is also a small firmware-side detail: U-Boot or the kernel can advertise WCID descriptors so Windows loads the WinUSB driver by itself. The README describes the project as the 'real cross platform' successor to the older mfgtools, running on Linux, Windows and macOS.

## Install

```
brew install uuu
# Needs an NXP i.MX board in USB recovery mode and a USB cable to do anything real. Without one, only --help is useful.
```

## Try this

```
uuu --help
```
Lists the options and the built-in commands, which works without any board attached.

```
uuu -v u-boot.imx
```
Downloads u-boot.imx to a board in recovery mode, with verbose output showing the SDP commands.

```
uuu -d u-boot.imx
```
Runs in daemon mode, waiting for a known device to appear and sending the image each time the board resets into recovery.

## What's unique

It goes straight to the i.MX boot ROM's USB recovery path and makes it scriptable, with list files, an interactive shell and a daemon that re-flashes the board on every reset.

## Caveats

It is only useful with an NXP i.MX board; the README says macOS support is 'not test yet', and it warns that 32-bit systems have problems with big files.

## Links

- [GitHub repository (homepage)](https://github.com/nxp-imx/mfgtools)
- [Releases (prebuilt binaries)](https://github.com/nxp-imx/mfgtools/releases)
- [Wiki](https://github.com/nxp-imx/mfgtools/wiki)
- [Python bindings (wrapper)](https://github.com/nxp-imx/mfgtools/tree/master/wrapper)
