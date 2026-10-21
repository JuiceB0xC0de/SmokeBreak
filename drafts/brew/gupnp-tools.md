---
name: gupnp-tools
title: GUPnP Tools
source: brew
category: fundamentals
commitment: quick
tags: [discovery, gui, network, protocol, quick, upnp]
homepage: https://wiki.gnome.org/GUPnP/
scout_score: 8
status: draft
---

# GUPnP Tools

**TLDR;** Six GNOME-hosted tools for finding UPnP devices on your network and poking at them, built as free replacements for Intel's UPnP tools.

GUPnP Tools is a set of client and server side programs for testing and debugging UPnP devices and control points. It installs six executables: gssdp-discover, gupnp-av-cp, gupnp-event-dumper, gupnp-network-light, gupnp-universal-cp and gupnp-upload. They are built on the GUPnP library. The pages behind this entry do not describe what each tool takes in or prints, so the names are a starting point, not a manual.

The project describes itself as "free replacements of Intel UPnP tools that use GUPnP." Intel's tools were proprietary, and this set exists so the same kind of inspection can be done with open, GPL-licensed software. Its stated aim is to let people "easily test and debug one's UPnP devices and control points."

The larger idea is UPnP itself, a protocol for devices on a local network to announce themselves and be controlled by others. Most people never see that conversation. A tool that lists what is announcing itself, and lets you call into it, turns a hidden layer of the network into something you can look at. The dependency list includes GTK, so several of these tools are likely graphical programs, though the brief does not confirm this.

## Install

```
brew install gupnp-tools
```

## Try this

```
gssdp-discover --help
```
Prints the options for the discovery tool, the natural first stop for seeing what is on your network.

```
gupnp-universal-cp --help
```
Shows the options for the universal control point, which is likely the general-purpose way to browse and control a device.

```
gupnp-event-dumper --help
```
Shows the options for the event dumper.

## What's unique

It is an open, GNOME-hosted set of UPnP debugging tools that stands in for a vendor's proprietary ones, with separate programs for discovery, control, events, and a demo server.

## Caveats

The homepage is a retired wiki stub and the brief found no usage examples or release dates, so what each tool does is unverified and the project's maintenance status is unknown.

## Links

- [GitLab repository for gupnp-tools](https://gitlab.gnome.org/GNOME/gupnp-tools)
- [GNOME wiki GUPnP page (retired archive)](https://wiki.gnome.org/GUPnP/)
