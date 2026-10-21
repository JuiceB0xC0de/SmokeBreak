---
name: open-jtalk
title: Open JTalk
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, japanese, speech, tts]
homepage: https://open-jtalk.sourceforge.net/
scout_score: 6
status: draft
---

# Open JTalk

**TLDR;** A Japanese text-to-speech system built from a chain of speech research tools, with a trained voice and dictionary you can inspect.

Open JTalk takes Japanese text and produces synthesized Japanese speech. The homepage describes it in one line and does not spell out inputs or outputs further. Homebrew installs two executables, `open_jtalk` and `hts_engine`.

It does not run on its own. It needs a Japanese dictionary and a separate HTS voice file. The homepage offers the dictionary as something to compile yourself or as precompiled packages in Shift-JIS, EUC-JP or UTF-8. The voice is a separate binary download, described as trained on the Nitech Japanese Speech Database.

The homepage links to HTK, HTS, SPTK, the hts_engine API, MeCab and the NAIST Japanese Dictionary. MeCab handles analysis of the Japanese text. The scout's note says the synthesis is HMM-based, statistical-parametric speech, though the homepage does not say so itself. That is the door: a speech system where the training data, the toolkits and the text analysis are all named and open, instead of one opaque model.

This is the older approach to synthetic speech, from before neural voices. Reading its parts is a good way to see how speech gets modelled and generated.

## Install

```
brew install open-jtalk
# You also need a dictionary (compile it, or download a precompiled Shift-JIS, EUC-JP or UTF-8 package) and a separate HTS voice file from the homepage.
```

## Try this

```
open_jtalk --help
```
Lists the options, including where it expects the dictionary and voice files.

```
hts_engine --help
```
Shows the options for the standalone synthesis engine that produces audio from a voice model.

## What's unique

The whole pipeline is open and named: HTS, SPTK, MeCab, the NAIST dictionary and a public speech database. You can follow how text becomes a voice.

## Caveats

The homepage says it works on Linux and does not mention macOS. The latest release is from 2018 and the voice from 2012, so maintenance is unconfirmed.

## Links

- [Open JTalk homepage](https://open-jtalk.sourceforge.net/)
