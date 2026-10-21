---
name: arss
title: arss
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [audio, image, quick, resynthesis, spectrogram]
homepage: https://arss.sourceforge.net/
scout_score: 6
status: draft
---

# arss

**TLDR;** Turns a sound file into a spectrogram image, then turns any image, edited or hand-drawn, back into sound.

ARSS, the Analysis & Resynthesis Sound Spectrograph, is a command-line program that analyses a sound file into a spectrogram picture. The step that makes it interesting is the reverse. It can synthesise that picture, or any image you made yourself, back into audio. The homepage lists time stretching, pitch shifting, filtering in an image editor and drawing sounds by hand as uses.

Under the hood it skips the short-time Fourier transform most spectrographs use. Instead the signal goes through a bank of overlapping logarithmic-scale Hann-window filters. The magnitude of the analytic signal in each band becomes an envelope, and each envelope is one horizontal line of the image, with amplitude mapped linearly to brightness. Synthesis runs this backwards: each line is upsampled to the output sample rate and used to modulate either a sine wave at the band's centre frequency or filtered noise.

The idea underneath is that sound and image can be the same data. Once a sound is an array of envelopes, a paintbrush, a blur or a crop becomes an audio effect. The author frames it as open-ended: "Who knows what else, there's a lot of room for experimentation".

The project is old. The homepage says it is "now superseded by Photosounder", a graphical program that uses most of the same techniques. The command-line tool still shows the idea in its barest form.

## Install

```
brew install arss
# depends on fftw, which brew installs for you
```

## Try this

```
arss --help
```
Prints the usage text, so you can see the options for analysing a sound into an image and synthesising an image back into sound.

## What's unique

It uses a filter bank with envelope detection instead of the usual STFT, closer to how analogue spectrographs worked. The same tool analyses and resynthesises, so you can paint a spectrogram and hear it.

## Caveats

The homepage says the site has been in hiatus since February 2009, the last release mentioned is 0.2.3 from 2008, and the page offers no install guide or documentation beyond one gcc line.

## Links

- [ARSS homepage (Michel Rouzic)](https://arss.sourceforge.net/)
