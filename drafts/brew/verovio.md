---
name: verovio
title: Verovio
source: brew
category: take-things-apart
commitment: afternoon
tags: [abc, afternoon, library, mei, music, musicxml, notation, svg]
homepage: https://www.verovio.org
scout_score: 6
status: draft
---

# Verovio

**TLDR;** Turns machine-readable music scores (MEI, MusicXML, ABC, Humdrum and more) into SVG sheet music from one command.

Verovio reads a digital score and engraves it as SVG, the way a printed page of sheet music would look. Its native input is MEI, the Music Encoding Initiative format, a scholarly XML encoding of music. Its converters also accept Plaine & Easie Code, Humdrum, Musedata, MusicXML, EsAC and ABC, so those formats can be engraved too.

The README calls it "a fast, portable and lightweight library for engraving Music Encoding Initiative (MEI) digital scores into SVG images." The command-line tool is one way to use the engine. The same code is packaged as a library with bindings for JavaScript, Python, Java, Swift and Go, so it can sit inside web, mobile and desktop apps.

The idea underneath is that a score is data, and notation is a rendering of it. Verovio is written in standard C++ and uses SMuFL (Standard Music Font Layout) for its glyphs, so the music font can be swapped. Seeing how a text encoding of notes, beams and slurs becomes a laid-out page is a door into music encoding and digital musicology.

## Install

```
brew install verovio
# Pre-built binaries exist only for Homebrew on macOS. On Linux and Windows you build from source with CMake and a C++17 compiler.
```

## Try this

```
verovio -h full
```
Prints the full help output, including the default resource path.

```
verovio -o output.svg Hummel_Concerto_for_trumpet.mei
```
Engraves an MEI file with default options and writes the sheet music to output.svg, which you can open in a browser.

## What's unique

It is a small engine built around MEI that works as a command-line tool and as an embeddable library. It also converts several older music-encoding formats on the fly, where most tools handle only one input format.

## Caveats

Only macOS has a pre-built binary, so Linux and Windows users must compile it, and mixing installed and local builds can break resource lookup.

## Links

- [Verovio homepage](https://www.verovio.org)
- [GitHub repository and README](https://github.com/rism-digital/verovio)
- [Reference book: command-line build and usage](https://book.verovio.org/installing-or-building-from-sources/command-line.html)
- [Verovio Online Editor / Viewer](http://editor.verovio.org)
