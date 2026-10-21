---
name: fwknop
title: fwknop
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, firewall, network, protocol, security, ssh]
homepage: https://www.cipherdyne.org/fwknop/
scout_score: 6
status: draft
---

# fwknop

**TLDR;** Hides a service like SSH behind a default-drop firewall and opens it only when one encrypted, authenticated packet arrives, so nmap sees nothing listening.

fwknop (FireWall KNock OPerator) implements Single Packet Authorization, or SPA. The firewall drops everything by default, so the protected service, usually SSH, shows no open port. A client sends one encrypted packet saying what access it wants. The server daemon, fwknopd, never listens on a port. It sniffs traffic passively with libpcap, and if a packet decrypts, verifies and is not a replay, it opens the firewall for that client for a limited time.

The idea is an upgrade to port knocking. The author describes SPA as "next generation Port Knocking (PK), but solves many of the limitations exhibited by PK while retaining its core benefits." Classic knocking sends a sequence of packets to closed ports, which is open to replay and to spoofed packets that break a knock in progress. A single packet carrying a real payload avoids those problems.

The payload is encrypted with Rijndael or with GnuPG, then an HMAC is appended, so authentication is applied after encryption. The server checks the HMAC before it decrypts anything, which keeps the crypto and GnuPG code away from unauthenticated input. Replays are rejected by comparing SHA-256 digests. On iptables, the ACCEPT rules go into custom chains and are removed after a timeout.

Under the tool is a larger question: what does it mean for a service to be reachable only by those who can prove something first? In the project's words, "anyone using nmap to look for SSHD can't even tell that it is listening."

## Install

```
brew install fwknop
# Server setup needs a firewall (iptables, firewalld, ipfw or PF) and keys in /etc/fwknop/access.conf; the HMAC key is generated with --key-gen.
```

## Try this

```
fwknop --help
```
Lists the client options, including how to specify the access request, keys and destination.

```
fwknopd --help
```
Lists the server daemon options for the passive packet sniffer and firewall handling.

## What's unique

There is no listening server to connect to. The daemon sniffs passively, and the HMAC is checked before any decryption runs.

## Caveats

Firewall support is limited to iptables, firewalld, ipfw and PF, NAT works only with iptables, and the README's account of the project's state is dated (it describes the 2.5 release, while the homepage lists 2.6.11).

## Links

- [fwknop homepage](https://www.cipherdyne.org/fwknop/)
- [fwknop tutorial](http://www.cipherdyne.org/fwknop/docs/fwknop-tutorial.html)
- [fwknop source on GitHub](https://github.com/mrash/fwknop)
