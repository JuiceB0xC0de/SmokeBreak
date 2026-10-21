---
name: shairport-sync
title: shairport-sync
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, airplay, audio, clock-sync, multi-room, network, protocol]
homepage: https://github.com/mikebrady/shairport-sync
scout_score: 5
status: draft
---

# shairport-sync

**TLDR;** An AirPlay audio receiver that turns a Unix machine into a speaker target, and keeps playback locked to the sender's clock by resampling on the fly.

Shairport Sync receives audio streamed from Apple devices, or from other AirPlay sources such as OwnTone, and hands it to a sound system (ALSA, sndio, PipeWire, PulseAudio, CoreAudio), a unix pipe, or STDOUT. It can be built for AirPlay 2, with stereo, multichannel and lossless 24-bit stereo at 48,000 frames per second, or as classic AirPlay 1. Metadata such as artist and cover art, plus remote control, are exposed over MQTT, D-Bus and an MPRIS-like interface.

The interesting part is timing. In the README's words, "Full audio synchronisation means that audio is played on the output device at exactly the time specified by the audio source." Rather than just buffering, it compares the source's timestamps with timing feedback from the local audio system, then adds or drops frames by resampling slightly so playback stays in step. libsoxr provides higher-quality resampling when the CPU can afford it. That is what makes several receivers in a house play the same thing together.

The README says Apple's AirPlay protocols are unpublished, so the project is the result of study and analysis of how they behave. It descends from a substantial rewrite of Shairport 1.0. For AirPlay 2, clock sync uses PTP through a separate companion daemon called NQPTP, while classic AirPlay uses a variant of NTP-style synchronisation. Reading how those two differ is a good way into how networked audio stays in time.

## Install

```
brew install shairport-sync
# The brief did not verify the Homebrew formula. The README points to BUILD.md for building from source; some features need build-time flags (CONFIGURATION FLAGS.md).
# AirPlay 2 builds need the separate NQPTP companion app.
# Runtime settings: scripts/shairport-sync.conf. A Docker image is also available: mikebrady/shairport-sync.
```

## Try this

```
shairport-sync --help
```
Prints the command-line options, including how to choose the output backend and receiver name.

## What's unique

Most receivers just buffer. This one stretches and shrinks the stream by resampling to hold playback within a fraction of a millisecond of the source clock with ALSA, and it comes with its own AirPlay 2 timing companion.

## Caveats

The AirPlay protocols are unofficial, so the README gives no assurance it will keep working; it also does not support AirPlay video or photo streaming, AirPlay 2 has listed limitations, and timing is weaker through PipeWire and PulseAudio than through ALSA or sndio.

## Links

- [Homepage (GitHub repo and README)](https://github.com/mikebrady/shairport-sync)
- [Building guide (BUILD.md)](https://github.com/mikebrady/shairport-sync/blob/master/BUILD.md)
- [AirPlay 2 features and limitations (AIRPLAY2.md)](https://github.com/mikebrady/shairport-sync/blob/master/AIRPLAY2.md)
- [Docker Hub image](https://hub.docker.com/r/mikebrady/shairport-sync)
