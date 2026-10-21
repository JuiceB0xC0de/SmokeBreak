---
name: tcptraceroute
title: tcptraceroute
source: brew
category: fundamentals
commitment: quick
tags: [network, protocol, quick, root, tcp, traceroute]
homepage: https://github.com/mct/tcptraceroute
scout_score: 6
status: draft
---

# tcptraceroute

**TLDR;** A traceroute that probes with TCP packets instead of ICMP or UDP, so you can see the path that ordinary connection attempts take.

tcptraceroute does one thing: you give it a destination, and it lists the routers between you and that host. Classic traceroute sends ICMP or UDP probes. This one sends TCP packets, so the probes look like the start of a normal connection.

The practical point is that some firewalls drop ICMP or UDP probes but let TCP through. A classic traceroute can stall at such a firewall, while a TCP probe may get further, so the two tools can show different paths to the same host. The README gives no motivation beyond its one-line description, so this reading is an inference, not the author's stated reason.

The README does not explain the mechanism. Its dependencies, libnet for building packets and libpcap for capturing them, suggest it crafts raw TCP packets and watches for the replies to work out which hop answered. That makes it a small way into a larger idea: the network does not treat all traffic alike, and where a packet gets dropped depends on what it looks like.

It is a single C program, and the project is quiet. The README copyright runs 2001-2015. Because the idea is simple and the protocols have not changed, it still works as a way to learn how paths and filters behave.

## Install

```
brew install tcptraceroute
# needs root to send raw packets: run it as sudo tcptraceroute
# building from source needs libnet and libpcap installed first
```

## Try this

```
tcptraceroute --help
```
Prints the usage text and the options this build supports. The README documents no options itself.

```
sudo tcptraceroute --help
```
The same help text, run as root, which is how you will run real traces.

## What's unique

It swaps the usual ICMP or UDP probes for TCP packets, so it shows the path that connection attempts take rather than the path of diagnostic traffic.

## Caveats

It needs root, the project looks quiet since about 2015, and the README is thin: no output example, and the author's site did not load.

## Links

- [GitHub repository (homepage)](https://github.com/mct/tcptraceroute)
- [INSTALL file](https://github.com/mct/tcptraceroute/blob/master/INSTALL)
- [Author's updates page (did not load)](http://michael.toren.net/code/tcptraceroute/)
