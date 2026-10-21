---
name: ocproxy
title: ocproxy
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, network, proxy, socks, tcp-ip, userspace, vpn]
homepage: https://github.com/cernekee/ocproxy
scout_score: 6
status: draft
---

# ocproxy

**TLDR;** A userspace TCP/IP stack that turns an OpenConnect VPN tunnel into a local SOCKS5 server and forwarded ports, with no root and no routing changes.

ocproxy is a helper for OpenConnect, the open-source client for Cisco AnyConnect-style VPNs. Normally a VPN creates a kernel tunnel device and rewrites the routes, so every program on the machine starts sending traffic through it. ocproxy takes a different path. OpenConnect hands it the tunnel's file descriptor, and ocproxy runs the whole TCP/IP stack inside its own process using lwIP, a small embedded network stack.

The result is a local SOCKS5 server (`-D`) and local ports that forward to hosts on the far side of the VPN (`-L`). Only the connections you point at it go through the tunnel. The rest of the host's traffic never notices. This also works where root is unavailable or unwelcome, such as shared multiuser machines, and it lets you connect to several VPNs at once even when their address ranges overlap.

The idea underneath is that a network stack is just code. It does not have to live in the kernel. Once the packets arrive on a file descriptor, a program can speak TCP, answer DNS, and hand out connections as ordinary sockets. Reading how ocproxy takes its settings from environment variables set by OpenConnect (`INTERNAL_IP4_ADDRESS`, `VPNFD` and others) is a compact lesson in how VPN clients and their scripts talk to each other.

The repository also includes an experimental companion, vpnns. It uses Linux user and network namespaces to run a whole application in its own network world attached to the VPN, so no proxy settings are needed. The README claims it needs no root and no host network changes.

## Install

```
brew install ocproxy
# Also needs OpenConnect and a VPN gateway you can log in to. ocproxy is launched by OpenConnect, not run directly.
```

## Try this

```
openconnect --script-tun --script "./ocproxy -L 2222:unix-host:22 -L 3389:win-host:3389 -D 11080" vpn.example.com
```
OpenConnect starts ocproxy as its tunnel script, opening a SOCKS5 server on port 11080 and forwarding local ports 2222 and 3389 across the VPN.

```
ssh -p2222 localhost
```
Connects through the forwarded port to unix-host:22 on the far side of the VPN.

```
socksify ssh unix-host
```
Runs ssh through the built-in SOCKS5 server using the socksify wrapper.

## What's unique

It replaces the kernel tunnel device with a userspace TCP/IP stack, so one application or port can use a VPN without root or touching the host's routes.

## Caveats

The README shows no release dates and mentions Ubuntu 14.04 and 16.04 packages, so it may be dated; vpnns is Linux-only and marked experimental, and you need a working OpenConnect VPN to try any of it.

## Links

- [ocproxy GitHub repository](https://github.com/cernekee/ocproxy)
- [OpenConnect project](http://www.infradead.org/openconnect/)
- [FoxyProxy (browser proxy extension referenced in README)](http://getfoxyproxy.org/)
