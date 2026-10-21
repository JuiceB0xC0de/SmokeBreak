---
name: dnstop
title: dnstop
source: brew
category: fundamentals
commitment: quick
tags: [dns, network, pcap, protocol, quick, tui]
homepage: http://dns.measurement-factory.com/tools/dnstop/index.html
scout_score: 5
status: draft
---

# dnstop

**TLDR;** A tcpdump-style console tool that turns DNS packets into live ranked tables of who is asking for what, and which queries look wrong.

dnstop is a libpcap application, like tcpdump, that listens to DNS traffic and shows it as tables. Instead of a scrolling stream of packets, it counts and ranks: source addresses, destination addresses, query types, response codes, opcodes, and top, second, and third level domains. It handles both IPv4 and IPv6.

The page describes it as a way to "Stay on Top of Your DNS Traffic". To that end it ships filters for queries that are probably unwanted: unknown or invalid TLDs, queries whose name is already an IP address, PTR queries for RFC1918 address space, and responses with code REFUSED. Each of these is a small lesson in how DNS gets misused, misconfigured, or leaked from private networks.

It reads from a live capture device or from a saved tcpdump file, so you can watch your own network or study a capture after the fact. The underlying idea is that DNS runs under almost everything you do and almost nobody looks at it. Watching the ranked tables for a few minutes shows how chatty a normal machine is, and what a resolver is really asked.

## Install

```
brew install dnstop
# Live capture usually needs elevated privileges (e.g. sudo); the homepage does not say so explicitly.
```

## Try this

```
dnstop --help
```
Prints the usage text so you can see the options for choosing a capture device or a savefile.

## What's unique

It gives a live, ranked-table view of DNS on the wire, with built-in filters aimed at spotting bad or suspicious queries such as invalid TLDs and RFC1918 reverse lookups.

## Caveats

The homepage is the only source and is thin, with no docs, screenshots, or release date, so the project's maintenance status is unknown.

## Links

- [Homepage](http://dns.measurement-factory.com/tools/dnstop/index.html)
