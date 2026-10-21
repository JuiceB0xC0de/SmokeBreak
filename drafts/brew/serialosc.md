---
name: serialosc
title: serialosc
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, monome, needs-hardware, network, osc, quick]
homepage: https://github.com/monome/docs/blob/gh-pages/serialosc/osc.md
scout_score: 6
status: draft
---

# serialosc

**TLDR;** A daemon that turns monome grid and arc controllers into OSC devices, so any music software that speaks OSC can read their buttons and light their LEDs.

serialosc is a small server for monome hardware, the minimalist grids of buttons and knob rings used in the small-instrument and live-performance scene. In its own words, it is "a daemon that waits for you to plug a monome in, then it spawns off a dedicated server process to route OSC messages to and from your monome."

The protocol is plain OSC over UDP. The main server listens on port 12002. A client sends `/serialosc/list` or `/serialosc/notify` to learn which devices are attached and which port each one uses. Each device gets its own port, and the client talks to it directly. Key presses arrive as messages like `<prefix>/grid/key`, and LEDs are set with messages like `<prefix>/grid/led/set`. The daemon also advertises a `_monome-osc._udp` service over zeroconf, so clients can find it on the network.

The idea underneath is that a physical object becomes a few lines of network messages. Anything that can send UDP, such as a script, a patching environment or a sequencer, can treat a grid of lit buttons as a display and an input. The protocol reference also documents compact bitmask messages for the 64-LED and 256-LED layouts, which is more efficient than setting LEDs one at a time. Reading that page is a good way to see how a hardware interface gets designed.

## Install

```
brew install serialosc
Needs a monome grid or arc plugged in to do anything useful. Mac and Windows installers are also on the GitHub releases page.
```

## Try this

```
serialoscd --help
```
Shows the options for the daemon that waits for a monome to be plugged in.

```
serialosc-detector --help
```
Shows the options for the helper that detects connected monome devices.

```
serialosc-device --help
```
Shows the options for the per-device server process the daemon spawns.

## What's unique

Unlike a typical MIDI or HID bridge, serialosc uses OSC over UDP and gives each device its own port, so any OSC-capable environment can drive a grid directly.

## Caveats

It is only useful with monome hardware, and the brief found no release or maintenance dates, so check the releases page for activity.

## Links

- [OSC protocol reference (homepage)](https://github.com/monome/docs/blob/gh-pages/serialosc/osc.md)
- [serialosc repository](https://github.com/monome/serialosc)
- [serialosc releases (mac and windows installers)](https://github.com/monome/serialosc/releases)
- [serialosc documentation](https://monome.org/docs/serialosc)
