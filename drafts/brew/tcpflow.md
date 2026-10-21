---
name: tcpflow
title: tcpflow
source: brew
category: fundamentals
commitment: quick
tags: [forensics, network, pcap, protocol, quick, tcp]
homepage: https://github.com/simsong/tcpflow
scout_score: 5
status: draft
---

# tcpflow

**TLDR;** tcpflow turns captured TCP traffic into a directory of files, one per connection and direction, so you can grep a network conversation like text.

tcpflow reads TCP packets, either live from a network interface through libpcap or from a saved tcpdump capture, and rebuilds each connection as its own byte stream. Every direction of every flow becomes a file named after the source and destination IP and port. It can also write a DFXML report listing each flow's addresses, ports, byte and packet counts, and optionally an MD5 of each stream.

It was written by Jeremy Elson to capture data from programs that speak undocumented protocols, so they could be reverse engineered. It was later used for HTTP analysis. Simson Garfinkel now maintains it and uses it for network forensics. The README puts the aim this way: "tcpflow can show hundreds, thousands, or hundreds of thousands of TCP connections in context."

The idea underneath is that a packet capture is a pile of fragments, and the conversation only appears once you reassemble it. tcpflow tracks sequence numbers, so it rebuilds streams correctly despite retransmissions or out-of-order delivery. Once each conversation is a plain file, the usual Unix tools work on it: grep, hash, diff, or feed it to something else. With `-a` it also splits HTTP responses into header and body files, and decompresses gzip bodies into a separate file.

## Install

```
brew install tcpflow
# Capturing live packets usually needs root or capture privileges. Reading a saved capture file does not.
```

## Try this

```
tcpflow --help
```
Lists the options, including the output file name template controls (-F and -T) and the HTTP post-processing option (-a).

## What's unique

Wireshark shows packets or one connection at a time. tcpflow gives you a folder of every connection, ready for grep and scripts, and can pull HTTP bodies out of a capture.

## Caveats

It does not handle IP fragments, so flows containing them are recorded incorrectly (the README calls this rare), and the project looks quiet, with a 1.6 rewrite described in 2020 as about three quarters done.

## Links

- [GitHub repository (homepage)](https://github.com/simsong/tcpflow)
- [Technical report: Passive TCP Reconstruction and Forensic Analysis with tcpflow](https://calhoun.nps.edu/handle/10945/36026)
- [Downloads directory (DigitalCorpora)](http://digitalcorpora.org/downloads/tcpflow/)
- [Open issues](https://github.com/simsong/tcpflow/issues?state=open)
