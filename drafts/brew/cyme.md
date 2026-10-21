---
name: cyme
title: cyme
source: brew
category: take-things-apart
commitment: quick
tags: [cross-platform, lsusb, quick, rust, tui, usb]
homepage: https://github.com/tuna-f1sh/cyme
scout_score: 6
status: draft
---

# cyme

**TLDR;** A cross-platform lsusb replacement that prints your USB buses and devices as a tree, down through descriptors, interfaces and endpoints.

Cyme lists the USB buses and devices on the machine it runs on. The output can be a plain list, a tree, lsusb-compatible text, or JSON. It can filter by vendor, class or name, and it can show or hide display blocks. Its `watch` subcommand follows hotplug events as devices come and go.

The author is an embedded developer who used a USB listing tool constantly and found lsusb's verbose dump too noisy, its tree short on useful data, and its behaviour poor outside Linux. The project began as a replacement for a barely working lsusb script and as a Rust refresher, and grew into a cross-platform lsusb.

The idea underneath is that every USB device describes itself. It reports a descriptor tree: device, configurations, interfaces, endpoints. Every plug-in negotiates that structure with the host. Raising the verbosity (`-v`, up to `-vvv`) walks you down that tree, so you can see what your keyboard, hub or dev board is telling the machine about itself.

The default build uses a pure Rust profiler built on nusb. Alternative backends exist: libusb, which lsusb uses, and macOS system_profiler parsing.

## Install

```
brew install cyme
# no hardware needed beyond the USB ports already on your machine
# alternatively: cargo install --locked cyme
# icons need a Nerd Font; otherwise pass --encoding utf8 or --icon never
```

## Try this

```
cyme --tree
```
Lists every bus and device in a tree with the default display blocks.

```
cyme --tree -vvv
```
Goes down the tree through configurations to interfaces and endpoints.

```
cyme --json watch | jq '.buses[] | .devices[]? | select( (.last_event | has("connected")))'
```
Streams hotplug events as JSON and shows newly connected devices as you plug them in.

## What's unique

It runs on macOS and Windows as well as Linux, and its tree view reaches down to endpoints. It can also export a tree to JSON and replay it later, with an option to mask serial numbers before sharing.

## Caveats

On Linux, sudo is needed to read root hub string descriptors and some devices, and Apple VHCI devices such as the T2 chip are listed without verbose data. The README itself says it is 'not perfect'.

## Links

- [GitHub repository (homepage)](https://github.com/tuna-f1sh/cyme)
- [API docs on docs.rs](https://docs.rs/cyme/latest/cyme/)
- [YouTube demo of the watch subcommand](https://youtu.be/ohRBrVBRolA)
