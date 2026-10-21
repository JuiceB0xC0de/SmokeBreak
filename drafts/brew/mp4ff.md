---
name: mp4ff
title: mp4ff
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, file-formats, go, library, mp4, streaming, video]
homepage: https://github.com/Eyevinn/mp4ff
scout_score: 5
status: draft
---

# mp4ff

**TLDR;** A Go library and nine command-line tools that print the box tree inside MP4 files and rewrite, crop, encrypt or decrypt them.

mp4ff reads and writes MP4, the ISO base media file format (ISOBMFF). An MP4 file is a nested tree of boxes, each with a four-letter name and a size. mp4ff parses that tree into Go types and writes it back out. It understands AVC and HEVC video, AAC and AC-3 audio, stpp and wvtt subtitles and timed metadata, and the brief lists further codecs including AV1, VP8/VP9, VVC, IAMF and MPEG-H 3D Audio.

The project is focused on fragmented MP4, the variant used for streaming in MPEG-DASH, MSS and HLS fMP4, though it also handles progressive files. A progressive file keeps one moov box and one mdat box. A fragmented file has an init segment followed by many small segments, each carrying its own metadata and media data. The library exposes both shapes, and it has a lazy mode that reads only metadata and fetches media bytes by range later.

The command-line tools are thin front ends on that library. mp4ff-info prints the box hierarchy as a tree, which is a good way to see how a file is built. mp4ff-pslister, mp4ff-nallister and mp4ff-subslister list parameter sets, NAL units and subtitles. mp4ff-crop, mp4ff-defragment, mp4ff-encrypt, mp4ff-decrypt and mp4ff-mvhevc write new files. Encryption covers the CENC schemes cenc and cbcs.

The idea underneath is that most video you watch online is a stack of these boxes, and once you can see them, streaming stops being a black box. The README does not describe the output format of the listers, so look at the output before relying on it.

## Install

```
brew install mp4ff
# or, with Go: go install github.com/Eyevinn/mp4ff/cmd/mp4ff-info@latest (repeat per tool)
# No account or hardware needed for the local tools.
```

## Try this

```
mp4ff-info --help
```
Shows the options for the tool that prints an MP4 file's box hierarchy as a tree.

```
mp4ff-nallister --help
```
Shows how to list the NAL units inside a video track.

```
mp4ff-defragment --help
```
Shows how to turn a fragmented MP4 into a progressive one.

## What's unique

Most MP4 tools only inspect files. mp4ff is also a library that rewrites boxes and handles CENC encryption and decryption, with broad codec coverage.

## Caveats

The README says the API is pre-1.0 and may change in minor ways, mp4ff-crop only works on progressive files, and mp4ff-encrypt and mp4ff-decrypt only on fragmented ones.

## Links

- [Homepage and README (GitHub)](https://github.com/Eyevinn/mp4ff)
- [ChangeLog](https://github.com/Eyevinn/mp4ff/blob/master/CHANGELOG.md)
- [Releases](https://github.com/Eyevinn/mp4ff/releases)
