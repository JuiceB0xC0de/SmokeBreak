---
name: cmu-pocketsphinx
title: PocketSphinx
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, cli, cmu, json, speech-recognition]
homepage: https://cmusphinx.github.io/
scout_score: 5
status: draft
---

# PocketSphinx

**TLDR;** A small, old-school speech recognizer from Carnegie Mellon that turns audio into line-delimited JSON, and can force-align a known transcript to word-level timestamps.

PocketSphinx is an open-source, speaker-independent, large-vocabulary continuous speech recognition engine from Carnegie Mellon University. The `pocketsphinx` command reads single-channel 16-bit PCM audio from files or standard input and prints one JSON object per utterance, with start time, duration, probability, full text, and per-word segments. The same engine is also available as a C library and Python bindings.

It does not use a neural network pipeline. The README says: "Though the algorithms and models implemented by PocketSphinx are now quite old (dating back to the 1970s in some cases!) they are still useful in many applications due to their compactness and efficiency." It descends from Sphinx-II and earlier CMU systems, with later work adding speed and memory optimizations, fixed-point computation, JSGF grammar support, and portability.

The `align` command is a good side door. Give it audio and the exact text spoken, and it force-aligns the words to the sound, with optional phone-level or state-level segmentation. That shows what a speech decoder is actually doing: matching audio frames against acoustic models and a language model. For live use, `sox` captures or converts audio into the format `pocketsphinx soxflags` reports, and pocketsphinx reads it from a pipe.

The README is candid and a little funny. It explains why the version number is so large and says of the JSON output, "I realize this isn't the prettiest format, but it sure beats XML."

## Install

```
brew install cmu-pocketsphinx
# Live and format-converting examples also need sox: brew install sox
# Live recognition needs a working microphone. No account or API key is needed.
```

## Try this

```
pocketsphinx single speech.wav
```
Recognizes a single-channel WAV file as one utterance and prints JSON. The README warns results "may not be wonderful".

```
pocketsphinx align goforward.wav "go forward ten meters"
```
Force-aligns the known text to the audio and prints word-level timing as JSON. The text must be normalized: no punctuation, consistent case.

```
sox -d $(pocketsphinx soxflags) | pocketsphinx -
```
Captures audio from the microphone through sox and recognizes speech segment by segment, printing one JSON line each.

## What's unique

It is a compact, decades-old recognizer that still runs locally and is maintained. Its forced-alignment mode and terse JSON output (keys b, d, p, t, w) make it easy to script with pipes.

## Caveats

The README is unsure about Mac OS X support, the homepage is only a news page, partial results are not printed, and the README documents none of the extra pocketsphinx_* tools that brew installs.

## Links

- [Project homepage](https://cmusphinx.github.io/)
- [GitHub repository and README](https://github.com/cmusphinx/pocketsphinx)
- [Python API documentation](https://pocketsphinx.readthedocs.io)
- [C API documentation](https://cmusphinx.github.io/doc/pocketsphinx/)
