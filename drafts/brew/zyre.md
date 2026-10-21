---
name: zyre
title: Zyre
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, discovery, library, network, p2p, protocol, zeromq]
homepage: https://github.com/zeromq/zyre
scout_score: 5
status: draft
---

# Zyre

**TLDR;** A C library where programs on the same LAN find each other by UDP beacon and swap group messages with no broker, server, or configuration.

Zyre is a C library for group messaging between peers on a local network. A program creates a node, starts it, and joins named groups. The node then finds other nodes on the same LAN by broadcasting UDP beacons, connects to them directly, and reports what happens as events: ENTER, EXIT, JOIN, LEAVE, WHISPER and SHOUT. You send to one peer with `zyre_whisper` or to a whole group with `zyre_shout`.

The point is that nothing sits in the middle. The README says Zyre "needs no administration or configuration" and that "peers talk to each other without any central brokers or servers." Its listed uses are local service discovery, clustering services on one Ethernet network, controlling smart devices, and multi-user mobile apps such as smart classrooms. The README also claims a new peer joins in about one second, on WiFi as well as Ethernet.

Underneath is the ZRE protocol (RFC 36). Each node beacons on UDP port 5670 by default and sends heartbeats. Once peers have found each other, they connect over ZeroMQ using a Dealer-Router pattern, which the README says avoids losing messages unless a peer application terminates. For networks where broadcast is unsuitable, a gossip discovery mode (`zyre_gossip_bind`, `zyre_gossip_connect`) replaces the beacons.

The brew package ships a single executable, `zpinger`. The README says to run it on two or more PCs to test that discovery works, but does not describe what it prints.

## Install

```
brew install zyre
# Pulls in czmq and zeromq. To build from source instead, the README builds libsodium (optional), libzmq, czmq, then zyre, in that order. No account or runtime is needed.
```

## Try this

```
zpinger
```
Run it on two or more machines on the same LAN to test that Zyre discovery works. The README does not say what it prints.

```
zpinger --help
```
Shows whatever options the executable offers, since the README does not document them.

```
gcc myapp.c -lzyre -lczmq -lzmq -o myapp
```
The typical link line for your own program that includes zyre.h, if you want to write a node yourself.

## What's unique

It is a brokerless discovery and group-messaging layer in which nodes find each other by UDP beacon and talk directly, with the ENTER event carrying each peer's name and headers. The protocol is written up as a public spec, RFC 36.

## Caveats

It is mainly a library, so the one executable is a connectivity test and you need a second machine on the LAN to see anything. Some API features, including CURVE security setup, are draft-only, and the README shows signs of age such as Travis CI and Freenode references.

## Links

- [Zyre GitHub repository (homepage)](https://github.com/zeromq/zyre)
- [RFC 36 ZRE protocol specification](http://rfc.zeromq.org/spec:36/ZRE)
- [Zyre issue tracker](https://github.com/zeromq/zyre/issues)
