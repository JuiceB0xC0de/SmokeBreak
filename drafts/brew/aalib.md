---
name: aalib
title: aalib
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [ancient, ascii, graphics, library, quick, terminal]
homepage: https://aa-project.sourceforge.net/aalib/
scout_score: 6
status: draft
---

# aalib

**TLDR;** A 1990s library that draws graphics as ASCII characters on any terminal, with a bundled demo that renders a roaring fire in text.

AA-lib is a portable graphics library whose output is text. Programs call a standard drawing API, and the library turns the pixels into characters on a terminal of any kind. The homepage puts it as: "It works on a terminal of any kind, it is fast and portable, it gives to you standard API."

The origin story is small and specific. The project began with a Linux penguin logo shown on Hercules monitors, converted to ASCII by matching regions of the image against a table that approximates font bitmaps. The author's stated motive is simplicity: video cards, low-frequency monitors and crashing graphical apps cause many problems, and the page says text output gives old hardware more power. Its closing line on the subject is "I vote for simplicity."

The idea underneath is that a character cell is a very coarse pixel, and picking the glyph whose shape best matches the patch of image behind it gives you grayscale from punctuation. Once you see that, every text-mode video player and terminal image viewer looks like a descendant. The same author later made XaoS, a fractal zoomer, and the BB demo to show off the library.

Homebrew installs five executables built on it: aafire, aainfo, aalib-config, aasavefont and aatest. The project is old, with its latest news item dated April 2001, but a library for drawing with text has little to go out of date.

## Install

```
brew install aalib
```

## Try this

```
aafire
```
Runs the bundled demo, which draws a fire animation using only text characters.

```
aainfo
```
Reports what AA-lib detects about your terminal and its display driver.

```
aatest --help
```
Shows the options for the test program that exercises the library's rendering.

## What's unique

It is a text-mode rendering library from the 1990s with a standard drawing API, and it has a demo that is instantly recognizable. Many later ASCII renderers trace back to this idea.

## Caveats

The project is quiet, with release candidates from 2001 on its download page, a thin README, and documentation pages I could not locate.

## Links

- [AA-lib homepage](https://aa-project.sourceforge.net/aalib/)
- [AA-project homepage](https://aa-project.sourceforge.net/)
