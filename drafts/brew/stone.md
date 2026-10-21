---
name: stone
title: stone
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, c, network, proxy, ssl, tcp, tunneling, udp]
homepage: https://www.gcd.org/sengoku/stone/
scout_score: 6
status: draft
---

# stone

**TLDR;** A tiny C program that relays TCP and UDP connections at the application layer, and can wrap plain services in SSL or tunnel streams through HTTP proxies.

Stone listens on one port, opens a connection to another, and copies bytes between them. You give it a listen spec and a destination spec, such as `stone outer:telnet 10023`, and anything that connects to port 10023 on that machine ends up talking to telnet on `outer`. The same trick works for UDP, so DNS and NTP queries can be relayed across a boundary.

The interesting part is the suffixes. Add `/ssl` to a listener and a plain HTTP server starts speaking https. Add `/http` and a stream gets carried inside HTTP POST requests through an ordinary proxy, with a second stone on the far side to unwrap it. `/proxy` adds credentials to requests for a browser that cannot send them. `/apop` lets a mail client without APOP reach an APOP server. Run as `stone proxy 8080`, it is a small HTTP proxy.

The author wrote it for firewalls, at a time when Unix boxes were the usual firewall and Windows NT machines were starting to be used too, so it runs on both. He also points out that the source is about 10000 lines of C, which keeps the risk of security holes low. That small size makes it readable: a whole relay, SSL terminator and tunnel in one file, a good way to see what a proxy does at the socket level.

## Install

```
brew install stone
# SSL features need OpenSSL; POP-to-APOP conversion needs an MD5 program installed.
```

## Try this

```
stone --help
```
Prints the usage summary, showing the listen and destination spec syntax and the available options.

```
stone proxy 8080
```
Starts a tiny HTTP proxy on port 8080 that you can point a browser or curl at.

```
stone localhost:http 443/ssl
```
Wraps the local plain HTTP port in SSL so the same server answers https on port 443.

## What's unique

One small C program covers a TCP/UDP relay, SSL wrapping, an HTTP proxy, HTTP tunneling and IPv4/IPv6 conversion. The tunnel that carries a stream inside HTTP POST through an ordinary proxy is the standout trick.

## Caveats

It is a firewall-era tool with a quiet release history (2.4 dated 2019), thin build and SSL documentation, and a relay you should think hard about before exposing to a network.

## Links

- [Stone homepage](https://www.gcd.org/sengoku/stone/)
- [Author's home page (Hiroaki Sengoku)](https://www.gcd.org/sengoku/)
