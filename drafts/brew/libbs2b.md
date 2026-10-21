---
name: libbs2b
title: libbs2b
source: brew
category: sound-and-live-coding
commitment: quick
tags: [audio, crossfeed, dsp, headphones, library, quick]
homepage: https://bs2b.sourceforge.net/
scout_score: 6
status: draft
---

# libbs2b

**TLDR;** A tiny headphone crossfeed filter that bleeds each stereo channel into the other ear, so music sounds less like it is stuck inside your skull.

libbs2b is a C library and set of plugins implementing the Bauer stereophonic-to-binaural DSP, usually shortened to bs2b. It takes a stereo signal and mixes a filtered, delayed copy of each channel into the opposite channel. The Homebrew formula installs two command-line tools, bs2bconvert and bs2bstream, though the homepage does not document how they are used.

The reasoning is on the project's page. Stereo records are mixed for loudspeakers, where each ear hears both speakers, the far one slightly later and duller because the head is in the way. Headphones skip all that, so the channels arrive hard-separated. The author calls the result a 'superstereo' effect and ties it to listening fatigue. Crossfeed adds back a little of the missing leakage.

The implementation is small. It uses single-pole recursive filters, O[n] = a0 * I[n] + a1 * I[n-1] + b1 * O[n-1], which the author says behave like analog RC filters. He contrasts this with FFT-based crossfeed, which he associates with comb-filter artifacts. A low-pass and a high-boost set the response and delay. The page is upfront about limits: no ambience simulation, and no HRTF at high frequencies.

The homepage includes a Perl script, bs2b-H-transform.pl, that prints the filter's response, with presets named after Bauer's default, Chu Moy and Jan Meier. It makes this a good way to see what a crossfeed design is made of, even if you never use the library.

## Install

```
brew install libbs2b
# Depends on libsndfile. The homepage has no build instructions. The theory script needs Perl with Math::Complex.
```

## Try this

```
perl bs2b-H-transform.pl 700 -6.75   -2.25
```
Prints the frequency and delay response for the default preset (700Hz, 4.5dB), using the script from the homepage's Theory section.

```
perl bs2b-H-transform.pl 650 -10.917 -1.417
```
Prints the same response for Jan Meier's preset (650Hz, 9.5dB), so you can compare it to the default.

```
bs2bconvert --help
```
Asks the installed converter tool to describe itself, since the homepage does not document its usage.

## What's unique

It is a small, documented DSP built from a few one-pole filters, with presets tied to named crossfeed designs. The homepage ships the script that computes the response, so you can check the math yourself.

## Caveats

The homepage does not document bs2bconvert or bs2bstream and has no build instructions; SourceForge lists both GPLv2 and MIT, and its reviews (2012 to 2018) mention only Windows players.

## Links

- [Project homepage](https://bs2b.sourceforge.net/)
- [SourceForge project page (downloads, reviews, licence)](https://sourceforge.net/projects/bs2b/)
