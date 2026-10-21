---
name: allureofthestars
title: Allure of the Stars
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, haskell, roguelike, squad, tactics]
homepage: https://allureofthestars.com/
scout_score: 6
status: draft
---

# Allure of the Stars

**TLDR;** A near-future sci-fi roguelike where you command a whole squad, with deterministic combat and bullets you can sidestep, written in Haskell.

Allure of the Stars is a turn-based roguelike built on the LambdaHack engine, written in Haskell. You control each member of a squad by hand. The homepage says the best tactic is often to "scout with only one character (a classic roguelike feel) and let others guard important areas".

The turns are fine-grained. Projectiles fly over time at different speeds, so you can sidestep them or shoot them down. Combat is deterministic: randomness comes only from AI decisions and procedural generation. Health barely regenerates, and each character has 10 equipment slots.

The design rule underneath it is that factions and actors all play by the same rules. Player and AI share the same field of view, skill checks, and use of equipment and terrain. Each faction also has one shared, unlimited inventory that sits at a physical place on the map, so it can be ransacked. Several levels advance at once while others are frozen, and all of them persist.

The author describes the goal as a roguelike that feels like a shared experience with trusted friends, fighting as one organism with little communication. The interface is deliberately sparse so your imagination does the sensory work, "like when reading a book, but with less words and more action."

## Install

```
brew install allureofthestars
# or play in the browser with no install: http://allureofthestars.com/play
```

## Try this

```
Allure --help
```
Lists the command-line options of the installed game executable.

```
Allure
```
Starts the game so you can try the squad-based play.

## What's unique

It combines per-character squad control, deterministic combat, dodgeable projectiles and faction inventories that exist as physical objects on the map. Player and AI follow identical rules, which is strict for the genre.

## Caveats

The brief could not confirm a source repository or recent release dates (the homepage copyright reads 2015-2021), and the game may have a steep learning curve; one quoted critic says "I have no idea what's going on".

## Links

- [Homepage](https://allureofthestars.com/)
- [Browser play](http://allureofthestars.com/play)
