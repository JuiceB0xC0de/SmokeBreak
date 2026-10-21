---
name: instead
title: INSTEAD
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, game-engine, interactive-fiction, lua, sdl, text-adventure]
homepage: https://instead.hugeping.ru/
scout_score: 6
status: draft
---

# INSTEAD

**TLDR;** A small Lua-driven interpreter for text adventures from the Russian interactive fiction scene. Hand it a zipped game and it plays.

INSTEAD is an interpreter for text adventure games. It loads a game from a folder or a zip archive and plays it in a window with text, and optionally pictures and sound. The homepage places the genre somewhere between interactive literature, visual novels and classic point-and-click adventures. It also says the engine can serve as a simple 2D engine.

Games are written in Lua. The engine is small and the authoring format is open: a game is a plain script plus assets, not a compiled binary. You can unzip a game into `~/.instead/games/`, pass a zip on the command line, or press F4 inside the program to pick a file.

The project comes out of the Russian-language interactive fiction community, and that shows. The homepage and most documentation are in Russian, and the homepage claims good Russian-language documentation for authors. It also mentions a parser layer called Metaparser 3, though the brief did not cover it. The README is in English but terse. Developer docs ship with the distribution in a `doc/` directory.

The idea underneath is that a whole game can be a readable script that a tiny runtime interprets. That makes it a way into how interactive fiction engines are built, and into a corner of the genre that most English-language players have never seen.

## Install

```
brew install instead
# Needs a game to play: INSTEAD does not ship with one in the brief. Get a game zip from the project site or the community.
```

## Try this

```
instead <game.zip>
```
Runs a zip-packed INSTEAD game directly, with no unpacking needed.

```
instead
```
Opens the interpreter without a game; press F4 to pick a game file from a dialog.

```
instead --help
```
Lists the command-line options.

## What's unique

Games are plain Lua scripts in folders or zips, so the engine stays small and the format is open. It is also a window into a Russian-language interactive fiction scene.

## Caveats

The homepage and most documentation are in Russian, master builds only against SDL3 (SDL2 users need a separate branch), and you must find games to play yourself.

## Links

- [Homepage (Russian)](https://instead.hugeping.ru/)
- [GitHub repository and README](https://github.com/instead-hub/instead)
- [Documentation](https://instead-hub.github.io/#doc)
