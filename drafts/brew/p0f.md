---
name: p0f
title: p0f
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, fingerprinting, network, passive, protocol, tcp]
homepage: https://lcamtuf.coredump.cx/p0f3/
scout_score: 7
status: draft
---

# p0f

**TLDR;** p0f identifies the operating system and software on both ends of a network connection by listening only, sometimes from a single SYN packet, without sending a probe.

p0f watches TCP/IP traffic and guesses what is on the other end. It reads the quirks of a handshake, such as the relationship between window size and MTU, and matches them against a signature database. It also reads HTTP request and response headers for application-level clues. For each detection it prints a text block with fields like os, dist, params, raw_sig, mtu, uptime and the http request. It can also report link type, distance, language preference and NAT or proxy setups.

The author's pitch is an alternative to active scanners like NMap, which can be blocked, slow, unreliable, or set off alarms. p0f never interferes: it only reads traffic that is already going by. The homepage lists uses such as penetration-test reconnaissance, network monitoring, spotting unauthorized network interconnects, abuse prevention and forensics.

The idea underneath is that every network stack has habits. Two machines following the same protocol still fill in the optional parts differently, and those differences leak identity to anyone listening. Reading a raw signature and seeing why it points to one OS is a good way into how TCP actually behaves on the wire.

Version 3 is described as a complete rewrite with a new signature database. It can run in the foreground or as a daemon with a real-time API for other components. The page says earlier p0f versions are reused in projects such as pfSense, Ettercap, PRADS and the OpenBSD firewall.

## Install

```
brew install p0f
# Brew installs no listed executables for this formula, so check where the binary lands. The homepage offers 3.09b as a source download; the README (not reviewed here) covers building. Capturing traffic typically needs elevated privileges. The p0f-sendsyn tool for collecting SYN+ACK signatures must be compiled from the supplied source.
```

## Try this

## What's unique

It learns about machines from a single ordinary SYN, with no probing at all. The author says many other tools either reuse p0f's TCP checks or use weaker methods.

## Caveats

The code looks old (copyright 2000-2014, latest named version 3.09b), the public demo is broken, signature coverage is uneven, and the brew formula lists no executables, so the install path is unverified.

## Links

- [p0f v3 homepage](https://lcamtuf.coredump.cx/p0f3/)
