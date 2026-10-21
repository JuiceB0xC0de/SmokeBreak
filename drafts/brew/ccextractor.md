---
name: ccextractor
title: CCExtractor
source: brew
category: take-things-apart
commitment: quick
tags: [c, captions, quick, srt, subtitles, video]
homepage: https://www.ccextractor.org
scout_score: 6
status: draft
---

# CCExtractor

**TLDR;** Pulls closed captions and subtitles out of TV recordings and other media files, and writes them as SRT or WebVTT.

CCExtractor is a command-line tool, written mostly in C, that reads a media file such as a `.ts` transport stream and writes out the subtitles it finds. Per the README, SRT and WebVTT are among the output formats. It can also work in real time, translate subtitles, pull captions from DVDs, and convert closed captions into subtitles. There is a Windows GUI and a Flutter GUI too.

The project exists because subtitles matter to language learners and to people who are hard of hearing. Its stated aim is to make subtitle generation easy and to keep up with broadcast sources and formats around the world: "We intend to keep up with all sources and formats." The homepage claims that many subtitle files downloaded from the web for TV shows started life as its `.srt` output.

The door it opens is the idea that captions in a recording are data riding along with the video, not part of the picture, and that someone has to dig them out. The README does not explain how the extraction works internally, so that part is yours to explore. Run it on a recording, compare the output with what the player shows, and read the source if you want to know where the text comes from.

A small detail hints at the downstream uses: WebVTT output can optionally include an `X-TIMESTAMP-MAP` header, which HLS streaming workflows need and which is off by default.

## Install

```
brew install ccextractor
```

## Try this

```
ccextractor
```
Run with no arguments, it prints the list of parameters with a short description of each.

```
ccextractor input.ts
```
Extracts the subtitles from a media file you supply. The README's basic usage is `ccextractor <input>`.

```
ccextractor input.ts --timestamp-map -o output.vtt
```
Writes WebVTT output with the X-TIMESTAMP-MAP header that HLS workflows need.

## What's unique

It calls itself the de-facto open source standard for caption extraction, and aims to handle broadcast sources from almost anywhere in the world. Its `.srt` output reportedly ended up in many subtitle files people download.

## Caveats

The homepage says the project is still in beta, volunteers run it informally, and the README warns that source builds, especially with Rust, can hit unexpected build or link problems.

## Links

- [Homepage](https://www.ccextractor.org)
- [GitHub repository and README](https://github.com/CCExtractor/ccextractor)
- [Downloads](https://ccextractor.org/public/general/downloads/)
- [Command line usage docs](https://ccextractor.org/public/general/command_line_usage/)
