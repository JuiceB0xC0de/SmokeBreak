---
name: espeak-ng
title: espeak-ng
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, formant-synthesis, language, quick, speech, tts]
homepage: https://github.com/espeak-ng/espeak-ng
scout_score: 6
status: draft
---

# espeak-ng

**TLDR;** A tiny formant speech synthesizer that speaks over 100 languages from the terminal, built from modelled vocal-tract resonances instead of recordings.

espeak-ng reads text from an argument, a file or stdin and speaks it aloud. It can also write the result as a WAV file, or emit phonemes for another speech engine to use. It is written in C and also ships as a shared library.

The sound comes from formant synthesis. Rather than stitching together recordings of people, it generates speech from modelled resonances of the vocal tract. That is why the whole multilingual package stays small. The README is upfront about the cost: the speech "is clear, and can be used at high speeds, but is not as natural or smooth as larger synthesizers which are based on human speech recordings."

The project is a cleaned-up fork of the older eSpeak engine, started in late 2015 to tidy the code, add features and improve the languages. It keeps eSpeak's command-line options and C API for compatibility, but the data was renamed to espeak-ng-data and is not interchangeable with the original.

The door it opens is how a language gets turned into sound. Text becomes phonemes with pitch and length, and then a synthesizer renders them. espeak-ng can stop at the phoneme stage and act as a front end, or hand those phonemes to MBROLA diphone voices as a backend.

## Install

```
brew install espeak-ng
# Depends on pcaudiolib. If the build has no audio output, the guide says it may run silently. No account needed.
```

## Try this

```
espeak-ng hello
```
Speaks the word hello. Without working audio support it may produce no sound.

```
espeak-ng hello --stdout|aplay
```
Sends the audio to standard output and pipes it to aplay (paplay on Ubuntu), a workaround when direct output is silent.

```
espeak-ng --help
```
Lists the command-line options, including voice, speed and output choices.

## What's unique

It is a living fork that keeps eSpeak's options and C API while fitting 100+ languages into a few megabytes. It can also act as a phoneme front end for other engines, or drive MBROLA voices.

## Caveats

Speech is intelligible but robotic, SSML support is incomplete, and on Linux audio can fail silently when pcaudiolib or PulseAudio is missing.

## Links

- [Homepage / README (GitHub)](https://github.com/espeak-ng/espeak-ng)
- [User guide](https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md)
- [Supported languages](https://github.com/espeak-ng/espeak-ng/blob/master/docs/languages.md)
