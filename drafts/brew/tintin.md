---
name: tintin
title: TinTin++
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [accessibility, afternoon, automapper, mud, old-school, scripting, tui]
homepage: https://tintin.mudhalla.net/
scout_score: 6
status: draft
---

# TinTin++

**TLDR;** A terminal client for MUDs, the text-based multiplayer games, with a built-in scripting language for triggers, aliases, timers and an automapper.

TinTin++ (tt++) connects to MUD servers and shows their text in a VT100 terminal interface. MUDs are multiplayer worlds that run entirely as text. The client sits between you and the server and can rewrite, react to and automate what passes through.

The automation is the interesting part. tt++ has its own scripting language for triggers, aliases, highlights and timers. Triggers can match with Perl-compatible regular expressions. The homepage describes the engine as fast, with just-in-time compilation. It also includes an automapper that builds a map of the world as you move through it, and it can split the screen and divert text into subwindows.

The homepage says that, although it is primarily a MUD client, it can also be used as a Unix shell command language and as a multiplexer that runs other console programs such as bash, ssh or sftp inside the client, with full access to the scripting language. So the same idea of pattern-matching on a text stream and reacting to it applies to a shell session as much as to a dungeon.

The homepage also stresses accessibility. It is a non-graphical command interface that works with screen readers.

## Install

```
brew install tintin
# the executable is tt++
```

## Try this

```
tt++ --help
```
Prints the command-line options for the client.

```
tt++
```
Starts the client at its prompt, where you can type commands and scripts.

```
#help
```
Typed inside tt++, opens the built-in help files.

## What's unique

It is a MUD client that doubles as a general scripting and multiplexing environment for console programs. It also has a built-in automapper and a stated focus on screen-reader accessibility.

## Caveats

The homepage shows no release dates, so recent activity is unconfirmed, and its Windows support list (XP through 10) looks dated.

## Links

- [TinTin++ homepage](https://tintin.mudhalla.net/)
