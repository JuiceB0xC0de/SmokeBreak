---
name: dosbox-staging
title: DOSBox Staging
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, audio, dos, emulator, games, retro]
homepage: https://dosbox-staging.github.io/
scout_score: 6
status: draft
---

# DOSBox Staging

**TLDR;** A modern DOSBox fork that runs old DOS games and programs in a window, with CRT shader emulation and period sound hardware built in.

DOSBox Staging emulates a complete DOS-era PC on a modern machine. You point it at a DOS program or game and it gives you an emulated machine with video, sound and mouse input. It reads DOSBox-style configuration files, and the README calls it a "(mostly) drop-in replacement for older DOSBox versions".

The project describes itself as "a modern continuation of DOSBox with advanced features and current development practices." Its extras are mostly about making old software look and sound the way it once did. It advertises zero-config CRT and scanline display emulation that picks a shader based on the emulated video mode and your host resolution. It also lists a long run of period sound hardware: Roland MT-32 and SC-55, PC speaker, Covox, Gravis UltraSound and more. There is also an HTTP API for remote control and tools.

The larger idea is that a whole computing environment can be preserved as software. Once you have a DOS machine in a window, you can poke at how people ran programs from a different era: boot prompts, config files, sound card setup, and software written directly against the hardware.

## Install

```
brew install dosbox-staging
# Homebrew lists the executable as dosbox-staging. The project's own site also offers stable builds for Windows, macOS and Linux.
# You supply your own DOS software to run.
```

## Try this

```
dosbox-staging --help
```
Prints the command-line options so you can see what the emulator accepts.

## What's unique

Compared with plain DOSBox, it picks a CRT-style shader automatically from the video mode and ships emulation for a wide range of period sound hardware. It also offers an HTTP API for remote control.

## Caveats

It is only mostly drop-in compatible with older DOSBox configurations, and the brief shows no release or last-commit dates, so exact recency is unknown.

## Links

- [Project website](https://dosbox-staging.github.io/)
- [Getting started guide](https://www.dosbox-staging.org/getting-started/)
- [Source repository](https://github.com/dosbox-staging/dosbox-staging)
- [Development builds](https://www.dosbox-staging.org/download/development-builds/)
