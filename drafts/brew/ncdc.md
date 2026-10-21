---
name: ncdc
title: ncdc
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, file-sharing, network, p2p, protocol, tui]
homepage: https://dev.yorhel.nl/ncdc
scout_score: 5
status: draft
---

# ncdc

**TLDR;** A terminal client for Direct Connect, the hub-based peer-to-peer file-sharing network, speaking both the ADC and NMDC protocols through an ncurses interface.

ncdc connects to several Direct Connect hubs at once. It handles hub chat and private messages, browses user lists and other users' file lists, and manages your own shares, searches, uploads, downloads and queue. It is written in C and released under the MIT license.

Direct Connect is an older style of peer-to-peer network. Instead of one global swarm, you join a hub, a server run by a community, and see the people and shares there. Clients then transfer files directly between each other. ncdc speaks both of the protocols in use: the older NMDC and the newer ADC.

The feature list shows some of the protocol machinery: downloads checked against TTH hashes, multi-source and segmented transfers, TLS on hub and client connections, encrypted ADC SUDP search replies over UDP, and sendfile() for uploads. Reading how a client handles these is a way into how a hub-based network differs from the swarm model most people know.

The homepage calls it "a lightweight direct connect client with a friendly ncurses interface." It is in passive maintenance: version 1.25 is dated 2025-03-04, and the author says new features are unlikely.

## Install

```
brew install ncdc
# No account or hardware needed. You will need the address of a Direct Connect hub to join.
```

## Try this

```
ncdc --help
```
Prints the command-line options so you can see what the client accepts before launching the interface.

```
ncdc
```
Starts the ncurses interface, where you can configure your nick and shares and connect to a hub.

## What's unique

It is a full terminal client for both ADC and NMDC. The homepage lists per-hub settings, one listen port for TLS and TCP, and Trust on First Use for TLS hubs as uncommon among DC clients.

## Caveats

Development is passive and new features are unlikely, and the homepage lists NAT traversal, OP features and SOCKS support as missing.

## Links

- [ncdc homepage](https://dev.yorhel.nl/ncdc)
- [Installation instructions](https://dev.yorhel.nl/ncdc/install)
- [Git repository (development version)](git://g.blicky.net/ncdc.git)
