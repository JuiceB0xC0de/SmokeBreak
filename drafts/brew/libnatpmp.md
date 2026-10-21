---
name: libnatpmp
title: libnatpmp
source: brew
category: fundamentals
commitment: quick
tags: [c, nat, network, protocol, quick, router]
homepage: https://miniupnp.tuxfamily.org/libnatpmp.html
scout_score: 7
status: draft
---

# libnatpmp

**TLDR;** A small C client library, plus the natpmpc tool, for NAT-PMP: the protocol that lets a program ask your router for its public address and an open port.

NAT-PMP, the NAT Port Mapping Protocol, lets a program on a private network ask its router two things: what is my public address, and can you forward a public port to this private one. libnatpmp is a C client for that exchange. Its author describes it as "an attempt to make a portable and fully compliant implementation of the protocol for the client side."

The homepage calls NAT-PMP "the direct concurrent to the UPnP IGD specification" and says it was mainly supported by Apple software and hardware at the time. So it is a second answer to a problem most people only know through UPnP: how does a peer-to-peer app, game or server behind a home router become reachable without manual configuration?

The library is built for event loops. All calls are asynchronous and use non-blocking sockets. You send a request with calls like sendpublicaddressrequest or sendnewportmappingrequest, wait on the socket with select() or poll() using getnatpmprequesttimeout() as the timeout, then call readnatpmpresponseorretry() until it stops returning NATPMP_TRYAGAIN. The homepage walks through this as a small state machine: get the public address, then create a mapping, for example a TCP redirect with a 3600-second lifetime.

The Homebrew formula also installs natpmpc, a command-line client. The pages I read say nothing about its options or output, so start with its help text. The library is old, with the homepage last modified in 2008, but the protocol is small and the code is a short read.

## Install

```
brew install libnatpmp
# natpmpc talks to your router, so it only does something useful on a network whose gateway supports NAT-PMP
```

## Try this

```
natpmpc --help
```
Prints the usage text for the client, which is the quickest way to see what it can ask a router.

## What's unique

It is a compact client for NAT-PMP, the lesser-known sibling of UPnP IGD, with an API designed around asynchronous, event-driven code.

## Caveats

The homepage was last modified in 2008 and the project looks dormant; the homepage samples omit error checking, and whether natpmpc gets an answer depends on your router supporting NAT-PMP.

## Links

- [libnatpmp homepage](https://miniupnp.tuxfamily.org/libnatpmp.html)
- [GitHub repository (mirror README)](https://github.com/miniupnp/libnatpmp)
- [Mirror of the homepage cited in the README](http://miniupnp.free.fr/libnatpmp.html)
