---
name: udp2raw-multiplatform
title: udp2raw-multiplatform
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, firewall, network, protocol, raw-sockets, tunnel, udp]
homepage: https://github.com/wangyu-/udp2raw-multiplatform
scout_score: 6
status: draft
---

# udp2raw-multiplatform

**TLDR;** A tunnel that wraps UDP traffic in fake TCP or ICMP packets, so it slips past firewalls that block UDP, now built for Windows, Mac and BSD.

udp2raw takes UDP packets on a local port, wraps them in FakeTCP, UDP or ICMP headers using a raw socket, optionally encrypts them, and sends them to a server. The server unwraps them and hands plain UDP to a service on its side. This repo, udp2raw_mp, is the Windows, Mac and BSD build. Its README describes it as the cross-platform version, and says it is protocol-compatible with the Linux original, so a Linux server can talk to it.

The interesting part is FakeTCP. The program simulates a three-way handshake, sequence and ack numbers, and TCP options such as MSS, sackOk, TS and wscale. A firewall sees what looks like a TCP connection. Underneath it is still unreliable UDP, with no congestion control and no retransmission. In the project's words: "Firewalls will regard FakeTCP as a TCP connection, but its essentially UDP." That is also why something like OpenVPN can ride on it without the TCP-over-TCP stalls you get from tunnelling inside a real TCP session.

The idea underneath is how networks decide what a packet is. Middleboxes classify traffic by headers and behaviour, and this tool shows how thin that classification can be. Encryption and integrity are set with --cipher-mode and --auth-mode, and heartbeats let the client reconnect on a new port while UDP sessions stay alive. The options are candid about the trade-off: xor plus simple is said to fool most packet inspection on routers but not stop serious attacks.

Since 2021 this repo's code has been merged upstream into udp2raw-tunnel. This repo now only publishes binaries, handles issues and holds wiki articles. The upstream repo is where the mechanism and usage text live.

## Install

```
brew install udp2raw-multiplatform
# installs the udp2raw_mp executable and needs libnet. Raw sockets usually need administrator or root privileges. The brief did not cover Windows or Mac setup steps. Binaries are also on the repo's Releases page.
```

## Try this

```
udp2raw_mp --help
```
Prints the option list, including the raw modes (faketcp, udp, icmp), cipher and auth settings.

```
./udp2raw_amd64 -s -l0.0.0.0:4096 -r 127.0.0.1:7777    -k "passwd" --raw-mode faketcp -a
```
Upstream Linux server example: listens on a TCP-looking port 4096 and forwards to a local UDP service on 7777. Swap in udp2raw_mp for the binary name; I did not verify the flags on the non-Linux builds.

```
./udp2raw_amd64 -c -l0.0.0.0:3333  -r44.55.66.77:4096  -k "passwd" --raw-mode faketcp -a
```
Upstream client example: takes local UDP on port 3333 and tunnels it to the server at 44.55.66.77:4096 as FakeTCP.

## What's unique

FakeTCP runs the full TCP-looking handshake and sequence bookkeeping while staying unreliable UDP underneath. It is also one of the few tools of this kind with native Windows, Mac and BSD builds.

## Caveats

This repo's README is a short pointer to the wiki and upstream, so detail for udp2raw_mp itself is thin; the example commands come from the Linux build, and the -a iptables behaviour is Linux-specific.

## Links

- [udp2raw-multiplatform homepage](https://github.com/wangyu-/udp2raw-multiplatform)
- [udp2raw-multiplatform wiki](https://github.com/wangyu-/udp2raw-multiplatform/wiki)
- [upstream udp2raw-tunnel repo (code home)](https://github.com/wangyu-/udp2raw-tunnel)
- [upstream udp2raw wiki](https://github.com/wangyu-/udp2raw-tunnel/wiki)
