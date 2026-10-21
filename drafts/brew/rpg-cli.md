---
name: rpg-cli
title: rpg-cli
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, rpg, rust, shell, tui]
homepage: https://olano.dev/blog/deconstructing-the-role-playing-videogame/
scout_score: 6
status: draft
---

# rpg-cli

**TLDR;** A tiny JRPG where cd is the movement command: the deeper you wander from home, the tougher the monsters, and your filesystem becomes the dungeon.

rpg-cli is a minimalist role-playing game written in Rust. You play it with ordinary shell commands. `cd` moves the hero, `ls` looks for treasure chests, `buy` lists the shop, and `todo` shows a quest checklist. Output is a plain text status block with HP, MP, XP, stats, equipment and gold. Distance from your home directory sets the difficulty, so farther directories hold tougher enemies and better loot.

The author, Facundo Olano, wanted to strip a JRPG down to its mechanics, "the simplest thing that could possibly pass as a video game." The command line was the narrowest interface he could think of. In his words, "a classic JRPG is pure mechanism, a kind of puzzle." Battles are fully automatic, borrowing the auto-battle button from Suikoden 2. Each side acts by its speed stat, and the hero attacks unless HP is low and a potion is on hand. Stats are cut down to HP, strength and speed, and gear is generic and level-based (sword[1], sword[5]), so better equipment simply replaces worse.

There is a neat Unix lesson underneath. A program cannot change its parent shell's directory, so the game keeps its own record of where the hero is. A small shell function calls rpg-cli, then runs `cd` to whatever `rpg-cli pwd` reports. The README also offers a hardcore variant that overrides the built-in `cd`, so every directory change can start a fight.

Death is permanent. There is no save and reload, but a tombstone stays in the directory where the hero died. A new hero who walks there can recover the gold, items and equipment.

## Install

```
brew install rpg-cli
# Then add a wrapper function to your shell rc file so the shell follows the hero:
rpg () { rpg-cli "$@"; cd "$(rpg-cli pwd)"; }
# Prebuilt binaries and `cargo install` (needs a Rust toolchain) are also options. Fish users: see the shell integration guide.
```

## Try this

```
rpg reset
```
Re-rolls the hero with new random stats, then you can run `rpg` to see the new character.

```
rpg cd dev/
```
Moves the hero into a subdirectory, possibly triggering random battles along the way.

```
rpg buy
```
Lists what the home directory shop sells, with gold prices: sword, shield, potion, remedy and escape.

## What's unique

Using `cd` as the way to explore a dungeon, with difficulty set by distance from home, is an unusual framing that is hard to find elsewhere. Auto-battle and three stats keep it very small.

## Caveats

Death is permanent and the game is hard to play well; the README warns that going too far without healing will likely kill your hero. The cd override can confuse other shell habits, and the unsigned macOS release binary needs right-click, then Open.

## Links

- [Homepage (blog post: Deconstructing the Role-Playing Video Game)](https://olano.dev/blog/deconstructing-the-role-playing-videogame/)
- [GitHub repository and README](https://github.com/facundoolano/rpg-cli)
- [GitHub releases (prebuilt binaries)](https://github.com/facundoolano/rpg-cli/releases/latest)
- [Shell integration guide](https://github.com/facundoolano/rpg-cli/blob/main/shell/README.md)
