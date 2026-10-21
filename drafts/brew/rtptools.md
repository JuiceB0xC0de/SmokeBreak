---
name: rtptools
title: rtptools
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, network, packets, protocol, rtp, voip]
homepage: https://github.com/irtlab/rtptools
scout_score: 6
status: draft
---

# rtptools

**TLDR;** Six small Unix programs that record, replay, hand-build and relay RTP streams, the packet format underneath VoIP calls and video conferencing.

RTP, the Real-time Transport Protocol, is how audio and video usually travel across a network in phone calls and video conferences. rtptools is a set of small command-line programs for handling that traffic. The README describes them as "a set of small applications that can be used for processing RTP data."

The core is a record-and-replay pair. rtpdump parses RTP packets and prints their details, and can also write them to a file. rtpplay plays a recorded session back onto the network. rtpsend takes a textual description of packets, written by hand or produced by rtpdump, and generates real RTP packets from it. multidump and multiplay start several rtpdump or rtpplay instances at once.

The sixth tool, rtptrans, is an RTP translator. It relays a stream between unicast and multicast networks, which is the sort of plumbing a conference system needs when some participants cannot receive multicast.

The idea underneath is that a real-time media stream is just packets you can capture, read as text, edit and send again. Once you can do that, you can see sequence numbers, timestamps and payload types for yourself, and fake a stream without a phone or camera. The README gives no usage examples and sends readers to the individual manpages.

## Install

```
brew install rtptools
```

## Try this

```
rtpdump --help
```
Prints the usage summary for the tool that parses and records RTP packets.

```
rtpplay --help
```
Shows the options for replaying a session recorded by rtpdump.

```
rtpsend --help
```
Shows how to generate RTP packets from a textual description.

## What's unique

It is a small record, edit and replay pipeline for RTP, where rtpdump's output is designed to feed rtpplay and rtpsend. Each tool does one job in the Unix manner.

## Caveats

The README has no usage examples and no sign of recent activity, so expect to learn from the manpages, and you will need RTP traffic or a hand-written packet description to play with.

## Links

- [GitHub repository (homepage)](https://github.com/irtlab/rtptools)
