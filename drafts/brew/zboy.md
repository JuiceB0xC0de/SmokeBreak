---
name: zboy
title: zBoy
source: brew
category: games
commitment: quick
tags: [emulator, gameboy, quick, retro, sdl, two-player]
homepage: https://zboy.sourceforge.net/
scout_score: 5
status: draft
---

# zBoy

**TLDR;** A small open-source Game Boy emulator that can link two virtual consoles over a LAN and rebuild hi-score tables for games with no battery save.

zBoy is an emulator for the original Game Boy (the DMG model), written by Mateusz Viste. It loads ROM files and plays them with keyboard, joypad, or both. It can save and load game state, take PCX screenshots, and emulate the battery-backed memory in cartridges that had one. Video can be scaled with Scale2x or Scale3x.

Two features set it apart. It emulates the link cable between two consoles, so two players can play head to head over a LAN. It also saves hi-scores for games that never had battery RAM and so could never keep their own tables. The homepage describes both features but not how they are implemented, so the internals are yours to find out.

The idea underneath is that a handheld from 1989 is a small, well-bounded machine, and emulating it is a good way to learn how hardware gets recreated in software. A link cable is a serial connection, and carrying it over a network shows how a physical protocol can be turned into packets.

zBoy ships no games, and the author says so. The site points to a public domain game pack for testing.

## Install

```
brew install zboy

This pulls in sdl2-compat. You supply your own ROM files. The homepage offers a public domain game pack for testing.
```

## Try this

```
zboy --help
```
Prints the available options, a starting point for loading a ROM and choosing scaling or controls.

## What's unique

It is one of the very few Game Boy emulators that emulate the link cable for two-player play over LAN. It also reconstructs hi-score saving for games with no battery RAM.

## Caveats

The homepage shows a copyright line of 2010-2020 and no release version or repository activity, so the current state is unconfirmed, and it does not describe a terminal interface.

## Links

- [zBoy homepage](https://zboy.sourceforge.net/)
