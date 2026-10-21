---
name: sox
title: SoX
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, cli, converter, effects, quick]
homepage: https://sox.sourceforge.net/
scout_score: 7
status: draft
---

# SoX

**TLDR;** SoX is a command-line audio tool that converts sound files between formats and runs effects and filters on them, all from a shell pipeline.

SoX, short for Sound eXchange, reads audio in many formats, optionally applies effects and filters, and writes the result in another format. The project describes itself as "the Swiss Army Knife of sound processing utilities." It has been around since 2000 at least, which makes it a long-standing part of the Unix audio toolbox.

Homebrew installs four programs. `sox` does the conversion and processing. `play` and `rec` are shortcuts for playing and recording audio. `soxi` reports information about a sound file. The formula pulls in libraries for FLAC, MP3 (LAME and MAD), Ogg Vorbis, Opus and libsndfile, so a wide range of formats should work after a plain install.

The idea underneath is that audio can be treated like text in a pipeline: a file goes in, a chain of small transformations is applied, and a file comes out. Once sound is something you can filter and rewrite with one command, you can script batch conversions, build test signals, or treat a sound file as raw material for experiments.

The pages the brief draws on gave no usage examples, so the commands below stick to the help output.

## Install

```
brew install sox
```

## Try this

```
sox --help
```
Prints the list of supported file formats, effects and options, which is a quick tour of what SoX can do.

```
soxi --help
```
Shows how to use the file-information tool that reports details about a sound file.

```
play --help
```
Shows the options for the playback front end.

## What's unique

SoX combines format conversion and effects in one pipeline-friendly command, and it has been doing so for decades. That makes it a common building block in audio scripts.

## Caveats

The official manual page returned a 404 when the brief was written, and SourceForge reviewers report install trouble on Windows; the Homebrew build was not tested here.

## Links

- [Homepage](https://sox.sourceforge.net/)
- [SourceForge project page](https://sourceforge.net/projects/sox/)
