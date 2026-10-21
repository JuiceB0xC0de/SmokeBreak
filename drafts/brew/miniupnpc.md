---
name: miniupnpc
title: miniupnpc
source: brew
category: fundamentals
commitment: quick
tags: [c, nat, network, protocol, quick, ssdp, upnp]
homepage: http://miniupnp.free.fr/
scout_score: 8
status: draft
---

# miniupnpc

**TLDR;** A tiny dependency-free C client that finds your router over UPnP and asks it to open ports, a hands-on door into how NAT traversal works.

MiniUPnP is a small family of C programs around the UPnP Internet Gateway Device (IGD) protocol, the mechanism that lets a machine on a home network ask its router to open a port. MiniUPnPc is the client side. It finds a gateway on the LAN and sends it port-mapping requests. Its companion MiniUPnPd is the server side, a daemon that runs on a Linux or BSD box acting as the gateway and turns those requests into firewall rules (pf, ipfw, ipf, netfilter or nftables).

The author built it because libupnp was too heavy for him. In his words, he wanted "the simplest library possible, with the smallest footprint and no dependencies to other libraries such as XML parsers or HTTP implementations." The client library is described as under 50KB of x86 code, written in pure ANSI C. The daemon runs as one process with no extra threads and makes no system() or exec() calls.

Underneath is a protocol most people use daily without seeing it. The client finds the router with SSDP, a multicast discovery protocol. It then talks SOAP over HTTP to the gateway's services to add or remove port mappings. A small companion, MiniSSDPd, listens for discovery traffic so several UPnP clients can skip their own search and set up redirections faster. Because the code is small and the dependencies are few, it also works as a readable reference for both ends of the exchange.

## Install

```
brew install miniupnpc
# installs the client tools: external-ip, upnp-listdevices, upnpc
# needs a UPnP-capable router on your LAN to talk to; the daemon (MiniUPnPd) is a separate project component and needs a supported firewall backend to build
```

## Try this

```
upnpc --help
```
Prints the client's usage, showing what it can ask a gateway to do.

```
upnp-listdevices --help
```
Shows the options for discovering UPnP devices on your network.

```
external-ip --help
```
Shows usage for the helper that asks the gateway for your external IP address.

## What's unique

It is a tiny, dependency-free C implementation of both sides of UPnP IGD, small enough to read and to run on low-memory routers.

## Caveats

The homepage was last modified in August 2024 but the maintenance cadence is unclear, the ipf backend is described as not maintained, and the README warns that MiniUPnPd has had vulnerabilities in the past, so keep it updated and keep SSDP and HTTP/SOAP ports reachable only from the LAN.

## Links

- [MiniUPnP project homepage](http://miniupnp.free.fr/)
- [GitHub repository (README)](https://github.com/miniupnp/miniupnp)
- [Primary Git host (Framagit)](https://framagit.org/miniupnp/miniupnp/)
