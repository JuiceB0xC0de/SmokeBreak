---
name: lcs
title: Liberal Crime Squad
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, oubliette, rpg, satire, strategy, terminal]
homepage: https://sourceforge.net/projects/lcsgame/
scout_score: 6
status: draft
---

# Liberal Crime Squad

**TLDR;** A satirical terminal strategy RPG where you recruit Elite Liberal radicals to stop the United States sliding into Arch-Conservatism.

Liberal Crime Squad is a console-based political role-playing and strategy game written in C++. You recruit a team of radicals and try to steer the country away from what the project calls a descent into Arch-Conservatism. The tone is satire throughout.

Its gameplay is, in the project's words, "based loosely on the classic 1983 RPG Oubliette." That puts it in a small lineage of text-mode games that turn a squad, a map of choices and a lot of consequences into a long campaign, with politics as the setting instead of dungeons.

One reviewer on the project page compares the developers' humor and thoroughness to NetHack, calling it "almost NetHack-esque DevTeamThinksOfEverything." The same reviewer says the source is manageable enough to contribute to, which makes it a possible door into reading an old C++ game codebase.

The project is old. The SourceForge page shows registration in 2007 and a last update in September 2015. The brief does not describe the controls or interface, so expect to learn them by playing.

## Install

```
brew install lcs
```

## Try this

```
crimesquad
```
Launches the game in your terminal so you can start recruiting your squad.

```
crimesquad --help
```
Asks the executable for its usage information, if it provides any.

## What's unique

It is a political satire built on the Oubliette lineage of squad RPGs, which is an unusual niche. A reviewer compares its thoroughness to NetHack.

## Caveats

The last SourceForge update was in 2015, the Homebrew formula is marked deprecated, and the brief found no README or documentation, so expect to figure out the controls yourself.

## Links

- [SourceForge project page](https://sourceforge.net/projects/lcsgame/)
