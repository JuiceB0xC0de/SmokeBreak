---
name: aubio
title: aubio
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, beat-tracking, cli, library, music-information-retrieval, pitch]
homepage: https://aubio.org
scout_score: 6
status: draft
---

# aubio

**TLDR;** A C library with command-line tools that listen to audio and print note onsets, pitch, beats and tempo as plain timestamps and numbers.

aubio listens to an audio signal and labels what it hears. Feed it a sound file and it can report where notes start, what pitch is playing, where the beats fall, which stretches are quiet, and MFCC features. Each job has its own tool: `aubioonset`, `aubiopitch`, `aubiotrack`, `aubionotes`, `aubiomfcc` and `aubioquiet`. `aubiocut` goes one step further and slices a sound file at the onsets or beats it finds.

The authors say these tasks are difficult, so they gathered them into one library. In the README's words: "aubio is a library to label music and sounds. It listens to audio signals and attempts to detect events." Those events might be a drum hit, the frequency of a note, or the tempo of a rhythmic melody.

The idea underneath is turning sound into annotations: a stream of samples becomes a short list of times and values you can script against. The algorithms are written to be causal, so they work on audio as it arrives and can run in real time with low delay. The core is C, and the Python module exposes aubio's arrays directly as NumPy arrays. That makes it a way into music information retrieval, the field of teaching programs to hear rhythm and pitch.

## Install

```
brew install aubio
```

## Try this

```
aubio --help
```
Shows the main aubio command and the analysis it offers.

```
aubioonset --help
```
Lists the options for the onset detector, which prints the times where notes or hits begin.

```
aubiopitch --help
```
Lists the options for the pitch tracker, which prints pitch values over time.

## What's unique

The same causal algorithms work offline on files and in real time on live audio, on top of a C core with no required dependencies. The name is a deliberate typo of "audio".

## Caveats

The status is unclear: the homepage copyright reads 2003-2018 and no recent release date was visible. The README also warns that errors are likely in the results, and the license is GPL.

## Links

- [Homepage](https://aubio.org)
- [Manual (Sphinx)](https://aubio.org/manual/latest/)
- [Developer docs (Doxygen)](https://aubio.org/doc/latest/)
- [GitHub repository](https://github.com/aubio/aubio)
