---
name: usbtree
title: usbtree
source: brew
category: radio-and-hardware
commitment: quick
tags: [hot-plug, needs-hardware, quick, rust, tui, usb]
homepage: https://gnomeria.github.io/usbtree/
scout_score: 7
status: draft
---

# usbtree

**TLDR;** A live, color-coded USB device tree in your terminal that flashes hot-plugged devices and shows unplugged ones as red ghosts.

usbtree is a terminal UI that draws the USB bus as a tree: hubs, the devices hanging off them, device classes, link speeds, and a panel logging plug and unplug events. It rescans every second. A newly plugged device flashes green, and an unplugged one lingers as a red crossed-out ghost for 30 seconds before it disappears.

It reads the bus through nusb, a pure-Rust library, so there is no libusb and no root needed for the basic tree. Names come from a fallback chain: your own overrides.ids file, then the strings the device reports about itself, then a downloadable usb.ids list (via `--updatelist`), then an embedded snapshot, then vendor and class guesses. Composite devices are classified by their interface classes, so a MOTU audio interface shows as Audio instead of a vague Misc.

The idea underneath is that USB is a tree, not a pile of ports. Every device sits behind a hub, hubs share bandwidth, and each device announces what it is through descriptors. Watching that tree change as you plug things in makes the topology visible. On Linux it can also show live traffic: URBs per second without privileges, or real bytes per second as root with the usbmon module loaded. A `p` key toggles a PCI view.

The homepage describes it as 'Everything lsusb -t shows, plus names that make sense, hot-plug awareness, and live traffic.'

## Install

```
brew install usbtree
# Homebrew covers Linux and Apple Silicon macOS. Other options: a shell installer (Linux/macOS), a PowerShell installer (Windows), release archives, or cargo install --git https://github.com/gnomeria/usbtree
# No account or runtime needed. USB hardware is optional thanks to --demo.
```

## Try this

```
usbtree --demo
```
Runs the interface with simulated devices, so you can see the tree and hot-plug effects without any hardware.

```
usbtree
```
Shows your real USB tree live. Plug and unplug something to watch it flash green or leave a red ghost.

```
usbtree --help
```
Lists the available options, including the `--dump` flag for scripts and `--updatelist` for refreshing names.

## What's unique

It is a single static binary with no libusb, and it combines friendly names, hot-plug ghosts, live traffic sparklines and composite-device classification in one view.

## Caveats

Live per-device traffic and safe eject only work on Linux, prebuilt binaries are unsigned (macOS needs xattr to clear quarantine), and there is no prebuilt Intel macOS build.

## Links

- [Homepage](https://gnomeria.github.io/usbtree/)
- [GitHub repository](https://github.com/gnomeria/usbtree)
