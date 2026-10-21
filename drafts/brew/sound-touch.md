---
name: sound-touch
title: SoundTouch
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, bpm, library, pitch-shift, time-stretch, wav]
homepage: https://www.surina.net/soundtouch/
scout_score: 5
status: draft
---

# SoundTouch

**TLDR;** A small C++ audio library, with a bundled command-line tool called soundstretch, that changes tempo and pitch independently or together, and can estimate a track's BPM.

SoundTouch is an open-source library for changing the tempo, pitch, or playback rate of audio. It takes 16-bit integer or 32-bit float audio, mono, stereo, or multi-channel, and returns processed audio. The homepage says it is meant for developers who need tempo and pitch control, "or just for playing around with the sound effects." It also includes a beats-per-minute estimator.

The idea underneath is that speed and pitch are normally tied together. Speed up a record and it gets higher as well as faster. SoundTouch separates them into three modes. Tempo changes speed without changing pitch. Pitch changes key without changing speed. Playback rate changes both at once, "as if a vinyl disc was played at different RPM rate." Pulling those apart is time-stretching and pitch-shifting, a core technique in DJ tools, music practice apps, and audio editors.

The Homebrew formula installs soundstretch, the example command-line utility from the source kit. According to the homepage, it works on .wav files. The homepage links to a tutorial on the theory of audio time and pitch scaling, but it does not describe the algorithm itself, so that is where to dig further.

The library is small. The page describes a single C++ class as the programming interface, with examples and bindings for C#, Java, and Pascal/Delphi. It has been around since 2001.

## Install

```
brew install sound-touch
```

## Try this

```
soundstretch --help
```
Prints the usage text and the options for changing tempo, pitch, and playback rate on a .wav file.

## What's unique

It is a long-lived time-stretch and pitch-shift engine reduced to one C++ class, with BPM detection included. The author claims CD-quality stereo can run in real time on a 133 MHz Pentium.

## Caveats

It is mostly a library, the bundled soundstretch tool only handles .wav files, and real-time use has about 100 ms of latency. I could not confirm recent activity from the homepage.

## Links

- [SoundTouch homepage](https://www.surina.net/soundtouch/)
