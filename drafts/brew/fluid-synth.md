---
name: fluid-synth
title: FluidSynth
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, library, midi, soundfont, synthesizer]
homepage: https://www.fluidsynth.org
scout_score: 6
status: draft
---

# FluidSynth

**TLDR;** A software synthesizer that turns MIDI into sound using SoundFont instrument banks, the software version of a hardware MIDI synth.

FluidSynth reads MIDI events, from an input device or a MIDI file, and renders them to audio using a SoundFont as its instrument bank. A SoundFont is a file of recorded instrument samples plus rules for playing them. The brief describes FluidSynth as "the software analogue of a MIDI synthesizer." It has no GUI of its own. You drive it through a built-in command line shell, or through the shared library other programs embed.

It came out of an online multi-user game project that wanted SoundFont-based music. Wavetable synthesis is cheap on CPU, and small MIDI files plus SoundFonts are easier to download than recorded audio. Because sound had to work on Linux, macOS and Windows with any sound card, the team needed a software SoundFont synthesizer that did not depend on platform-specific libraries.

That design goal explains why it shows up everywhere. The homepage lists frontends and music programs built on its API, including QSynth, LMMS, MusE and Denemo. It supports SoundFont 2.04 modulators for real-time effect control, SoundFont 3 (Vorbis-compressed SF2), and DLS Level 1 and 2.

The idea underneath is the split between score and sound. MIDI says which notes to play and how hard, and says nothing about what they sound like. Swap the SoundFont and the same file becomes a different instrument set. It is a small, practical way into how a lot of game and desktop music works.

## Install

```
brew install fluid-synth
You also need a SoundFont (.sf2 or .sf3) file to get any sound, and a MIDI file or MIDI input device to feed it. The brief did not cover where to get one.
```

## Try this

```
fluidsynth --help
```
Lists the command line options, including how to load a SoundFont and choose an audio driver.

## What's unique

It is a self-contained SoundFont synthesizer built to be embedded as much as used, so many other music programs run on it. It has no GUI of its own.

## Caveats

There is no GUI and no sound without a SoundFont file, so you work in the command line shell, a frontend, or the API.

## Links

- [Homepage](https://www.fluidsynth.org)
- [Wiki (documentation hub)](https://www.fluidsynth.org/wiki)
- [API documentation](https://www.fluidsynth.org/wiki/api/)
