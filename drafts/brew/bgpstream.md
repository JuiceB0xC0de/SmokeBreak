---
name: bgpstream
title: BGPStream
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, bgp, internet, network, protocol, routing]
homepage: https://bgpstream.caida.org/
scout_score: 6
status: draft
---

# BGPStream

**TLDR;** Give it a time window and it streams real BGP routing updates from Route Views and RIPE RIS, one line per announcement or withdrawal.

BGP is the protocol that networks use to tell each other which IP prefixes they can reach. Every route announcement and withdrawal between autonomous systems is part of the record of how the internet's routing shifts over time. Public projects like Route Views and RIPE RIS collect those messages from many vantage points and archive them as MRT files.

BGPStream, from CAIDA, hides the archive hunting. Its command-line tool, `bgpreader`, takes a time window and asks a broker service which archive files cover it. It then prints each BGP element (an announcement, withdrawal, RIB entry or peer state message) as one line on standard output. Filters narrow the stream by collector, peer ASN, origin ASN, prefix, community or AS-path regex. Leave out the end time and it switches to live mode.

The homepage describes the framework as built for scientific research, operational monitoring and post-event analysis. It also advertises C/C++ and Python APIs (PyBGPStream). The command-line tool is the quickest way in: pick a moment when something broke, and read what the routers were saying.

The default output follows BGPdump's one-line format, and `-m` produces the exact `bgpdump -m` format. Per the docs, `bgpreader` can in some cases replace BGPdump in older scripts.

## Install

```
brew install bgpstream
# needs an internet connection: the default data source is the BGPStream Broker service, which points at Route Views and RIPE RIS archives. No account or API key was seen.
```

## Try this

```
bgpreader
```
Prints the usage text, listing the data interfaces, filters and output options.

```
bgpreader -w 1445306400,1445306402 -c route-views.sfmix
```
Reads a two-second window (Unix epoch times) from the route-views.sfmix collector and prints each BGP element as a line.

```
bgpreader -w 1445306400,1445306402 -p ris -m
```
Reads the same window from RIPE RIS only, printing in bgpdump -m format.

## What's unique

Route Views and RIPE RIS archives are exposed as a single stream queried by time window, and moving from history to live monitoring is a one-parameter change.

## Caveats

The brief found no release date or last-commit date, so how actively it is maintained is unclear. Live mode and the Kafka interface were not tested, and `parsebgp` was not documented on any page read.

## Links

- [BGPStream homepage](https://bgpstream.caida.org/)
- [BGPReader documentation](https://bgpstream.caida.org/docs/tools/bgpreader)
- [GitHub repository (CAIDA/bgpstream)](https://github.com/CAIDA/bgpstream)
