---
name: gpsim
title: gpsim
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, debugger, hardware, microcontroller, pic, simulation]
homepage: https://gpsim.sourceforge.net/
scout_score: 7
status: draft
---

# gpsim

**TLDR;** A simulator for Microchip PIC microcontrollers that runs real firmware on a virtual chip with simulated pins, LEDs, switches and an LCD, debuggable like gdb.

gpsim loads a PIC program and runs it on a software model of the chip. The model covers the core, the I/O pins and the internal peripherals. You get a gdb-style command line, plus a GTK interface with a register viewer, source browser, breadboard viewer and scope viewer. Breakpoints, single-stepping, disassembly and memory editing are all there.

The author's stated goal is accuracy: gpsim "has been designed to be as accurate as possible", so you can test a PIC "the same way you would in the real world". It also aims to offer debugging features usually found only in in-circuit emulators. One example is a trace buffer that, in the homepage's words, "tracks every action of the simulator (whether you want it or not)". Another is breakpoints that fire on register read and write values.

The underlying idea is that a microcontroller is a small deterministic machine, and you can watch it work without owning the chip. Peripherals and outside hardware are modelled as stimuli and loadable modules wired to the simulated pins. The homepage lists pull-up and pull-down resistors, USART, switches, logic gates, LEDs, a rotary encoder, an I2C EEPROM and an LCD. You can step through firmware and see exactly which register change lights a pin.

## Install

```
brew install gpsim
```

## Try this

```
gpsim --help
```
Prints the command-line options so you can see how to load a program.

```
gpsim
```
Starts the simulator. Its prompt is where you issue commands.

```
processor list
```
Typed inside gpsim, lists the supported PIC processors. The homepage calls this the best way to check.

## What's unique

It aims for chip-level accuracy and gives you in-circuit-emulator-style tools, such as an always-on trace buffer and value-based breakpoints, with no hardware attached.

## Caveats

The homepage is dated 2017 and shows no recent release, the processor list stops at several 2010-era chips, and the author says "gpsim is not fancy, but it's improving."

## Links

- [gpsim homepage](https://gpsim.sourceforge.net/)
