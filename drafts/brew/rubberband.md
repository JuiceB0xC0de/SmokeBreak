---
name: rubberband
title: Rubber Band
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, dsp, library, pitch-shift, quick, time-stretch]
homepage: https://breakfastquay.com/rubberband/
scout_score: 6
status: draft
---

# Rubber Band

**TLDR;** Change the speed of a recording without changing its pitch, or the pitch without the speed, from one command line.

Rubber Band is a C++ audio time-stretching and pitch-shifting library, with a free command-line tool built on top of it. The tool reads a WAV file (via libsndfile), takes a time ratio and a pitch shift in semitones, and writes a new file. Slow a recording down and the pitch stays put. Shift the pitch and the length stays put.

That sounds like a small trick, but it is a real signal processing problem. Speeding up a tape raises its pitch because time and frequency are tied together in the waveform. Pulling them apart means analysing the audio and deciding what to repeat, drop, or blend. The library is built for developers who want that inside their own applications, and the command-line tool is the README's example of offline use. The LADSPA and LV2 plugins are its examples of real-time use.

There are two engines. R2 (Faster) is the default for the `rubberband` binary. R3 (Finer) is selected with `-3` or the `rubberband-r3` executable. According to the README, R3 gives better results on most material, especially complex mixes, vocals and bass-heavy music, at much higher CPU cost. Running the same file through both is a quick way to hear what the trade-off sounds like.

## Install

```
brew install rubberband
# command-line tool reads and writes audio files via libsndfile; WAV is the format the brief documents
```

## Try this

```
rubberband -t 1.5 -p 2.0 test.wav output.wav
```
Stretches test.wav to 50% longer, raises the pitch by a whole tone, and writes output.wav.

```
rubberband -t 2.0 test.wav slow.wav
```
Doubles the duration while leaving the pitch alone (pitch is only changed if you pass -p).

```
rubberband -h
```
Prints the full list of options for the command-line tool.

## What's unique

Stretch and pitch are fully independent, and two engines let you trade CPU for quality. The same codebase also yields a library, plugins, and a Vamp plugin that exposes the stretch decisions the library makes.

## Caveats

The license is GPL v2 or later, and a commercial license is needed to ship it in proprietary apps or on the Apple App Store.

## Links

- [Homepage](https://breakfastquay.com/rubberband/)
- [Usage text for the command-line tool](https://breakfastquay.com/rubberband/usage.txt)
- [Conceptual notes and integration examples](https://breakfastquay.com/rubberband/integration.html)
- [GitHub mirror](https://github.com/breakfastquay/rubberband)
