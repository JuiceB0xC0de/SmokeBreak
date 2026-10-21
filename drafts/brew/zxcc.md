---
name: zxcc
title: zxcc
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [8-bit, afternoon, cp/m, cross-compiler, emulator, retro]
homepage: https://www.seasip.info/Unix/Zxcc/
scout_score: 8
status: draft
---

# zxcc

**TLDR;** A CP/M 2/3 emulator for UNIX that lets eight-bit-era compilers and build tools run as ordinary command-line cross-compilers on a modern machine.

ZXCC emulates CP/M so that software written for 1970s and 80s eight-bit machines can run as a normal program on UNIX. Its stated main purpose is to let Hi-Tech C for CP/M work as a cross-compiler. It also runs the CP/M build tools MAC, RMAC, GENCOM and LINK.

The design is aimed at toolchains, not games or nostalgia. Two libraries do the work. CPMREDIR makes directories on the host look like CP/M drives, and ZXCC uses it for every drive. CPMIO handles terminal emulation (VT52, VT100, or native), with multiple modes modelled on MYZ80 under DOS.

The interesting idea is how little an operating system needs to be for a program to run. CP/M programs talk to a small set of system calls. If you emulate those calls and map the filesystem, a 40-year-old compiler runs unchanged and reads and writes your files. That makes it a way into how early compilers, linkers and assemblers were put together.

The two libraries are LGPL and can be used separately. The author also uses CPMREDIR in his JOYCE PCW emulator.

## Install

```
brew install zxcc
```

## Try this

```
zxcc --help
```
Asks the emulator for its usage text. The homepage does not document command-line use, so this is the safest first step.

```
zxc --help
```
Tries the wrapper installed alongside zxcc. The page does not confirm what it does, so check what it prints.

```
zxas --help
```
Tries the assembler front end listed in the package. Its behaviour is not described on the homepage.

## What's unique

It is a CP/M emulator built to run toolchains, not to play games. Its filesystem and terminal layers are split out as reusable LGPL libraries.

## Caveats

The homepage is dated 2013-12-28 and documents no command-line usage, so expect to figure out the tools yourself and bring your own CP/M software such as Hi-Tech C.

## Links

- [ZXCC homepage](https://www.seasip.info/Unix/Zxcc/)
