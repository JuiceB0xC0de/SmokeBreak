---
name: stubby
title: Stubby
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dns, network, privacy, protocol, tls]
homepage: https://dnsprivacy.org/wiki/display/DP/DNS+Privacy+Daemon+-+Stubby
scout_score: 5
status: draft
---

# Stubby

**TLDR;** A local DNS daemon that wraps your machine's plain DNS queries in TLS and sends them to a privacy resolver, with Wireshark ready to watch it.

Stubby listens on the loopback addresses (127.0.0.1 and ::1), port 53. Point your system's resolver at it and every DNS query your machine makes is forwarded over TLS (DNS-over-TLS) to upstream servers, rather than going out in plain text. The default configuration uses Strict Privacy and spreads queries across a subset of test servers. The YAML config can point it at others, such as Cloudflare or Quad9.

It exists to encrypt the hop between a desktop or laptop and a DNS Privacy resolver. Ordinary DNS is unencrypted, so anyone on the path can read which names you look up. Stubby is the small piece that fixes that hop without changing your applications.

It is deliberately narrow. It does not cache or recurse. It turns stub queries into TLS queries, and it can sit in front of Unbound or BIND to handle their upstream connections. Options such as strict TLS authentication, EDNS0 padding, client-subnet privacy and a 10-second idle timeout map onto settings in the getdns library it is built on.

The idea underneath is that DNS, one of the oldest plain-text protocols on the network, can be wrapped in TLS. Run Stubby, then watch port 853 in Wireshark to see what that looks like on the wire.

## Install

```
brew install stubby
# needs the getdns and libyaml libraries (brew pulls both in)
# config on *nix: /usr/local/etc/stubby/stubby.yml (override with -C); restart after changes
# binding port 53 needs root, or setcap on Linux
```

## Try this

```
sudo stubby
```
Runs Stubby in the foreground as root so it can bind port 53 on the loopback addresses.

```
dig @127.0.0.1 www.example.com
```
Sends a query straight to the local Stubby, which forwards it upstream over TLS and returns the answer.

```
sudo /usr/local/sbin/stubby-setdns-macos.sh
```
On macOS, switches system DNS to Stubby. Add -r to revert to the DHCP nameservers.

## What's unique

It does one thing: turn plain stub queries into TLS queries. The macOS script switches your whole system over with one command and undoes it with another, so it is easy to try and back out of.

## Caveats

Command-line only, described as early-stage but suitable for technical users; the project's activity is hard to confirm, the macOS GUI is unmaintained, and only DNS-over-TLS is supported, not DNS-over-HTTPS.

## Links

- [Stubby homepage (dnsprivacy.org)](https://dnsprivacy.org/dns_privacy_daemon_-_stubby/)
- [Stubby source on GitHub](https://github.com/getdnsapi/stubby)
- [Stubby configuration guide](https://dnsprivacy.org/wiki/display/DP/Configuring+Stubby)
