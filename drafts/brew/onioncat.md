---
name: onioncat
title: OnionCat
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, i2p, ipv6, network, overlay, tor, vpn]
homepage: https://github.com/rahra/onioncat
scout_score: 6
status: draft
---

# OnionCat

**TLDR;** OnionCat turns a Tor hidden service or I2P identity into an IPv6 address on a TUN device, so ordinary IP tools can talk over the onion network.

OnionCat (command `ocat`) is a userland program that opens a TUN device and gives it an IPv6 address derived from your .onion or I2P identifier. The kernel sends packets for that address to ocat. ocat relays them through Tor's SOCKS proxy (default 127.0.0.1:9050) to the peer's hidden service, where another OnionCat instance unwraps them. TCP and UDP are the main use. In the README's words, "You can think of it as a peer-to-peer VPN between hidden services."

The idea underneath is that a name can double as an address. In Tor mode the prefix is `fd87:d87e:eb43::`, and in I2P (GarliCat) mode it is `fd60:db4d:ddb5::`. The rest of the address comes from the hidden-service identifier. Routing needs no directory: the address already says where to connect. Ordinary sockets and tools work over the overlay without per-app proxy settings.

There is a small diagnostic trick in the README. Pinging `fd87:d87e:eb43::dead:beef` tests the link between the kernel and ocat, and pinging `fd87:d87e:eb43::feed:beef` tests the Tor side. The `-i` and `-o` flags convert between onion IDs and IPv6 addresses and then exit, which is a quick way to see the mapping.

The project dates back to 2008, and its man page is dated 2023. Modern Tor v3 addresses are too long to fit into an IPv6 address. Peers on v3 need manual entries in a hosts file, and the client must be started with `-H`.

## Install

```
brew install onioncat
# Running it needs a Tor (or I2P) instance with a configured hidden service, and root to set up the TUN device. ocat then drops to a 'tor' user (or uid 65534).
```

## Try this

```
ocat --help
```
Prints the options and usage, a good first look before setting up a hidden service.

```
ocat -i onion_id
```
Converts an onion_id to its IPv6 address and exits, with no network needed.

```
ocat -o IPv6_address
```
Converts an OnionCat IPv6 address back to the onion_id and exits.

## What's unique

It maps a hidden-service name directly to an IPv6 address, so any IP-based program can use Tor or I2P as a network without proxy support of its own.

## Caveats

OnionCat does no encryption of its own ("a plain tunneling through TCP sessions"), Tor v3 peers need hand-maintained hosts entries, and the local controller on port 8066 is unauthenticated and not meant for production.

## Links

- [Homepage / source README](https://github.com/rahra/onioncat)
- [Intro to OnionCat4 and HSv3](https://github.com/rahra/onioncat/blob/master/doc/INTRO_TO_ONIONCAT4.txt)
- [Docs folder](https://github.com/rahra/onioncat/tree/master/doc)
