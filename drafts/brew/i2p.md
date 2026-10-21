---
name: i2p
title: I2P
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, anonymity, java, network, overlay, protocol]
homepage: https://geti2p.net
scout_score: 7
status: draft
---

# I2P

**TLDR;** A full anonymous network running inside the internet, with its own sites, mail, IRC and torrents, routed through volunteer peers.

I2P, the Invisible Internet Project, is an overlay network: a network built on top of the ordinary internet that has its own addressing and routing. Traffic is wrapped in several layers of encryption and relayed through a mesh of volunteer-run routers, so no single node sees both the sender and the receiver. In the project's words, "Your IP and identity are hidden from the network itself."

The homepage says no central servers control routing. Every participant runs a router that also relays for others. That is the trade at the heart of the design: you get anonymity by becoming part of the crowd that provides it. The homepage cites 40K+ active routers and more than 20 years of activity.

I2P is mostly a place to host and reach services inside the network, not a proxy for browsing the open web. The docs list I2P Mail, IRC over I2P, BitTorrent over I2P, an address book, and eepsites (websites that live only on I2P). The docs index also has pages on Garlic Routing and Tunnel Routing, the mechanisms behind the message bundling and path building. That is where the real reading starts.

The brew package installs two executables: `i2prouter`, which appears to be the router launcher, and `eepget`, whose usage I could not confirm from the pages read. Both need Java, which brew pulls in as a dependency.

## Install

```
brew install i2p
# Pulls in openjdk and java-service-wrapper. Setup steps after install are not verified; the docs index lists per-platform guides and a Router Console Configuration Guide at geti2p.net/en/docs.
```

## Try this

```
i2prouter --help
```
Prints the usage for the router launcher, which shows how to start and stop the router.

```
eepget --help
```
Prints the usage for eepget, the other installed tool, so you can see what it fetches and how.

## What's unique

It is a complete network with its own services, not an anonymizing gateway to the regular web. Every user's router also relays traffic for others.

## Caveats

I could not verify setup steps or the command list from the pages read, and the anonymity claims are the project's own framing, so read the docs before trusting it with anything that matters.

## Links

- [I2P homepage](https://geti2p.net)
- [I2P docs](https://geti2p.net/en/docs/install)
