---
name: libcaca
title: libcaca
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [ancient, ascii-art, graphics, library, quick, terminal]
homepage: http://caca.zoy.org/wiki/libcaca
scout_score: 7
status: draft
---

# libcaca

**TLDR;** A text-mode graphics library that draws in coloured characters instead of pixels, with demos like a fire effect and an image-to-ASCII converter.

libcaca is a C graphics library that outputs text instead of pixels, "so that it can work on older video cards or text terminals." It takes graphics or images and renders them as coloured characters. It offers Unicode output, up to 2048 colours (some devices only handle 16), dithering of colour images, and canvas operations such as blitting and rotation.

The brew package installs eight executables: `cacaview`, `cacaplay`, `cacafire`, `cacaclock`, `cacademo`, `cacaserver`, `img2txt` and `caca-config`. The homepage does not describe them individually, but the names of the first four are listed as text-mode demos. The `--help` flag on each is the place to start.

It is a successor to AAlib. On Unix it renders through S-Lang or ncurses, and it also runs natively on DOS and Windows. The idea underneath is that a terminal is a low-resolution display with a palette and a character set, and that dithering and colour mapping can carry a surprising amount of an image through that bottleneck.

The author is upfront that this is deliberate pointlessness: "I am perfectly aware that libcaca is the waste of time it looks to be. No need to tell me about that." He defends the project with a Cyrano de Bergerac quote and Théophile Gautier's preface to Mademoiselle de Maupin, which is also where the name comes from.

## Install

```
brew install libcaca
```

## Try this

```
cacaview --help
```
Shows the options for the image viewer that displays pictures as coloured text in your terminal.

```
img2txt --help
```
Shows how to convert an image file into coloured ASCII text.

```
cacafire --help
```
Shows the options for the text-mode fire demo.

## What's unique

It goes beyond AAlib with Unicode, up to 2048 colours and dithering, and ships its own text-mode demos. It is openly built for the pleasure of pointless craft.

## Caveats

The latest release listed is 0.99.beta19 from May 2014, and the homepage is an old Trac wiki page with no current usage or build instructions.

## Links

- [libcaca homepage (Caca Labs wiki)](http://caca.zoy.org/wiki/libcaca)
- [Caca Labs](http://caca.zoy.org/)
- [libcaca Git mirror (HTTP)](http://caca.zoy.org/git/libcaca.git)
