---
name: chromaprint
title: Chromaprint
source: brew
category: quick-weird-payoffs
commitment: quick
tags: [acoustid, audio, ffmpeg, fingerprinting, quick]
homepage: https://acoustid.org/chromaprint
scout_score: 7
status: draft
---

# Chromaprint

**TLDR;** Chromaprint turns audio into a compact fingerprint string with one command, the same kind of signature AcoustID uses to recognise songs.

Chromaprint is a C library plus a command-line tool called fpcalc. The library takes decoded, uncompressed audio samples and returns a short fingerprint. fpcalc wraps it and uses FFmpeg to decode and resample files first, so you can point it at ordinary audio files.

It was built as the client side of the AcoustID project, which identifies recordings by matching fingerprints. In the README's words, it is "designed to identify near-identical audio and the fingerprints it generates are as compact as possible to achieve that." The intended uses are full-file identification, duplicate detection and monitoring long streams.

The idea underneath is that sound can be reduced to a small signature that survives re-encoding, so two copies of the same recording produce similar fingerprints even when the bytes differ. The README does not walk through the algorithm. The homepage links a blog post, "How does Chromaprint work?", and the README credits published work on computer-vision-style music identification and index-based audio matching as background.

The design is a deliberate trade. The README says it "trades precision and robustness for search performance", so it is not a general-purpose fingerprinter. fpcalc can also emit JSON, which makes it easy to call from any language without binding to the C API.

## Install

```
brew install chromaprint
# installs the fpcalc executable; ffmpeg is pulled in as a dependency
# no account or configuration needed to generate fingerprints
```

## Try this

```
fpcalc --help
```
Lists the options fpcalc supports, including how to choose the output format.

## What's unique

It is the fingerprinting engine behind AcoustID, small enough to run as one command, with fingerprints tuned for fast searching rather than for general-purpose precision.

## Caveats

It only generates fingerprints; identifying a song needs a separate AcoustID lookup, and the library itself does not decode audio files, so fpcalc relies on FFmpeg.

## Links

- [Chromaprint homepage](https://acoustid.org/chromaprint)
- [Chromaprint GitHub repository](https://github.com/acoustid/chromaprint)
- [pyacoustid (Python wrapper)](https://github.com/beetbox/pyacoustid)
