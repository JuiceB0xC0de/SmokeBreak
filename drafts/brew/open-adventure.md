---
name: open-adventure
title: open-adventure
source: brew
category: games
commitment: afternoon
tags: [afternoon, game, history, interactive-fiction, text-adventure]
homepage: http://www.catb.org/~esr/open-adventure/
scout_score: 7
status: draft
---

# open-adventure

**TLDR;** A faithful, authorized port of Colossal Cave Adventure, the 1970s cave-exploring text game that started a genre, playable as `advent` in your terminal.

Open Adventure is Colossal Cave Adventure, the game where you type short commands like "go north" and read what the cave says back. This is the 1995 430-point version, which the project calls Adventure 2.5. It is a forward port of the Crowther and Woods code to modern systems, not a rewrite.

The homepage describes it as "the last descendant of the original 1976 Colossal Cave Adventure worked on by the original authors - Crowther & Woods; it is shipped with their permission and encouragement." The aim is to keep a foundational game playable and buildable on current machines. The built program is called `advent`, the original PDP-10 name, and the project notes this avoids a collision with the BSD Games version.

Underneath it is a door into the history of interactive fiction. Nearly every text adventure, and a good part of how games talk to players, descends from this cave. The port is also a small lesson in software preservation: recent changes include removing the legacy 1-based indexing inherited from the Fortran-era code, which meant bumping the save-file format version.

## Install

```
brew install open-adventure
# Installs the `advent` executable. No accounts or hardware needed. If building from source instead, you need libedit, Python 3, and PyYAML.
```

## Try this

```
advent
```
Starts the game at the prompt. Type short commands and read the cave's replies.

```
advent --help
```
Shows the program's command-line options.

## What's unique

It is the preserved lineage of the original game, endorsed by its authors, ported carefully rather than reimplemented. Even the binary name follows the historical one.

## Caveats

Building from source needs Python 3 and libedit; the Homebrew formula handles that for you. The recent changes mention a code hardening pass done with ChatGPT, which some readers may want to weigh.

## Links

- [Project homepage](http://www.catb.org/~esr/open-adventure/)
- [Source repository on GitLab](https://gitlab.com/esr/open-adventure)
- [Installation instructions](http://www.catb.org/~esr/open-adventure/INSTALL.html)
