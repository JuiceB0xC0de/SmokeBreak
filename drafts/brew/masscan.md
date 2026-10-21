---
name: masscan
title: masscan
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, c, network, port-scanner, protocol, security, tcp]
homepage: https://github.com/robertdavidgraham/masscan/
scout_score: 5
status: draft
---

# masscan

**TLDR;** A TCP port scanner built to sweep huge address ranges, up to the whole IPv4 Internet, by randomly permuting probes with its own TCP/IP stack.

Masscan takes IPv4 or IPv6 addresses or ranges plus a list of ports, and prints the open host and port pairs. Output can be a plain list, grepable text, JSON, XML or binary. It can also finish TCP connections to grab banners from services such as SSH, HTTP, SMB, RDP and VNC. Its options are modelled on nmap's, so the syntax feels familiar.

The author's pitch is scale. In his words: "This is an Internet-scale port scanner. It can scan the entire Internet in under 5 minutes, transmitting 10 million packets per second, from a single machine." Nmap is built for depth on a few machines, and masscan is built for breadth across many.

Two ideas sit underneath it. First, it is asynchronous, with separate transmit and receive threads, in the same family as ZMap, scanrand and unicornscan. It does not wait on each connection. Second, it walks a single index from zero and passes each index through an encryption function. The probe order looks random, so no one network gets hammered in a burst, yet every target is still hit exactly once. The same trick lets a scan pause with ctrl-c and resume from the saved index.

To send packets this fast, masscan runs its own user-mode TCP/IP stack and bypasses the operating system's. That makes it quick, and it explains the odd setup for banner grabbing. The local OS sees replies it knows nothing about and may answer them itself, so you give masscan a separate source IP or firewall off a port. It is a good way to learn what a TCP handshake looks like when you do it by hand.

## Install

```
brew install masscan
# The README describes building from source (needs git, make and a C compiler): git clone, cd masscan, make; the binary lands in bin/masscan.
# Scans send raw packets, so the README's examples imply running as root or with sudo.
```

## Try this

```
masscan --nmap
```
Lists the extra nmap-compatible options masscan accepts, a quick view of how closely it mirrors nmap.

```
masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112
```
The README's basic example: scans ports 80 and 8000-8100 on an IPv4 /8 and an IPv6 /112, printing open ports to stdout. Only scan networks you are allowed to scan.

```
masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112 --echo > xxx.conf
```
Writes the full current configuration to a file instead of scanning, which you can reuse later with -c.

## What's unique

Scan order comes from encrypting a linear index, so probes are random across the target space without repeats and a scan can resume from a saved position. It also keeps nmap-style options and output while running at very high packet rates.

## Caveats

Masscan uses its own ad hoc TCP/IP stack, so anything beyond simple scans can conflict with the local one; it only does SYN scanning, and the README warns it is "fast enough to melt most networks", so scan only what you have permission to scan.

## Links

- [Project homepage and README (GitHub)](https://github.com/robertdavidgraham/masscan/)
- [ntop PF_RING installation guide (for PF_RING ZC mode)](https://www.ntop.org/installation-guide-for-pf_ring/)
