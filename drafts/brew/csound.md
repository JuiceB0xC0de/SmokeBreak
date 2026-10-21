---
name: csound
title: Csound
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, language, music, synthesis]
homepage: https://csound.com
scout_score: 9
status: draft
---

# Csound

**TLDR;** A sound synthesis language from 1985 where you write instruments and a score as text, and the computer renders them into audio.

Csound is a free and open source audio programming language. You describe instruments in an orchestra, which is code that defines how a sound is built, and you describe what they play in a score, which is a list of note and control events. Csound reads both and renders audio. The core is a C library with a command-line frontend, and the project says it runs on desktop, mobile, embedded, server and web platforms.

It descends from the MUSIC-N series by Max Mathews, the earliest computer music software. In the homepage's words, it "has its roots in the earliest of computer software." Barry Vercoe first released Csound in 1985, and it has been part of the computer music world since then.

The idea underneath is that a sound is a program. Instead of tweaking knobs on a synth, you build the signal path yourself and decide what each part does. That makes it a door into synthesis, signal processing and algorithmic composition. The Homebrew formula installs about thirty executables, including analysis and conversion utilities such as pvanal, sndinfo, csanalyze and makecsd.

The README says little about features. The depth is in the reference manual, so expect to spend your first session reading docs rather than running examples.

## Install

```
brew install csound
# Optional, macOS only, for the Java bindings: add to ~/.zshrc or ~/.profile
export CLASSPATH="$HOMEBREW_PREFIX/opt/csound/libexec/csnd6.jar:."
mkdir -p ~/Library/Java/Extensions
ln -s "$HOMEBREW_PREFIX/opt/csound/libexec/lib_jcsound6.jnilib" ~/Library/Java/Extensions
```

## Try this

```
csound --help
```
Prints the command-line options for the renderer, a first look at how orchestra and score files get turned into audio.

## What's unique

It is one of the oldest continuously developed music synthesis languages, with a direct line back to MUSIC-N. Few tools let you build every part of a sound from text.

## Caveats

Csound 7 is still in beta and the 6.x line is end-of-life, so the Homebrew version and the current docs may not match exactly.

## Links

- [Csound homepage](https://csound.com)
- [Csound Reference Manual](http://docs.csound.com)
- [Csound API reference](http://csound.github.io/docs/api/index.html)
- [Csound on GitHub](https://github.com/csound/csound)
