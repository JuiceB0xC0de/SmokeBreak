---
name: opendht
title: OpenDHT
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dht, library, network, p2p, protocol]
homepage: https://github.com/savoirfairelinux/opendht
scout_score: 6
status: draft
---

# OpenDHT

**TLDR;** A C++17 distributed hash table you can join on the public network, with dhtnode, a command-line node for putting and getting values from strangers' machines.

OpenDHT is a library for a distributed hash table: a key-value store spread across many machines with no central server. Every node can read and write values, and values are stored across the network with redundancy. Programs use it through a map-style C++17 API, with bindings for C, Rust and Python 3, or through an optional REST proxy.

The Homebrew package installs `dhtnode`, a command-line tool that runs a DHT node and lets you do get and put operations on text values. The source tree also ships `dhtchat`, a simple chat client that runs over the DHT, though the brief lists only `dhtnode` as installed by the formula.

A node starts with a generated RSA identity on a chosen port and joins the network through a known bootstrap node. Data lives under hashed keys. An optional public-key layer built on GnuTLS lets values be signed or encrypted. The README says little about routing internals, so the wiki is the place to look next.

The project describes itself as an easy-to-use in-memory data store "designed for large networks and small devices", resilient to network disruption. It began from jech/dht by Juliusz Chroboczek, which the README credits. The idea underneath is how a network can store and find data when nobody is in charge of it.

## Install

```
brew install opendht
# first run needs network access to a bootstrap node; the project's example uses bootstrap.jami.net on port 4222
```

## Try this

```
dhtnode --help
```
Lists the options for running a node, including the port and the bootstrap address to join.

```
pip install opendht
```
Installs the Python 3 binding from PyPI, so you can call get and put from a script.

## What's unique

It is a real peer-to-peer system you can join on the public network, not a toy. The same API is available from C++, C, Rust, Python and a REST proxy, and stored values can be signed or encrypted.

## Caveats

The README sends most documentation to a wiki, so routing and storage details are thin, and the example depends on a bootstrap node run by the Jami project.

## Links

- [OpenDHT homepage (GitHub)](https://github.com/savoirfairelinux/opendht)
- [OpenDHT wiki (documentation)](https://github.com/savoirfairelinux/opendht/wiki)
- [Running a node with dhtnode (wiki)](https://github.com/savoirfairelinux/opendht/wiki/Running-a-node-with-dhtnode)
- [BUILD.md (build instructions)](https://github.com/savoirfairelinux/opendht/blob/master/BUILD.md)
