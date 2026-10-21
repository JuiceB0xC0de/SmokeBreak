---
name: lft
title: lft
source: brew
category: fundamentals
commitment: quick
tags: [network, protocol, quick, tcp, traceroute]
homepage: https://pwhois.org/lft/
scout_score: 6
status: draft
---

# lft

**TLDR;** A traceroute that works at the transport layer, aimed at tracing paths through networks where ordinary traceroute probes get dropped, and it ships a second tool, whob.

LFT stands for Layer Four Traceroute. Its Homebrew description calls it an advanced traceroute tool. The formula installs two executables: lft, the tracer itself, and whob, whose purpose the brief does not describe.

The scout's note says lft sends TCP SYN probes instead of the usual ICMP or UDP ones. That matters because many firewalls drop the probes classic traceroute relies on, while TCP traffic to an open port is often allowed through. The brief could not confirm this against the project's own documentation, so treat it as the likely idea rather than a verified description.

The door it opens is how a path through the internet is discovered at all: each hop reveals itself through how a router or middlebox answers a packet. Changing the kind of packet you send changes what you learn. Comparing lft's output with plain traceroute toward the same host is a good way to see that for yourself.

## Install

```
brew install lft
```

## Try this

```
lft --help
```
Prints the usage text and options, which is the reliable way to see what this build supports.

```
whob --help
```
Prints usage for the second installed tool, so you can find out what it does.

## What's unique

It probes with TCP at the transport layer rather than relying only on ICMP or UDP, so it can show paths that ordinary traceroute cannot. That claim comes from the scout note and is unverified.

## Caveats

The homepage returned HTTP 403 and the README could not be read, so this entry rests on Homebrew metadata and a scout note; project status and usage details are unknown.

## Links

- [Homepage](https://pwhois.org/lft/)
