---
name: snapcast
title: Snapcast
source: brew
category: sound-and-live-coding
commitment: afternoon
tags: [afternoon, audio, multiroom, network, streaming, sync]
homepage: https://github.com/snapcast/snapcast
scout_score: 5
status: draft
---

# Snapcast

**TLDR;** Snapcast turns any audio source into a synchronized multiroom system, with every client playing the same stream within a fraction of a millisecond.

Snapcast is a client-server audio system. The server, `snapserver`, reads raw PCM audio from a source such as a named pipe (`/tmp/snapfifo`), an ALSA capture device, a TCP stream, or another process's stdout. It encodes the audio (FLAC by default, or PCM, Vorbis, Opus), stamps each chunk with the server's time, and sends it over TCP to any number of `snapclient` programs. Each client plays through its operating system's audio API.

It is not a player. In the README's words, it is "an extension that turns your existing audio player into a Sonos-like multiroom solution." You point MPD, Mopidy, mpv, VLC or similar at the pipe, and Snapcast handles distribution. The aim is multiroom audio without buying proprietary hardware, while staying generic about what produces the sound.

The interesting part is the timing. Each client continuously syncs its clock with the server, buffers decoded chunks, and plays each one at the right server-time moment. When a client's clock drifts, it does not resample. It drops or duplicates single samples, which the README says is inaudible, and it claims the typical deviation stays below 0.2 ms. That claim is the author's own and was not verified here.

Control goes through a bundled web app (Snapweb) and a JSON-RPC API covering volume, mute, naming, streams and groups. Third-party controllers exist, including Home Assistant, Music Assistant, an Android app and an ESP32 client.

## Install

```
brew install snapcast
# Installs snapserver and snapclient. Server config lives in /etc/snapserver.conf. You also need an upstream player or source to feed audio into the server.
```

## Try this

```
cat /dev/urandom > /tmp/snapfifo
```
With snapserver running and a client connected, pipes random noise into the server's fifo so the client plays static, which confirms the chain works.

```
man snapserver
```
Shows the server's command-line options and how it reads its configuration.

```
snapclient --help
```
Lists the client's options, including how to choose an audio backend and sound card.

## What's unique

It keeps clients in sync by dropping or duplicating individual samples rather than resampling, and it works with whatever player you already use. A wide set of inputs and third-party controllers surrounds it.

## Caveats

It is not a standalone player and needs something feeding its pipe, and the brief could not confirm recent release activity.

## Links

- [GitHub homepage and README](https://github.com/snapcast/snapcast)
- [Configuration docs](https://github.com/snapcast/snapcast/blob/master/doc/configuration.md)
- [Player setup guide (MPD, Mopidy, and others)](https://github.com/snapcast/snapcast/blob/master/doc/player_setup.md)
- [JSON-RPC control API](https://github.com/snapcast/snapcast/blob/master/doc/json_rpc_api/control.md)
