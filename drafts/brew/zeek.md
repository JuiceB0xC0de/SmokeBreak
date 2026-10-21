---
name: zeek
title: Zeek
source: brew
category: take-things-apart
commitment: afternoon
tags: [afternoon, network, protocol, scripting, security]
homepage: https://zeek.org/
scout_score: 6
status: draft
---

# Zeek

**TLDR;** Zeek watches network traffic and turns it into structured logs of what every protocol conversation did, steered by its own scripting language.

Zeek is a passive network monitor, formerly called Bro. It sits on a sensor, watches traffic go by, and analyzes application-layer protocols such as HTTP, DNS, SSL/TLS and SSH. What comes out is not alerts from a signature list but structured transaction logs, extracted file contents, and whatever custom output you script.

Vern Paxson began it in the 1990s to give deep insight into activity on university and national lab networks. It has been a research and operations tool for a long time. The project describes itself as "flexible, scriptable, and powered by defenders."

The idea underneath is that monitoring policy is code. Zeek keeps extensive application-layer state about the network and runs event handlers written in its own domain-specific language. The README says this means it is not restricted to any particular detection approach. You decide what a connection, a DNS lookup or a certificate means for your site.

It is explicitly not a firewall or intrusion prevention system: "Zeek is not an active defense mechanism. Instead, it operates quietly on a sensor." It observes and records, and never blocks.

## Install

```
brew install zeek
# The formula also installs Spicy/HILTI tools, BTest, zeekctl and zkg (the package manager). No account or hardware is needed to try scripts.
```

## Try this

```
zeek --help
```
Lists the options for the main binary, including how to read a packet capture or sniff an interface.

```
zeek hello.zeek
```
Runs the README's hello-world script, saved as hello.zeek, which prints Hello World! from a zeek_init event.

```
zeek-cut --help
```
Shows how to pull chosen columns out of Zeek's tab-separated logs.

## What's unique

Zeek is a scripted, passive analyzer rather than a signature box. Its own language turns raw traffic into site-specific structured logs. It also has a browser playground at try.zeek.org.

## Caveats

It observes and logs but does not block traffic, and it is built for sensor deployments, so the interesting use needs real or captured traffic.

## Links

- [Zeek homepage](https://zeek.org/)
- [Documentation (stable)](https://docs.zeek.org/en/stable/index.html)
- [Try Zeek playground](https://try.zeek.org)
- [GitHub repository](https://github.com/zeek/zeek)
