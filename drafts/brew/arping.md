---
name: arping
title: arping
source: brew
category: fundamentals
commitment: quick
tags: [arp, network, protocol, quick, root-needed]
homepage: https://github.com/ThomasHabets/arping
scout_score: 6
status: draft
---

# arping

**TLDR;** Asks the local network who owns an IP address by sending ARP requests, and can also ping a raw MAC address to find out which IP it uses.

Arping is a small C command-line tool that sends ARP "who-has" requests to your LAN and prints the "is-at" replies. Give it an IPv4 address and it tells you whether the address is taken and which MAC address answers for it. Plain ping can fail when a host blocks ICMP. ARP sits below that, so a machine that drops everything else still answers, and still leaves an entry in your ARP cache.

Thomas Habets wrote it for cases where ping is unreliable or unavailable. One example in the README is a catch-22: you hold a block of real addresses, you cannot ping an address before taking it, and you cannot choose a free one without knowing which are used. Asking at the link layer gets around that.

The second mode runs the other way. Given a MAC address, arping sends an ICMP echo to a broadcast IP inside an Ethernet frame addressed only to that MAC. If the target replies, the reply reveals its IP. Many systems ignore broadcast pings, so the README shows how to adjust the target with `-T` and even sketches a brute-force loop over candidate addresses.

The README is a good way into ARP itself. It includes real tcpdump traces of the request and reply, so you can see the protocol that every machine on your network uses constantly and rarely shows you.

## Install

```
brew install arping
# Sending raw packets normally needs root, so run it with sudo. Depends on libnet (and libpcap), which Homebrew pulls in.
```

## Try this

```
arping --help
```
Lists the options, including the -T broadcast target and the -b and -B switches the README mentions.

```
sudo arping -T 192.168.0.255 00:01:02:03:04:05
```
Pings a MAC address by sending an ICMP echo to the subnet broadcast address inside a frame addressed to that MAC (adjust the address and MAC for your network).

```
tcpdump -vven 'arp or icmp'
```
Captures the ARP and ICMP packets in a second terminal, the same way the author produced the traces in the README, so you can watch the requests and replies.

## What's unique

It pairs a plain ARP probe with a trick that most tools skip: pinging a MAC address directly to learn its IP. The README also explains the protocol with real packet traces and is candid about the limits.

## Caveats

Round-trip times can be off by milliseconds, pinging a MAC only works if the target answers broadcast ICMP (many systems do not), and I could not confirm how recently it has been maintained.

## Links

- [Project homepage (GitHub README)](https://github.com/ThomasHabets/arping)
- [Author's SynScan page](http://www.habets.pp.se/synscan/)
- [Mailing list (synscan group)](https://groups.google.com/g/synscan)
