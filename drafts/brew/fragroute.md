---
name: fragroute
title: fragroute
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ids-evasion, ip-fragmentation, network, old, protocol]
homepage: https://www.monkey.org/~dugsong/fragroute/
scout_score: 6
status: draft
---

# fragroute

**TLDR;** A packet-mangling tool that rewrites your outgoing traffic to one host, fragmenting, reordering, and overlapping packets to show how intrusion detection systems get fooled.

fragroute sits between your machine and a chosen target host and intercepts everything you send to it. A small ruleset language tells it what to do with each outbound packet: delay, duplicate, drop, fragment, overlap, print, reorder, segment, source-route, or otherwise alter it. The target still receives your traffic, only chopped up and shuffled.

The author wrote it to test network intrusion detection systems, firewalls, and basic TCP/IP stack behaviour. It implements most of the attacks in the January 1998 Secure Networks paper "Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection." The core idea from that paper is that a monitoring device has to reassemble packets the way the real destination will. If it guesses differently about overlapping fragments or out-of-order segments, an attacker can show the monitor one stream and the host another.

Because it rewrites real packets instead of simulating them, you can watch how an actual stack reacts to odd but legal traffic. The homepage also lists ideas such as simulating one-way latency, loss, and retransmission, and evading passive OS fingerprinting. The homepage does not explain the ruleset syntax or the internals. For that you need the fragroute(8) manpage, which the brief did not cover.

## Install

```
brew install fragroute
# Homebrew installs libdnet and libevent as dependencies. Upstream builds from source (fragroute-1.2.tar.gz) and also lists libpcap. Packet interception generally needs root.
```

## Try this

## What's unique

It rewrites live outbound packets for a single host using a tiny ruleset language, which makes the 1998 IDS evasion paper something you can reproduce rather than just read.

## Caveats

The software and its platform notes are old (1998-era references, Windows 2000 drivers), the homepage gives no release date or license, and the author asks you not to abuse it, so only use it on hosts you are allowed to test.

## Links

- [fragroute homepage](https://www.monkey.org/~dugsong/fragroute/)
