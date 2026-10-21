---
name: lldpd
title: lldpd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, daemon, lldp, network, protocol]
homepage: https://lldpd.github.io/
scout_score: 7
status: draft
---

# lldpd

**TLDR;** A daemon that speaks LLDP, the neighbour-discovery protocol switches use constantly, so your machine can tell you which switch port it is plugged into.

lldpd implements IEEE 802.1AB, the Link Layer Discovery Protocol. It sends LLDP frames out of every network interface and listens for frames from neighbours. Each device announces who it is and which port it is on. You query the results with `lldpcli`, as text or XML, or through SNMP. It also partially speaks LLDP-MED and some vendor protocols (CDP, FDP, SONMP, EDP).

LLDP exists as an inter-vendor replacement for proprietary protocols like Cisco's CDP and Extreme's EDP. The project's own framing: "LLDP allows you to know exactly on which port is a server (and reciprocally)." This is the sort of thing that is running on a lot of network gear and that most developers never look at.

The daemon uses privilege separation. A small root process does the privileged work, and a second unprivileged process in a chroot does most of the rest. Reading the code and the README is a decent way to see how a long-running network daemon is meant to be built.

The frames are plain link-layer multicast, sent to 01:80:c2:00:00:0e. That means you can also watch them with tcpdump and see the protocol itself, not only the tool's summary of it.

## Install

```
brew install lldpd
# Needs a real network interface with a neighbour that sends LLDP (a managed switch, usually). Privilege separation needs a system user and group named _lldpd.
```

## Try this

```
lldpcli --help
```
Lists the commands in the interactive client that talks to the running daemon.

```
docker exec lldpd lldpcli show neighbors
```
Asks a running lldpd container which neighbours it has discovered on the host's interfaces.

```
tcpdump -s0 -vv -pni eth0 ether dst 01:80:c2:00:00:0e
```
Captures raw LLDP frames on eth0 so you can see the neighbour announcements on the wire.

## What's unique

It is a small, widely deployed daemon for a protocol most people never see, and it also answers in CDP, FDP, SONMP and EDP. Its README troubleshooting section is unusually candid about kernel quirks and network cards that swallow LLDP.

## Caveats

You need a neighbour that actually sends LLDP to see anything useful, Windows is unsupported, and some Intel X710 and ice cards need their firmware LLDP agent stopped.

## Links

- [Homepage](https://lldpd.github.io/)
- [GitHub repository](https://github.com/lldpd/lldpd)
- [Installation guide](https://lldpd.github.io/installation.html)
