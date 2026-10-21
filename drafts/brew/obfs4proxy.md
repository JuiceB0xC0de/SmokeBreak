---
name: obfs4proxy
title: obfs4proxy
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, censorship, network, protocol, proxy, tor]
homepage: https://gitlab.com/yawning/obfs4
scout_score: 7
status: draft
---

# obfs4proxy

**TLDR;** A Tor pluggable transport that wraps Tor traffic in the obfs4 protocol, so censors have a harder time recognising it.

obfs4proxy is a pluggable transport proxy for Tor. It sits between Tor and the network and implements obfs4, a protocol meant to disguise Tor traffic so it is harder to identify. The project page calls it "The obfourscator (obfs4proxy)".

The reason it exists is censorship. Where Tor connections are blocked or detected, a transport like this changes what the traffic looks like on the wire. The scout's notes describe the goal as making traffic look like random noise. That wording is unverified here, because the README and spec did not load when this entry was prepared.

The idea underneath is the pluggable transport: Tor does not need to know how its traffic gets disguised. A separate program handles that layer, and different disguises can be swapped in. Reading the obfs4 spec, which lives in the project's doc folder, is the best way into how the disguise works.

This is mostly something Tor runs for you, not a tool you drive by hand. The reading is more interesting than the running.

## Install

```
brew install obfs4proxy

It is meant to be used alongside Tor, so you will need Tor installed to see it do anything. Configuration details were not available, so check the project README.
```

## Try this

```
obfs4proxy --help
```
Prints the proxy's usage text, a quick way to see what options the binary exposes.

## What's unique

Most network tools show you traffic. This one is about hiding it, and it is a concrete example of Tor's pluggable transport idea.

## Caveats

Maintenance status is unknown, the project page shows a January 2019 creation date, and the README and spec could not be read, so usage details need checking at the source.

## Links

- [Project homepage (GitLab)](https://gitlab.com/yawning/obfs4)
