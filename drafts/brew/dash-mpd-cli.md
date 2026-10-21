---
name: dash-mpd-cli
title: dash-mpd-cli
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, dash, media, protocol, rust, streaming, video]
homepage: https://emarsden.github.io/dash-mpd-cli/
scout_score: 5
status: draft
---

# dash-mpd-cli

**TLDR;** Feed it a DASH manifest URL and it fetches the segments and muxes them into one local video file, exposing how adaptive streaming is assembled.

Most streaming video is not a file. It is a manifest, an XML document called an MPD, that lists audio and video tracks at several bitrates, each cut into short segments served over plain HTTP. dash-mpd-cli reads that manifest, picks a representation by bitrate, codec, language, resolution, stream id or role, downloads the segments, and hands them to an external muxer to stitch into a single file.

The output container comes from the filename extension. Asking for .mkv, .mp4 or .webm makes it try mkvmerge, ffmpeg, VLC or MP4Box in a preference order, which `--muxer-preference` can override. It can also fetch subtitles in formats such as WebVTT, TTML and SRT.

The author wrote it to watch a public broadcaster's replay programme at a gym with a flaky network. The README describes it as a tool for downloading media for local use. Underneath is the idea that a player is just a client making a series of HTTP requests against a manifest. Once you see that, you can follow how a player picks quality, and where multi-period manifests and XLink elements fit in.

It is written in Rust, MIT-licensed, and built on the dash-mpd-rs library. It can also read browser cookies, send Basic or Bearer auth, and rewrite the MPD with an XSLT stylesheet before downloading.

## Install

```
brew install dash-mpd-cli
# Homebrew pulls in ffmpeg, bento4 and mkvtoolnix. Alternatives: cargo install dash-mpd-cli, or the container ghcr.io/emarsden/dash-mpd-cli (about 220 MB, bundles every helper). You need an MPD URL to do anything useful.
```

## Try this

```
dash-mpd-cli --help
```
Prints the full list of flags for choosing quality, muxers, auth, subtitles and decryption.

```
podman run --rm -v .:/content ghcr.io/emarsden/dash-mpd-cli -v <MPD-URL> -o foo.mp4
```
Runs the container, downloads the stream behind the manifest verbosely, and writes foo.mp4 to the current directory.

## What's unique

The README claims it handles multi-period manifests, XLink elements and xHE-AAC audio that yt-dlp, ffmpeg, VLC and streamlink reportedly fail on. It can also rewrite the manifest with XSLT before downloading.

## Caveats

Live DASH streams are not really supported (pseudo-live works with --enable-live-streams), HLS and Smooth Streaming are out, DRM needs a key you supply, and the brief could not confirm recent release dates.

## Links

- [Homepage and user manual](https://emarsden.github.io/dash-mpd-cli/)
- [GitHub repository and README](https://github.com/emarsden/dash-mpd-cli)
- [dash-mpd-rs core library](https://github.com/emarsden/dash-mpd-rs)
