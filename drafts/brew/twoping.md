---
name: twoping
title: 2ping
source: brew
category: fundamentals
commitment: quick
tags: [network, ping, protocol, python, quick]
homepage: https://www.finnie.org/software/2ping/
scout_score: 6
status: draft
---

# 2ping

**TLDR;** A ping that tells you whether a lost packet died on the way out or on the way back, using a three-way exchange with a listener.

2ping is a command-line ping utility written in Python 3. You run the client against a host that is running a 2ping listener. Each probe line is marked as received, outbound lost, or inbound lost, and the summary gives outbound, inbound and undetermined loss counts plus round-trip min/avg/max.

Ordinary ping can only say that a packet or its reply went missing. It cannot say which leg failed. 2ping was built to make that split visible, which matters when a path is asymmetric, such as a congested uplink, a one-way filter, or a flaky wireless hop that only hurts one direction.

The trick is a three-way exchange, in the project's words "akin to TCP SYN, SYN/ACK, ACK". After the fact, the client and the listener compare their state and work out where each loss happened. The protocol has its own written specification and is described as version-agnostic, so clients and listeners of different versions are meant to interoperate.

That makes it a small door into how probing tools reason about networks: what a single lost packet can and cannot tell you, and what extra state you need to learn more. The 2ping6 executable is listed alongside it for IPv6.

## Install

```
brew install twoping
# the client needs a 2ping listener at the far end: run `2ping --listen` on a host you control, or use a public one such as test.2ping.net
# requires Python 3 (installed by brew as a dependency)
```

## Try this

```
2ping test.2ping.net
```
Pings the public test listener and prints each probe as received, outbound lost or inbound lost, then a summary with outbound/inbound/undetermined counts.

```
2ping --listen
```
Starts a listener on a stable host so other machines can run 2ping against it.

```
2ping remotehost
```
Runs the client against a host you control that is already running a listener.

## What's unique

Most ping tools only count losses. 2ping compares state between client and listener after a three-way exchange, so each lost probe is attributed to a direction.

## Caveats

A listener must be running at the far end, so you can only test hosts you control or the public listeners, which the author asks you not to flood (no interval faster than 0.2 seconds).

## Links

- [2ping homepage](https://www.finnie.org/software/2ping/)
- [2ping issue tracker on GitHub](https://github.com/rfinnie/2ping/issues)
- [2ping pull requests on GitHub](https://github.com/rfinnie/2ping/pulls)
