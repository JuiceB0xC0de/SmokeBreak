---
name: oggz
title: oggz
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, audio, cli, containers, file-formats, ogg]
homepage: https://www.xiph.org/oggz/
scout_score: 5
status: draft
---

# oggz

**TLDR;** A command-line toolkit for looking inside Ogg files: dump packets, validate streams, cut by time, and merge or sort logical bitstreams.

Oggz is a C library, liboggz, with a command-line tool on top. The main `oggz` binary takes subcommands such as info, dump, scan, validate, chop, merge, sort, rip, comment and diff. Most of them also install as separate `oggz-*` executables. It reads Ogg files that follow RFC3533 and can parse the headers for CELT, CMML, FLAC, Kate, PCM, Speex, Theora and Vorbis, plus Ogg Skeleton streams.

The homepage describes liboggz as an improvement on the reference libogg, adding seeking, validation and timestamp interpretation. The tool exposes those features for everyday work. Output is either a new Ogg file, a text report, or a hexdump of packets. `dump` can also turn a hexdump back into an Ogg file, so you can edit packets by hand and rebuild the file.

The underlying idea is that Ogg is a container: pages of packets, grouped into logical bitstreams, with the codec data inside. Oggz lets you see that structure. Its `chop` command shows why it matters. To cut a time range, it keeps copies of the input headers plus the codec data needed to start decoding, including the prior keyframe for video codecs. The clip therefore begins in a decodable state.

`oggz-chop` can also detect that it is running as a CGI script and read a `t=` query parameter. A web server can then serve time slices of Ogg media over HTTP without a streaming server.

## Install

```
brew install oggz
```

## Try this

```
oggz --help
```
Lists the subcommands and options for the main tool.

```
oggz help chop
```
Shows help for the chop subcommand, which cuts a time range out of an Ogg file.

## What's unique

It treats Ogg as a container you can open up, with packet hexdumps that round-trip back to a file. Its time-based chop keeps the codec dependencies so a cut clip still decodes, and it can run as a CGI script.

## Caveats

Header parsing and seeking only cover a specific set of codecs, so other codecs may not be understood, and the chop CGI setup needs a web server configured by hand.

## Links

- [Oggz homepage](https://www.xiph.org/oggz/)
- [liboggz git repository (gitlab)](https://gitlab.xiph.org/xiph/liboggz)
- [Xiph downloads](https://xiph.org/downloads/)
