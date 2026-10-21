---
name: veilid
title: Veilid
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, network, p2p, privacy, protocol, rust]
homepage: https://veilid.com/
scout_score: 6
status: draft
---

# Veilid

**TLDR;** An open-source peer-to-peer app framework where every running app is a node that relays end-to-end encrypted data, with no central server in the middle.

Veilid is a framework for building apps that exchange data without a central server. According to the project's homepage video, every device running a Veilid app is a node. Messages pass through other participating nodes, and those nodes cannot read them because the content is end-to-end encrypted. The network is the apps themselves.

The project frames this as a response to servers and intermediaries that can read, store, or sell private communications. Its own line is "Privacy is a human right." The stated goal is to remove the middle man so that "it's just you and someone else chatting privately." It is written in Rust with Flutter bindings, and the first public app built on it is VeilidChat, currently in beta.

The idea underneath is the interesting part: a network with no operator, where relaying, storing and routing are all done by the participants. The video compares the design to Tor and IPFS and calls it faster. That is the project's own claim, and the pages read for this entry do not explain the routing mechanism in technical terms.

The brew package installs two executables, `veilid-server` and `veilid-cli`. The names suggest a node you run and a client to talk to it, but the documentation read for this entry does not confirm that. Expect to learn by reading source and `--help` output.

## Install

```
brew install veilid
```

## Try this

```
veilid-server --help
```
Lists the options for the node process, which is the part that would join the network.

```
veilid-cli --help
```
Lists the options for the command-line client.

## What's unique

It is pitched as a general application framework rather than a single chat app, with every participating app acting as a relay node.

## Caveats

Documentation is thin: the README is one line pointing to a wiki that loaded empty, the homepage is mostly marketing, and its claims about speed and privacy are unverified.

## Links

- [Veilid homepage](https://veilid.com/)
- [Source repository (GitLab)](https://gitlab.com/veilid/veilid)
- [Project wiki (loaded empty)](https://gitlab.com/veilid/veilid/-/wikis/home)
