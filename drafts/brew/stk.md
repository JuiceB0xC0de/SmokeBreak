---
name: stk
title: STK (Synthesis ToolKit)
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, c++, library, physical-modelling, synthesis]
homepage: https://ccrma.stanford.edu/software/stk/
scout_score: 7
status: draft
---

# STK (Synthesis ToolKit)

**TLDR;** A C++ library from Stanford's CCRMA of readable physical-model instruments and synthesis building blocks, written to teach how sound is made sample by sample.

STK is a set of C++ classes for audio signal processing and algorithmic synthesis. It is a library you write programs against, not a single application. It includes unit generators, physical-model instruments, modal synthesis, FM patches, and a control format called SKINI. Output goes to real-time audio and MIDI on Linux, macOS and Windows, or to files in SND, WAV, RAW, AIFF and MAT formats.

Perry Cook wrote it to have synthesis, processing and control units he could teach and research with, in a portable form. He also wanted to help people who struggle to turn physical-model papers into working instruments, since stable parameter values are hard to find. The README describes it as tutorial code and a base for further research.

The idea underneath is simple: you connect unit-generator objects together and call their tick() function to produce one sample at a time. Newer releases add a StkFrames class for multichannel audio and a Messager class that takes control input from pipes, sockets or MIDI. Reading the source of a plucked string or a blown pipe shows how a physical model turns into a few lines of delay lines and filters.

The README states the goal as code that still compiles and runs in five to ten years, with no hidden drivers or unusual dependencies. The project has existed since 1996. In its own words: "Despite being available in one form or another since 1996, we still consider STK to be alpha software."

## Install

```
brew install stk
# Headers go on a standard path: #include "stk/FileLoop.h"
# src/, projects/ and rawwaves/ are copied to $HOMEBREW_PREFIX/opt/stk/share/stk
# Needs a C++ compiler. Tcl/Tk 8.0+ is only needed for the optional GUIs.
```

## Try this

```
treesed --help
```
Runs the one executable the formula installs. The README does not describe it, so see what it reports.

```
ls $HOMEBREW_PREFIX/opt/stk/share/stk
```
Lists the copied src, projects and rawwaves directories, where the instrument source and example programs live.

## What's unique

It is a teaching-oriented toolkit that predates most modern music-DSP libraries, with physical-modelling instruments you can read and modify. It is built to stay compilable with no unusual dependencies.

## Caveats

The README calls it alpha software with no guarantees, there is no graphical patching front end, and the brief found no recent release or commit date.

## Links

- [STK homepage (CCRMA)](https://ccrma.stanford.edu/software/stk/)
- [STK on GitHub (thestk/stk)](https://github.com/thestk/stk)
