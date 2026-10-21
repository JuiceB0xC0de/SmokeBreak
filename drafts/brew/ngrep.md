---
name: ngrep
title: ngrep
source: brew
category: fundamentals
commitment: quick
tags: [dns, http, network, packets, pcap, protocol, quick]
homepage: https://github.com/jpr5/ngrep
scout_score: 6
status: draft
---

# ngrep

**TLDR;** ngrep is grep for the network: give it a regex and a filter, and it prints live packets whose payloads match.

ngrep captures packets through libpcap, either live from an interface or from a saved pcap file. It matches each payload against an extended regular expression, or a hex pattern with `-X`, and prints the matches with addresses and flags. It understands IPv4 and IPv6, TCP, UDP, ICMP, IGMP and raw packets. The same filter syntax tcpdump uses (BPF) narrows what gets captured in the first place.

The author built it to debug plaintext protocols such as HTTP, IMAP, DNS and SIP, to look at suspicious traffic like malware communications, and to search pcap dumps for particular patterns. The README is frank that it could also collect plaintext credentials, and adds: "Like all useful tools, it can be used for good and for bad."

The idea underneath is that a packet is just bytes with a header, and you already know how to search bytes. Pointing `grep` thinking at port 25 or port 21 shows how much of the network still travels as readable text. It also shows why that is a problem.

The `-r` flag resolves Docker and Podman container IPs to container names. A capture on a bridge network then reads as one service talking to another, not as a list of 172.18.x addresses.

## Install

```
brew install ngrep
# Capturing packets usually needs elevated privileges on the host, so you may need sudo. The README does not spell this out.
# Alternative per the README: docker pull ghcr.io/jpr5/ngrep:latest
```

## Try this

```
ngrep -W byline port 80
```
Shows plain HTTP traffic with line breaks respected, so headers are readable.

```
ngrep -O /tmp/dns.dump -d any -T port domain
```
Captures DNS traffic on every interface into a dump file, printing time differences between packets.

```
ngrep -r -d docker0 -q '' port 53
```
Watches DNS lookups between containers, matching every packet, with container names in place of IPs.

## What's unique

It keeps the grep model of pattern plus filter, and the `-r` flag turns Docker and Podman container IPs into names in live output. The same expression works on a live interface or a saved pcap.

## Caveats

Only plaintext payloads are readable, so most modern HTTPS traffic will show nothing useful, and the Docker route needs host networking plus the NET_RAW capability.

## Links

- [ngrep on GitHub](https://github.com/jpr5/ngrep)
- [EXAMPLES.md (usage walkthroughs)](https://github.com/jpr5/ngrep/blob/master/EXAMPLES.md)
- [DOCKER.md (Docker usage)](https://github.com/jpr5/ngrep/blob/master/DOCKER.md)
- [Releases (binaries)](https://github.com/jpr5/ngrep/releases)
