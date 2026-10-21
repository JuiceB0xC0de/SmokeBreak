---
name: inspectrum
title: inspectrum
source: brew
category: radio-and-hardware
commitment: afternoon
tags: [afternoon, gui, iq, needs-capture-file, sdr, signals, spectrogram]
homepage: https://github.com/miek/inspectrum
scout_score: 8
status: draft
---

# inspectrum

**TLDR;** A desktop tool that opens recorded radio captures as zoomable spectrograms, so you can measure and decode signals long after they were received.

inspectrum analyses captured radio signals, mainly IQ recordings from software-defined radio receivers. You open a sample file and it draws a spectrogram you can zoom and pan. Alongside it are plots of amplitude, frequency, phase and the raw IQ samples.

The work happens with cursors. You mark out the period of a burst, read off a symbol rate, and extract the symbols. You can then export a time window, filtered samples, or demodulated data. It works on files only, not live radio, and it reads many raw formats (SigMF, cf32, cs8, cu8 and others) without conversion. The README claims support for files of 100GB and more.

The idea underneath is that radio is just numbers once you record it. An IQ file is a stream of complex samples, and a spectrogram turns it into a picture where modulation, bursts and timing can be seen. Working offline means you can stop, rewind and measure the same transmission as often as you like, which is how many people learn to reverse engineer an unknown wireless protocol.

## Install

```
brew install inspectrum
# You need a capture file to open. Hardware is only needed if you want to record your own.
```

## Try this

```
inspectrum --help
```
Shows the options the installed binary accepts.

```
inspectrum [filename]
```
Opens a capture file as a spectrogram. The extension sets the sample format, for example .cu8 for RTL-SDR recordings or .cf32 for complex floats.

## What's unique

It opens raw IQ files from many SDR tools directly and handles very large recordings, so you can go from capture to measured symbols in one window.

## Caveats

Unknown file extensions are read as cf32, which gives wrong plots if the guess is wrong, and 64-bit samples are truncated to 32-bit; I could not confirm how recently the project was updated.

## Links

- [GitHub homepage and README](https://github.com/miek/inspectrum)
- [Build instructions (wiki)](https://github.com/miek/inspectrum/wiki/Build)
- [Homebrew formula](https://formulae.brew.sh/formula/inspectrum)
