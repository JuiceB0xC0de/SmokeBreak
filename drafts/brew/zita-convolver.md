---
name: zita-convolver
title: zita-convolver
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, c++, convolution, dsp, library, reverb]
homepage: https://kokkinizita.linuxaudio.org/linuxaudio/
scout_score: 5
status: draft
---

# zita-convolver

**TLDR;** A C++ library that convolves audio with very long impulse responses, like reverbs, at zero delay and moderate CPU cost, using non-uniform FFT partitions.

libzita-convolver is a real-time convolution engine. It takes an input signal and an impulse response (IR), the recorded fingerprint of a room, a speaker or a piece of gear, and produces the input as if it had been played through that thing. Convolution is how a convolution reverb puts your dry guitar into a cathedral.

The hard part is doing this live with long IRs. Direct convolution is far too slow for a multi-second reverb tail, and a plain FFT approach forces you to wait for a whole block of samples before you can output anything. Zita-convolver splits the IR into partitions of non-uniform size: small ones at the start, where low delay matters, growing to "the most efficient size further on". The homepage says this allows "zero-delay processing of very long IRs (e.g. reverbs) with moderate CPU load", and lets you trade CPU load against processing delay.

The work is spread over up to five threads, one per partition size, running at priorities equal to or just below the calling thread. The homepage says this helps CPU allocation when several instances run at once. It also handles matrices of inputs and outputs, up to 64 by 64 depending on CPU, and sparse or diagonal matrices skip empty cells and empty partitions.

The library has no commands of its own. The same page lists the JACK applications jconvolver and fconvolver as built on it, so it is the engine under real command-line tools, and reading about its partitioning is a good way into how convolution reverbs work.

## Install

```
brew install zita-convolver
# Installs the library and its fftw dependency only. There is no executable. You need a C++ project to link against it.
```

## Try this

## What's unique

The non-uniform partitioning with one thread per partition size gives zero-delay convolution of very long IRs without the CPU cost of a uniform scheme.

## Caveats

It is a library with no executables, the homepage is a sitewide index that is always under construction, and it gives no install steps, version or release dates.

## Links

- [Kokkini Zita Linux Audio homepage](https://kokkinizita.linuxaudio.org/linuxaudio/)
