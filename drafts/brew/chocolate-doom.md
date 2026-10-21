---
name: chocolate-doom
title: Chocolate Doom
source: brew
category: games
commitment: afternoon
tags: [afternoon, ancient, doom, game, preservation, source-port]
homepage: https://www.chocolate-doom.org/
scout_score: 5
status: draft
---

# Chocolate Doom

**TLDR;** A source port of Doom that tries to behave exactly like the 1993 DOS original, bugs included, and also runs Heretic, Hexen and Strife.

Chocolate Doom is a reimplementation of the Doom engine for modern machines. Unlike most ports, it does not add features. It aims to match the DOS executables, so the game looks, sounds and handles like the original. Its README says it aims for "accurate reproduction of the original DOS versions of the games, including bugs."

The bugs are kept on purpose. Vanilla Doom quirks that players and level designers have relied on for decades are preserved, and the ones deliberately left alone are documented in a NOT-BUGS file. It is also meant to stay compatible with DOS demo, configuration and savegame files, so a DOS default.cfg should work unchanged.

The idea underneath is preservation by reimplementation: rather than emulating a DOS machine, the engine is rewritten to reproduce the old program's behaviour. That makes it a good way to see what the original engine really did, and why fans and modders treat "vanilla" as a fixed target.

The package also installs Heretic, Hexen and Strife on the same engine, each with a setup tool, plus a server executable for multiplayer. Setup tools edit chocolate-doom.cfg. For total conversions, the -merge option merges a PWAD into the IWAD in memory, so the IWAD on disk is never modified.

## Install

```
brew install chocolate-doom
# Installs the engine only, with no levels. You must supply your own Doom IWAD, or find free levels online. The original levels are still under copyright.
```

## Try this

```
chocolate-doom-setup
```
Opens the setup tool to configure display, input, sound and music, saved to chocolate-doom.cfg.

```
chocolate-doom -merge thetc.wad
```
Plays a total conversion by merging the WAD into the main IWAD in memory, leaving the IWAD on disk untouched.

```
chocolate-doom -merge batman.wad -deh batman.deh vbatman.deh
```
Runs Batman Doom, merging the WAD and applying DeHackEd patches with -deh.

## What's unique

Most Doom ports add features, but this one deliberately removes the urge to improve anything. Fidelity to DOS behaviour, original bugs included, is the whole point.

## Caveats

It ships no levels, so you need your own IWAD or free levels, and the README admits some DOS behaviour is very hard to reproduce.

## Links

- [Chocolate Doom homepage](https://www.chocolate-doom.org/)
- [GitHub repository](https://github.com/chocolate-doom/chocolate-doom)
- [Issue tracker](https://github.com/chocolate-doom/chocolate-doom/issues)
