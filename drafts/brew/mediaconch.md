---
name: mediaconch
title: MediaConch
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, audio, ffv1, file-formats, matroska, preservation, video]
homepage: https://mediaarea.net/MediaConch
scout_score: 5
status: draft
---

# MediaConch

**TLDR;** A conformance checker for archival video and audio files that tells you whether a Matroska, FFV1 or LPCM file really follows its spec.

MediaConch checks preservation-level audiovisual files against rules. It has four parts: an implementation checker (does the file follow the format spec?), a policy checker (does it meet the rules your institution set?), a reporter, and a fixer. It targets Matroska, LPCM and FFV1, and it runs from the command line, a GUI, or a web interface. The output is conformance and technical reports.

It exists for memory institutions such as archives and libraries, which need to know that the files in their collections are valid and will stay readable. The project's stated aim is "furthering the longevity of Matroska, Linear Pulse Code Modulation (LPCM) and FF Video Codec 1 (FFV1) as recommended digital preservation audiovisual formats." The README frames it as a way to validate files, assess them, and find ways to repair them.

The idea underneath is that a file that plays is not the same as a file that is correct. Container formats leave room for malformed structures, odd choices and quiet corruption, and a long-term archive cannot rely on whichever player happens to forgive them. Checking a file against a spec and a written policy is a way to see how a media container is put together. The analysis engine is MediaInfoLib, extended with Matroska and FFV1 tests.

It comes from MediaArea, the team behind MediaInfo. They also contribute to the standardization of Matroska and FFV1 themselves, and they keep a public research corpus (MediaConch_MKVSurvey) and sample files for testing.

## Install

```
brew install mediaconch
```

## Try this

```
mediaconch --help
```
Prints the command-line options, which is the place to start since the brief lists no example commands.

## What's unique

It is aimed at archival preservation rather than general media inspection, and its authors help shape the Matroska and FFV1 standards it checks against.

## Caveats

The pages disagree on licensing (BSD-2-Clause on the homepage, GPLv3 or MPLv2 terms in the README), and the README says test-file coverage is still being built.

## Links

- [MediaConch homepage](https://mediaarea.net/MediaConch)
- [GitHub repository and README](https://github.com/MediaArea/MediaConch)
- [Downloads page](https://mediaarea.net/MediaConch/download.html)
- [MediaConchOnline](https://mediaarea.net/MediaConchOnline/)
