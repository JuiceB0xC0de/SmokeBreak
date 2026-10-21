---
name: stuntman
title: Stuntman
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, nat, network, protocol, stun, udp]
homepage: https://www.stunprotocol.org
scout_score: 7
status: draft
---

# Stuntman

**TLDR;** A STUN server and client that tell you which public IP and port the internet sees you as, and probe how your NAT behaves.

Stuntman is an open source implementation of STUN, Session Traversal Utilities for NAT. A STUN server does one small thing: a client sends it a binding request, and it answers with the public IP address and port the request appeared to come from. That is how a machine behind a home router learns what address the outside world sees.

The package installs `stunserver`, `stunclient`, and `stuntestcode`. The server speaks UDP or TCP over IPv4 or IPv6, and by default listens on port 3478. In basic mode it uses one port. In full mode it listens on two different IP addresses, which lets the client run the NAT behavior and filtering tests from RFC 5780. The client implements all of those tests, so it can report how your NAT maps and filters traffic, not only your address.

The idea underneath is NAT traversal, the hidden problem behind video calls, games, and peer-to-peer apps. Two machines behind routers cannot simply connect, and STUN is one piece of how they find each other. The homepage is upfront that "STUN by itself does not solve the NAT Traversal problem for P2P connectivity issues." Stuntman gives you a working piece of the larger machinery to read and run. It also ships code libraries for building a STUN client into your own program.

## Install

```
brew install stuntman
# Open your firewall for the server's port (3478 by default) if you want others to reach it.
```

## Try this

```
stunserver --help
```
Lists the server's command-line options. Run with no arguments, it listens on port 3478 on all adapters.

```
stunclient --help
```
Shows the client's options, including how to pick a server and port.

```
stunclient stun.selbie.com
```
Asks a STUN server by hostname which public address and port it sees you as. This is the README's own example.

## What's unique

It is a complete RFC 5389 and 5780 implementation with a built-in NAT behavior test suite, not just a bare binding responder. It also has a hook for plugging in your own authentication.

## Caveats

TLS mode is not implemented, authentication is off by default and you must write the lookup hooks yourself, and in full mode `stunclient localhost` may fail because the server does not listen on loopback.

## Links

- [Homepage](https://www.stunprotocol.org)
- [GitHub repository and README](https://github.com/jselbie/stunserver)
