---
name: yaze-ag
title: yaze-ag
source: brew
category: take-things-apart
commitment: afternoon
tags: [8-bit, afternoon, cp/m, emulator, retro, z80]
homepage: https://agl.yaze-ag.de/
scout_score: 7
status: draft
---

# yaze-ag

**TLDR;** A Z80 CPU emulator that boots real CP/M 2.2 and 3.1 in your terminal, with undocumented opcodes and adjustable clock speed.

YAZE-AG (Yet Another Z80 Emulator, by Andreas Gerlich) emulates the Z80, the 8-bit processor behind a generation of home computers and CP/M business machines. It grew out of yaze-1.10 and adds CP/M 3.1 support. The homepage says it is "designed to provide an exact simulation of the Z80 microprocessor".

The author's first line is blunt: "YAZE-AG is a Z80-CPU-Emulator and NOT a CP/M-Emulator!" You supply an operating system, either original CP/M or a replacement such as ZPM3N10 or Superdos, plus disk images in the .ydsk format. The `cdm` utility manages those images. Host directories can be mounted as CP/M drives, and the R.COM and W.COM utilities move files between the host and the emulated machine.

Under the hood is a Z80 core with an emulated memory management unit, built from Michael Haardt's page-table idea. A custom BIOS provides CP/M 3.1 features such as date, disk change and multi-I/O. The emulator also handles undocumented opcodes and can be throttled to a chosen clock speed, so software written for a 4 MHz machine runs at the speed its authors expected.

The door it opens is old 8-bit computing: a whole operating system, its tools and its software, small enough to understand, running on a CPU whose every instruction you can study.

## Install

```
brew install yaze-ag
# You also need a CP/M boot file (yaze-cpm3.boot or yaze.boot) and disk images. Start with the `yaze` script, which drives `yaze_bin`. No accounts or extra hardware needed.
```

## Try this

```
yaze
```
Starts the emulator through its wrapper script, which drives yaze_bin, and boots into the emulated CP/M session.

```
sys clock 4000
```
At the emulator's monitor, limits the CPU to 4.0 MHz so games written for that clock run at their original speed.

```
sys clock 0
```
Removes the speed limit and runs the emulated Z80 flat out.

## What's unique

It emulates undocumented Z80 opcodes and lets you set the clock speed to match original hardware. It also ships BOOTSYS, which restarts CP/M 3.1 from inside CP/M.

## Caveats

The author calls 2.51.3 (February 2022) the final release and is adding no more features, and it is a bare CPU emulator that needs a CP/M boot file and disk images supplied by you.

## Links

- [Project homepage](https://agl.yaze-ag.de/)
- [ZSM4 Macro Assembler (bundled, GPLv2)](https://github.com/hperaza/ZSM4)
- [Cpmtools (reading other floppy formats)](http://www.moria.de/~michael/cpmtools/)
