---
name: ecasound
title: ecasound
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, cli, effects, multitrack, old-school, tui]
homepage: https://nosignal.fi/ecasound/
scout_score: 7
status: draft
---

# ecasound

**TLDR;** A command-line multitrack audio recorder and effects processor, where oscillators and MIDI controllers can drive effect parameters while the sound plays.

Ecasound is a package for multitrack audio processing. Simple jobs are covered: playback, recording, format conversion. It also does multitrack effects, mixing, and what the homepage calls signal recycling. It ships with a console-mode interface, and the brew package adds a set of small single-purpose tools next to the main binary: `ecaplay`, `ecaconvert`, `ecanormalize`, `ecafixdc`, `ecalength`, `ecasignalview` and `ecamonitor`.

The idea underneath it is that audio is a graph you describe, not a session you click through. Inputs, outputs, effects and audio objects are chained together in various ways. Their parameters can be controlled by operator objects like oscillators and MIDI-CCs. A slow oscillator wired to a filter or an amplitude parameter turns a static effect into a moving one, and all of it is written as a command line you can save and script.

The homepage gives no more specific problem statement than being a general-purpose tool for this kind of work. It is old: the copyright line reads 1999-2020. That age shows in the design, which is a small instrument you drive from a terminal. The same shape of thinking, chains of objects with modulation sources attached, shows up again in modular synths and live-coding environments.

## Install

```
brew install ecasound
```

## Try this

```
ecasound --help
```
Prints the main options, a first look at how inputs, outputs and effect chains are specified.

```
ecaplay --help
```
Shows the simple playback front-end that ships alongside the main binary.

```
ecasignalview --help
```
Shows the options for the signal level viewer included in the package.

## What's unique

Effect parameters can be driven by operator objects such as oscillators and MIDI-CCs, inside a scriptable command-line recorder with a console interface. It also ships a family of small ec* utilities.

## Caveats

The latest release on the homepage is 2.9.3 from January 2020, so check that it builds and runs cleanly on your system; Windows support is Cygwin only.

## Links

- [Homepage](https://nosignal.fi/ecasound/)
