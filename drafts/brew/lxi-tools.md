---
name: lxi-tools
title: lxi-tools
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, lua, needs-hardware, network, protocol, scpi, test-equipment]
homepage: https://lxi-tools.github.io
scout_score: 6
status: draft
---

# lxi-tools

**TLDR;** Command-line and GUI tools for finding and talking to network-attached lab instruments like oscilloscopes and power supplies, using SCPI over LXI.

lxi-tools is a small set of programs for instruments that sit on a network and speak LXI: oscilloscopes, power supplies, spectrum analyzers, multimeters. The `lxi` command can discover them on the local network, send SCPI commands and print the replies, grab a screenshot of the instrument's display, and benchmark how fast it answers. `lxi-gui` wraps the same abilities in a GTK interface.

Underneath is a plain idea. Modern bench equipment is often a small computer with an Ethernet port, and it accepts text commands. SCPI is the standard command language, and `*IDN?` is the standard first question: who are you? Discovery works by broadcasting on each local interface, or by mDNS with a flag. Commands travel over VXI11 on port 111 or raw TCP, which defaults to port 5025. Everything goes through the liblxi library.

Screenshots are handled by per-instrument plugins, covering Keysight, LeCroy, Rigol, Rohde & Schwarz, Siglent and Tektronix models. You can name a plugin or let the tool autodetect one, and the image can go to stdout to be piped into other tools. The Lua scripting layer lets you control an instrument, log readings to CSV and draw live charts.

The README states its aim as "To make better and simpler open source tools for managing network attached LXI compatible test instruments." It is an independent community project, not affiliated with the LXI Consortium.

## Install

```
brew install lxi-tools
# Needs an LXI-capable instrument reachable on your network. The GUI pulls in GTK4 and libadwaita. The screenshot pipe example needs ImageMagick installed separately.
```

## Try this

```
lxi discover
```
Searches the local network for LXI devices and lists any it finds by IP.

```
lxi scpi --address 10.42.1.20 "*IDN?"
```
Sends the standard identification query to the instrument at that address and prints its reply.

```
lxi screenshot --list
```
Lists the built-in screenshot plugins, one per supported instrument family.

## What's unique

It puts discovery, SCPI, screenshot capture and Lua scripting for a niche instrument protocol behind one CLI and GUI. The plugin-based screenshot system makes pulling a scope's display into a file a one-liner.

## Caveats

You need a real LXI instrument on your network to see anything happen, some instruments need raw TCP on a specific port rather than discovery, and the Windows installer and the Tektronix 2000 screenshot plugin are marked experimental.

## Links

- [Homepage](https://lxi-tools.github.io)
- [GitHub repository and README](https://github.com/lxi-tools/lxi-tools)
- [Wiki (instrument notes, known issues, SCPI commands)](https://github.com/lxi-tools/lxi-tools/wiki/)
- [Lua script API documentation](https://github.com/lxi-tools/lxi-tools/blob/master/doc/lua-api.txt)
