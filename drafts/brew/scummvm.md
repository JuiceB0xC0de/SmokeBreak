---
name: scummvm
title: ScummVM
source: brew
category: games
commitment: afternoon
tags: [adventure, afternoon, game, gui, preservation, retro]
homepage: https://www.scummvm.org/
scout_score: 5
status: draft
---

# ScummVM

**TLDR;** ScummVM replaces the executables of hundreds of classic adventure games so LucasArts, Sierra and other old titles run natively on modern systems.

ScummVM is a program that runs classic graphical adventure and role-playing games, provided you already have their data files. You point it at a folder of original game data, and it plays the game using its own engine code instead of the executable the game shipped with. The homepage lists over 325 supported adventure games from studios such as LucasArts, Sierra On-Line, Revolution Software, Cyan and Westwood.

The idea underneath it is that a game is two things: data (art, scripts, sound) and an engine that interprets that data. Old engines were tied to hardware and operating systems that no longer exist. If you rewrite the engine and keep the data untouched, the game keeps working. The project's own words: "ScummVM is a complete rewrite of these games' executables and is not an emulator." It does not imitate an old machine. It reimplements the game logic.

The work is organised per game family. Each family has an engine, and games get added or fixed engine by engine. The 2026.4.0 release post says it added 194 newly supported games and 12 new engines. Some titles, such as The Colony and Dungeon Master, are in public testing and need a daily development build rather than the stable release.

The homepage frames the project as preservation and playability. It runs on Windows, Linux, macOS, iOS, Android, Switch and Dreamcast, among others.

## Install

```
brew install scummvm
# You also need the original game data files. The homepage suggests your old floppies, or a free copy of The Colony from ZOOM Platform.
```

## Try this

```
scummvm
```
Opens the graphical launcher, where you add a folder of game data and start playing.

```
scummvm --help
```
Lists the command-line options.

## What's unique

It reimplements the games' engines instead of emulating old hardware, which is how one program covers hundreds of titles across many platforms.

## Caveats

ScummVM does not ship any games, so you must already own or legally obtain the data files, and some titles need daily development builds.

## Links

- [ScummVM homepage](https://www.scummvm.org/)
