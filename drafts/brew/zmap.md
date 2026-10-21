---
name: zmap
title: ZMap
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ipv4, network, protocol, research, scanning]
homepage: https://zmap.io
scout_score: 7
status: draft
---

# ZMap

**TLDR;** A stateless scanner that sends one packet per address and can sweep the whole public IPv4 space on a single port in under 45 minutes.

ZMap sends a single probe packet, such as a TCP SYN, to each address in the IPv4 space or a slice of it you choose. It prints the IPs that answer to stdout and shows a live progress line on stderr. You pick a port and a probe module, and it does the rest.

The idea underneath is statelessness. A conventional scanner tracks every connection it opens. ZMap does not: it fires one packet per target, visits addresses in a random permutation, and recognises replies without per-connection bookkeeping. The README says this lets it scan the whole IPv4 space on one port in under 45 minutes on a gigabit connection. The project was built so researchers could run Internet-wide surveys of the hosts and services that make up the public internet.

The formula also installs three helpers: zblocklist, ziterate and ztee. ZMap only finds who answers. For banner grabs and TLS handshakes, the wider ZMap Project offers ZGrab 2, plus other tools such as ZDNS and LZR. The homepage zmap.io is an umbrella page for that whole suite.

The README has a serious section on ethics. In its words: "Performing Internet-wide scans can have serious ethical and operational implications." It asks users to scan at the slowest speed necessary and to give network operators a way to opt out.

## Install

```
brew install zmap
# ZMap needs root to run. No account or API key is mentioned.
# Optional 10GbE speeds need netmap or PF_RING.
```

## Try this

```
zmap --help
```
Lists the options, probe modules and output settings, a good way to see what the scanner can be told to do before you aim it at anything.

```
sudo zmap -p 80
```
The README's first example: probes the entire IPv4 space on TCP port 80 and prints responding addresses. Read the caveats before running this.

## What's unique

Where a typical port scanner such as nmap works through a few hosts in depth, ZMap trades depth for breadth, using stateless single-packet probes to sweep the whole IPv4 space in minutes.

## Caveats

Needs root, and a full-internet scan has real ethical and operational consequences, so scan only what you should and as slowly as necessary; it is a single-packet scanner, so banner grabs need ZGrab 2.

## Links

- [ZMap Project homepage](https://zmap.io)
- [GitHub repository and README](https://github.com/zmap/zmap)
- [Getting Started Guide (wiki)](https://github.com/zmap/zmap/wiki/Getting-Started-Guide)
- [Original ZMap paper (USENIX Security 2013)](https://zmap.io/paper.pdf)
