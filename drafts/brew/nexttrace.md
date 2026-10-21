---
name: nexttrace
title: NextTrace
source: brew
category: fundamentals
commitment: quick
tags: [cli, icmp, network, quick, routing, traceroute]
homepage: https://www.nxtrace.org/
scout_score: 5
status: draft
---

# NextTrace

**TLDR;** A traceroute that labels every hop with its location and network owner, and can draw the route on a map.

NextTrace is a Go command-line route tracer. Give it an IP address, hostname or URL and it sends ICMP probes by default (TCP or UDP are optional), listing each hop between you and the target over IPv4 or IPv6. Each hop is annotated with geographic and network-owner data, and the README prints a MapTrace link that draws the path from the per-hop coordinates.

The project describes itself as "An open source visual routing tool that pursues light weight, developed using Golang." The idea is that a plain traceroute gives you a column of IP addresses, and the interesting part is working out where those addresses are and who runs them. Reading a path this way shows where traffic leaves your ISP, which carriers it crosses, and where a detour adds latency.

The full build bundles more than tracing. It has MTR-style continuous probing, path-MTU discovery, a standalone DNS client, a CDN speed test, and a mode that annotates IP addresses in piped text. Output can be terminal text, a summary table, pipe-delimited RAW lines or JSON. Three build flavors (full, tiny, and an MTR-only one called ntr) are produced from one codebase using compile-time build tags.

## Install

```
brew install nexttrace
# needs root to send probes: sudo nexttrace <ip>
# Homebrew-core provides only the Full flavor; the tap nxtrace/nexttrace has all three.
# Map and location data need network access to the NextTrace API, IPInfo, or IP-API.com.
```

## Try this

```
sudo nexttrace 1.0.0.1
```
Runs a default ICMP traceroute to that address, listing each hop with location and network-owner details.

```
sudo nexttrace --table 1.0.0.1
```
Traces once and prints a final summary table.

```
sudo nexttrace -t 1.1.1.1
```
Switches to MTR mode, continuously probing and refreshing the table in real time.

## What's unique

Few traceroute tools put geography and network ownership on each hop and draw the path on a map. This one also folds in MTR, path-MTU discovery and a DNS client.

## Caveats

It needs root, Windows support is experimental, the map and location data depend on external services, and the README says plain `nexttrace <target>` will switch to MTR mode in a release no earlier than 2027.

## Links

- [Homepage (JavaScript-only)](https://www.nxtrace.org/)
- [GitHub repository NTrace-core](https://github.com/nxtrace/NTrace-core)
- [traceMap visualization component](https://github.com/nxtrace/traceMap)
- [Downloads page](https://www.nxtrace.org/downloads)
