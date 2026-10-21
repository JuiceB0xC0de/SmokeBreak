---
name: notcurses
title: Notcurses
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [kitty, library, quick, sixel, terminal-graphics, tui, video]
homepage: https://nick-black.com/dankwiki/index.php/Notcurses
scout_score: 6
status: draft
---

# Notcurses

**TLDR;** A terminal graphics library that stacks transparent planes of text and pixels, shipped with demos that play video and show images in your terminal.

Notcurses is a C library for building text interfaces on modern terminal emulators. Programs draw into stacked rectangular planes using 24-bit color, Unicode, and transparency. The library composes them into one frame and writes it out as UTF-8 and escape codes. It also ships a handful of small tools built on it: ncls, an ls that can display media; ncplayer for images and video; nctetris; and a large demo.

The composition model is the interesting part. For each screen cell, the library walks down the plane stack from the top until a glyph and its foreground and background colors are settled. Each color channel carries two alpha bits (opaque, blend, transparent, or high-contrast) that decide how much of the planes below shows through. Glyph choice is independent of alpha, so you get layered, translucent text on a character grid.

Images and video go through ffmpeg or OpenImageIO. They can be drawn with character-cell blitters, or with real pixel protocols such as Sixel and the Kitty graphics protocol, depending on what your terminal supports. The author puts the design this way: "Notcurses assumes the maximum and steps down (by itself) when necessary." Curses, by his account, assumes the minimum and makes you work to go up.

It is deliberately not an ncurses replacement. It abandons the X/Open Curses API, so existing curses programs will not just run on it. Think of it as a different answer to what a terminal program can be, with wrappers for C++, Rust, and Python.

## Install

```
brew install notcurses
# At runtime TERM must match your terminal and have an up-to-date terminfo entry, or Notcurses refuses to start. Use a UTF-8 locale. If your terminal supports 24-bit color but does not advertise it, set COLORTERM=truecolor.
```

## Try this

```
notcurses-info
```
Prints what Notcurses detected about your terminal's capabilities and lets you inspect how your font renders the drawing characters.

```
notcurses-demo
```
Runs the demo program, which the README says covers most of the library's functionality.

```
ncplayer --help
```
Lists the options for the media player that shows images and video in the terminal.

## What's unique

It treats pixel graphics as a first-class part of a text UI. One API covers Sixel, the Kitty protocol, and the Linux framebuffer, with cell-based blitters as fallbacks. Its plane model adds z-order and per-channel alpha to a character grid, which is unusual among terminal libraries.

## Caveats

Output quality depends heavily on your terminal and font (screen and mosh render poorly), and it is not a drop-in ncurses replacement.

## Links

- [Homepage (dankwiki)](https://nick-black.com/dankwiki/index.php/Notcurses)
- [GitHub repository and README](https://github.com/dankamongmen/notcurses)
- [Man pages and docs](https://notcurses.com)
- [Free guidebook PDF (Hacking the Planet! with Notcurses)](https://nick-black.com/htp-notcurses.pdf)
