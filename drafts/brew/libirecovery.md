---
name: libirecovery
title: libirecovery
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, bootloader, ios, library, needs-hardware, reverse-engineering, usb]
homepage: https://www.libimobiledevice.org/
scout_score: 7
status: draft
---

# libirecovery

**TLDR;** A library and command-line tool that talks to the iBoot bootloader of an Apple device in recovery mode over raw USB, below the operating system.

libirecovery implements the USB conversation with iBoot/iBSS, the low-level bootloader code an iPhone or iPad runs when it is in recovery mode. The bundled utility, `irecovery`, has one documented entry point: `irecovery --shell`, which opens a simple interactive shell on an attached device. Inside it you type iBoot commands, not Unix ones. Examples are `setenv`, `saveenv` and `reboot`.

Most iPhone tooling on Linux talks to services running on a booted phone. This talks to the stage before that, where there is no OS to ask. That makes it a door into how Apple devices boot, restore and recover, and into the idea that a bootloader is its own small environment with variables and commands.

The README says it is a fork of an older version from openjailbreak.org, and that it is meant to be used with `idevicerestore` from the libimobiledevice project. That wider project has existed since 2007 and set out to give Linux users access to iPhones. On Linux the library uses libusb, and on macOS it uses IOKit.

The README is brief and does not spell out the risks of writing iBoot variables. Treat `saveenv` as something to use on purpose, and ideally on a device you can afford to restore. The project states it is independent and not approved by Apple.

## Install

```
brew install libirecovery
# Needs an Apple device attached over USB and in recovery mode. The README suggests `ideviceenterrecovery` from libimobiledevice to get it there.
```

## Try this

```
irecovery --help
```
Prints the usage and the list of command-line options.

```
man irecovery
```
Opens the manual page, which the README says documents the options in full.

```
irecovery --shell
```
Connects to a device in recovery mode and opens an interactive shell for iBoot commands such as `setenv auto-boot true`, `saveenv` and `reboot`.

## What's unique

Where libimobiledevice talks to services on a booted iPhone, this talks to the bootloader itself, so it works when the OS is not running and gives direct access to iBoot environment variables.

## Caveats

It needs a real Apple device in recovery mode (not normal mode), and the README does not warn about the risks of writing iBoot variables.

## Links

- [Homepage (libimobiledevice project)](https://www.libimobiledevice.org/)
- [Repository (GitHub)](https://github.com/libimobiledevice/libirecovery)
- [Issue tracker](https://github.com/libimobiledevice/libirecovery/issues)
- [Mailing list](https://lists.libimobiledevice.org/mailman/listinfo/libimobiledevice-devel)
