---
name: ltc-tools
title: ltc-tools
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, jack, protocol, smpte, timecode]
homepage: https://github.com/x42/ltc-tools
scout_score: 8
status: draft
---

# ltc-tools

**TLDR;** Command-line tools that generate and decode linear timecode, the SMPTE clock signal from film and video that is carried as an audible audio tone.

Linear Timecode (LTC) is a way of putting a clock into an audio signal. The libltc README describes it as "an encoding of SMPTE timecode data as a Manchester-Biphase encoded audio signal" that is "commonly recorded on a VTR track or other storage media." In practice, hours, minutes, seconds and frames get turned into a stream of sound that a tape deck or audio interface can carry like any other track.

ltc-tools is a set of command-line front-ends built on the libltc library. The executable names suggest a split: ltcgen and jltcgen likely generate timecode, and ltcdump and jltcdump likely decode it. The jltc* names suggest JACK variants, and jltcntp, jltctrigger and jltc2mtc hint at NTP, triggering and MIDI timecode conversion. These roles are inferred from the names only. The project's README is two lines long and does not describe the individual tools.

The idea underneath is that a clock can be a sound. Once you see that, you can ask how two machines that share nothing but an audio cable stay in sync, and how film and broadcast gear solved that problem decades ago. libltc's documentation site is the place to start reading about the format.

## Install

```
brew install ltc-tools
# depends on jack, libltc and libsndfile, which brew pulls in. The jltc* tools likely expect a running JACK audio server, though the README does not say so.
```

## Try this

```
ltcgen --help
```
Prints the options of the timecode generator, which is the quickest way to see what it can write.

```
ltcdump --help
```
Prints the options of the decoder, which should read timecode out of an audio file.

```
jltcdump --help
```
Shows the usage of the JACK-based decoder, which presumably listens to a live JACK audio port.

## What's unique

It is a small, rare toolkit for a broadcast-era protocol where the clock is an audio signal you can record, play back and hear. Few command-line tools handle timecode at all.

## Caveats

The README is only two lines, so per-tool usage is undocumented in what was read, and the project's maintenance status is unknown; the jltc* tools probably need a JACK audio setup.

## Links

- [ltc-tools homepage (GitHub)](https://github.com/x42/ltc-tools)
- [libltc (required library, GitHub)](https://github.com/x42/libltc)
- [libltc API reference and docs](https://x42.github.io/libltc/)
