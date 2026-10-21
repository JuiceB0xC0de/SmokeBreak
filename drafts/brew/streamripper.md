---
name: streamripper
title: streamripper
source: brew
category: fundamentals
commitment: quick
tags: [internet-radio, mp3, network, protocol, quick, shoutcast]
homepage: https://streamripper.sourceforge.net/
scout_score: 5
status: draft
---

# streamripper

**TLDR;** A command-line recorder that captures an internet radio stream to disk and, per its description, cuts it into tracks using the titles the station sends.

Streamripper is a GPL command-line program for recording streaming MP3 radio. Point it at a stream and it writes the audio to your hard drive. The homepage describes it as an application "that lets you record streaming mp3 to your hard drive".

The interesting part is the splitting. Per Homebrew's description and the scout's notes, it uses Shoutcast's title-streaming to separate tracks. A radio stream is one endless run of audio, but the server also sends song titles alongside it. Streamripper can watch for those title changes and use them as cut points, so you get one file per song rather than one giant recording. The brief did not confirm the mechanism from the docs, so treat the details as something to look up.

The idea underneath is in-band signalling: a continuous stream carries its own labels, and a small tool can use them to turn a firehose into structured files. It is a good way into how Shoutcast-style streaming works over plain HTTP.

The project is old. The homepage news stops in 2008, and the site lists many front ends, from Windows to OSX to Java, several of them marked dead. The command-line tool is the part Homebrew installs.

## Install

```
brew install streamripper
```

## Try this

```
streamripper --help
```
Prints the list of options so you can see what the recorder can do before pointing it at a stream.

## What's unique

It turns a continuous radio stream into per-track files by reading the stream's own title metadata. It also has an unusually large family of front ends for a project this small.

## Caveats

The homepage's news ends in 2008, several listed front ends are marked dead, and the track-splitting mechanism was not verified against the docs.

## Links

- [Streamripper homepage](https://streamripper.sourceforge.net/)
