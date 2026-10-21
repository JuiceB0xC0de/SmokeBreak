---
name: ndpi
title: nDPI
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, c, dpi, library, network, protocol]
homepage: https://www.ntop.org/products/deep-packet-inspection/ndpi/
scout_score: 5
status: draft
---

# nDPI

**TLDR;** An open source C library that works out which application protocol a network flow belongs to by looking at the traffic itself, not the port number.

nDPI is a deep packet inspection library. Give it packets or flows and it reports the application protocol (the README cites 450+), a traffic category, flow risks, and metadata such as URLs, TLS certificates and operating system. It is built to be embedded in other software through a C API. ntop's own tools (ntopng, nProbe, nProbe Cento) use it, and so do third-party applications.

The homepage says it extends the original OpenDPI library, adding protocols that were otherwise only in OpenDPI's paid version, under the LGPL. The underlying problem is stated in the README: "nowadays the concept of port=application no longer holds." Port 443 can carry almost anything, so the only way to classify traffic is to inspect payloads and flow behaviour.

That is the door it opens. Each protocol has its own dissector under src/lib/protocols/, so you can read how a protocol is recognised from its first few packets. The homepage also describes ETA (Encrypted Traffic Analysis) for classifying TLS and QUIC without decrypting, and FPC (First Packet Classification).

The brief does not document what the two Homebrew executables, ndpiReader and ndpiSimpleIntegration, do. Their names suggest a packet reader and a minimal integration example, but treat that as a guess and check --help.

## Install

```
brew install ndpi
```

## Try this

```
ndpiReader --help
```
Prints the options of the installed reader tool, which is the quickest way to see what it can do.

```
ndpiSimpleIntegration --help
```
Shows how the second installed executable is invoked, if it offers help output.

## What's unique

It is a library rather than a sniffer, and the README says ntop removed features that slow the engine for monitoring use. It also goes past naming the protocol to extract metadata, flag risks, and classify encrypted TLS and QUIC traffic.

## Caveats

The README admits detection is not guaranteed to be error free or 100% accurate, and asks you to have authorization before inspecting traffic you do not own.

## Links

- [nDPI product page (homepage)](https://www.ntop.org/products/deep-packet-inspection/ndpi/)
- [GitHub repository and README](https://github.com/ntop/ndpi)
- [Paper: nDPI: Open-source high-speed deep packet inspection (IWCMC 2014)](http://luca.ntop.org/nDPI.pdf)
- [The Ultimate Guide to nDPI (YouTube, 2025)](https://www.youtube.com/watch?v=NndEp7__Y1A)
