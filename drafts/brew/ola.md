---
name: ola
title: OLA (Open Lighting Architecture)
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, art-net, dmx, lighting, needs-hardware, protocol, sacn]
homepage: https://www.openlighting.org/ola/
scout_score: 6
status: draft
---

# OLA (Open Lighting Architecture)

**TLDR;** A daemon and toolkit for talking to stage lighting gear over DMX, Art-Net and sACN, a protocol world most developers never touch.

OLA is a lighting-control package. The Homebrew formula installs a daemon, `olad`, and a large set of command-line tools. Going by their names, these cover DMX512 output, RDM device discovery and configuration, Art-Net and E1.31 (sACN) over the network, USB DMX interfaces, timecode, and a recorder. The brief was written without access to the README or docs, so those functions are inferred from the executable names and not confirmed.

The idea underneath is that stage lighting runs on its own small family of protocols. DMX512 is a serial bus that carries channel values to fixtures. Art-Net and sACN carry the same kind of data over ordinary IP networks. RDM adds a way to ask fixtures what they are and change their settings. OLA appears to sit in the middle as a router, with the daemon holding universes and the tools patching inputs and outputs to them.

The tool list suggests a full toolkit and not a single utility. It includes a DMX console and monitor, a stream client, universe naming and stats, merge and priority controls, and USB Pro firmware and sniffer tools. That makes it a way into how theatre, club and installation lighting is wired together, without needing to buy a lighting desk.

## Install

```
brew install ola
# Homebrew caveat: Python support has been removed (https://github.com/OpenLightingProject/ola/issues/2008). Check that issue if you expect Python bindings.
# Real fixtures or a USB DMX interface are likely needed to see physical output; setup steps were not verified.
```

## Try this

```
olad --help
```
Shows the options for the OLA daemon that the other tools talk to.

```
ola_dmxconsole --help
```
Shows usage for the interactive DMX console tool.

```
ola_set_dmx --help
```
Shows how to send channel values to a DMX universe from the command line.

## What's unique

It covers the whole lighting protocol stack in one package: DMX, Art-Net, sACN, RDM and USB interfaces. Few general-purpose developer tools go near this area.

## Caveats

The homepage returned HTTP 500 and the README did not load, so function, status, platform support and first-run steps are unverified, and Python support has been removed.

## Links

- [Project homepage](https://www.openlighting.org/ola/)
- [GitHub repository](https://github.com/OpenLightingProject/ola)
- [Python removal issue cited by Homebrew caveat](https://github.com/OpenLightingProject/ola/issues/2008)
