---
name: edgevpn
title: EdgeVPN
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, go, libp2p, network, p2p, vpn]
homepage: https://mudler.github.io/edgevpn
scout_score: 5
status: draft
---

# EdgeVPN

**TLDR;** A single Go binary that builds a private network between machines over libp2p, with no central server, just a shared token.

EdgeVPN creates a virtual network interface (edgevpn0 by default) on each machine and gives every node a virtual IP such as 10.1.0.11/24. Nodes that start with the same token find each other over libp2p and join the same network. No coordinator, no host list, no server to run.

The token is the whole idea. It is the network's configuration, base64-encoded, and the README says exposing it gives full control of the network. Generate one, hand it to a friend, and you share a network. Network state, including DHCP and DNS registries, lives in a small replicated ledger that the peers keep among themselves instead of on a server.

The author, Ettore Di Giacinto, says it began as his first experiment with libp2p and as a wish for a more open ngrok alternative that needs less infrastructure. So the same binary can also expose TCP services through a reverse proxy and send files between peers. A web UI and a REST API sit on top.

The door here is peer-to-peer networking: how nodes discover each other with no fixed address, and how shared state survives without a central owner.

## Install

```
brew install edgevpn
# Creating the virtual interface will probably need root or equivalent privileges; the README does not spell this out.
```

## Try this

```
edgevpn -g > config.yaml
```
Generates a new network config file you can reuse as EDGEVPNCONFIG.

```
EDGEVPNTOKEN=$(edgevpn -g -b)
```
Generates a portable base64 token that identifies a new network.

```
EDGEVPNTOKEN=.. edgevpn --address 10.1.0.11/24
```
Starts a node on that network with a virtual IP; run it on other machines with 10.1.0.12 and so on, using the same token.

## What's unique

One binary combines a VPN, an ngrok-style reverse proxy, peer-to-peer file transfer and a replicated ledger carrying DHCP and DNS state. The network's identity is just a shareable token.

## Caveats

The README says it has not had a full security audit and should not carry sensitive traffic or run in production, and connections can take up to five minutes to form.

## Links

- [Homepage and documentation](https://mudler.github.io/edgevpn)
- [GitHub repository](https://github.com/mudler/edgevpn)
- [Install EdgeVPN tutorial](https://mudler.github.io/edgevpn/docs/tutorials/install/)
- [When not to use EdgeVPN](https://mudler.github.io/edgevpn/docs/explanation/when-not-to-use-edgevpn/)
