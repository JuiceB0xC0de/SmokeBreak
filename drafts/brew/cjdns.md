---
name: cjdns
title: cjdns
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, cryptography, ipv6, mesh, network, protocol]
homepage: https://github.com/cjdelisle/cjdns/
scout_score: 8
status: draft
---

# cjdns

**TLDR;** An encrypted IPv6 mesh network where your address is derived from your public key, so no registry hands out addresses and no one can forge yours.

Cjdns is a daemon that brings up a virtual network interface and gives your machine an IPv6 address. That address is not assigned by anyone. It comes from your public key, so owning the address and owning the key are the same thing. The README puts it this way: "Cjdns implements an encrypted IPv6 network using public-key cryptography for address allocation and a distributed hash table for routing."

Nodes find each other by peering over ordinary UDP, either with peers you configure by hand or through DNS seeders by default. Traffic between cjdns nodes is encrypted, and routing runs over a distributed hash table instead of a central routing authority. The result is an overlay network that sits on top of the regular internet and needs no radio hardware.

The idea underneath is a question: what if identity and address were the same thing? Most of the internet separates the two and relies on registries, certificate authorities and DNS to join them. Cjdns collapses them into a keypair. The README says this gives "near-zero-configuration networking" and avoids many security and scalability problems of existing networks. The project's whitepaper and goals documents go deeper, though the brief did not cover them.

The config file holds your private key, which is your identity. The README says: "Protect your conf file!" Lose it and you lose your address. If someone else gets it, they can impersonate you.

## Install

```
brew install cjdns
# Needs a TUN device. On Linux, /dev/net/tun must exist and be accessible; on macOS skip that check.
# The daemon runs as root by default.
```

## Try this

```
cjdroute --genconf | sudo tee -a /etc/cjdroute.conf
```
Generates a new config with a fresh keypair, and so a new IPv6 address, and appends it to /etc/cjdroute.conf.

```
sudo cjdroute < /etc/cjdroute.conf
```
Starts the daemon as root, reading the config from stdin, and brings up your local cjdns IPv6 host.

```
cjdnstool --help
```
Lists the admin API client's commands for talking to the running node on its local admin port.

## What's unique

Addresses are derived from keys rather than assigned. It is also a mesh design that runs as an IPv6 overlay on plain UDP peering, so you can join with only an internet connection.

## Caveats

The brief found no release or commit dates, so project activity is unclear; by default the daemon runs as root, and default DNS seeding tells seed operators you run cjdns unless you comment out dnsSeeds.

## Links

- [Homepage / README](https://github.com/cjdelisle/cjdns/)
- [Cjdns Whitepaper](https://github.com/cjdelisle/cjdns/blob/master/doc/Whitepaper.md)
- [Project Goals](https://github.com/cjdelisle/cjdns/blob/master/doc/projectGoals.md)
