---
name: inform6
title: Inform 6
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, compiler, interactive-fiction, retro, text-adventure, z-machine]
homepage: https://inform-fiction.org/inform6.html
scout_score: 7
status: draft
---

# Inform 6

**TLDR;** A 1993 compiler for writing text adventures in a C-like language, producing Z-machine story files and still serving as the engine under Inform 7.

Inform 6 is a compiler written in C. You give it source files in the Inform language, which looks somewhat like C, plus the Inform 6 library. It produces a Z-machine story file, the same kind of file Infocom used for its text adventures. A Z-machine interpreter then runs that file.

Graham Nelson released the first version in 1993. The README ties it to a community tradition: after the Z-machine format was reverse-engineered in the late 1980s, Inform made it practical to write new games for it. The README says this led to "hundreds of free games" from the rec.arts.int-fiction Usenet community.

The compiler does not contain the adventure-game behaviour. The library supplies parsing, rooms, objects and the standard way a text adventure responds to you, and you write your game against it. The library is a separate download, so the compiler alone is not enough to write a game. There is no IDE. You work in a plain text editor and run the compiler.

The README calls the language stable, with only bug fixes and minor non-breaking features added, though development continues. It is also the code generator underneath Inform 7, so it is still in use. The Homebrew package also installs punyinform, pblorb and scanblorb helpers, which the README does not describe.

## Install

```
brew install inform6
# The compiler does not include the Inform 6 library. Stable library releases are on the IF Archive, and development is on GitLab.
# You will also need a Z-machine interpreter to run the story files you compile.
```

## Try this

```
inform --help
```
Prints the compiler's usage and switches, a first look at how source becomes a story file.

```
punyinform --help
```
Shows the usage of the punyinform helper that Homebrew installs alongside the compiler.

## What's unique

It is a small C compiler for a 1993 language that still feeds Inform 7 underneath. Writing against it means working directly with a language and a library, with no IDE.

## Caveats

The homepage calls itself a historical reference last updated in July 2020, while the GitHub README says development continues, and you must fetch the separate Inform 6 library to write a real game.

## Links

- [Inform 6 homepage (historical reference)](https://inform-fiction.org/inform6.html)
- [Inform 6 compiler repository (GitHub)](https://github.com/DavidKinder/Inform6)
- [Inform 6 library development (GitLab)](https://gitlab.com/DavidGriffith/inform6lib)
