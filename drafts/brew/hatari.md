---
name: hatari
title: Hatari
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, atari, demoscene, emulator, hardware-emulation, retro]
homepage: https://www.hatari-emu.org/
scout_score: 6
status: draft
---

# Hatari

**TLDR;** An Atari ST, STE, TT and Falcon emulator that copies the hardware closely enough to run old games and demo-scene tricks.

Hatari emulates the Atari ST family of home computers: the ST, STE, TT and Falcon. It runs on Linux, BSD, macOS, Windows and anything else SDL supports, and it can also run in a browser. The project's stated aim is to emulate the hardware "as close as possible so that it is able to run most of the old ST games and demos."

That goal separates it from emulators built mainly to give a good home for GEM applications. Hatari models things like raster interrupts, border effects and PSG sample sound, which are the tricks demo-scene programmers used to push the machine past what it was designed to do. Running a demo on it is a way to see how much software of that era depended on exact chip timing.

The ST and STE are the well-covered part. For the TT and Falcon, Hatari adds the Videl video chip and the DSP 56001, which the site calls still in development and experimental.

The installed tools hint at the surrounding workflow. There are helpers for building hard disk images, converting disk images (`zip2st`, `hmsa`), and profiling emulated programs (`hatari_profile`). Hatari can also mount a host directory as an ST drive, so you can move files in without building a disk image.

It will not boot without a TOS image, the Atari's operating system ROM. That cannot be shipped with Hatari, so you either dump one from your own Atari or use EmuTOS, a free replacement.

## Install

```
brew install hatari
You also need a TOS image before it will run: dump one from your own Atari, or use the free EmuTOS. The site suggests roughly 1 GHz or more for ST/STE emulation and over 2 GHz for Falcon.
```

## Try this

```
hatari --help
```
Lists the emulator's command-line options, including machine type and how to point it at a TOS image.

```
hatari-prg-args --help
```
Shows usage for the helper that launches Atari programs with arguments.

```
atari-hd-image --help
```
Shows how to create an Atari hard disk image to mount in the emulator.

## What's unique

Hatari puts hardware accuracy ahead of a comfortable GEM desktop, so games and demos that rely on raster and border tricks have a chance of working.

## Caveats

You must supply a TOS image (or use EmuTOS), TT and Falcon emulation is experimental, and the brief could not confirm how recently the project has been updated.

## Links

- [Hatari homepage](https://www.hatari-emu.org/)
