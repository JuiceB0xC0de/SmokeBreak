---
name: gerbv
title: gerbv
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, electronics, file-formats, gerber, gui, pcb, visual]
homepage: https://gerbv.github.io/
scout_score: 5
status: draft
---

# gerbv

**TLDR;** A desktop viewer that draws the Gerber files PCB factories use, letting you see how a circuit board is described layer by layer.

Gerbv opens Gerber RS-274X files, Excellon drill files and CSV pick-and-place files, and draws the layers on screen. Gerber is the format a PCB fabrication house receives: one file per copper layer, solder mask, silkscreen and so on, each a list of plotting instructions. Loading a board's files here shows how a finished design breaks down into those plain layers.

It began as one of the utilities of the gEDA electronic design project and is now maintained separately. The README is candid about its history: "This is basically a fork of the fork. There have been many chefs trying to fix this soup, but they have never gotten to the bottom of the problems." The original creator has returned to maintain it, with a dated plan in which CMake modernisation, deb/rpm packaging and bug fixes are done, while the GTK-3 port and documentation are still open.

The core lives in a separate library, libgerbv, which other programs can use to parse, edit, export and render Gerber data. The project documents six example programs: load, merge, export, filter, draw, and embed in a window. For a small viewer that is a useful way into the format itself, not only into looking at boards.

The README states the current focus as "to view and manipulate trusted gerber files". It warns against opening untrusted files without precautions.

## Install

```
brew install gerbv
# Needs a desktop session: this is a GTK-2 GUI application. Homebrew marks the formula deprecated, but the README describes the project as maintained.
```

## Try this

```
gerbv --help
```
Lists the command-line options, so you can see how to load layer files and export from the terminal.

## What's unique

The viewer is built on libgerbv, a separate embeddable library with documented example programs. That makes it a way into the Gerber format as well as a way to look at boards.

## Caveats

It is still built on GTK-2.0 with a non-trivial GTK-3 port planned, it does not support RS-274D files, and you should not open untrusted Gerber files without isolating it.

## Links

- [Homepage](https://gerbv.github.io/)
- [GitHub repository](https://github.com/gerbv/gerbv)
- [libgerbv API documentation](https://gerbv.github.io/doc/)
- [BUILD.md (CMake build guide)](https://github.com/gerbv/gerbv/blob/develop/BUILD.md)
