---
name: exult
title: Exult
source: brew
category: games
commitment: afternoon
tags: [afternoon, ancient, game, game-engine, gui, preservation, rpg]
homepage: https://exult.sourceforge.io/
scout_score: 5
status: draft
---

# Exult

**TLDR;** An open-source engine that runs Ultima VII, the early-1990s RPG, on modern systems by reading your own copy of the original game files.

Exult reimplements the Ultima VII game engine. It does not ship the game. You point it at the data, graphics, music and plot files from a legal copy of The Black Gate or its sequel Serpent Isle, and it runs them natively on current Windows, macOS and Android.

The project's stated reason is preservation: as computers change, classic games risk being lost. It describes Ultima VII as a game that "many consider to be one of the most immersive games ever produced". Keeping it playable means rebuilding the engine rather than emulating the old hardware around it.

That split between engine and data is the idea underneath. Because Exult has to read the original file formats, it has grown into a toolkit: Exult Studio, a level and content editor, plus GIMP and Aseprite plug-ins for the game's SHP graphics format. A community Ultima VI remake mod also runs on the engine. It is a good way to see how a game of that era was put together from data files and an engine that interprets them.

## Install

```
brew install exult
# The formula installs only the engine. You must supply your own legal copy of the Ultima VII game files.
# Audio settings live in ~/Library/Preferences/exult.cfg: set `driver` to `CoreAudio` for CoreAudio, and `use_oggs` to `yes` to use the audio pack.
```

## Try this

```
exult --help
```
Lists the command-line options the engine accepts.

```
exult
```
Starts the engine. With the original Ultima VII data in place, it loads the game.

## What's unique

It is a pure engine with no bundled assets, rather than a remake with new art. It has also grown an editor, graphics plug-ins, an Android port and a mod ecosystem around it.

## Caveats

It does nothing useful without your own legal copy of the Ultima VII data, and the project's news lists a few known issues, such as the game quitting instead of returning to the menu after the ending.

## Links

- [Exult homepage](https://exult.sourceforge.io/)
