---
name: open-simh
title: Open SIMH
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, emulation, history, pdp-11, simulation, unix, vax, vintage]
homepage: https://opensimh.org/
scout_score: 8
status: draft
---

# Open SIMH

**TLDR;** A family of simulators that boot historic computers like the PDP-8, PDP-11 and VAX in software, so their original operating systems run unchanged.

Open SIMH is one framework with many machine-specific simulators. Each one emulates the CPU and devices of a single historic machine, such as a PDP-1, PDP-8, PDP-10, PDP-11, VAX, Altair or SDS 940. The original operating system and software then run as they did on the real hardware. The homepage notes that Version 7 Unix, released in 1979, "runs unchanged today on SimH".

The simulators share a command layer called SCP. At its `sim>` prompt you attach disk and tape images to simulated devices, boot, set breakpoints, and inspect the machine with SHOW and HELP. Console I/O goes to your terminal or to a TELNET port, and some simulators can open an SDL2 video window. Scripting is built in: DO files with labels, GOTO, IF and ON error traps, plus EXPECT and SEND for automating a login prompt.

The homepage describes the aim as preserving the knowledge held in old software by letting people execute and experience it on simulated original hardware. SIMH was started by Bob Supnik, originally at Digital Equipment Corporation, and extended by many contributors. This Open SIMH repository dates from a split from an earlier codebase in May 2022.

The idea underneath is that a computer is a specification you can run. Once a machine is simulated, its operating system, its quirks and its front-panel conventions become things you can poke at, and the SHOW commands help you see what the hardware was made of.

## Install

```
brew install open-simh
# Ethernet and video support rely on host libraries (vde, libpcap, SDL2). You also need disk or tape images of the operating system you want to boot, which the package does not supply.
```

## Try this

```
pdp11 --help
```
Starts the PDP-11 simulator binary; the brief does not confirm that this flag is supported, so start it without arguments for the sim> prompt if it fails.

```
HELP dev
```
At the sim> prompt, shows built-in help for a device; HELP dev ATTACH and HELP dev REGISTERS go deeper.

```
SHOW FEATURES
```
At the sim> prompt, lists the devices and features of the running simulator.

## What's unique

It covers dozens of machines under one command interface, including rarities like the SDS 940, Sigma and AT&T 3B2 families. It runs the original period software unchanged rather than imitating it.

## Caveats

The package installs only the simulators; you have to find bootable disk or tape images yourself, and the brief could not confirm recent release or commit dates.

## Links

- [Open SIMH homepage](https://opensimh.org/)
- [Source repository (README)](https://github.com/open-simh/simh)
- [SIMH v4.0 status and command reference](https://github.com/open-simh/simh/blob/master/SIMH-V4-status.md)
