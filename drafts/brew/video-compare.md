---
name: video-compare
title: video-compare
source: brew
category: take-things-apart
commitment: quick
tags: [codecs, ffmpeg, gui, quick, sdl2, video]
homepage: https://github.com/pixop/video-compare
scout_score: 5
status: draft
---

# video-compare

**TLDR;** Plays two videos in sync under a draggable slider so you can see exactly what a codec, resize, or filter did to every frame.

video-compare opens two video files (or a reference plus several renditions, or one file against itself) in a single SDL2 window. A slider splits the picture between them, or you can stack them vertically or switch to a subtraction view that shows only the differences. The inputs can differ in resolution, frame rate, codec, container, colour format, dynamic range, or duration. It also handles images and image sequences.

It exists for the question anyone who encodes video eventually asks: what did this setting actually change? The README describes it as a way to visually compare the impact of codecs, resizing algorithms, and other modifications on two files played in sync. Since FFmpeg does the decoding, you can pass FFmpeg filter chains to each side separately with `-l` and `-r`. That lets you crop, pad, convert to grayscale, deinterlace, denoise, or change speed before the comparison. The README calls it "the Swiss Army knife for cropping/padding (comparing videos with different aspect ratios), adjusting colors, deinterlacing, denoising, speeding up/slowing down, etc."

The idea underneath is that compression and processing losses are hard to describe but easy to see when two versions sit next to each other. A `__` placeholder compares a video against a filtered or time-shifted copy of itself without retyping the path. A time-shift flag lines up files that are slightly out of sync. Playback runs from an in-memory buffer, with frame stepping and zoom for inspecting single frames.

## Install

```
brew install video-compare
# optional, for broader codec and format support such as JPEG XL:
brew install ffmpeg-full
# needs a desktop session: it opens an SDL2 window
```

## Try this

```
video-compare video1.mp4 video2.mp4
```
Opens a window with both videos in sync and a slider you move to reveal one or the other.

```
video-compare -m vstack video1.mp4 video2.mp4
```
Stacks the two videos vertically at full size, with no slider.

```
video-compare -l crop=iw:ih-240 -r format=gray,pad=iw+320:ih:160:0 video1.mp4 video2.mp4
```
Applies a different FFmpeg filter chain to each side: the left is cropped, the right is turned grayscale and padded.

## What's unique

The per-side `-l` and `-r` flags take any FFmpeg filter chain, and the `__` placeholder compares a file against a processed copy of itself. Together with the multi-rendition mode, that makes it a tool for judging encoder output, not just a player with two panes.

## Caveats

There is no audio playback, seeks land on the nearest keyframe, and the README gives no clear sign of recent activity; pre-built binaries exist only for Windows 10 64-bit.

## Links

- [GitHub repository and README (homepage)](https://github.com/pixop/video-compare)
- [Homebrew formula](https://formulae.brew.sh/formula/video-compare)
- [Releases (Windows binaries)](https://github.com/pixop/video-compare/releases)
