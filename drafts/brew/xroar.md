---
name: xroar
title: XRoar
source: brew
category: take-things-apart
commitment: afternoon
tags: [6809, 8-bit, afternoon, debugging, emulator, retro]
homepage: https://www.6809.org.uk/xroar/
scout_score: 8
status: draft
---

# XRoar

**TLDR;** An emulator for the Dragon 32/64 and Tandy Colour Computers, with a GDB stub for stepping through 6809 machine code.

XRoar emulates the Dragon 32/64, the Tandy Colour Computers 1, 2 and 3, the Tandy MC-10, and some similar machines and clones. These are 8-bit home computers from the early 1980s, built around the Motorola 6809 processor. XRoar runs them on a modern desktop, showing the emulated display and playing the emulated sound.

It does not ship with the machines' firmware. You supply ROM images, which the homepage says can be extracted from real hardware or obtained from the Dragon Archive or the Color Computer Archive. Without them, the emulator is not much use. It also handles emulated disk and tape media, though the brief does not go into formats.

The project is a door into how small computers worked. The 6809 is a well-regarded 8-bit CPU, and the author also links asm6809, an assembler for writing Dragon machine code. Version 1.12 added GDB remote-debugging support for the emulated CPU, so you can attach a debugger and inspect code and hardware state in a machine that has no operating system to speak of. The homepage also offers XRoar Online, a browser version, so you can see a Dragon boot before installing anything.

## Install

```
brew install xroar
# You also need firmware ROM images for the machine you want to emulate. XRoar does not include them.
```

## Try this

```
xroar --help
```
Lists the command-line options, including machine selection and media options.

```
git clone https://www.6809.org.uk/git/xroar.git
```
Fetches the source from the author's site, if you want to read how a 6809 machine is emulated.

## What's unique

It covers both the Dragon and Tandy CoCo/MC-10 families in one actively maintained emulator, and offers GDB remote debugging of the emulated 6809, plus a browser version for trying it first.

## Caveats

Firmware ROMs are not included and must be found separately, and the GTK+ 2 interface is deprecated.

## Links

- [XRoar homepage](https://www.6809.org.uk/xroar/)
- [XRoar git repository](https://www.6809.org.uk/git/xroar.git)
