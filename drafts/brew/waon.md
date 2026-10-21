---
name: waon
title: WaoN
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, fft, midi, old, transcription]
homepage: https://kichiki.github.io/WaoN/
scout_score: 8
status: draft
---

# WaoN

**TLDR;** WaoN listens to a WAV file and writes out the notes it hears as a MIDI file, running a synthesiser's job in reverse.

WaoN is a command-line wave-to-notes transcriber. It reads a WAV file, or anything SoX can decode, and writes a format 0 MIDI file of the notes it detects. Input and output can both be stdin and stdout, so it works as a small Unix filter. The README calls it "the inverse of 'timidity'", which turns MIDI into sound.

The author built it for a personal reason: "My original intention is to pick up voicing of harmony from sound of my favorite pianists." He did not know of a working tool like this on Unix, so he wrote one.

Underneath it is spectral analysis. WaoN runs an FFT over the audio in frames (hanning window and 2048 samples by default) and uses a phase-vocoder correction to refine the frequency estimates. Cutoff, peak-threshold and pitch-range options decide which spectral peaks count as notes, and optional drum-removal and octave-removal filters clean up the result. Turning a messy waveform into discrete notes is a hard, open-ended problem, and the options show where it gets difficult.

Version 0.11 also ships pv, a phase vocoder for time-stretching and pitch-shifting, and gwaon, a GUI for both tools. The project is old and quiet, and its README still lists "improve algorithms" as a TODO, so expect to tune the settings by hand.

## Install

```
brew install waon
# Optional: install mpg123 and sox to feed it MP3s or other formats
```

## Try this

```
waon --help
```
Prints the options for files, FFT size, window type, note selection, and drum and octave removal.

```
waon -i waltz4DB.wav -o waltz4DB.mid -w 3 -n 4096 -s 2048
```
Transcribes a WAV to MIDI with a 4096-sample FFT and a 2048-sample step, the README's tip for better time resolution.

```
cat dolphineD.wav | waon -i - -o - | timidity -id -
```
Pipes the transcription straight into timidity so you hear the machine's reading of the recording.

## What's unique

It runs a synthesiser's job in reverse, turning recorded audio into MIDI notes, and does it as a small Unix filter that pipes into timidity. It also ships a phase vocoder, pv, for time-stretching and pitch-shifting.

## Caveats

The last release was 0.11 in 2015, output is MIDI format 0 only, and the README's own TODO asks for examples and instructions, so expect to experiment with the options.

## Links

- [Homepage (redirect stub)](https://kichiki.github.io/WaoN/)
- [Source repository and README](https://github.com/kichiki/WaoN)
