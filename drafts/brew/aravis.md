---
name: aravis
title: Aravis
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, cameras, genicam, library, needs-hardware, protocol]
homepage: https://github.com/AravisProject/aravis
scout_score: 6
status: draft
---

# Aravis

**TLDR;** A C library that speaks the GigE Vision and USB3 protocols of industrial cameras, with a built-in fake camera so you can try it without hardware.

Aravis is a glib/gobject library for video acquisition from GenICam cameras. GenICam is the standard interface family for industrial machine vision cameras. Aravis implements the gigabit ethernet (GigE Vision) and USB3 protocols those cameras use. Your program gets video frames and camera control through the library API.

Besides the library, it ships a basic ethernet camera simulator and a simple video viewer. The viewer is built on GStreamer1 and Gtk+3, and an optional GStreamer plugin is included too. The brew install gives you five executables, all with a `-0.8` suffix: `arv-tool`, `arv-viewer`, `arv-test`, `arv-camera-test` and `arv-fake-gv-camera`.

The interesting part is the door it opens. Industrial cameras are not webcams. They announce themselves on the network, expose their settings through a standard description, and stream frames over protocols most developers never see. The README gives no further motivation or internals, so the docs are the place to learn how it works.

There is also an unusual contribution rule. Code for the GigE Vision and USB3 Vision protocols must not be based on the A3 specification documents, because A3 forbids their use for open source implementations.

## Install

```
brew install aravis
# For GStreamer to find the bundled plugin:
export GST_PLUGIN_PATH=$HOMEBREW_PREFIX/opt/aravis/lib/gstreamer-1.0
# Real camera use needs a GenICam camera on the network or USB.
```

## Try this

```
arv-fake-gv-camera-0.8 --help
```
Shows the options for the bundled fake GigE camera, which stands in for real hardware.

```
arv-tool-0.8 --help
```
Lists what the command-line tool can do with cameras it finds.

```
arv-viewer-0.8 --help
```
Shows the options for the simple GStreamer and Gtk+3 video viewer.

## What's unique

It bundles a fake GigE camera simulator next to the real library, so you can test acquisition code with no hardware. Its README also bars contributors from using the A3 spec documents for the protocol code.

## Caveats

Real use needs a GenICam camera on the network or USB, and the full build pulls in GStreamer and Gtk+3; the README documents no command-line tool list.

## Links

- [GitHub repository (homepage)](https://github.com/AravisProject/aravis)
- [Documentation (stable)](https://aravisproject.github.io/aravis/aravis-stable)
- [Forum](https://aravis-project.discourse.group)
- [GenICam standard](http://www.genicam.org)
