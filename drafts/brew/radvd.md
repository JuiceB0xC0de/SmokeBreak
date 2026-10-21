---
name: radvd
title: radvd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, daemon, ipv6, ndp, networking, protocol, slaac]
homepage: https://radvd.litech.org/
scout_score: 5
status: draft
---

# radvd

**TLDR;** A small daemon that sends IPv6 Router Advertisements, the quiet messages that let every device on a LAN pick its own address and default router.

radvd is the IPv6 Router Advertisement Daemon. It runs on a Linux or BSD machine acting as an IPv6 router, listens for Router Solicitation messages from hosts, and sends Router Advertisements (RFC 4861) onto the local network. It also sends them periodically to the all-routers multicast group. Its input is a configuration file, radvd.conf, which describes prefixes, lifetimes, route information and DNS options for each interface.

The advertisements are what make IPv6 stateless autoconfiguration work. A host joins a network, asks who the routers are, and gets back a prefix and a default router. It then builds its own address with no DHCP server involved. radvd can also hand out DNS servers and search domains through the RDNSS and DNSSL options. The project's own line is that its messages are required for IPv6 stateless autoconfiguration.

The design is deliberately narrow. The README's FAQ is blunt: "Radvd is not a routing or forwarding daemon." It advertises, and it does not assign addresses, set up routes or enable forwarding. Those jobs are left to the admin or init scripts. That makes it a clear view of one small piece of Neighbor Discovery.

The package also ships radvdump, which dumps the Router Advertisements it sees on the wire. Between the two, you can both send and inspect the messages that every IPv6 network sends constantly. The changelog goes back to 2001, and the project is still maintained.

## Install

```
brew install radvd
# Needs root or equivalent privileges to open raw ICMPv6 sockets, and a Linux or BSD router setup to be useful. Homebrew may not be the natural route here; the project builds from source with ./configure, make and make install.
```

## Try this

```
radvd --help
```
Lists the daemon's command-line options, including how to point it at a configuration file.

```
radvdump --help
```
Shows the options for the companion tool that prints Router Advertisements seen on the wire.

## What's unique

It does one job, advertising prefixes and options, and refuses to configure interfaces, addresses or routes. It is also the long-running reference daemon for SLAAC and RDNSS on many Linux systems.

## Caveats

Linux is the supported platform and BSD mileage may vary; Secure Neighbor Discovery (SEND) is not implemented, and you must set up addresses, routes and forwarding yourself.

## Links

- [radvd homepage](https://radvd.litech.org/)
- [radvd GitHub repository](https://github.com/radvd-project/radvd)
