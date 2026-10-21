---
name: argus
title: Argus
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, flow, forensics, monitoring, netflow, network, pcap]
homepage: https://openargus.org
scout_score: 5
status: draft
---

# Argus

**TLDR;** A network flow sensor, in development since 1984, that turns live traffic or pcap files into compact flow records you can filter and summarise later.

Argus reads packets from a network interface or a pcap file and aggregates them into flow records: one record per conversation, rather than one line per packet. Each record is written in Argus's own binary format and carries metrics such as packet dynamics, jitter and throughput. The README says it covers all network activity, not just IP.

The idea underneath is the audit trail. The homepage says the design was modeled on the telephone network's Call Detail Record. You do not keep every packet, you keep a durable account of who talked to whom, when, and how much. That is the basis of flow-level monitoring, used for operations, security analysis, performance monitoring and forensics. The README calls Argus "the original network flow monitoring technology, developed since 1984".

The sensor is only half the system. The flow keys are configurable (the README names a classic 5-tuple and a Layer 2 matrix key), and the output file is read by a separate package, argus-clients, which holds tools such as ra, rasum and racluster. There is also a real-time mode where tools like ratop watch flows live. The Homebrew formula installs the sensor and its argus-* helper scripts. The client tools are not included, so you will need to get them separately to read what the sensor writes.

## Install

```
brew install argus
# Live capture needs root (sudo).
# The client tools (ra, rasum, racluster, ratop) are a separate package, argus-clients, and are not installed by this formula.
# Match major versions: clients 3.0 cannot read 5.0 data.
```

## Try this

```
argus -r capture.pcap -w output.argus
```
Reads an existing pcap file and writes its flows to an Argus record file, with no live capture or root needed.

```
sudo argus -i eth0 -w /var/log/argus/data.argus
```
Monitors interface eth0 live and writes flow records to a file.

```
argus -i eth0 proto tcp -w tcp.flow.argus
```
Captures on eth0 with a filter so only TCP flows are recorded.

## What's unique

It is among the oldest flow-monitoring systems, with a record model meant as a superset of NetFlow and IPFIX, and it covers non-IP traffic too.

## Caveats

The brew formula installs only the sensor, so you need the separate argus-clients package to read the records, and the homepage and README disagree on the licence (GPLv2 vs GPLv3) and the latest version.

## Links

- [Homepage (openargus.org)](https://openargus.org)
- [Argus sensor source (GitHub README)](https://github.com/openargus/argus)
- [Argus clients source (GitHub)](https://github.com/openargus/clients)
