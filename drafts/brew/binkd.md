---
name: binkd
title: binkd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, ancient, bbs, fidonet, network, protocol]
homepage: https://github.com/pgul/binkd
scout_score: 5
status: draft
---

# binkd

**TLDR;** A mailer daemon that carries FidoNet mail and files over TCP/IP, a way to touch the store-and-forward BBS networks that predate the internet.

binkd is a mailer for FTN, the Fido Technology Network family, which includes FidoNet. These networks grew up around dial-up bulletin board systems. Each system collected mail and files, then called a neighbour on a schedule to hand them on. Nobody needed a permanent connection, and messages hopped from node to node until they arrived.

binkd keeps that model and swaps the transport. The README describes it as "a Fidonet mailer designed to operate via TCP/IP networks", and as a way to make "efficient utilization of TCP/IP protocol suite as a transport layer in FTN-based (Fido Technology Network) networks." Instead of a modem call, one node connects to another over the internet and the two exchange queued mail and file bundles.

The idea underneath is store-and-forward networking: no central server, just a web of peers that pass traffic along on a schedule. It is a different shape from the always-on, request-and-response internet most developers know. The README is brief and does not explain the protocol or configuration. The linked FAQ and manuals, in English and Russian, are where the detail lives. A community with echomail areas and mirrors still seems to surround it.

## Install

```
brew install binkd
# The brief documents a source build instead: git clone https://github.com/pgul/binkd, cp mkfls/unix/* . then ./configure && make
# Running it usefully needs a binkd.cfg and, in practice, a FidoNet-style node or a peer to connect to.
```

## Try this

```
git clone https://github.com/pgul/binkd
```
Fetches the source, which is the install route the README documents for UNIX.

```
make -n install
```
After building, shows what make install would do without touching your system.

```
configure --prefix=/another/path
```
Builds binkd for a different install directory instead of the default /usr/local.

## What's unique

It is a working piece of FidoNet infrastructure, carrying pre-internet store-and-forward mail over TCP/IP, with manuals in both Russian and English.

## Caveats

The README is thin on configuration, the status is unclear with no releases listed, and the linked manuals are old, covering 0.9.2 and 0.9.9.

## Links

- [Homepage (GitHub repository)](https://github.com/pgul/binkd)
- [FAQ](http://binkd.grumbler.org/binkdfaq.shtml)
- [English manual for binkd 0.9.2 (archived)](http://web.archive.org/web/20131010041927/http://www.doe.carleton.ca/~nsoveiko/fido/binkd/man/)
- [Russian manual for binkd 0.9.9](http://binkd.grumbler.org/binkd-ug-ru.htm.win.ru)
