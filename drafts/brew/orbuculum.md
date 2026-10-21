---
name: orbuculum
title: Orbuculum
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, arm, debugging, embedded, firmware, needs-hardware, tracing]
homepage: https://github.com/orbcode/orbuculum
scout_score: 6
status: draft
---

# Orbuculum

**TLDR;** A crystal ball for microcontrollers: command-line tools that read the trace pins of an Arm Cortex-M chip and show printf text, profiles and instruction trace while firmware runs.

Orbuculum is a set of command-line tools for decoding what an Arm Cortex-M CPU sends out of its trace pins. That means SWO (serial wire output, UART or Manchester encoded) and, with ORBTrace hardware, the parallel TRACE pins. The data arrives through a debug probe such as a Black Magic Probe, a SEGGER J-Link, an FTDI or USB serial adapter, OpenOCD or PyOCD, or an ORBTrace Mini. It can also be read from a saved raw file.

The design is a mux with clients. The `orbuculum` mux talks to the probe and offers a network feed that any number of clients can connect to. Clients then each do one job: `orbcat` prints ITM text channels like a serial console, `orbtop` samples the program counter and totals time per function, `orbstat` gathers statistics, `orbmortem` works with instruction trace, and `orbzmq` republishes channels over ZeroMQ. Since 2.2.0 the feed uses orbflow, a COBS-framed, sequenced packet protocol.

The idea underneath is observing a running chip without stopping it or adding much load. The README says an Orbuculum is a crystal ball, 'used for seeing things that would be otherwise invisible'. The mux is also built to survive probe and target disconnects and restarts, which happen constantly on a real bench.

## Install

```
brew install orbuculum
Needs a supported debug probe and a Cortex-M target configured to emit SWO or TRACE. That is usually done from gdb with Support/gdbtrace.init, or from firmware code via the libtrace library. Without hardware you can only work from a saved raw capture.
```

## Try this

```
orbuculum --monitor 1000
```
Starts the mux, which picks up a Black Magic Probe or ORBTrace Mini automatically and reports link status every 1000 ms.

```
orbcat -c 0,"%c"
```
Prints ITM channel 0 as characters on stdout, mirroring the text the target sends on that channel.

```
orbtop -e ~/Develop/STM32F103-skel/ofiles/firmware.elf
```
Samples the program counter and totals time per function, using your own firmware ELF to resolve symbol names.

## What's unique

Any number of clients can read one trace feed, and the same clients work against live hardware or a recording. An ORBTrace Mini FPGA probe can also strip TPIU framing on the device itself to save bandwidth.

## Caveats

It needs a supported debug probe and a configured Cortex-M target; parallel trace (ETM) support is beta, and ETM4 decode in orbmortem is experimental.

## Links

- [GitHub repository (homepage)](https://github.com/orbcode/orbuculum)
- [GitHub releases](https://github.com/orbcode/orbuculum/releases)
- [Orbcode project site](https://www.orbcode.org)
- [Orbcode Discord](https://discord.gg/P7FYThy)
