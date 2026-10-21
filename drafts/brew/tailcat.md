---
name: tailcat
title: tailcat
source: brew
category: fundamentals
commitment: quick
tags: [go, nat-traversal, netcat, network, quick, tailscale, wireguard]
homepage: https://github.com/tailscale/tailcat
scout_score: 6
status: draft
---

# tailcat

**TLDR;** A netcat that tunnels over Tailscale's WireGuard data plane with no account, no root and no setup, just a short address you hand to the other side.

Tailcat connects two machines with an encrypted tunnel and then lets you pipe things through it. Run `tailcat` on one machine and it prints an address starting with `tc`. Hand that address to the other machine and you can send stdin, forward TCP ports, run an SSH or SFTP server, drop files into an inbox, or measure throughput. The README's own tagline is "Tailscale without Tailscale, by Tailscale".

The address is the interesting part. It encodes a WireGuard keypair, by default a pre-shared key, and the region of a DERP relay, all as base64 CBOR. The client connects to the same relay and sends a discovery message, and the server adds it as a WireGuard peer. The handshake first runs through the relay while the tool hole-punches toward a direct UDP path. If that works, traffic leaves the relay entirely.

It does this as a userspace library, built on WireGuard, magicsock and gVisor's netstack. That means no TUN device, no routing table changes, no DNS changes and no root. It is also a Go library, so the same machinery can be embedded in other programs.

The underlying idea is the split between a control plane, which decides who may talk to whom, and a data plane, which moves the packets. Tailcat keeps only the data plane and lets you pass the connection details around however you like. Using it is a good way to see how NAT traversal and relay fallback work in practice.

## Install

```
brew install tailcat
```

## Try this

```
tailcat
```
Starts a listener, picks a relay region, and prints a line like 'Server listening with new address: tc...'. Whatever a client sends appears on its stdout.

```
echo hello | tailcat tcXXXXXXXXX
```
On a second machine, pipes 'hello' to the address printed by the server (use your own address in place of the placeholder). The server's stdout receives it.

```
tailcat ping --until-direct <tc-addr>
```
Pings the server and keeps trying until the path upgrades from the DERP relay to a direct UDP connection. Exits non-zero if it never does.

## What's unique

It reuses Tailscale's own WireGuard, magicsock and netstack code as a userspace tool, so you get NAT traversal and encryption without an account or root. The address itself carries the keys.

## Caveats

The README promises no stability for the CLI, API or wire format, and the public DERP relays have no uptime guarantee and could be withdrawn.

## Links

- [GitHub repository and README](https://github.com/tailscale/tailcat)
- [Go reference (pkg.go.dev)](https://pkg.go.dev/github.com/tailscale/tailcat)
- [Experimental in-browser web demo](https://tailscale.github.io/tailcat/)
- [Default DERP map](https://tailcat.dev/derpmap.json)
