---
name: codec2
title: Codec 2
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, c, codec, radio, speech]
homepage: https://www.rowetel.com/?page_id=452
scout_score: 7
status: draft
---

# Codec 2

**TLDR;** An open source speech codec that squeezes intelligible voice into 700 to 3200 bits per second, built for amateur digital radio.

Codec 2 takes raw 16-bit, 8 kHz speech samples and turns them into a bitstream of somewhere between 700 and 3200 bits per second. A matching decoder turns that stream back into speech. For scale, that is a small fraction of what a phone call uses. The installed programs are c2enc, c2dec, c2demo and c2sim, and they are written in C99.

It exists for low bandwidth HF and VHF digital radio, where every bit costs signal strength. The homepage says it fills a gap in open source voice codecs below 5000 bit/s, and that informal listening tests put the 700 bit/s mode above MELP and comparable to TWELP at 600 bit/s. The codec grew out of a 1997 PhD thesis on harmonic sinusoidal coding, and the homepage notes that it has just one voicing bit, unlike mixed excitation codecs such as AMBE and MELP.

The repo is larger than the codec. It also holds HF/VHF modems (OFDM, FSK and others), the FreeDV API that combines codec, modem and forward error correction, and GNU Octave simulation code. Seen that way, the codec is one layer of a complete open digital voice radio stack, and the rest of the stack is there to read.

The fun part is listening. Encode the same sample at 3200, then 1300, then 700C, and hear what a voice sounds like as the budget shrinks. The README points to doc/codec2.pdf for the algorithm itself.

## Install

```
brew install codec2
# The README's own samples (raw/hts1a.raw) come from the git repo: git clone https://github.com/drowe67/codec2. You can also feed in your own raw 16-bit, 8 kHz mono speech file.
```

## Try this

```
c2enc 2400 hts1a.raw hts1a_c2.bit
```
Compresses a raw speech file to a bit file at 2400 bit/s.

```
c2dec 2400 hts1a_c2.bit hts1a_c2_2400.raw
```
Decodes the bit file back to raw speech samples you can play and compare.

```
c2enc 700C hts1a.raw hts1a_c2.bit
```
Encodes the same speech at 700 bit/s so you can hear how much the voice degrades.

## What's unique

It is an open codec aimed at the range below 5000 bit/s, where the well-known alternatives are proprietary. It sits in a repo that also has the modems and voice protocol it was built to travel over.

## Caveats

The maintainers say they have limited resources, and several modes (including 700C) are no longer actively maintained after a 2023 refactor; the README says a major redevelopment is under way. Background noise is a known weak point, and the tools expect raw 8 kHz 16-bit audio rather than WAV files.

## Links

- [Homepage (Rowetel, Codec 2 page)](https://www.rowetel.com/?page_id=452)
- [GitHub repository (drowe67/codec2)](https://github.com/drowe67/codec2)
- [FreeDV project site](https://freedv.org)
- [FreeDV GUI repository](https://github.com/drowe67/freedv-gui)
