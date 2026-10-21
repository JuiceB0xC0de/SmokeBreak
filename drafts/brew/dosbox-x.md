---
name: dosbox-x
title: DOSBox-X
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, dos, emulator, gui, preservation, retro]
homepage: https://dosbox-x.com/
scout_score: 5
status: draft
---

# DOSBox-X

**TLDR;** A DOS emulator that aims past games: it emulates whole pre-2001 PCs, including PC-98 and Windows 9x guests, for preservation and testing.

DOSBox-X is a fork of DOSBox, taken from the DOSBox SVN Daum branch in mid-2011 and now a separate project. It runs DOS programs on modern Windows, Linux and macOS. It emulates PCs from the IBM PC/XT/AT class up to late-1990s machines, plus NEC PC-98, AX and DOS/V systems. The README says Windows 1.0 through ME can run as guests, with 3.x and 9x officially supported.

The author's complaint about the original is that it concentrates on games and uses game-oriented kludges. DOSBox-X instead makes changes that real DOS systems and non-game software need. The stated goal is accurate enough emulation for historical preservation, testing, and new DOS development.

The idea underneath is that a PC of that era is a pile of separate parts: CPU, disk controller, sound card, graphics card, network card. DOSBox-X lets you choose each one. It covers CPUs up to Pentium III and MMX, IDE, 3dfx Voodoo and Glide, NE2000 networking, and FluidSynth and MT-32 MIDI. Behaviour is set in a .conf file or command-line options, and there is a drop-down menu and a built-in configuration tool. Changing those settings and seeing what breaks is a good way to learn what the old hardware did.

The project is clear about its limits. It will not emulate Pentium 4 or later, post-2001 hardware, or Windows Vista and later, and it points to Bochs, QEMU, 86Box or PCem for those.

## Install

```
brew install dosbox-x
```

## Try this

```
dosbox-x --help
```
Lists the command-line options for the emulator.

```
KEYB /?
```
Typed at the DOSBox-X prompt, shows help for the keyboard-layout command.

```
CHCP /?
```
Typed at the DOSBox-X prompt, shows help for the codepage command.

## What's unique

Its scope is unusual: it aims to cover essentially every pre-2001 PC hardware scenario, including PC-98 and DOS/V, and to host Windows 9x guests. The README names this as its main departure from DOSBox.

## Caveats

The README says it is not a secure containment tool, so do not run it as root or Administrator; full FPU precision and cycle-accurate timing are not goals, and the main developer says he has limited time.

## Links

- [DOSBox-X homepage](https://dosbox-x.com/)
- [DOSBox-X Wiki](https://dosbox-x.com/wiki)
- [GitHub repository](https://github.com/joncampbell123/dosbox-x)
- [Feature Highlights (wiki)](https://dosbox-x.com/wiki/DOSBox%E2%80%90X%E2%80%99s-Feature-Highlights)
