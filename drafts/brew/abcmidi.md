---
name: abcmidi
title: abcMIDI
source: brew
category: sound-and-live-coding
commitment: quick
tags: [abc-notation, audio, midi, music, quick, text-to-music]
homepage: https://ifdo.ca/~seymour/runabc/
scout_score: 5
status: draft
---

# abcMIDI

**TLDR;** Turns tunes written as plain text in abc notation into MIDI files, and back again, with a small kit of tools for transposing and inspecting them.

abc notation is a way of writing a tune as lines of ordinary text: letters for notes, a few symbols for length and key, a header for title and meter. abcMIDI is a package of C programs for working with those files. The headline tool, abc2midi, reads an abc file and writes a MIDI file you can play in any MIDI player.

The rest of the package works around that. abc2abc transposes and rewrites abc files. midi2abc goes the other direction, from MIDI back to abc. mftext prints a MIDI file as readable text. abcmatch finds common elements across a collection of tunes, midicopy copies parts of a MIDI file into a new one, and midistats reports on a MIDI file. yaps is an older PostScript renderer; the README says it has been superseded by abcm2ps and abc2svg.

The software was created by James Allwright in the early 1990s and is now maintained by Seymour Shlien. The homepage frames these programs as the engines behind graphical front-ends such as runabc and EasyAbc. The idea underneath is music as text: once a tune is a text file, you can diff it, search it, transpose it with a script, and keep a collection of them like source code.

The code is decades old, but the repository now has a CMake build with sanitizer presets and golden-file tests. Binary MIDI output is piped through mftext so it can be compared as text.

## Install

```
brew install abcmidi
# You will also want a MIDI player to hear the output; the package does not include one.
```

## Try this

```
abc2midi --help
```
Prints the usage text for the abc-to-MIDI converter, the main program in the package.

```
mftext --help
```
Shows how to print a MIDI file as readable text, useful for seeing what abc2midi actually wrote.

```
abc2abc --help
```
Lists the options for transposing and rewriting abc files.

## What's unique

It is one of the long-running original toolsets for abc notation, with converters in both directions plus text dumping of MIDI, so a tune can round-trip between text and MIDI.

## Caveats

The tools are command-line only; a MIDI player is needed to hear anything, and the GUIs runabc and EasyAbc are separate installs.

## Links

- [Homepage (runabc and abcMIDI downloads)](https://ifdo.ca/~seymour/runabc/)
- [GitHub repository README](https://github.com/sshlien/abcmidi)
- [abc2midi guide](https://abcmidi.sourceforge.io)
