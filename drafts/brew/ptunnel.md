---
name: ptunnel
title: ptunnel
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, icmp, network, ping, protocol, tunnel]
homepage: https://www.cs.uit.no/~daniels/PingTunnel/
scout_score: 8
status: draft
---

# ptunnel

**TLDR;** Carries TCP connections inside ICMP echo packets, so an ssh session can ride on ordinary pings when a network blocks everything else.

Ptunnel is a small program that tunnels TCP through ICMP echo requests and replies, the packets ordinary ping uses. You run a proxy on a machine that can be reached from the internet, and a client on your own machine. The client listens on a local TCP port and forwards each connection, wrapped in pings, to a destination you name. The proxy unwraps the data and opens the real TCP connection.

The author wrote it for one situation: an open wireless network that lets you ping anywhere but blocks outgoing TCP and UDP, so you cannot check mail. In the author's words, "For those times when everything else is blocked."

The interesting part is the protocol, which the homepage documents in unusual depth. The client sends echo requests (type 8) and the proxy answers with echo replies (type 0). Ptunnel's own packet format sits in the payload, with a magic number to tell its packets from real pings. Packets carry sequence and acknowledgement numbers modelled on TCP, and the first unacknowledged packet is resent after 1.5 seconds. Optional password authentication uses an MD5 challenge-response, and a random ICMP identifier keeps concurrent tunnels apart.

It is effectively a miniature reliable transport built on a protocol that was never meant to carry data. Reading how it does that is a good way into how ICMP works, why firewalls treat it specially, and what ping traffic can hide.

## Install

```
brew install ptunnel
# Needs root for raw sockets (run with sudo). You also need a second, publicly reachable machine to run the proxy end.
```

## Try this

```
ptunnel --help
```
Prints the usage summary for proxy and client modes.

```
sudo ./ptunnel
```
Starts the proxy on the remote machine; root is needed for raw sockets.

```
sudo ./ptunnel -p proxy.pingtunnel.com -lp 8000 -da login.domain.com -dp 22
```
Starts the client listening on local port 8000, forwarding to login.domain.com port 22 through the proxy. Then run `ssh -p 8000 localhost` to connect.

## What's unique

It uses only the ICMP echo mechanism, so it can work where nothing but ping is allowed. The homepage spells out the whole protocol: packet format, state codes, sliding window and the MD5 handshake.

## Caveats

Last updated in 2011 (version 0.72), needs root, and has no congestion control; the README measures about 150 kb/s down and 50 kb/s up, and any gateway that filters ICMP breaks it.

## Links

- [Ptunnel homepage (README and docs)](https://www.cs.uit.no/~daniels/PingTunnel/)
