---
name: monocle
title: monocle
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, bgp, internet, network, protocol, routing, rust]
homepage: https://github.com/bgpkit/monocle
scout_score: 5
status: draft
---

# monocle

**TLDR;** A Rust command-line tool for searching, parsing and live-watching BGP routing data, so you can see how the internet's routes change from a shell.

BGP, the Border Gateway Protocol, is how networks tell each other which IP prefixes they can reach. Public collectors such as RIPE RIS and Route Views record these announcements and publish them as MRT archives. Monocle turns those scattered archives into something you can query from a terminal. It also handles supporting datasets like RPKI, prefix-to-AS mappings, AS relationships and AS registration info.

There are four main ways in. `parse` reads a local or remote MRT file. `search` asks the BGPKit Broker for matching public archive files. `watch` subscribes to the live RIPE RIS Live stream. `rib` rebuilds the routing table at a chosen timestamp by loading the nearest earlier RIB and replaying updates up to that moment. All of them share one filter vocabulary: origin ASN, prefix, peer, community, AS-path regex. Output can be a table, markdown, JSON, JSON lines, PSV or SQLite, and there is an HTTP/SSE server mode too.

The idea underneath is that the global routing table is a public, constantly changing record. Route leaks, hijacks and outages show up in it as announcements and withdrawals. With a filter and a prefix you can watch a network's routes appear and disappear, then record the stream to a file and replay it offline later. The README describes itself as "A commandline application to search, parse, and process BGP information in public sources."

## Install

```
brew install monocle
# or: cargo install monocle
# or use the Docker image (it defaults to server mode)
# No account or special hardware is mentioned. Search and parse download large public archive files.
```

## Try this

```
monocle time 1704067200
```
Converts a Unix timestamp to RFC 3339 and a human-readable form, a quick check that the install works.

```
monocle search -t 2024-01-01 -d 1h -p 1.1.1.0/24 --use-cache
```
Finds public MRT archive data for one hour touching 1.1.1.0/24 and caches the downloaded files.

```
monocle watch --host rrc00 --prefix 45.57.60.0/24 -S --record incident.mrt.bz2
```
Streams live updates for that prefix and its sub-prefixes from one RIS collector and records them to an MRT file for later replay with parse.

## What's unique

Watch and parse share one filter vocabulary, so a live capture can be saved as MRT and replayed offline with the same filters. The rib command rebuilds the routing table at an arbitrary timestamp instead of just handing you raw archive files.

## Caveats

Live data comes only from RIPE RIS collectors, not global visibility. An unfiltered watch needs --firehose (about 5k messages per second), and rib aborts if any selected collector lacks a RIB at or before the requested time.

## Links

- [Homepage (GitHub repository)](https://github.com/bgpkit/monocle)
- [API documentation (docs.rs)](https://docs.rs/monocle)
- [crates.io package](https://crates.io/crates/monocle)
- [BGPKit Broker (data source used by search)](https://github.com/bgpkit/bgpkit-broker)
