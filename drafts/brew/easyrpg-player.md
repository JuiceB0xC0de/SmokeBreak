---
name: easyrpg-player
title: EasyRPG Player
source: brew
category: games
commitment: afternoon
tags: [afternoon, emulation, game, gui, interpreter, retro, rpg-maker]
homepage: https://easyrpg.org/
scout_score: 5
status: draft
---

# EasyRPG Player

**TLDR;** An open-source interpreter that runs RPG Maker 2000 and 2003 games on modern systems, and in a browser, without the original engine.

EasyRPG Player plays games made with RPG Maker 2000 and 2003, plus games in the EasyRPG format. You point it at an existing game project folder and it draws the game on screen with SDL. Audio, fonts and images come from a set of supporting libraries. It ships no games of its own.

To read the original game data it uses liblcf, a parser for the engine's file formats. The Player then runs the game logic and rendering itself, so the game's own data is used as is, with no port or re-export. The README also describes an Emscripten target, which is how the browser version is built.

It is the playback half of the wider EasyRPG Project, a community effort to build a free, open-source tool compatible with RPG Maker 2000/2003 games. The homepage pitch is "Play your own RPG games anywhere". The underlying idea is rebuilding a closed, aging engine from its data formats so the games outlive the platform they were made for.

## Install

```
brew install easyrpg-player
# You must supply your own RPG Maker 2000/2003 game folder (the one containing RPG_RT.exe). The Player includes no games.
```

## Try this

```
easyrpg-player --help
```
Lists the command-line options the Player accepts.

```
easyrpg-player
```
Run from inside an RPG Maker 2000 or 2003 game folder (next to RPG_RT.exe), it starts that game in a window.

## What's unique

It runs the original game data of a mostly forgotten engine instead of requiring a port, and the same codebase can also target a web page.

## Caveats

You have to bring your own RPG Maker 2000/2003 game, and I could not confirm the date of the latest release, though daily CI builds and SDL3 support suggest it is maintained.

## Links

- [Project homepage](https://easyrpg.org/)
- [GitHub repository (Player)](https://github.com/EasyRPG/Player)
- [Documentation wiki](https://wiki.easyrpg.org)
- [Daily builds (CI)](https://ci.easyrpg.org/view/Player/)
