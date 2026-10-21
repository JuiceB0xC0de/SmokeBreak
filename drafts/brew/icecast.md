---
name: icecast
title: Icecast
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, http, internet-radio, network, streaming]
homepage: https://icecast.org/
scout_score: 5
status: draft
---

# Icecast

**TLDR;** Free server software from Xiph.org that takes an audio stream from a source and serves it to listeners over HTTP, the machinery behind many internet radio stations.

Icecast takes live or prerecorded audio and video from a source and serves it to listeners over HTTP. Its homepage says it supports Ogg (Vorbis and Theora), Opus, WebM and MP3. It can run an internet radio station, a private jukebox, or something in between.

It comes from Xiph.org, the group behind Opus, FLAC, Vorbis, Theora, Speex and XSPF, and has a long history in internet radio. The homepage describes it as versatile: new formats can be added relatively easily, and it supports open standards for communication and interaction.

The idea underneath is that a radio station can be an ordinary web server holding a long-lived connection open. A source client sends audio in, the server relays it to however many listeners connect, and nothing needs special infrastructure. The homepage and docs index do not spell out the input protocol or listener URLs, so the version-specific docs are the place to learn those details.

The brew description says 'Streaming MP3 audio server', which undersells it. MP3 is only one of several formats it handles.

## Install

```
brew install icecast
# The brief gives no first-run steps. You will also need a source client to send audio in, and the docs for your version explain configuration.
```

## Try this

```
icecast --help
```
Prints the server's command-line options, the safest first look since the brief lists no other commands.

## What's unique

It serves several open codecs (Ogg Vorbis/Theora, Opus, WebM) alongside MP3 from one server, and it belongs to the Xiph.org family of open media formats.

## Caveats

The 2.5.0 docs are marked WIP, and 2.4.4 gets only security fixes, with support ending 2026-12-31; the brief gives no install or first-run steps.

## Links

- [Icecast homepage](https://icecast.org/)
- [Icecast documentation index](https://icecast.org/docs/)
