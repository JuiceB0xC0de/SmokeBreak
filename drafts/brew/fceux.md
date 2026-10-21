---
name: fceux
title: FCEUX
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, debugger, emulator, gui, nes, retro, reverse-engineering]
homepage: https://fceux.com/
scout_score: 5
status: draft
---

# FCEUX

**TLDR;** An NES/Famicom emulator whose debugger tools let you watch 8-bit programs run, one instruction at a time.

FCEUX is an NES/Famicom emulator. Homebrew describes it as an "All-in-one NES/Famicom Emulator" and installs a single executable, `fceux`. It is a graphical program built on Qt and SDL.

The scout notes say it includes debugger tools for watching 8-bit programs execute. That is the part worth a break. A console from the 1980s is small enough to hold in your head, so an emulator with a debugger turns a game into something you can step through and inspect, rather than just play.

The homepage could not be read when this entry was written, so the project's own account of why it exists is missing. Details about its tools, first-run steps and ROM handling are unverified here. Expect to find them in the app's menus and on the project site.

## Install

```
brew install fceux

It is a GUI application and needs a ROM file to run anything. You supply your own ROMs.
```

## Try this

```
fceux --help
```
Prints the command-line options the installed build supports.

## What's unique

Per the scout notes, its debugger tools for watching 8-bit programs execute set it apart from plain play-only emulators. That claim is unverified from the project's own pages.

## Caveats

The homepage was unreachable when this entry was researched, so project status, commands and docs are unverified, and you need your own ROMs.

## Links

- [Homepage](https://fceux.com/)
