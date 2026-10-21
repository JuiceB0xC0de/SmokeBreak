---
name: tsshd
title: tsshd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, go, network, protocol, quic, roaming, ssh, udp]
homepage: https://trzsz.github.io/tsshd
scout_score: 5
status: draft
---

# tsshd

**TLDR;** An SSH server that moves your session onto UDP after login, so it survives IP changes, sleep and dropped links, much like mosh.

tsshd is the server half of a pair. The client, tssh (from the trzsz-ssh project), first logs in over ordinary TCP SSH. That login starts a fresh tsshd process on the server, which picks a random UDP port in the range 61001-61999 and sends the port and session keys back through the SSH channel. The SSH connection is then closed, and the session continues over QUIC or KCP on UDP.

The roaming trick sits on the client. A proxy implementing Go's net.PacketConn interface sits between the QUIC or KCP layer and the network. When heartbeats stop, it can re-authenticate to the server from a new address, so the transport above it never sees an interruption. Authentication packets are encrypted with AES-256-GCM and carry a strictly increasing sequence number to block replays. QUIC runs over TLS 1.3.

The author says it was inspired by mosh and wants the same survival across roaming and sleep/wake. It takes a different route: it keeps ordinary SSH behaviour and bootstraps through a normal login. The README says tssh and tsshd "work exactly like ssh", with no plans for mosh-style local echo or line editing. It aims for OpenSSH compatibility and supports UDP port forwarding, local and remote.

The underlying idea is that SSH's session semantics do not have to be tied to one TCP connection. Reading how the handoff, the proxy and the replay protection fit together is a compact way into transports, session identity and NAT roaming. The README also describes a Go middleware framework for building custom roaming SSH services.

## Install

```
brew install tsshd
# Server needs tsshd installed and reachable; the client needs tssh (trzsz-ssh).
# If tsshd is not on the server PATH, set TsshdPath or pass --tsshd-path.
# The default UDP port range can be changed with TsshdPort.
```

## Try this

```
tssh --udp xxx
```
Logs in to host xxx over ordinary SSH, then moves the session to UDP in roaming mode; otherwise it is used like ssh.

```
tssh --udp --kcp xxx
```
Same login, but uses the KCP transport instead of QUIC.

```
tsshd --help
```
Lists the server's options.

## What's unique

It does not replace SSH. It bootstraps through a normal SSH login, then hands the session to a per-session UDP process. The client's in-memory packet proxy hides IP changes from QUIC or KCP.

## Caveats

Roaming needs the tssh client, since plain OpenSSH clients cannot use it, and there is no mosh-style local echo; if UDP is blocked, UdpProxyMode TCP works but adds latency.

## Links

- [Homepage](https://trzsz.github.io/tsshd)
- [GitHub repository](https://github.com/trzsz/tsshd)
- [tssh client (trzsz-ssh)](https://github.com/trzsz/trzsz-ssh)
- [Chinese docs](https://trzsz.github.io/cn/tsshd)
