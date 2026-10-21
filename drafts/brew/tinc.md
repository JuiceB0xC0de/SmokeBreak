---
name: tinc
title: tinc
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, mesh, network, protocol, tunnelling, vpn]
homepage: https://www.tinc-vpn.org/
scout_score: 5
status: draft
---

# tinc

**TLDR;** A mesh VPN daemon where every node connects directly to every other, with no central hub and one config file per new node.

tinc is a VPN daemon called tincd. It uses tunnelling and encryption to build a private network between hosts on the Internet. The VPN shows up to the operating system as an ordinary network device, so existing software needs no changes. Traffic is authenticated and encrypted with LibreSSL or OpenSSL, and can optionally be compressed with zlib or LZO.

The interesting part is the topology. Most VPNs are a hub with spokes, and every packet goes through the hub. In tinc, nodes form a mesh. In the project's words: "VPN traffic is always (if possible) sent directly to the destination, without going through intermediate hops." NAT traversal works as long as one node accepts incoming connections on a public IP address, even a dynamic one.

Adding a node means adding a configuration file. In the project's words, there is "no need to start new daemons or create and configure new devices or network interfaces." The homepage also pitches it as a way to link Ethernet segments, so LAN-only applications and games can run across the Internet.

The manual's table of contents lists a UDP tunnel, a meta-connection, a meta-protocol, and an authentication protocol. That makes it a good door into how tunnelling VPNs are put together: a control channel for peers to find and authenticate each other, and a data channel for the packets.

## Install

```
brew install tinc

Setting it up needs a TUN/TAP device on your OS, and you generate a keypair and write main and host config files by hand. The manual covers this with a worked example.
```

## Try this

```
tincd --help
```
Lists the daemon's command-line options, a starting point before reading the manual's configuration chapter.

## What's unique

It is a decentralised mesh in which every node routes directly to every other, rather than funnelling traffic through a central server. Growing the network takes one config file.

## Caveats

Setup is manual (TUN/TAP, keypairs, config files), the homepage's platform list still names Windows 2000 through 8, and 1.0.37 is described as likely the last 1.0 release.

## Links

- [Homepage](https://www.tinc-vpn.org/)
- [Documentation (tinc Manual)](https://www.tinc-vpn.org/documentation/)
