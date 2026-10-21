---
name: chuck
title: ChucK
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, generative, language, live-coding, music]
homepage: https://chuck.cs.princeton.edu/
scout_score: 9
status: draft
---

# ChucK

**TLDR;** A programming language where time is a built-in concept, so you write code that makes sound and rewrite it while it plays.

ChucK is a language for real-time sound synthesis and music. You write a program, it produces audio, and you can add or change code while the sound is running. The homepage says it supports MIDI, OpenSoundControl, HID devices and multi-channel audio.

The idea underneath is what the project calls "strongly-timed" programming: "a unique time-based, concurrent programming model that is precise and expressive." In most languages, time is something you borrow from the operating system. Here, time is part of the language itself, and many concurrent bits of code can be lined up against it. That makes it a way into thinking about rhythm, scheduling and synthesis as a program structure rather than as a timeline in a music app.

It was built for composers, researchers and performers who want a serious tool that is still, in the project's words, "fun, easy to learn." The homepage credits the ChucK Team with a span of "2003 => now" and lists a wider ecosystem: ChuGL for graphics, WebChucK for browsers, ChuMP as a package manager, and integrations with Unity, TouchDesigner, Unreal, Pure Data and Max/MSP.

## Install

```
brew install chuck
# Needs working audio output. The homepage gives no further install or first-run steps.
```

## Try this

```
chuck --help
```
Prints the command-line options, which is the quickest way to see how to run a program and how live code changes are handled.

## What's unique

Time is a first-class part of the language, and you can change code while sound plays. Most text-based audio tools do not combine the two.

## Caveats

Several ecosystem pieces are marked early or alpha (ChuGL, Chunreal, ChucK~ for Pure Data and Max/MSP), and the homepage gives no first-run instructions, so expect to read the docs.

## Links

- [ChucK homepage](https://chuck.cs.princeton.edu/)
