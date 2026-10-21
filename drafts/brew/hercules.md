---
name: hercules
title: Hercules
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, emulator, ibm, mainframe, operating-systems, retro]
homepage: https://sdl-hercules-390.github.io/html/
scout_score: 8
status: draft
---

# Hercules

**TLDR;** A software emulator of IBM System/370, ESA/390 and z/Architecture mainframes, so you can boot period operating systems like MVS or VM on an ordinary computer.

Hercules emulates the processor and I/O of IBM mainframes in software. You describe the virtual machine in a Hercules Configuration File, then start the emulator and operate it through an emulated console, including a built-in 3270 terminal. The result is a mainframe operator's console rather than a simplified simulator.

Disks and tapes are ordinary host files. The bundled utilities create and convert them: `dasdinit` makes emulated disk volumes, `maketape` and `hetinit` make tape images, and `tapecopy` and `dasdcopy` move data between formats. That is why the formula installs around fifty executables. Most are small tools for handling these image formats.

The project exists so hobbyists and systems programmers can run period mainframe software without IBM hardware. Its homepage quotes users on the nostalgia and learning value: "Never in my wildest dreams did I expect to see MVS running on a machine that I personally own." The door it opens is how a mainframe works. Channels, DASD volumes, tape datasets and operator consoles all work differently from a modern PC.

This SDL 4.x "Hyperion" build is a fork that describes itself as the only actively maintained version. It adds fixes and features such as QDIO/OSA networking and a redesigned I/O subsystem.

## Install

```
brew install hercules
# You still need a Hercules Configuration File and an operating system image to IPL. The README does not spell out first-run steps; see the Installation and Operation page.
```

## Try this

```
hercules --help
```
Prints the emulator's command-line options, a first look at how it is started.

```
dasdinit --help
```
Shows how to create an emulated DASD disk image file, the first step in building a virtual machine's storage.

```
maketape --help
```
Shows the options for creating a tape image file for the emulated machine.

## What's unique

It covers three generations of IBM mainframe architecture, from System/370 to 64-bit z/Architecture, and gives you a real 3270 operator console instead of a toy simulator.

## Caveats

You need to supply your own configuration file and operating system media, and the README gives no first-run walkthrough. The brief also could not confirm a recent release date.

## Links

- [SDL Hercules 4.x Hyperion homepage](https://sdl-hercules-390.github.io/html/)
- [Source code repository on GitHub (SDL Hyperion)](https://github.com/sdl-hercules-390/hyperion)
- [Hercules Installation and Operation (overview of building)](http://sdl-hercules-390.github.io/html/hercinst.html#install)
