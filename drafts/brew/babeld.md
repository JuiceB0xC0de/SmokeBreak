---
name: babeld
title: babeld
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ipv6, mesh, network, protocol, routing]
homepage: https://www.irif.fr/~jch/software/babel/
scout_score: 6
status: draft
---

# babeld

**TLDR;** A small routing daemon for Babel, an IETF-standard protocol that lets wired and wireless mesh nodes find loop-free paths to each other.

Babel is a distance-vector routing protocol for IPv6 and IPv4, and babeld is its reference implementation. You start the daemon on each node, name the interfaces it should use (`babeld eth1`), and the nodes exchange updates and build routes to one another's addresses. One update packet can carry both IPv6 and IPv4 routes.

The homepage says Babel draws on DSDV, AODV and Cisco's EIGRP, but is designed to work well in wireless mesh networks as well as wired ones. The daemon checks what kind of link it is on. On a wired link it turns on optimisations that make it about as efficient as traditional routing protocols. On a wireless link it turns them off and uses the ETX packet-loss metric, designed for 802.11 WiFi. Convergence is slower there, but the quirks of radio links do not break routing.

The idea underneath is how routers avoid looping packets forever. In the project's words: "in a pure mesh network, Babel never creates a routing loop, and in a prefix-based network, all routing loops are guaranteed to disappear as soon as one update went around a loop (there is no "counting to infinity")." It is a good way into how mesh networks and home routers work out paths on their own.

Babel is a standard, RFC 8966, with a family of related RFCs covering authentication, DTLS, source-specific routing and Homenet. That is a lot of specification behind a small daemon.

## Install

```
brew install babeld
# Running it for real needs root, a network interface, and unique IPv6 and/or IPv4 addresses on each node. A second machine or VM helps to see it route.
```

## Try this

```
babeld --help
```
Prints the daemon's options so you can see what it can be configured to do.

```
# babeld eth1
```
Starts the daemon on eth1 and begins exchanging routing updates with any Babel neighbours on that link.

```
# babeld -C 'redistribute metric 128' eth1
```
Starts babeld on eth1 and redistributes all routes into Babel, as you would on an Internet gateway node.

## What's unique

It switches between wired and wireless behaviour depending on the link it detects, and carries IPv4 and IPv6 routes in the same updates. It is also a small daemon backed by a full IETF standard.

## Caveats

The brief could not confirm recent activity; wireless convergence is slow by design, up to about 40 seconds after heavy packet loss; and the README's examples use older Linux tools like iwconfig.

## Links

- [Babel homepage (Julius Chroboczek)](https://www.irif.fr/~jch/software/babel/)
- [babeld GitHub repository and README](https://github.com/jech/babeld)
