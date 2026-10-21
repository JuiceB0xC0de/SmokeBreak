---
name: rpki-client
title: rpki-client
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, bgp, network, protocol, routing, security]
homepage: https://www.rpki-client.org/
scout_score: 6
status: draft
---

# rpki-client

**TLDR;** An OpenBSD validator that fetches the global RPKI repositories and checks which networks may announce which internet routes, emitting data for routers.

rpki-client is an implementation of the Resource Public Key Infrastructure for what the standards call Relying Parties. It queries the global RPKI repository system, validates the untrusted inputs it receives, and outputs validated ROA payloads and BGPsec Router keys. A ROA is a signed statement that a given network is allowed to originate a given block of IP addresses.

The output is meant to be consumed. It can be formatted as configuration for OpenBGPD or BIRD, or as CSV or JSON for other routing stacks. A router can then compare a BGP announcement against the validated data, which is the BGP Prefix Origin Validation described in RFC 6811. The background is in RFC 6480.

The idea underneath is how the internet decides whether to believe a route announcement. BGP was built on trust, and RPKI adds a cryptographic chain that says who holds which address space. This tool is the part that walks that chain and rejects what does not verify, so it is a door into how routing security works in practice.

The project is developed by a named group of OpenBSD developers, including Theo de Raadt. The portable version, maintained by Sebastian Benoit and Job Snijders, tracks the OpenBSD base component, which ships every six months. The code is under the ISC license.

## Install

```
brew install rpki-client
# depends on libretls, openssl@4 and rsync, which brew pulls in
# upstream recommends a signed release tarball instead: ./configure && make
```

## Try this

```
rpki-client --help
```
Prints the usage summary and lists the options, including how output formats are chosen.

## What's unique

It is a validator that feeds routers directly, emitting OpenBGPD and BIRD configuration rather than only a raw data dump. It is also a portable build of a component from the OpenBSD base system.

## Caveats

Upstream says the portable version is tested regularly only on Alpine, CentOS/RHEL/Rocky, Debian, Fedora, FreeBSD, macOS, OpenBSD and Ubuntu, and recommends a verified release tarball over a package manager. Its docs give no example invocation, and a full run fetches repository data from the network.

## Links

- [Homepage](https://www.rpki-client.org/)
- [GitHub portable repository](https://github.com/rpki-client/rpki-client-portable)
- [RFC 6811 (BGP Prefix Origin Validation)](https://www.rfc-editor.org/rfc/rfc6811)
