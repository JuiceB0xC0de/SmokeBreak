---
name: robotfindskitten
title: robotfindskitten
source: brew
category: games
commitment: quick
tags: [ancient, game, quick, tui, zen]
homepage: https://robotfindskitten.org/
scout_score: 6
status: draft
---

# robotfindskitten

**TLDR;** A tiny zen terminal game where a robot walks a field of symbols looking for a kitten, ported to dozens of platforms since 1997.

robotfindskitten is a small terminal game. A robot, drawn as `@`, wanders a field of ASCII symbols looking for a kitten, drawn as `k`. The homepage calls it "Yet another zen simulation" and bills itself as "helping robots find kittens since 1997".

The homepage presents it as a joke that is also an art piece. The brief did not include a README or source, so the exact controls and gameplay details are not confirmed here. The premise is in the title.

The interesting part is its reach. The download index lists more than fifty directories of ports, from the 68000 and Amiga to TI calculators, NXT and Wii, plus Palm OS, Java, Python and PHP. It is a program small enough that nearly anyone can rewrite it for whatever machine they have. That makes it a gentle way into the culture of portable toy software and of treating a tiny joke as a long-running shared project.

## Install

```
brew install robotfindskitten
```

## Try this

```
robotfindskitten
```
Starts the game: a robot among a field of symbols, with a kitten somewhere out there.

```
robotfindskitten --help
```
Prints the available options, if the build supports them.

## What's unique

It is a single joke that has been ported to an enormous range of machines, including calculators and game consoles, and the homepage is itself an ASCII-art box with a symbol field and a cat.

## Caveats

Probably quiet rather than actively maintained: the download directory timestamps run from 2003 to 2014, and I could not verify controls or build details.

## Links

- [Homepage](https://robotfindskitten.org/)
- [Download index (all ports)](https://robotfindskitten.org/download)
