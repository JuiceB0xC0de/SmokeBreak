---
name: lilypond
title: LilyPond
source: brew
category: languages-and-oddities
commitment: afternoon
tags: [afternoon, gnu, language, music, notation, typesetting]
homepage: https://lilypond.org
scout_score: 6
status: draft
---

# LilyPond

**TLDR;** A music engraving program where you type sheet music as plain text and a compiler typesets it into a score.

LilyPond takes a text file describing a piece of music, with notes written as letters and numbers and special commands marked by backslashes, and compiles it into engraved sheet music. The site says it covers classical, early, modern, vocal, tablature, lead sheet, educational and orchestral work, and even Schenker graphs.

The text-input model is a deliberate choice. In the project's words: "LilyPond is primarily concerned with producing top-quality engraved sheet music; creating a Graphical User Interface (GUI) would distract us from this goal." The aim is to bring the look of traditionally engraved music to computer printouts.

The idea underneath is that a score can be source code. Music can be assigned to named variables, so one source can feed both a transposed part and a concert-pitch full score, and changing a note updates both. Accidentals are placed automatically from note names: -is means sharp and -es means flat, with Dutch note names by default and other languages available. As the site puts it, "In some ways, LilyPond is more similar to a programming language than graphical score editing software."

Homebrew also installs converters for other formats: abc2ly, etf2ly, midi2ly and musicxml2ly bring existing music in, and convert-ly updates older input files to newer syntax.

## Install

```
brew install lilypond
```

## Try this

```
lilypond --help
```
Lists the compiler's options, a first look at how it turns a text file into a score.

```
musicxml2ly --help
```
Shows how to convert a MusicXML file from another notation program into LilyPond text.

```
convert-ly --help
```
Shows the tool that rewrites older LilyPond input files to match newer syntax.

## What's unique

Notation is code. You write text and the compiler does the engraving, rather than dragging notes on a toolbar. Shared variables keep a full score and its parts in sync from one source file.

## Caveats

The site warns that new users often find text input odd and recommends the Learning manual first; there is no graphical note entry, though third-party editors add it.

## Links

- [LilyPond homepage](https://lilypond.org)
- [Text input overview](https://lilypond.org/text-input.html)
