---
name: tgif
title: tgif
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, ancient, gui, hypertext, vector-graphics, x11]
homepage: https://sourceforge.net/projects/tgif/
scout_score: 5
status: draft
---

# tgif

**TLDR;** An old X11 vector drawing editor that doubles as a browser for hyper-structured graphics, a web idea from 1994 that never caught on.

Tgif (pronounced t-g-i-f) is an Xlib-based interactive 2D drawing tool. You draw and edit vector objects in an X11 window, organise them with layers, and export to roughly ten graphical formats, according to one reviewer. It has no toolkit dressing, just Xlib and a lot of years behind it.

The author's framing is a drawing tool that keeps the user in control, without the many options of larger software. One long-time user calls it easy to learn and handy for quick electrical schematics or PCB layouts, and says it is not limited to what the designer chose. The same reviewer admits it has "some limitations and quirks due to its history, but it does its job well."

The odd part is the second half of the description: "It's also a hyper-structured-graphics browser on the web." Version 2.16, dated Dec 3, 1994, added this. Instead of pages of text with links, tgif can open drawings that are themselves the hypertext, with objects that link onward. Browsers and servers can be configured to hand such files to tgif. It is a small window onto a road the web did not take.

It is a piece of early-Unix-era software culture you can still run. The SourceForge page lists it as registered in 2000, and the author's page is still up.

## Install

```
brew install tgif
Needs an X11 server running (on macOS, something like XQuartz) since it draws through Xlib.
```

## Try this

```
tgif http://bourbon.usc.edu/tgif/index.obj
```
Opens the author's hyper-graphics home page inside tgif's own browser mode, if the server is still reachable.

```
tgif --help
```
Prints the command-line options.

## What's unique

A vector editor from the early X11 era that was also a browser for linked drawings, added to the program in 1994. Few tools from that period are still installable with one command.

## Caveats

Last SourceForge update was 2013-04-11, it needs X11, and a long-time user mentions quirks from its age.

## Links

- [SourceForge project page](https://sourceforge.net/projects/tgif/)
- [Author's WWW home page](http://bourbon.usc.edu/tgif/)
- [Hyper-graphics demo (index.obj, run via tgif)](http://bourbon.usc.edu/tgif/index.obj)
