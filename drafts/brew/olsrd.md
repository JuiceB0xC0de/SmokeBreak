---
name: olsrd
title: olsrd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, mesh, network, protocol, routing, wireless]
homepage: https://github.com/OLSR/olsrd
scout_score: 6
status: draft
---

# olsrd

**TLDR;** A routing daemon from community wireless mesh networks, where each node learns its neighbours and works out paths through the network with no central router.

olsrd is the olsr.org implementation of the Optimized Link State Routing Protocol, version 1 (RFC 3626, from the IETF MANET group). Each machine running it swaps link-state information with its neighbours and uses that to choose paths across a mesh. The olsr.org site describes it as built for mobile ad hoc networks on embedded devices "like commercial of the shelf routers, smartphones or normal computers."

It began as a 2004 Master Thesis by Andreas Tonnesen. It then grew into an open source project because, in the project's words, "the routing protocol was used by Freifunk, FunkFeuer and others to build Community Mesh Networks." The GitHub page says it is now maintained by Freifunk Berlin.

The idea underneath is a network that has no fixed topology and no one in charge. Nodes appear, vanish and move, and the routing tables have to keep up. Link-state routing is one answer to that problem, and reading about how olsrd handles it is a way into mesh networking in general.

The README is mostly license text, so expect to get your bearings from the olsr.org site and the repository's directories instead.

## Install

```
brew install olsrd
# A routing daemon normally needs root and a wireless interface. A real mesh needs more than one node, and the brief confirmed no setup steps beyond brew.
```

## Try this

```
olsrd --help
```
Prints the daemon's command-line options, which is the quickest way to see what it can be told to do.

## What's unique

It is a long-lived, real-world mesh routing daemon that community networks such as Freifunk and FunkFeuer have used, and it started as a master's thesis. Packaging exists for Debian, Red Hat, OpenBSD and Android.

## Caveats

This is olsrd v1, the older branch; olsr.org points to olsrd2 as the successor, and the README has no quickstart, so setup details are unverified.

## Links

- [GitHub repository](https://github.com/OLSR/olsrd)
- [olsr.org project site](http://www.olsr.org)
