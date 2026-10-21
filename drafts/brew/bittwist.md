---
name: bittwist
title: bittwist
source: brew
category: fundamentals
commitment: quick
tags: [ethernet, network, packets, pcap, protocol, quick]
homepage: https://bittwist.sourceforge.io
scout_score: 5
status: draft
---

# bittwist

**TLDR;** A libpcap packet generator and capture editor that rewrites header fields in .pcap files and replays them onto a live network at a set rate.

Bit-Twist is two tools. `bittwist` sends Ethernet frames onto a live network, either replayed from a tcpdump-style .pcap file or built from templates for Ethernet, VLAN, ARP, IPv4, IPv6, ICMPv4, ICMPv6, TCP and UDP headers. `bittwiste` is the companion editor. It changes fields in an existing capture file before you send it.

The author describes it as a complement to tcpdump. You capture traffic, edit it, and play it back. The homepage lists uses such as simulating traffic and testing firewalls, IDS/IPS, routers, switches and load balancers. The editor can rewrite most header fields, add random values to addresses, ports and sequence numbers, set QoS bits, resize packets, and append a payload pasted from Wireshark. Checksums are fixed automatically unless you turn that off.

Sending is paced by a built-in token bucket. You can aim for a fixed interval, a packets-per-second rate, or a line rate between 1 Mbps and 10 Gbps, and it can loop over several trace files indefinitely. The speed claims are the author's own and were not verified here.

The idea underneath is that a packet is just a structured pile of bytes, and the link layer is not magic. Once you can build and edit frames by hand, you can see what a switch, a firewall or an ARP table does with something slightly wrong. It is a niche, fairly dry tool, but it is a direct way in.

## Install

```
brew install bittwist
# Windows needs Npcap installed first. Sending on a live interface usually needs root privileges.
```

## Try this

```
bittwist --help
```
Prints the options for the packet sender, including how to pick an interface and a send rate.

```
bittwiste --help
```
Prints the options for the trace file editor and the header types it can rewrite.

## What's unique

Most replay tools only send. This one pairs a fast pcap sender with an editor that can rewrite headers, and its templates let you craft packets without any existing capture.

## Caveats

The documentation pages returned 404 when the brief was written, so syntax beyond --help is only in the man pages, and real line-rate throughput depends on your NIC.

## Links

- [Homepage](https://bittwist.sourceforge.io)
- [SourceForge project page](https://sourceforge.net/projects/bittwist/)
