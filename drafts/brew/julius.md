---
name: julius
title: Julius
source: brew
category: deeper-rabbit-holes
commitment: afternoon
tags: [afternoon, ancient, audio, japanese, science, speech-recognition]
homepage: https://github.com/julius-speech/julius
scout_score: 5
status: draft
---

# Julius

**TLDR;** A speech recognition decoder from 1997 that turns audio into words using models you supply, small enough to run on a microcontroller-class budget.

Julius is a large vocabulary continuous speech recognition decoder. You give it audio (a microphone, a network stream, or a list of files), a language model, and an acoustic model, and it prints the word sequence it thinks it heard. It can also produce N-best lists, word graphs, confusion networks, forced alignments and confidence scores. It runs as a command-line program, as a server, or as a library.

It began as research software for Japanese speech recognition in 1997 and was carried through several Japanese consortium projects. The README's stated goal is a high-performance, small-footprint decoder that runs in real time on everything from micro-computers to cloud servers, with a work area it claims stays under 32 MB.

The idea underneath is that a recognizer is a search problem, separate from the models it searches with. Julius uses a 2-pass tree-trellis search over a word N-gram and context-dependent HMMs, with pruning and beam tricks to keep it fast. Because the search is independent of model structure, you can swap in different acoustic models (HTK HMMs or DNN-HMMs) and language models, either word N-grams in ARPA format or hand-written grammars. In the README's words, "Since Julius itself is a language-independent decoding program, you can make a recognizer of a language if given an appropriate language model and acoustic model for the target language."

That makes it a good way to see what sits between a waveform and a transcript: pronunciation dictionaries, grammars, N-grams, and a decoder tying them together. It is not a download-and-talk tool, though. The models are separate downloads and the configs are hand-edited.

## Install

```
brew install julius
# Models are not bundled. For English, download ENVR-v5.4.Dnn.Bin.zip from SourceForge (JuliusModel page). For Japanese, use the separate dictation-kit repository.
# Microphone use needs a jconf file that sets -input mic.
```

## Try this

```
julius --help
```
Prints the full list of options; they are also documented in doc/Options.md and Sample.jconf.

```
julius -C julius.jconf -dnnconf dnn.jconf
```
Runs the English DNN model from the README's quick run to recognize the bundled mozilla.wav, after you edit dnn.jconf to match your Julius version.

```
julius -C mic.jconf -dnnconf dnn.jconf
```
Recognizes live microphone input, using a mic.jconf you write yourself that sets -input mic.

## What's unique

It reads standard HTK acoustic models and ARPA language models, and one process can run dictation, grammar-based and isolated-word recognition at once. Few decoders are this small or this model-agnostic.

## Caveats

The latest release named in the README is 4.6 from September 2020, and a working recognizer needs separately downloaded models plus manual config edits, with some DNN models requiring a modified fork.

## Links

- [Homepage / repository](https://github.com/julius-speech/julius)
- [Options documentation (doc/Options.md)](https://github.com/julius-speech/julius/blob/master/doc/Options.md)
- [Japanese dictation kit](https://github.com/julius-speech/dictation-kit)
- [Software DOI (Zenodo)](https://doi.org/10.5281/zenodo.2530396)
