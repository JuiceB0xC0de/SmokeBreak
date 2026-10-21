---
name: freediameter
title: freeDiameter
source: brew
category: fundamentals
commitment: afternoon
tags: [aaa, afternoon, diameter, network, protocol, telecom]
homepage: https://github.com/freeDiameter/freeDiameter
scout_score: 6
status: draft
---

# freeDiameter

**TLDR;** An open source C implementation of Diameter, the AAA protocol that succeeded RADIUS and quietly authenticates traffic inside telecom networks.

Diameter is a protocol designed to carry Authentication, Authorization and Accounting payloads. The project's README calls it "an evolution of the RADIUS protocol (as the name suggests)." It is the kind of protocol most developers never meet, because it lives between network equipment and the servers that decide who gets access and how usage is counted.

freeDiameter splits the job into pieces. libfdproto is a shared library for parsing and building Diameter messages and dictionaries. libfdcore is the framework core: peer connections, watchdogs, basic routing, and loading of extensions. freeDiameterd is a small daemon that reads the command line and starts that framework. Extensions add server applications, advanced routing, or peer management.

The underlying idea is that Diameter has a base protocol (RFC 3588) every node must support, plus application documents layered on top, such as NAS (RFC 4005) and EAP (RFC 4072). Reading how freeDiameter loads those as extensions is a way into how a real AAA protocol is structured. Software that needs to speak Diameter can link libfdcore directly instead of running the daemon.

The project was previously known as the "waaad" project (WIDE AAA Daemon).

## Install

```
brew install freediameter
# then edit $HOMEBREW_PREFIX/etc/freeDiameter.conf
# sample configs: $HOMEBREW_CELLAR/freediameter/1.6.0/share/doc/freediameter
# contrib files: $HOMEBREW_PREFIX/opt/freediameter/share/freediameter/contrib
```

## Try this

```
freeDiameterd --help
```
Prints the daemon's command-line options, a first look at what the framework lets you set at startup.

## What's unique

It is a full, modular Diameter stack rather than a client stub: a message library, a core framework, and loadable extensions you can reuse in your own software.

## Caveats

The project website is marked no longer maintained and its configuration wiki page returned a 404, so setup documentation may only exist in the archived copy; the source is still said to be maintained on GitHub.

## Links

- [GitHub repository](https://github.com/freeDiameter/freeDiameter)
- [Project website (archived, no longer maintained)](http://www.freediameter.net/)
