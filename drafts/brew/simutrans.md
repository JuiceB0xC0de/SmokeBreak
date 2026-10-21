---
name: simutrans
title: Simutrans
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, gui, multiplayer, open-source, simulation, transport]
homepage: https://www.simutrans.com/
scout_score: 6
status: draft
---

# Simutrans

**TLDR;** A long-running open-source transport simulator where you build rail, road, ship and air networks, and swappable paksets turn one engine into many different games.

Simutrans is a freeware, open-source game in which you run a transport company. You connect cities, industries, public buildings and tourist attractions by rail, road, ship and air, and you move passengers, mail and goods between them. Maps can be any size and need not be square. It has a graphical front end, and it can run multiplayer, with a server that friends join.

The idea underneath it is the pakset. A pakset is a separate bundle of graphics and data: objects, buying prices, maintenance costs, themes. The engine does not ship with one baked in. Swapping the pakset changes the gameplay, and the project puts it this way: "Every pakset is a new game." The same executable can therefore be a different economy and a different era depending on what you point it at.

The project is old. It began in 1997 under Hansjörg Malthaner, who retired around 2004, and a community team has maintained it since. The homepage currently lists version 125.0. The community still asks for help: "Simutrans is always looking for artists!" The brew formula also installs makeobj and nettool. The brief does not describe them, so check their --help output to see what they do.

## Install

```
brew install simutrans
# Paksets are not bundled with the code and carry their own licenses. You need at least one pakset to play. Get one from the homepage download or Steam.
```

## Try this

```
simutrans --help
```
Lists the command-line options of the game.

```
makeobj --help
```
Shows usage for the second installed executable. The brief does not describe it, so this is the way to find out what it does.

```
nettool --help
```
Shows usage for the third installed executable. The brief does not describe it either.

## What's unique

One engine runs many different games, because each pakset carries its own graphics, prices and rules. It is a 1990s-era transport sim that is still maintained by a community.

## Caveats

Paksets are required to play and are separate from the code, and the brief does not confirm that the brew formula fetches one. The README also says most people should use the stable release rather than nightly builds.

## Links

- [Simutrans homepage](https://www.simutrans.com/)
- [Simutrans Wiki](https://wiki.simutrans.com)
- [Steam store page](https://store.steampowered.com/app/434520/Simutrans/)
