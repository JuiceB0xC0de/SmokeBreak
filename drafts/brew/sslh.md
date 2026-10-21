---
name: sslh
title: sslh
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, network, protocol, proxy, ssh, tls]
homepage: https://www.rutschle.net/tech/sslh.shtml
scout_score: 6
status: draft
---

# sslh

**TLDR;** A daemon that listens on one port, such as 443, sniffs each client's first packet, and routes SSH, HTTPS or VPN traffic to the right backend.

sslh accepts TCP connections on one or more ports and reads the first data packet each client sends. It runs probes against that packet to decide what protocol is being spoken, then opens a connection to the matching backend and relays the traffic. It recognises HTTP, TLS (including SNI and ALPN), SSH, WireGuard, OpenVPN, tinc, XMPP and SOCKS5, plus anything a regular expression can match.

The README's typical use case is port 443. A corporate firewall that almost never blocks 443 can still let you reach SSH, as long as something on that port can tell SSH from HTTPS. The project calls itself "a protocol demultiplexer, or a switchboard."

The idea underneath is that most protocols announce themselves in their first few bytes, before any real conversation starts. A TLS ClientHello looks nothing like an SSH banner, and a server can tell them apart without being told. With the SNI and ALPN probe, one IP address can front a whole farm of virtual hosts.

There is also a transparent mode, so backends see the real client IP, and proxyprotocol support for passing client addresses along in HAProxy style. The daemon has fork-based, select-based and libev-based models.

## Install

```
brew install sslh
# Docker alternative: ghcr.io/yrutschle/sslh:latest (needs CAP_NET_RAW and CAP_NET_BIND_SERVICE)
# Binding to port 443 needs privileges, and you need real backends such as sshd and a web server to route to.
```

## Try this

```
sslh --help
```
Lists the command-line options, including the listen address and the per-protocol backend flags.

```
docker run --cap-add CAP_NET_RAW --cap-add CAP_NET_BIND_SERVICE --rm -it ghcr.io/yrutschle/sslh:latest --foreground --listen=0.0.0.0:443 --ssh=hostname:22 --tls=hostname:443
```
Listens on 443 and sends SSH connections to hostname:22 and TLS connections to hostname:443.

## What's unique

Unlike a plain port forwarder, it identifies the protocol from the first packet, so one public port can serve HTTPS, SSH and VPN traffic at once.

## Caveats

Transparent proxying is hard to set up and, per the README, depends heavily on your network; an openSUSE security review in 2025 found denial-of-service issues, so connection limits matter.

## Links

- [Homepage (redirects to GitHub)](https://www.rutschle.net/tech/sslh.shtml)
- [GitHub repository and README](https://github.com/yrutschle/sslh)
- [openSUSE security review (2025)](https://security.opensuse.org/2025/06/13/sslh-denial-of-service-vulnerabilities.html)
- [Mailing list](https://lists.rutschle.net/mailman/listinfo/sslh)
