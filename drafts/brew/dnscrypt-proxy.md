---
name: dnscrypt-proxy
title: dnscrypt-proxy
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dns, encryption, network, privacy, protocol]
homepage: https://dnscrypt.info
scout_score: 5
status: draft
---

# dnscrypt-proxy

**TLDR;** A local DNS proxy that wraps your machine's lookups in encrypted transports like DNSCrypt, DNS-over-HTTPS and Oblivious DoH, so you can see how resolver trust works.

dnscrypt-proxy is a Go program that listens on localhost and speaks ordinary DNS to your applications. Upstream, it forwards each query over an encrypted transport: DNSCrypt v2 (including a post-quantum variant), DNS-over-HTTPS, Anonymized DNSCrypt, or Oblivious DoH. Answers return to the client as plain DNS responses, so nothing else on the machine needs to change.

The idea underneath is that classic DNS is unauthenticated plaintext, and most people never look at who answers their questions. DNSCrypt takes a different approach to trust. Per the project site, clients are configured with a resolver IP address and a public key, so "Encryption starts from the very first query." There is no plaintext hostname lookup to bootstrap it, and each resolver's key is verified by signatures rather than certificate authorities.

The proxy also does several things around that core. It measures the speed of the resolvers you list and balances traffic across the fastest ones. It can cache answers and filter ads and malware. It also offers cloaking, described as "like a HOSTS file on steroids". To hide your client IP from the resolver, it can route through Tor, SOCKS proxies, or Anonymized DNS relays.

It is a good afternoon project: run it, watch what leaves your network interface, then open the config file and see how many choices a single DNS lookup involves.

## Install

```
brew install dnscrypt-proxy
# Config file: $HOMEBREW_PREFIX/etc/dnscrypt-proxy.toml
# By default it listens on 127.0.0.1 port 53, which needs admin rights.
# To use it, point your system DNS at 127.0.0.1 in System Preferences > Network > Advanced > DNS.
```

## Try this

```
dnscrypt-proxy --help
```
Lists the command-line options so you can see what the binary accepts before editing the config.

```
sudo tcpdump -i en1 -vvv 'port 443'
```
Watches encrypted traffic on port 443 (replace en1 with your interface). Homebrew says a working setup shows a line mentioning resolver.dnscrypt.info.

## What's unique

It bundles many encrypted DNS transports plus Tor and relay-based anonymization into one binary. The DNSCrypt protocol it centers on needs no certificate authorities.

## Caveats

Pointing system DNS at 127.0.0.1 affects the whole machine, and the README does not say how to undo it, so note your old DNS settings first.

## Links

- [DNSCrypt project home page (protocol)](https://dnscrypt.info)
- [dnscrypt-proxy documentation](https://dnscrypt.info/doc)
- [dnscrypt-proxy GitHub repository](https://github.com/DNSCrypt/dnscrypt-proxy)
