---
name: m1ddc
title: m1ddc
source: brew
category: radio-and-hardware
commitment: quick
tags: [ddc, macos, monitors, needs-hardware, protocol, quick]
homepage: https://github.com/waydabber/m1ddc
scout_score: 6
status: draft
---

# m1ddc

**TLDR;** A tiny command-line tool that talks DDC/CI to external monitors on Apple Silicon Macs, so you can set brightness, volume or input from a script.

m1ddc sends commands to an external display over DDC/CI, the control channel built into most monitors. You give it a verb (`set`, `get`, `chg`, `max`, or `display list`) and a setting such as luminance, contrast, volume, red or input. It then changes the display or prints the current value. It works with displays on USB-C/DisplayPort Alt Mode and on some built-in HDMI ports.

The idea underneath is that your monitor has its own small control protocol, separate from the picture. The buttons on the bezel and the on-screen menu use the same kind of commands. Settings are exposed as VCP-style codes, and the README lists raw values such as input 15 for DisplayPort 1, plus known values for Dell PBP/KVM and ASUS KVM switching. Those numbers are sent to the monitor more or less as they are.

You can pick a display by its number in `display list`, or by identifiers such as UUID, EDID or serial. `display list detailed` prints the extra attributes you need to find those. The README calls it a "little tool" that is "useful to embed in various scripts", and points to BetterDisplay's CLI for anything more advanced. The same author maintains BetterDisplay and a Swift DDC library, so this is the minimal companion to those.

## Install

```
brew install m1ddc
# Needs an Apple Silicon Mac and an external display that supports DDC/CI. The README's own route is to download the source and run `make`, which needs clang from Apple's Command Line Tools.
```

## Try this

```
m1ddc display list
```
Lists the connected external displays, with the numbers you use to address them.

```
m1ddc get luminance
```
Prints the current brightness of the default display.

```
m1ddc chg volume -10
```
Lowers the default display's speaker volume by 10.

## What's unique

It is a very small, scriptable way into the monitor's own control channel on Apple Silicon. It exposes raw VCP codes, including input and KVM switching, and offers several ways to address a specific display.

## Caveats

Apple Silicon only, with no Intel support. Built-in HDMI works on only some ports, and many settings depend on what your particular monitor supports.

## Links

- [m1ddc GitHub homepage and README](https://github.com/waydabber/m1ddc)
- [BetterDisplay CLI integration docs](https://github.com/waydabber/BetterDisplay/wiki/Integration-features,-CLI)
- [AppleSiliconDDC (Swift DDC library by the same author)](https://github.com/waydabber/AppleSiliconDDC)
