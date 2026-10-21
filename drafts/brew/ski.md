---
name: ski
title: ski
source: brew
category: games
commitment: quick
tags: [ancient, game, python, quick, tui, unix-history]
homepage: http://catb.org/~esr/ski/
scout_score: 6
status: draft
---

# ski

**TLDR;** A silly terminal skiing game where your jet-powered skis are on backwards, so you flee a Yeti while only seeing the slope behind you.

ski drops you onto an endless slope with jet-powered skis strapped on backwards. You cannot see what is ahead, only the ASCII slope drawn behind you. Each turn you type a single letter at a `?` prompt: turn, jump, teleport, launch an ICBM, summon the Fire Demon. A number before a command repeats it, so `4l` turns left four times.

The slope is read as characters. `.` is safe snow, `Y` is a tree and hurts, a blank space is bare ground that can make you fall, `#` is ice and stops you turning, and `A` is the Yeti, which crawls toward you one space per turn and grabs you within one space. Steer clear of it on a sunny day and it melts, though another turns up later. The run ends when something bad happens, and the score counts distance skied, jumps, Yetis melted and remaining health.

It is a revival of a classic Unix-era game, originally by Mark Stevans for Roy's Games, Inc. Eric S. Raymond wrote the Python implementation and added colour support and the invisible shell monster. The `!` command drops you into a Unix shell inside a space warp and returns you to the same spot afterward. The author's pitch is that the game proves you do not need fancy graphical user interfaces to have a good time.

## Install

```
brew install ski
```

## Try this

```
ski
```
Starts the game. You get the slope drawn behind you and a `?` prompt waiting for a command letter.

```
?
```
Typed at the game's prompt, not the shell. Shows the list of command letters.

```
4l
```
Typed at the game's prompt. Turns left four times in one go.

## What's unique

The skis-on-backwards premise makes you steer by looking behind you. The command list mixes nuclear ICBMs, hyperspace teleport, a Fire Demon and a shell escape, all in plain ASCII.

## Caveats

Terminal-only with no graphics, and the homepage asks for support via Patreon and SubscribeStar.

## Links

- [Homepage (catb.org)](http://catb.org/~esr/ski/)
- [Manual page (ski.html)](http://catb.org/~esr/ski/ski.html)
- [Project repository (GitLab)](https://gitlab.com/esr/ski)
