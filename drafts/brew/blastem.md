---
name: blastem
title: BlastEm
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, emulator, genesis, gui, retro, sega]
homepage: https://www.retrodev.com/blastem/
scout_score: 6
status: draft
---

# BlastEm

**TLDR;** A Sega Genesis emulator built to be both fast and accurate, tuned to run demanding demos and accuracy tests on modest old hardware.

BlastEm emulates Sega's 16-bit and 8-bit consoles. The Genesis (Mega Drive outside North America) is the primary focus. Its homepage also lists the Sega CD, 32X, Master System, Game Gear, SG-1000, SC-3000, Sega Pico and Yamaha Copera.

The pitch is two goals held together: "fast enough for your old PC" and "accurate enough for the most demanding demos". The homepage says it was developed on a 2011 netbook-class laptop and still runs Genesis emulation at full speed there. It also says BlastEm was the first emulator to properly run the Titan Overdrive 2 demo.

The idea underneath is that accuracy matters most for software that pushes the hardware past what the manuals describe. Demos and synthetic test ROMs lean on exact timing between the CPUs, video chip and sound chips. An emulator that passes them is modelling the machine's behaviour closely, not just approximating what games usually do. That makes it a door into how a 1980s-90s console actually works.

The brief covers only the project's homepage, which is a marketing summary. It gives no setup steps or documentation, so what follows the install is for you to discover.

## Install

```
brew install blastem
# Needs a ROM image you supply yourself. The formula pulls in glew and sdl2-compat for graphics and windowing.
```

## Try this

```
blastem --help
```
Prints the command-line options, if the build supports it, so you can see what the emulator accepts.

## What's unique

It aims for demo-grade accuracy without needing a fast machine, and claims to be the first emulator to run Overdrive 2 properly.

## Caveats

The brief could not reach a README or source repository, so maintenance status and platform details are unconfirmed, and the accuracy claims are the project's own.

## Links

- [BlastEm homepage](https://www.retrodev.com/blastem/)
