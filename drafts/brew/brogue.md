---
name: brogue
title: Brogue
source: brew
category: games
commitment: days-off
tags: [days-off, game, roguelike, sdl2, tui]
homepage: https://sites.google.com/site/broguegame/
scout_score: 7
status: draft
---

# Brogue

**TLDR;** A roguelike with no experience points: descend 26 randomly generated floors to fetch the Amulet of Yendor, surviving on what you find and how you use it.

Brogue is a single-player dungeon crawler. Each run generates a new dungeon, and your goal is to reach the 26th floor, take the Amulet of Yendor, and carry it back to the surface. You play with vi-keys (hjklyubn), the keypad, or the mouse. The `?` key opens a help screen.

The design choice that sets it apart is that your character does not level up. The original README says experience was removed "to reward exploration instead of combat". Power comes from items. Scrolls of Enchantment permanently improve one item of your choosing, staffs recharge over time, and allies can be won by freeing captives from the monsters holding them. Gold has no use except to set your score at death or victory.

The original game is by Brian Walker. The homepage now points players to Brogue: Community Edition (CE), a continuation that exists to "fix bugs and crashes", add quality-of-life features, and keep the game exciting. The idea underneath is that a game with few systems, all interacting, can be deep enough to replay for years. Every choice about where to put your enchantments shapes the whole run.

## Install

```
brew install brogue
# pulls in sdl2-compat and sdl2_image; graphical tiles are included and toggled with G
```

## Try this

```
brogue --help
```
Lists the command-line options the game supports.

```
brogue
```
Starts a new game with a freshly generated dungeon. Press ? for the help screen.

## What's unique

Character growth comes entirely from items rather than experience, and the item designs are unusually specific. Whips reach five spaces, flails strike as you step between adjacent cells, and searching takes five turns in a row.

## Caveats

The original homepage describes the older v1.7.5, the CE README warns CE "may differ" from the wiki, and I could not confirm which version Homebrew installs.

## Links

- [Original Brogue homepage (Google Sites)](https://sites.google.com/site/broguegame/)
- [Brogue: Community Edition on GitHub](https://github.com/tmewett/BrogueCE)
- [Brogue Wiki](https://brogue.fandom.com/wiki/Brogue_Wiki)
- [CE changes from original (wiki)](https://github.com/tmewett/BrogueCE/wiki/Changes-from-original)
