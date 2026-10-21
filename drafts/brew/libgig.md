---
name: libgig
title: libgig
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, audio, file-formats, library, samplers, soundfont]
homepage: https://www.linuxsampler.org/libgig/
scout_score: 5
status: draft
---

# libgig

**TLDR;** A C++ library and a drawer of command-line tools for opening, dumping, converting and extracting samples from Gigasampler, DLS, SoundFont, KORG and AKAI sampler files.

libgig loads, modifies and creates GigaStudio/Gigasampler (.gig) files and DLS (Downloadable Sounds) Level 1/2 files. It also reads KORG sample files (.KSF and .KMP), SoundFont v2 (.sf2) files and AKAI sampler data. The command-line tools are small programs built on the library, and the homepage presents them as examples of what it can do.

The tools take a sample-instrument file or an AKAI disk image and either print its structure or write something out. `gigdump`, `sf2dump`, `korgdump`, `akaidump` and `dlsdump` print what is inside a file. `gigextract`, `sf2extract` and `akaiextract` pull out the samples. `gigmerge`, `gig2mono`, `gig2stereo` and `korg2gig` merge or convert instrument files. `rifftree` is also in the set.

The idea underneath is that a sampled instrument is not just audio. It is a container holding recordings, plus the data that maps them across the keyboard, velocity layers and loop points. These formats are built on chunked file structures, and the dump tools let you look at how a real instrument is organised. Several of them are the kind of vendor sampler formats that are hard to inspect otherwise.

The library is used by LinuxSampler and its front ends such as qsampler and gigedit. The homepage gives no separate rationale beyond describing it as a library for these formats.

## Install

```
brew install libgig
# Homebrew installs the library and the command-line tools. The homepage itself distributes source tarballs, and building from source needs a C++11 compiler and an OS-provided UUID function.
```

## Try this

```
gigdump --help
```
Shows how to point the dump tool at a .gig file to print its internal structure.

```
sf2dump --help
```
Shows usage for printing the contents of a SoundFont 2 file.

```
gigextract --help
```
Shows how to extract the samples from a Gigasampler file.

## What's unique

One codebase reads and writes several different sampler formats (Gigasampler, DLS, KORG, SoundFont, AKAI) and ships small dump and conversion tools on top.

## Caveats

It is a library first, so the tools are basic, and you need your own sampler files to do anything with them.

## Links

- [libgig homepage](https://www.linuxsampler.org/libgig/)
