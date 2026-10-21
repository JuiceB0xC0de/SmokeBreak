---
name: decker
title: Decker
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, creative-tools, gui, html, hypercard, language, lil]
homepage: https://beyondloom.com/decker/
scout_score: 8
status: draft
---

# Decker

**TLDR;** A HyperCard-style sketchpad for making interactive cards with pictures, sound and scripts, saved as one HTML file, plus a terminal interpreter called Lilt.

Decker is a multimedia authoring tool built around the index-card model. A deck is a set of cards, and each card holds widgets: buttons, fields, sliders, canvases, grids. You paint, draw, record sound and wire cards together. Scripting is optional and written in Lil, which the project describes as a Q/APL-family language.

The homepage pitches it as one environment for digital arts and crafts, where you could write a zine, build an adventure game, make a utility or doodle pixel art. It names HyperCard as a key inspiration, alongside Bitsy, Twine, Flash, VisualBasic and TiddlyWiki. The aim is to erase the divide between users and authors. In its own words: "Decker is intended to be small, simple, and cozy. There are an infinite number of features that could potentially be added, but creative constraints are also valuable."

A deck can be saved as a single self-contained .html file that runs in a browser (Web-Decker), or run in the native C application on MacOS, BSD, Linux, Haiku and Windows. Scripts run in a sandbox so both versions behave the same, with an opt-in "Danger Zone" for non-portable operations.

Decks are stored in a line-oriented text format, which the README says works well with Git and SVN. Lilt, the command-line Lil interpreter, can read, write and run decks without a window. That makes decks something you can script and convert, not only click around in.

## Install

```
brew install decker
# installs both the decker app and the lilt command-line interpreter; depends on sdl2-compat and sdl2_image
```

## Try this

```
decker
```
Opens the native Decker application, where you can start painting cards and adding widgets.

```
lilt
```
Starts the interactive Lil session. The README shows reading a deck with d:read["examples/decks/color.deck"] and writing it out as HTML with write["color.html" d].

```
lilt --help
```
Lists the interpreter's options.

## What's unique

The output is a single HTML file that stays fully editable in the browser, and the same deck can be driven headlessly from a terminal by Lilt. It is also deliberately small, built around creative constraints.

## Caveats

The example deck path in the README comes from the source repository, so you may need to clone it to follow along; the SDL1.2 fallback build has reduced functionality.

## Links

- [Decker homepage](https://beyondloom.com/decker/)
- [Source on GitHub](https://github.com/JohnEarnest/Decker)
