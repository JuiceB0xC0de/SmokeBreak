---
name: gnunet
title: GNUnet
source: brew
category: fundamentals
commitment: days-off
tags: [days-off, naming, network, p2p, privacy, protocol]
homepage: https://gnunet.org/
scout_score: 6
status: draft
---

# GNUnet

**TLDR;** A protocol stack that tries to replace the Internet's plumbing with encrypted, metadata-hiding peer-to-peer networking, with about fifty command-line tools exposing its parts.

GNUnet is a framework and protocol stack for building secure, distributed applications. The homepage describes components for addressing, reliable encrypted channels with routing, resource discovery, and naming. It is one shared foundation rather than a single app. The brew package installs roughly fifty executables, each exposing a subsystem: gnunet-gns for naming, gnunet-cadet for encrypted channels, gnunet-fs for file sharing, gnunet-vpn, gnunet-messenger, gnunet-identity and more.

The project starts from a complaint about metadata. In its words: "Your metadata is just as revealing as the actual content; and it gets exposed on the Internet." Who talks to whom, when, how often and how much leaks even under transport encryption. The homepage also argues that every P2P project re-invents the same components, which multiplies the vulnerabilities, so GNUnet offers one shared set.

It is a self-organizing network with no public ledger: "GNUnet does not require a decentralized, public ledger." Decentralization is used only where it adds value. The homepage says the work rests on almost two decades of academic research, so this is a door into a lot of papers and design ideas about naming, routing and privacy that most developers never meet.

The pages read for this entry did not show tool input or output formats, so expect to learn the tools from the documentation. Versioned docs exist for several release branches.

## Install

```
brew install gnunet
```

## Try this

```
gnunet-arm --help
```
Shows the options for the service manager (ARM) that starts and stops GNUnet's background services.

```
gnunet-identity --help
```
Lists the options for managing your identities (key pairs) in GNUnet.

```
gnunet-gns --help
```
Shows how to look up names in GNUnet's naming system, an alternative to DNS.

## What's unique

Most P2P projects are a single app. GNUnet is a whole replacement stack with a stated goal of hiding metadata and avoiding blockchain-style consensus.

## Caveats

The brief found no install steps, commands or README (the GitHub URL returned 404), so expect to work from the docs, and a working node likely needs configuration and services running.

## Links

- [Homepage](https://gnunet.org/)
- [Documentation](https://docs.gnunet.org/)
