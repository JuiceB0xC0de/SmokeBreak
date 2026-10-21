---
name: hsd
title: hsd
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, blockchain, dns, network, nodejs, protocol]
homepage: https://handshake.org
scout_score: 6
status: draft
---

# hsd

**TLDR;** A full node for Handshake, a blockchain that acts as a DNS root zone, with a built-in resolver you can query with dig.

hsd is the reference implementation of the Handshake protocol, a peer-to-peer system for the root of the naming hierarchy. Instead of trusting a central root zone, every node validates the chain and serves the resulting root zone. To do that it runs a recursive resolver and an authoritative nameserver (ports 5349 and 5350 by default), so ordinary tools like dig can query it. It also ships a wallet server, command-line clients, and RPC and REST APIs.

The project's stated aim is to replace centralised root naming and certificate authorities with a system where, in its words, "every peer is validating and in charge of managing the root DNS naming zone". Names are won in on-chain auctions paid in HNS coin. The homepage argues that putting a price on names deters the spam and sybil attacks that pushed earlier decentralised naming systems toward central operators.

The auction is a sequence of commands: an open transaction starts bidding, bids carry a hidden lockup value, bids are later revealed, and the winner publishes records with sendupdate. Existing DNS owners can skip the auction by publishing a DNSSEC ownership proof and broadcasting it with sendclaim. The claim is mined on-chain and matures after about 30 days.

The door here is into how the DNS root works, what DNSSEC actually proves, and what happens when you try to make naming trustless. Handshake says it has no official foundation or controlling entity, and that multiple implementations may exist, so hsd is one of several.

## Install

```
brew install hsd
# Needs Node.js and unbound (both pulled in by brew). The README says libunbound must be present before installing hsd if you want the native resolver bindings. The hsd-rpc and hsw-rpc shortcuts and the CPU miner come from hs-client: npm install -g hs-client
```

## Try this

```
hsd --ns-port 5300
```
Starts the node with the authoritative nameserver moved to port 5300.

```
hsd-cli info
```
Returns basic information about the running node.

```
dig @127.0.0.1 www.ietf.org +dnssec
```
Sends a DNSSEC-enabled test query to the node's local recursive resolver.

## What's unique

The chain is treated as a root zone that any peer can validate, not just a ledger for moving money. Existing DNS owners can also claim their names with a DNSSEC proof instead of bidding.

## Caveats

The homepage calls Handshake experimental, the README warns hsd does not protect against lost funds from bugs or user error, its examples use testnet settings, and I could not confirm whether it is actively maintained.

## Links

- [Handshake project homepage](https://handshake.org)
- [HSD documentation site](https://hsd-dev.org)
- [HSD API docs](https://hsd-dev.org/api-docs)
- [HSD source on GitHub](https://github.com/handshake-org/hsd)
