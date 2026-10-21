---
name: netris
title: netris
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, multiplayer, ncurses, network, tui]
homepage: https://packages.debian.org/sid/netris
scout_score: 5
status: draft
---

# netris

**TLDR;** A two-player terminal Tetris played over a network, where clearing lines sends garbage rows to your opponent, with a documented protocol for writing bots.

Netris is a free, networked variant of Tetris that runs in the terminal using ncurses. Two players face each other over a network. Clear two or three lines with one piece and the opponent gets one or two unfilled lines pushed onto the bottom of their board. Clear four at once and they get four.

The single-player mode is an afterthought. In the author's words, it "is a tad boring at the moment because it never gets any faster and there's no scoring." The game is meant for head-to-head play.

The odd part is the robot hook. The package description says this version "at least partially supports robots," with the protocol described in the documentation and a sample robot in the examples. That turns a small old game into a way to write a program that plays Tetris against a person or another program, which is a good excuse to learn how a game talks to its clients.

The brief comes from the Debian package page, not the upstream project, so details such as the network transport and the protocol itself are not covered here. Those would be the first things to read in the installed documentation.

## Install

```
brew install netris
```

## Try this

```
netris --help
```
Prints the program's usage and options, a starting point for finding out how to start or join a two-player game.

## What's unique

It is an old-school two-player terminal Tetris with garbage-line attacks and a documented robot protocol with a sample bot, which is rare for a game this size.

## Caveats

Single-player mode never speeds up and has no scoring, robot support is only partial, and upstream activity is unknown since the brief came from a Debian package page.

## Links

- [Debian package page (homepage)](https://packages.debian.org/sid/netris)
