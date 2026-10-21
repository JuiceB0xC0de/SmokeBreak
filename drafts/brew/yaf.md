---
name: yaf
title: yaf
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ipfix, netflow, network, pcap, protocol]
homepage: https://tools.netsa.cert.org/yaf/
scout_score: 6
status: draft
---

# yaf

**TLDR;** A flowmeter that reads packets from an interface or pcap file and writes compact IPFIX records, one per connection, with optional protocol details attached.

YAF (Yet Another Flowmeter) watches network traffic, live or from a capture file, and groups the packets into bidirectional flows. Each flow becomes an IPFIX record describing one connection. Most of the payload is thrown away. In the project's words, "Flow records use a binary format, so they are much smaller than full packet captures or textual representations of the data."

It can also look inside payloads. When application labelling is enabled and a protocol is recognised (DNS, SSL, HTTP, SMTP and others), YAF exports protocol-specific fields alongside the flow. The homepage calls this deep packet inspection. Recognition works through regular expressions or plug-ins, and it has to be switched on.

YAF is the data collection component of the CERT NetSA Security Suite. It feeds downstream tools such as Analysis Pipeline, SiLK and Mothra. It began as an experimental implementation tracking IETF IPFIX work on bidirectional flows, archival formats and structured DPI export. That makes it a way into the question of what to keep when you cannot keep every packet.

Two features stand out. A packet-per-flow mode turns each packet into a one-packet flow, which keeps volume and timing without the full capture. The homepage suggests it for analysing covert timing channels and session hijacking. When reading pcap files, YAF can also write a metadata file of flow key hash, millisecond start time and capture file name. That lets an analyst find the same flow across several captures and pull the matching packets back out of the originals.

## Install

```
brew install yaf
# Dependencies pulled in by brew: glib, libfixbuf, libtool, gettext, pcre2. Live capture needs an interface you can read; pcap files work without one.
```

## Try this

```
yaf --help
```
Lists the options for input (live interface or pcap file), output (IPFIX), application labelling and pcap splitting.

```
yafscii --help
```
Shows usage for the tool that prints YAF's IPFIX output as text you can read.

```
yafMeta2Pcap --help
```
Shows how the flow metadata index is used to pull matching packets back out of the original captures.

## What's unique

Beyond plain flow export, it keeps a flow key hash index so one flow can be traced across several capture points and its packets recovered from the original pcaps. Its packet-per-flow mode keeps per-packet timing without storing the capture.

## Caveats

The current 3.x download is labelled pre-release (3.0.0.alpha4) and 2.x is the stable line, and DPI fields only appear when application labelling is enabled and the protocol is recognised.

## Links

- [YAF homepage](https://tools.netsa.cert.org/yaf/)
