---
name: ifuse
title: ifuse
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, fuse, ios, needs-hardware, protocol, usb]
homepage: https://libimobiledevice.org/
scout_score: 5
status: draft
---

# ifuse

**TLDR;** Mounts a USB-connected iPhone or iPad as an ordinary folder, using a reimplemented Apple protocol stack and no Apple software.

ifuse is a command-line FUSE filesystem for iOS devices. Give it a mountpoint and it shows a directory from the connected device there, so `ls`, `cp` and your file manager work on it. By default it exposes the Media partition, `/var/mobile/Media`, which holds photos and music. It can also mount the Documents folder or the whole sandbox container of a named app. On jailbroken devices with the AFC2 service it can mount the root filesystem.

Underneath, ifuse talks to the device through libimobiledevice. That library reaches the phone over USB via the usbmuxd daemon, then opens an AFC (Apple File Connection) session. ifuse registers that session with libfuse on Linux or macFUSE on macOS, and each read or write at the mountpoint becomes an AFC call.

The wider libimobiledevice project exists so Linux users can talk to iOS hardware without iTunes. Its homepage puts the goal as letting 'penguins talk to fruits'. ifuse is the small piece that turns that protocol work into something you can use with plain shell tools. It is also a way into how a phone exposes services over USB: multiplexing, pairing and trust, and per-app sandboxes.

## Install

```
brew install ifuse
# Needs a USB-connected, trusted iOS device and a running usbmuxd. On macOS, also install macFUSE and approve its system extension (restart required). On Linux you may need `sudo modprobe fuse` and to add your user to the fuse group.
# Use version 1.2.1 or later; 1.2.0 has a data-corruption bug.
```

## Try this

```
ifuse --list-apps
```
Lists installed file-sharing-enabled apps with their bundle identifiers.

```
ifuse <mountpoint>
```
Mounts the device's media partition (/var/mobile/Media) at the directory you give it.

```
fusermount -u <mountpoint>
```
Unmounts the filesystem when you are done, run as a regular user.

## What's unique

It is a small FUSE front end over a native, reimplemented iOS protocol stack, so you can browse a phone's files from a shell with no Apple software. The option to mount the root filesystem on jailbroken devices is unusual.

## Caveats

Version 1.2.0 has a serious bug that corrupts data, fixed in 1.2.1, so check the version you get; it also needs a trusted device, a running usbmuxd, and macFUSE on macOS.

## Links

- [Homepage (libimobiledevice)](https://libimobiledevice.org/)
- [ifuse repository and README](https://github.com/libimobiledevice/ifuse)
- [ifuse issue tracker](https://github.com/libimobiledevice/ifuse/issues)
