---
name: mobiledevice
title: mobiledevice
source: brew
category: take-things-apart
commitment: quick
tags: [apple, ios, macos, needs-hardware, quick, reverse-engineering, usb]
homepage: https://github.com/imkira/mobiledevice
scout_score: 6
status: draft
---

# mobiledevice

**TLDR;** A small macOS command-line tool that talks to iPhones and iPads over USB through Apple's private MobileDevice framework: list devices, install apps, tunnel ports.

mobiledevice wraps Apple's private, closed MobileDevice framework, the same layer the desktop side of iOS tooling uses to talk to a phone over USB. Subcommands cover listing connected devices by UDID, reading device properties, installing and uninstalling .app folders, and looking up a bundle identifier from a local .app. Output is plain text on stdout, errors go to stderr, and failures return a non-zero exit status, so it fits into shell scripts.

The README says it exists to automate installing and uninstalling apps without clicking through Xcode or iTunes. It also says: "You don't need a jailbroken device!"

The most interesting subcommand is `tunnel`. It listens on a local port on the Mac and forwards each connection over USB to a TCP port on the device. The README says this avoids needing Wi-Fi or a cellular connection. It is a small, shell-level view of how a desktop reaches into a phone, and a door into the USB multiplexing layer underneath iOS tooling.

Commands take an optional `-t` timeout and `-u` UDID, and default to the first detected device.

## Install

```
brew install mobiledevice
# Needs a Mac and an iPhone or iPad plugged in over USB. Installing apps also needs iOS development certificates already set up.
```

## Try this

```
mobiledevice help
```
Prints the usage screen listing every subcommand and its options.

```
mobiledevice list_devices
```
Lists the UDID of each connected device, one per line.

```
mobiledevice get_device_prop ProductType
```
Prints the ProductType property of the first detected device.

## What's unique

It turns a closed Apple framework into plain shell commands, and `tunnel` gives a USB-only route from the Mac's localhost to a TCP server on the device.

## Caveats

It depends on a private Apple framework, the README's tested-device list stops at iPhone 6, and its maintenance status is unclear, so it may break on newer OS versions.

## Links

- [GitHub repository and README](https://github.com/imkira/mobiledevice)
- [Japanese README](https://github.com/imkira/mobiledevice/blob/master/README_JP.md)
- [Contributors graph](https://github.com/imkira/mobiledevice/graphs/contributors)
