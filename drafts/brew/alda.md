---
name: alda
title: Alda
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, language, live-coding, midi, music, quick]
homepage: https://alda.io
scout_score: 7
status: draft
---

# Alda

**TLDR;** A text-based music language: write notes in a plain file or REPL, run one command, and hear them played back through MIDI.

Alda is a programming language for composing music. A score is a plain text file with markup-like notation for instruments, octaves, notes, rests and chords. The `alda` command-line tool reads the score and plays it. You can also pass a snippet as a string, or type lines into an interactive REPL and hear each one as you enter it.

The README says it lets you compose and play back music "using only your text editor and the command line," and that it is designed for "musicians who don't know how to program, as well as programmers who don't know how to music." It offers a text alternative to graphical sheet-music programs. The whole composition is one diffable file, so it fits into version control like any other source.

Under the hood, the client (written in Go) parses the score into an AST and sends events over OSC to a separate player process (Kotlin/Java on the JVM). The player produces MIDI using General MIDI instruments. Because the language is text and the client is scriptable, the README says you can also generate music programmatically, for algorithmic composition and live coding. That is the larger idea: notation as code, and code as something you can loop, transform and generate.

## Install

```
brew install alda
# pulls in openjdk, which the player process needs; no account or API key is mentioned
```

## Try this

```
alda play --code "piano: c6 d12 e6 g12~4"
```
Plays a short inline snippet on piano with no file needed.

```
alda repl
```
Starts an interactive session where code you type is played as you enter it.

```
alda parse -c 'piano: c/e/g+' -o ast
```
Prints the parsed score as a JSON AST, showing how the notation is understood.

## What's unique

The notation is markup-like rather than staff-based, and the whole piece is one diffable text file that plays from a terminal, with no GUI. The same language serves for quick sketches, a REPL, and programmatic composition.

## Caveats

Output is General MIDI instruments rather than rendered audio samples, and a score is limited to 15 simultaneous non-percussion instruments because of the 16 MIDI channels.

## Links

- [Homepage](https://alda.io)
- [GitHub repo and README](https://github.com/alda-lang/alda)
- [Changelog](https://github.com/alda-lang/alda/blob/master/CHANGELOG.md)
