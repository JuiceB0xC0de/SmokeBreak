---
name: packetry
title: Packetry
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, gui, needs-hardware, pcap, protocol, rust, usb]
homepage: https://github.com/greatscottgadgets/packetry
scout_score: 6
status: draft
---

# Packetry

**TLDR;** A Rust and GTK 4 USB 2.0 protocol analyser that shows traffic captured by Cynthion hardware, or read from a saved .pcap file.

Packetry is a graphical application for looking at USB 2.0 traffic. It takes in packets from a live capture through Cynthion, the open USB hardware from Great Scott Gadgets, or from a saved .pcap file, and lays them out in a window. The README calls it "A fast, intuitive USB 2.0 protocol analysis application for use with Cynthion."

The README gives no problem statement, and it does not explain how capture or decoding works internally. What it does say is that the app is written in Rust, with its GUI built on GTK 4 through the gtk-rs bindings. Given a capture filename as an argument, it tries to load that file on startup.

The idea underneath is that USB is a conversation you normally never see. Every keyboard, flash drive and webcam exchanges packets with the host, and an analyser sitting on the wire lets you read that exchange. That makes it a way into how devices enumerate, describe themselves and move data, and into reverse engineering a device whose behaviour you want to understand.

The only supported file format is .pcap with the LINKTYPE_USB_2_0 link layer header type. Live capture appears to be the main use, but saved captures can be opened without any hardware attached.

## Install

```
brew install packetry
# Live capture needs Cynthion hardware. Opening saved .pcap files does not.
# The README describes building from source: Rust 1.93 or newer plus GTK 4 headers, then cargo build.
```

## Try this

```
packetry --help
```
Lists the options the app accepts.

```
packetry-cli --help
```
Shows what the command-line companion offers.

## What's unique

It pairs a desktop analyser written in Rust and GTK 4 with open Cynthion hardware. Captures can also be inspected offline from .pcap files.

## Caveats

Live capture needs Cynthion hardware, only USB 2.0 is covered, and the brief could not confirm usage details because the documentation body text did not load.

## Links

- [Homepage (GitHub repository)](https://github.com/greatscottgadgets/packetry)
- [Packetry Documentation](https://packetry.readthedocs.io/)
- [Cynthion hardware](https://greatscottgadgets.com/cynthion/)
