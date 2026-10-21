---
name: bochs
title: Bochs
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, bios, bootloader, emulation, reverse-engineering, x86]
homepage: https://bochs.sourceforge.io/
scout_score: 7
status: draft
---

# Bochs

**TLDR;** Bochs is a software emulator of an entire x86 PC, CPU, devices and BIOS included, built for accuracy over speed.

Bochs emulates an Intel x86 PC in C++. It models the CPU, memory, common I/O devices and a custom BIOS, so an operating system such as Linux, DOS or Windows can boot inside a window on your machine. It can be built to emulate CPUs from the early 386 up to recent x86-64 Intel and AMD parts.

The key distinction is that Bochs is an emulator, not virtualization. Products like VirtualBox and VMware run guest code directly on the host CPU. Bochs interprets every instruction in software. In the project's words: "Bochs' emulation provides a controlled, accurate execution environment, at the cost of speed/performance." The README says this makes it portable across host architectures (x86, ARM and MIPS are mentioned).

The README says it is aimed at developing operating systems and bootloaders, running very old mission-critical software, and reverse-engineering system-level code. Because the whole machine is a program you can inspect, a PC stops being a black box. The scout notes a built-in debugger for stepping through BIOS and boot code, but the pages read for this entry do not mention one, so check the user guide before counting on it.

The install also gives you `bximage`, which is presumably the tool for making disk images. The sources read do not describe it, so look at its `--help`.

## Install

```
brew install bochs
```

## Try this

```
bochs --help
```
Lists the command-line options for the emulator.

```
bximage --help
```
Shows the options for the companion tool that ships with Bochs, which is meant for disk images.

## What's unique

It interprets every instruction of a whole PC in software, so it is deterministic and portable across host architectures, unlike the virtualization products it is often compared to.

## Caveats

It is slower than virtualization, the project says its bug tracker holds issues from incomplete device models (VGA, IDE, network card and others), and its disk image collection is out of date.

## Links

- [Homepage](https://bochs.sourceforge.io/)
- [Bochs GitHub repository](https://github.com/bochs-emu/Bochs)
- [User guide](https://bochs.sourceforge.io/cgi-bin/topper.pl?name=New+Bochs+Documentation&url=https://bochs.sourceforge.io/doc/docbook/user/index.html)
- [Virtualization without direct execution paper (ISCA-35 workshop)](https://bochs.sourceforge.io/Virtualization_Without_Hardware_Final.pdf)
