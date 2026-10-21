---
name: liquidsoap
title: Liquidsoap
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, ffmpeg, language, radio, streaming, video]
homepage: https://www.liquidsoap.info
scout_score: 7
status: draft
---

# Liquidsoap

**TLDR;** A scripting language for building radio stations and video streams, where playlists, crossfades and fallbacks are operators you wire together in a short file.

Liquidsoap is a language for describing audio and video streams. You write a `.liq` script that declares sources, such as a folder of music, a playlist, or a live RTMP feed from OBS. You combine them with operators like `rotate`, `crossfade` and `fallback`, then send the result to an output such as an Icecast server, YouTube Live over RTMP, SRT or HLS. The `liquidsoap` binary runs that graph as a long-lived process.

The idea underneath is that a radio station is a program. Its logic is what plays next, what happens when the live feed drops, and how tracks blend. That logic normally lives in a pile of config knobs or in a human at a mixing desk. Here it is code. The project's own phrasing is "Not a configuration file with a fixed set of knobs, but a real language built for streaming, so anything you can describe you can build."

FFmpeg is wired in, so the same language can re-encode a stream with FFmpeg encoders and filters, or pass it through untouched when no re-encoding is needed. Scheduling and request backends plug in as operators too, which keeps the station's behaviour next to the audio it controls.

It is aimed at internet radio and web TV. It is also a good way to see how a streaming pipeline fits together: sources, transformations and outputs as a graph.

## Install

```
brew install liquidsoap
# pulls in ffmpeg as a dependency. No account or hardware needed. The homepage recommends opam as the main route; the README also publishes apt, dnf and apk repositories.
```

## Try this

```
liquidsoap --help
```
Lists the command-line options of the interpreter so you can see how scripts are run.

```
./liquidsoap your_script.liq
```
Runs a script of your own. The README gives this form for running from a build tree, and with a brew install you would call `liquidsoap your_script.liq` instead.

## What's unique

The configuration is a real language, so a complete internet radio with weighted rotation, crossfades and an Icecast output fits in about ten lines. Most streaming tools give you a fixed set of settings instead.

## Caveats

The README warns that bugfix releases can change operator behaviour and break existing scripts, so it recommends a staging environment; the language server is also marked experimental.

## Links

- [Homepage](https://www.liquidsoap.info)
- [GitHub repository and README](https://github.com/savonet/liquidsoap)
- [Browser playground](https://www.liquidsoap.info/try/)
- [The Liquidsoap book (PDF)](http://www.liquidsoap.info/book/book.pdf)
