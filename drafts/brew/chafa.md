---
name: chafa
title: chafa
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [ansi, images, library, quick, sixel, terminal, unicode]
homepage: https://hpjansson.org/chafa/
scout_score: 9
status: draft
---

# chafa

**TLDR;** Chafa turns images and animated GIFs into Unicode and ANSI art in your terminal, or into Sixel and Kitty graphics where supported.

Chafa is a command-line tool with a C library behind it. It reads common image formats, including animated GIFs, and writes character art or terminal graphics protocols such as Sixels, Kitty and iTerm2. The homepage pitches it as a way to view "reasonable approximations" of pictures and animations in a terminal emulator.

The idea underneath is that a terminal is a grid of cells, and each cell can hold a glyph with a foreground and background colour. Chafa treats rendering as a matching problem: it maps patches of pixels onto a selectable set of Unicode symbols and picks colours in Truecolor, 256-colour, 16-colour or FG/BG modes. It can measure colour distance in RGB or DIN99d space, and it can load glyphs from any font file FreeType supports.

The homepage notes that other terminal graphics tools use only U+2580, the upper half block, and says Chafa's wider mix of symbol ranges gives much better quality by default. The same renderer sits behind a documented C API, with Python and JavaScript bindings maintained by others. The homepage also carries a blog series with a sense of humour, and defines the name as "cheap, low quality; lame".

## Install

```
brew install chafa
```

## Try this

```
chafa --help
```
Prints the options, including the choices for symbol sets, colour modes and output formats.

```
chafa --symbols vhalf
```
Restricts output to the upper half block only, the simpler rendering the homepage compares against. Give it an image file to see the difference.

```
man chafa
```
Opens the bundled man page with the full list of options.

## What's unique

Instead of a single block-character fallback, it combines several selectable Unicode symbol ranges and can draw glyphs from real font files. It also emits pixel-accurate protocols like Sixels and Kitty from the same tool.

## Caveats

Output is approximate by nature, and which image formats work depends on optional libraries if you build from source.

## Links

- [Homepage](https://hpjansson.org/chafa/)
- [Gallery](https://hpjansson.org/chafa/gallery/)
- [C API reference](https://hpjansson.org/chafa/ref/)
- [GitHub repository](https://github.com/hpjansson/chafa)
