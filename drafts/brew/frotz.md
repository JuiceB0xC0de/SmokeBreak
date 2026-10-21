---
name: frotz
title: Frotz
source: brew
category: games
commitment: quick
tags: [ancient, game, infocom, interactive-fiction, quick, terminal, z-machine]
homepage: https://661.org/proj/if/frotz/
scout_score: 7
status: draft
---

# Frotz

**TLDR;** A small C interpreter that runs Infocom's classic text adventures and other Z-machine story files in your terminal.

Frotz is an interpreter for Z-machine story files, the format Infocom used for its text adventures and that many later interactive fiction authors adopted. You hand it a story file, it runs the game in the terminal, you type commands, and it prints the replies. The project describes itself as "An interpreter for all Infocom and other Z-machine games" and is framed as a reference implementation of Graham Nelson's Z-machine standard 1.0.

The idea underneath is that Infocom did not ship native programs. It shipped games as bytecode for a small virtual machine, and any platform with an interpreter could run them. Frotz is that interpreter, ported to Unix so the old games run on modern systems. Once you have it, the same trick opens the whole world of interactive fiction: any Z-code file from the Interactive Fiction Archive plays the same way.

The package installs three binaries. frotz is the normal curses terminal interface, dfrotz is for dumb terminals and plain piped text, and sfrotz adds sound through SDL. The README says it plays all Z-code games including the rarely supported V6 format, and it reads config files.

Frotz does not include any games. You need to get a story file separately, for example from the Interactive Fiction Archive.

## Install

```
brew install frotz
# No games are included. Download a Z-code story file (for example from the Interactive Fiction Archive) to play.
```

## Try this

```
frotz --help
```
Lists the command-line options for the terminal interpreter.

```
dfrotz --help
```
Shows the options for the plain-text build, which suits pipes and scripts.

```
sfrotz --help
```
Shows the options for the SDL build with sound support.

## What's unique

It is a small, long-lived, portable C reimplementation of the Infocom Z-machine that plays nearly the whole Z-code catalogue, including V6. Three binaries split terminal, dumb-terminal and sound use.

## Caveats

The source is at GitLab while the GitHub mirror is deprecated, the README says 2.45pre while the newest listed tarball is 2.44 from 2015, and you must supply your own story files.

## Links

- [Homepage (file index)](https://661.org/proj/if/frotz/)
- [Live source repository (GitLab)](https://gitlab.com/DavidGriffith/frotz)
- [Interactive Fiction Archive, Frotz releases](http://www.ifarchive.org/if-archive/infocom/interpreters/frotz/)
