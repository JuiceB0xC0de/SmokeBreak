---
name: open-ocd
title: OpenOCD
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, boundary-scan, debugging, embedded, jtag, needs-hardware, swd]
homepage: https://openocd.org/
scout_score: 6
status: draft
---

# OpenOCD

**TLDR;** An open-source tool that talks to the debug port of a microcontroller over JTAG or SWD, so you can flash, halt and inspect a chip directly.

OpenOCD, the Open On-Chip Debugger, sits between your computer and an embedded chip. A hardware debug adapter (an FT2232 board, J-Link, ST-LINK, CMSIS-DAP and others) plugs into your machine, and its other end connects to a target board over JTAG or SWD. OpenOCD drives that adapter and gives you flash programming, memory access, breakpoints and debugging sessions against the chip.

It is built in layers, according to the user guide's table of contents. You pick and configure an adapter, set up a JTAG or SWD transport, and declare the TAPs that describe the target's scan chain. Then you define the target CPUs. A server stage exposes a GDB server, a telnet interface and a Tcl RPC interface. All of this is configured through Tcl scripts, and the 0.12.0 release notes list dozens of new board, target and adapter configs, including Raspberry Pi, ESP32 and STM32 parts.

The idea underneath is that most chips ship with a side door for debugging, and that door is a standard. Once you can speak JTAG, you can halt a CPU, read its memory, rewrite its flash, or walk a scan chain without the chip's own software cooperating. OpenOCD also covers boundary-scan work, with SVF and XSVF file playback, so it is not only a debugger.

The homepage is a news feed with no usage examples, so the user guide is the real starting point. Its sections on choosing a dongle, hooking up the adapter and configuration basics are where a first session begins.

## Install

```
brew install open-ocd
# Needs a supported debug adapter (dongle) and a target board, plus the matching interface and target config scripts.
```

## Try this

```
openocd --help
```
Prints the command-line options, including how to point OpenOCD at config scripts. No hardware is needed for this.

## What's unique

Support for boards, targets and adapters comes as Tcl config scripts, and the list is huge. The same tool also handles boundary-scan playback through SVF and XSVF, not just debugging.

## Caveats

You need a compatible debug adapter and a board to do anything real, and the homepage shows no commands, so expect to work from the user guide.

## Links

- [OpenOCD homepage](https://openocd.org/)
- [OpenOCD User's Guide (HTML)](https://openocd.org/doc/html/index.html)
- [0.12.0 git change log (SourceForge)](http://sourceforge.net/p/openocd/code/ci/v0.12.0/log/?path=)
