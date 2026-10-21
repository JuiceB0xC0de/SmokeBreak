---
name: minidlna
title: minidlna (ReadyMedia)
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, daemon, dlna, network, protocol, upnp]
homepage: https://sourceforge.net/projects/minidlna/
scout_score: 6
status: draft
---

# minidlna (ReadyMedia)

**TLDR;** A small C daemon that serves your music, photos and video to TVs and media players on the home network, via DLNA/UPnP-AV.

ReadyMedia, formerly MiniDLNA, is a media server daemon. Point it at folders of music, photos and video, and DLNA/UPnP-AV clients on the same network, such as smart TVs and media players, can find and play them. Its executable is `minidlnad`, a non-interactive daemon written in C. The project describes itself as "a simple media server software, with the aim of being fully compliant with DLNA/UPnP-AV clients."

It began life at NETGEAR: "originally developed by a NETGEAR employee for the ReadyNAS product line." That explains its shape, a small single-purpose service meant to run quietly on a modest box and do one job. The project also states that it is not endorsed by the Digital Living Network Alliance.

The interesting part is what sits underneath. A server like this is a way into how consumer devices discover and talk to each other on a home network: a TV appears to find the server on its own, browses a catalogue, and streams a file. The scout's view is that this makes it a practical door into the UPnP-AV family of protocols. The project page itself does not go into protocol detail, so the specifics are left for you to explore with a packet capture or the UPnP specs.

## Install

```
brew install minidlna
# To use `brew services`, put your configuration at ~/.config/minidlna/minidlna.conf
# Needs DLNA/UPnP-AV clients (a TV or media player) on the same network to be worth running.
```

## Try this

```
minidlnad --help
```
Prints the daemon's command-line options, the safest first look since the project page gives no usage examples.

## What's unique

It is a deliberately small, single-purpose C daemon for the server side of DLNA/UPnP-AV, born in a NAS product rather than as a general media centre.

## Caveats

The SourceForge page is thin, with no README or usage docs, is tagged Linux-only, and was last updated in June 2023.

## Links

- [SourceForge project page (homepage)](https://sourceforge.net/projects/minidlna/)
