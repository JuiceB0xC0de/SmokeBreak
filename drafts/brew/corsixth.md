---
name: corsixth
title: CorsixTH
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, gui, lua, reimplementation, simulation]
homepage: https://github.com/CorsixTH/CorsixTH
scout_score: 6
status: draft
---

# CorsixTH

**TLDR;** An open source rebuild of Theme Hospital, the 1997 hospital management sim, that runs on modern systems with zoom, 4K and a map editor.

CorsixTH is a reimplementation of Theme Hospital, the 1997 Bullfrog business sim in which you build and run a hospital full of absurd diseases. It is not an emulator or a repackaging. It is a new engine that plays the original game, and it runs on Windows, macOS, Linux and BSD.

It adds things the 1997 game never had: high resolutions, zooming, UI scaling, subtitles, more than 20 languages, custom levels and campaigns, custom music playback, and a built-in map editor. You can also build rooms while the game is paused.

The engine is mostly Lua, with the rest in C++. That makes it an approachable place to read how a classic management sim is put together, and the project invites contributors to fork it and start tinkering. The README says it uses graphics, sound and other data from the original game, so you need a copy of the original. The README's own words: "We use graphics, sound and other data from the original game."

The idea underneath is preservation by reimplementation. The old binary is replaced, the old assets are kept, and the game stays playable on current hardware.

## Install

```
brew install corsixth
You also need the original Theme Hospital data files, from an original CD or a download from GOG.com or EA. The wiki's Getting Started page covers first-run setup. Packaged builds also exist: Windows and macOS installers, a Linux AppImage, a Flatpak (com.corsixth.corsixth) and a Snap.
```

## Try this

```
CorsixTH
```
Launches the game. On first run you point it at your original Theme Hospital data files.

## What's unique

It is a full, actively contributed-to rebuild of a 1997 sim that keeps the original assets but adds modern display options, a map editor and custom campaigns.

## Caveats

It is not standalone, since it needs the original game's data files, and the README lists missing features such as multiplayer, AI hospitals and rats.

## Links

- [Homepage (GitHub repo)](https://github.com/CorsixTH/CorsixTH)
- [Getting Started wiki](https://github.com/CorsixTH/CorsixTH/wiki/Getting-Started)
- [Latest releases](https://github.com/CorsixTH/CorsixTH/releases/latest)
