---
name: bombadillo
title: Bombadillo
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, finger, gemini, gopher, protocol, tui]
homepage: https://bombadillo.colorfield.space/
scout_score: 8
status: draft
---

# Bombadillo

**TLDR;** A terminal browser for the non-web internet: gopher, gemini and finger, in one client, for anyone curious what the net looked like before HTTP took over.

Bombadillo is a terminal client for protocols other than HTTP. Its Homebrew description calls it a "non-web browser, designed for a growing list of protocols". The scout notes name gopher, gemini and finger, and that is as much as the available sources confirm.

The idea underneath is that the web is one protocol among many, and several small ones are still alive. Gopher is a menu-driven document system from the early 1990s. Gemini is a newer, deliberately minimal protocol. Finger is an old way of asking a host about a user. Each is simple enough to read about in an afternoon, and a single client that speaks several lets you compare them side by side.

The homepage and repository could not be read when this entry was written, so details such as keybindings, configuration and project activity are unverified. Treat the first run as exploration: launch it and see what it offers.

## Install

```
brew install bombadillo
```

## Try this

```
bombadillo --help
```
Prints the command-line options the installed version supports.

```
bombadillo
```
Starts the browser interface so you can look around and find its built-in help.

## What's unique

It handles several small non-web protocols in a single terminal client rather than being a reader for just one.

## Caveats

Project status, release date and documentation could not be checked, so how actively it is maintained is unknown.

## Links

- [Homepage](https://bombadillo.colorfield.space/)
