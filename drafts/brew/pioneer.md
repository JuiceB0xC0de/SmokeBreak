---
name: pioneer
title: Pioneer
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, gui, open-source, simulation, space]
homepage: https://pioneerspacesim.net/
scout_score: 6
status: draft
---

# Pioneer

**TLDR;** A free, open-source space sandbox where you fly between star systems, land on planets, and make a living by trading, smuggling, piracy, or bounty hunting.

Pioneer is a space adventure game set in the Milky Way at the turn of a future century. You explore star systems, land on planets, and decide how to earn a living: trading between systems, piracy, smuggling, bounty hunting, or missions for factions. The homepage says there are millions of star systems to visit.

The author's framing is an open-ended sandbox: "The universe is whatever you make of it." There is no single story to follow. The game is a loop of flying, docking, and choosing what kind of spacefaring life to lead.

The Homebrew package installs four executables. `pioneer` is the game. The other three, `editor`, `modelcompiler` and `savegamedump`, are named in the package but not described in the README. Going by their names, they look like tools for working with models and save files, which would fit the project's modding community. That is a guess from the names.

The project says it is "under constant development" and has "a friendly community of players, modders and developers around it." It is GPLv3, and the README is unusually explicit that it does not accept AI-generated code contributions, citing licensing.

## Install

```
brew install pioneer
# This is a graphical game with a window, not a terminal program. Prebuilt downloads are at https://pioneerspacesim.net/page/download/ and COMPILING.txt in the repo covers building from source.
```

## Try this

```
pioneer
```
Launches the game in a graphical window so you can start a new game and pick a starting system.

```
pioneer --help
```
Prints the command line options the game accepts.

```
savegamedump --help
```
Shows usage for the save game tool installed alongside the game.

## What's unique

It is a long-running, community-built open-source space sim with no scripted story, and its repo has a stated policy against AI-generated code contributions.

## Caveats

The brief found only weak evidence of recent activity (no release or commit dates), and the homepage and README disagree on the century of the setting.

## Links

- [Homepage](https://pioneerspacesim.net/)
- [GitHub repository](https://github.com/pioneerspacesim/pioneer)
- [Player wiki manual](https://wiki.pioneerspacesim.net/wiki/Manual)
- [Download page](https://pioneerspacesim.net/page/download/)
