---
name: switch-lan-play
title: switch-lan-play
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, arp, game, network, protocol, tunnel, udp]
homepage: https://github.com/spacemeowx2/switch-lan-play
scout_score: 5
status: draft
---

# switch-lan-play

**TLDR;** Tunnels a Nintendo Switch's local-network traffic through a relay on the internet, so games that expect a LAN think distant friends are next door.

Some games only look for opponents on the local network. They send ARP requests and broadcasts and expect neighbours to answer. switch-lan-play is a client and relay server pair that carries that traffic across the internet instead.

The `lan-play` client runs on a PC connected to the same router as the Switch. It picks up the Switch's ARP and IPv4 packets, wraps them in UDP, and sends them to a shared relay Server. The Server passes them on to the other players' clients, which hand them to their own consoles. An optional SOCKS5 proxy can sit in front of the client.

The interesting part is how the Server behaves like a very small network switch. It reads the source and target IP addresses from each payload and keeps a cache mapping source IP to LAN IP. When a packet's target is not in the cache, it does what a LAN does and broadcasts it. In the README's words: "If the target IP address shown in the payload doesn't match the cache, the packet is broadcast to the entire room." That one rule is how LAN-style discovery reaches everyone.

The wire protocol is just as small: a one-byte type field followed by the payload, with types KEEPALIVE, IPV4, PING and IPV4_FRAG. It is a readable example of faking a shared subnet with a relay and a cache.

## Install

```
brew install switch-lan-play
# You also need a relay Server (the Docker image or the Node server in the repo's server/ directory).
# The Switch needs a static IP set by hand, and the PC and Switch must be on the same router.
```

## Try this

```
lan-play --help
```
Lists the client's options, so you can see what it expects before pointing it at a server.

```
lan-play --socks5-server-addr example.com:1080
```
Runs the client through a SOCKS5 proxy. Traffic to the relay server does not go through the proxy.

```
docker run -d -p 11451:11451/udp -p 11451:11451/tcp spacemeowx2/switch-lan-play
```
Starts a relay Server in Docker, with UDP for game traffic and TCP for the monitor endpoint on port 11451.

## What's unique

It targets the broadcast-based discovery that LAN games rely on and carries it over the internet, using a relay that rebroadcasts unknown-target packets to the whole room.

## Caveats

Maintenance status is unclear from the README, and it needs a Switch with a manually set static IP, a PC on the same router, and a relay server that everyone connects to.

## Links

- [GitHub repository (homepage)](https://github.com/spacemeowx2/switch-lan-play)
- [Setup instructions for Switch](http://lan-play.com/install-switch)
- [lan-play.com](https://www.lan-play.com/)
