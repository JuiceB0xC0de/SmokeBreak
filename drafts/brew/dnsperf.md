---
name: dnsperf
title: dnsperf
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, benchmarking, dns, network, protocol]
homepage: https://www.dns-oarc.net/tools/dnsperf
scout_score: 5
status: draft
---

# dnsperf

**TLDR;** A DNS load generator from DNS-OARC that replays a file of queries at a server and ramps the rate until a resolver stops keeping up.

dnsperf and resperf are two benchmarking tools for DNS. dnsperf reads a file of queries, sends them to a server, and reports latency and throughput. resperf does something different: it steadily raises the query rate and watches the response rate, to find the point where a caching resolver stops keeping up.

The tools were written to help network operators measure their naming infrastructure and plan upgrades. Per the homepage, they "make it simple to gather accurate latency and throughput metrics for Domain Name Service (DNS)." dnsperf "self-paces" the query load to simulate network conditions, instead of just flooding the target. Newer versions are multithreaded, and each dnsperf client needs two cores.

The idea underneath is that a DNS server's behaviour changes with load, with the mix of queries, and with whether answers are cached. Feeding a resolver a realistic query file and watching where it bends teaches you how resolvers behave under pressure. Sample query data is published alongside the releases, so you have something to replay.

The lineage is Nominum, then Akamai (2006-2018), then DNS-OARC from 2019 onward. It is maintained, with a recent 2.16.0 release listed.

## Install

```
brew install dnsperf
# You supply your own query file and a target DNS server. Only test servers you run or have permission to load.
```

## Try this

```
dnsperf --help
```
Lists the options for pointing dnsperf at a server with a query data file.

```
resperf --help
```
Shows the options for the ramp-up mode that probes how far a caching resolver can go.

```
resperf-report --help
```
Shows the options for the report helper that accompanies resperf.

## What's unique

It paces traffic to imitate real Internet query patterns rather than only flooding a server. resperf adds a separate ramp-up mode aimed at caching resolvers.

## Caveats

You need a query file and a DNS server to aim at, and each dnsperf client wants two cores; the README's install lines cover Linux and BSD, not Homebrew.

## Links

- [DNS-OARC dnsperf homepage](https://www.dns-oarc.net/tools/dnsperf)
- [Source repository on Codeberg](https://codeberg.org/DNS-OARC/dnsperf)
- [Issues on Codeberg](https://codeberg.org/DNS-OARC/dnsperf/issues)
