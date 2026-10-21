---
name: pear
title: Pear
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, dht, hypercore, javascript, networking, p2p]
homepage: https://docs.pears.com
scout_score: 5
status: draft
---

# Pear

**TLDR;** A runtime for building and running apps that load directly from other peers, with no servers, using the Hypercore family of P2P modules.

Pear is an application runtime and toolchain from Holepunch. You install the `pear` CLI, then build, stage, and share desktop, terminal, or mobile apps that find each other and talk directly. Its own pitch: "Build, share, and extend unstoppable, zero-infrastructure P2P apps for mobile, desktop, and terminal."

The unusual part is where apps come from. Per the docs, "Pear loads applications remotely from peers and lets anyone create and share applications with peers." There is no central host. Updates travel over the air from peer to peer, and releases can be signed with multisig and shared through a `pear://` link.

Underneath is a stack of small P2P modules the docs name: HyperDHT for dialing a peer by key, Hyperswarm for finding peers by topic, Hypercore, Hyperbee and Hyperdrive for replicated storage, and Autobase for shared rooms. The getting-started tutorial builds a chat app in which peers discover each other through the DHT and stream messages directly. That tutorial is the real door: it shows how much of an app you can build without a server in the middle.

The runtime itself runs on Bare, a separate minimal JavaScript runtime that can also be used on its own. The desktop architecture combines Electron, Bare worker processes, storage, and over-the-air updates.

## Install

```
brew install pear
# Needs Node.js (installed as a brew dependency). The tutorial expects Node 22.17+ and npm 10.9+, plus a POSIX-style terminal (macOS, Linux, or Windows via WSL).
# Alternatives from the docs: curl https://install.pears.com/pear.sh | sh, or docker run -it --rm tetherto/pear
```

## Try this

```
pear --menu
```
Opens an interactive, filterable list of CLI commands with a form for flags (Pear 3.2.0+).

```
docker run -it --rm tetherto/pear
```
Starts an Ubuntu container with pear ready, so you can follow the tutorial without a local install.

```
pear --help
```
Lists the CLI commands, including the stage, build, and touch steps used for developing and releasing apps.

## What's unique

Apps are distributed and updated peer to peer, with multisig-signed releases and a pear:// link. Its Bare runtime can also be used on its own as an embeddable JavaScript runtime.

## Caveats

It is a platform rather than a small tool, so expect a learning curve, and shipping an app involves a multisig release flow with extra setup.

## Links

- [Pear docs homepage](https://docs.pears.com)
- [Getting started](https://docs.pears.com/getting-started)
- [hello-pear-electron template (GitHub)](https://github.com/holepunchto/hello-pear-electron)
