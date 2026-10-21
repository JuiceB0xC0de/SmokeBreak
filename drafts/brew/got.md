---
name: got
title: Game of Trees (got)
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, git, openbsd, tui, version-control]
homepage: https://gameoftrees.org/
scout_score: 6
status: draft
---

# Game of Trees (got)

**TLDR;** A version control system from OpenBSD developers that trades Git's flexibility for simplicity while keeping Git repositories as its storage format.

Game of Trees, or Got, is a version control system that, in its own words, "prioritizes ease of use and simplicity over flexibility." It stores everything in ordinary Git repositories, so the same checkout can be worked on with Got and with Git. Where Got lacks a feature, Git is still there to fill the gap.

It grew out of OpenBSD. The homepage says it is developed on OpenBSD by OpenBSD developers and other contributors, mainly for their own version control needs, and later used more widely by Unix-like users. The page opens with a quip from tedu@: "No mention of openbsd on the internet is complete without a long thread about source control migration."

The underlying idea is that you can design a different tool on top of an existing storage format. Because the on-disk data is Git's, adopting Got does not mean migrating history. You get a smaller, more opinionated interface to the same repository. The formula also installs more than a client: gotd is a hosting daemon, gotwebd a web frontend, and tog a terminal interface. Reading how a small project rethinks a crowded category is the draw.

## Install

```
brew install got

The homepage points macOS users to a 'Portable version' page. The portable build is secondary to the OpenBSD one. Git is still needed for anything Got has not implemented.
```

## Try this

```
got --help
```
Lists the Got subcommands, giving a quick sense of how small the command set is next to Git's.

```
tog --help
```
Shows the options for tog, the terminal interface that ships with Got.

```
gotd --help
```
Shows how to run the hosting daemon that serves repositories.

## What's unique

Got deliberately gives up flexibility for simplicity, and it keeps Git repositories as its on-disk format, so it can be adopted without moving any data. It also ships its own hosting daemon and web frontend.

## Caveats

The main audience is OpenBSD developers, the portable builds are secondary, and Got is not a full Git replacement.

## Links

- [Homepage](https://gameoftrees.org/)
