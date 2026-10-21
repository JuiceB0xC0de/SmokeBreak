---
name: snowflake
title: Snowflake
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, censorship, go, network, protocol, tor, webrtc]
homepage: https://www.torproject.org
scout_score: 6
status: draft
---

# Snowflake

**TLDR;** A Tor pluggable transport that routes blocked users' traffic through volunteer WebRTC proxies, so it looks like an ordinary video call.

Snowflake is a pluggable transport for Tor, written in Go. When a user's network blocks Tor, their client asks a broker for a volunteer proxy. The two then open a WebRTC peer connection, and the proxy relays the Tor traffic on to a Tor relay. To a network observer, the traffic looks like a WebRTC video or voice call.

The repository holds four programs: `snowflake-broker`, `snowflake-client`, `snowflake-proxy` and `snowflake-server`. Volunteers can help by leaving a browser tab or extension open, or by running the standalone proxy.

The design is a reply to two older tools. The README says Snowflake "combines the advantages of flashproxy and meek". Like meek, it needs no special setup for the user. Unlike meek, it does not push all traffic through a CDN. Domain fronting is used only for the brief signalling step and NAT piercing, so the CDN bill stays negligible. Like flashproxy, it draws on a large pool of volunteers, but WebRTC means they need no manual port forwarding: "NATs are no longer a usability barrier".

The idea underneath is a way into censorship circumvention as a protocol problem: signalling, NAT traversal, and traffic that blends into something too common to block.

## Install

```
brew install snowflake
# Installs the broker, client, proxy and server binaries. Using the client with Tor needs Tor itself, plus Bridge and ClientTransportPlugin lines in your torrc.
```

## Try this

```
snowflake-proxy --help
```
Lists the options for running a standalone volunteer proxy.

```
snowflake-client --help
```
Shows the flags for the client side that Tor launches as its transport plugin.

```
snowflake-broker --help
```
Shows the options for the broker that matches clients with proxies.

## What's unique

Anyone can volunteer a proxy by leaving a browser tab open, and the traffic is disguised as a WebRTC call. Domain fronting carries only the signalling, which keeps it cheap to scale.

## Caveats

The official GitLab repository returned 403 when the brief was written, so its activity could not be checked. The client and proxy setup guides were not read, and the GitHub mirror README looks old.

## Links

- [Snowflake project site](https://snowflake.torproject.org/)
- [Tor Project](https://www.torproject.org)
- [Snowflake wiki](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake/-/wikis/home)
- [Community guide to running a Snowflake proxy](https://community.torproject.org/relay/setup/snowflake/)
- [Source mirror (GitHub, keroserene/snowflake)](https://github.com/keroserene/snowflake)
